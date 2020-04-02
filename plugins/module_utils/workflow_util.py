# Copyright (c) IBM Corporation 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

try:
    import requests
except ImportError:
    requests = None
import json


def get_connect_argument_spec():
    """
    Return the arguments of ansible module used for session setup
    :rtype: dict[str, dict]
    """
    return dict(
        zmf_host=dict(required=True, type='str'),
        zmf_port=dict(required=False, type='int'),
        zmf_user=dict(required=False, type='str', no_log=True),
        zmf_password=dict(required=False, type='str', no_log=True),
        zmf_crt=dict(required=False, type='str', no_log=True),
        zmf_key=dict(required=False, type='str', no_log=True)
    )


def get_connect_session(module):
    """
    Return the connection session
    :param AnsibleModule module: the ansible module
    :rtype: Session
    """
    if requests is None:
        module.fail_json(msg='ImportError: cannot import requests')
    session = requests.Session()
    crt = module.params['zmf_crt']
    key = module.params['zmf_key']
    user = module.params['zmf_user']
    pw = module.params['zmf_password']
    if (crt is not None and crt.strip() != '') and (key is not None and key.strip() != ''):
        session.cert = (crt.strip(), key.strip())
    elif (user is not None and user.strip() != '') and (pw is not None and pw.strip() != ''):
        session.auth = (user.strip(), pw.strip())
    else:
        # fail the module since auth is must for zosmf connection
        module.fail_json(msg='HTTP setup error: either zmf_user/zmf_password or zmf_crt/zmf_key are required.')
    return session


def __get_request_headers():
    """
    Return the request headers for calling workflow APIs
    :rtype: dict[str, str]
    """
    return {'X-CSRF-ZOSMF-HEADER': 'TEST'}


def handle_request(module, session, method, url, params=None, rcode=200, timeout=30):
    """
    Return the response or error message of HTTP request
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str method: the method of HTTP request
    :param str url: the URL of HTTP request
    :param dict params: the params of HTTP request
    :param int rcode: the expected return code of HTTP request
    :param int timeout: the timeout of HTTP request
    :rtype: dict or str
    """
    try:
        if method == 'get':
            response = session.get(url, params=params, headers=__get_request_headers(), verify=False, timeout=timeout)
        elif method == 'put':
            response = session.put(url, data=json.dumps(params), headers=__get_request_headers(), verify=False, timeout=timeout)
        elif method == 'post':
            response = session.post(url, data=json.dumps(params), headers=__get_request_headers(), verify=False, timeout=timeout)
        elif method == 'delete':
            response = session.delete(url, headers=__get_request_headers(), verify=False, timeout=timeout)
    except Exception as ex:
        module.fail_json(msg='HTTP request error: ' + str(ex))
    else:
        response_code = response.status_code
        if response.content:
            response_content = json.loads(response.content)
        else:
            response_content = dict()
        if response_code == rcode:
            return response_content
        else:
            if 'messageText' in response_content:
                return 'HTTP request error: ' + str(response_code) + ' : ' + response_content['messageText']
            else:
                return 'HTTP request error: ' + str(response_code)


def cmp_list(list1, list2):
    """
    Recursively compare the given lists
    :param list list1: the given list
    :param list list2: the given list
    :returns: True if the given lists are same
    :rtype: bool
    """
    if len(list1) != len(list2):
        return False
    else:
        for v in list1:
            found = False
            for vv in list2:
                if (isinstance(v, str) or isinstance(v, bool)) and (isinstance(vv, str) or isinstance(vv, bool)):
                    if str(v).strip().upper() == str(vv).strip().upper():
                        found = True
                        break
                elif isinstance(v, list) and isinstance(vv, list):
                    if cmp_list(v, vv) is True:
                        found = True
                        break
                elif isinstance(v, dict) and isinstance(vv, dict):
                    if cmp_dict(v, vv) is True:
                        found = True
                        break
            if found is False:
                return False
    return True


def cmp_dict(dict1, dict2):
    """
    Recursively compare the given dicts
    :param dict dict1: the given dict
    :param dict dict2: the given dict
    :returns: True if the given dicts are same
    :rtype: bool
    """
    if len(dict1) != len(dict2):
        return False
    else:
        key1 = list(dict1.keys()).sort()
        key2 = list(dict2.keys()).sort()
        if key1 != key2:
            return False
        else:
            for k, v in dict1.items():
                if isinstance(v, str) or isinstance(v, bool):
                    if str(v).strip().upper() != str(dict2[k]).strip().upper():
                        return False
                elif isinstance(v, list):
                    if not isinstance(dict2[k], list):
                        return False
                    else:
                        if cmp_list(v, dict2[k]) is False:
                            return False
                elif isinstance(v, dict):
                    if not isinstance(dict2[k], dict):
                        return False
                    else:
                        if cmp_dict(v, dict2[k]) is False:
                            return False
    return True
