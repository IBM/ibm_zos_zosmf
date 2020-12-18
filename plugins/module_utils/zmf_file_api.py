# Copyright (c) IBM Corporation 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_util import handle_request_raw
import json
import re


def __get_file_apis():
    """
    Return the details of all z/OS UNIX file services APIs.
    :rtype: dict[str, dict]
    """
    return dict(
        # retrieve the contents of a USS file
        fetch=dict(
            method='get',
            url='https://{zmf_host}:{zmf_port}/zosmf/restfiles/fs/{file_src}',
            args={
                'research': dict(required=False, type='str', nickname='file_search.keyword'),
                'insensitive': dict(required=False, type='bool', default=True, nickname='file_search.insensitive'),
                'maxreturnsize': dict(required=False, type='int', default='100', nickname='file_search.maxreturnsize')
            },
            headers={
                'Content-Type': dict(required=False, type='str', default='text/plain', nickname=''),
                'X-IBM-Data-Type': dict(required=False, type='str', default='text', choices=['text', 'binary'], nickname='file_data_type'),
                'Range': dict(required=False, type='str', nickname=''),
                'X-IBM-Record-Range': dict(required=False, type='str', nickname=''),
                'If-None-Match': dict(required=False, type='str', nickname='file_checksum')
            },
            ok_rcode=200
        ),
        # write data to an existing USS file # TODO
        copy=dict(
            method='put',
            url='https://{zmf_host}:{zmf_port}/zosmf/restfiles/fs/{file_dest}',
            headers={
                'Content-Type': dict(required=False, type='str', default='text/plain', nickname=''),
                'X-IBM-Data-Type': dict(required=False, type='str', default='text', choices=['text', 'binary', 'record'], nickname='file_data_type'),
                'If-Match': dict(required=False, type='str', nickname='file_checksum')
            },
            ok_rcode=204
        )
    )


def __get_file_api_argument_spec(api):
    """
    Return the details of the specific file API.
    :param str api: the name of API
    :rtype: dict[str, str/int/dict]
    """
    file_apis = __get_file_apis()
    if api in file_apis:
        return file_apis[api]


def __get_file_api_url(module, url):
    """
    Return the parsed URL of the specific file API.
    :param AnsibleModule module: the ansible module
    :param str url: the initial URL of API
    :rtype: str
    """
    # format the input for zmd_port
    if module.params['zmf_port'] is None:
        module.params['zmf_port'] = ''
    else:
        module.params['zmf_port'] = str(module.params['zmf_port']).strip()
    # format the input for file_src & file_dest
    if module.params['file_src'].strip().startswith('/'):
        module.params['file_src'] = (module.params['file_src'].strip())[1:]
    if module.params['file_dest'].strip().startswith('/'):
        module.params['file_dest'] = (module.params['file_dest'].strip())[1:]
    matchObj = re.findall('{(.+?)}', url)
    for x in matchObj:
        if x == 'zmf_port' and module.params[x] == '':
            url = re.sub(':{' + x + '}', module.params[x], url)
        else:
            url = re.sub('{' + x + '}', module.params[x].strip(), url)
    return url


def __get_file_api_params(module, args):
    """
    Return the parsed params of the specific file API.
    :param AnsibleModule module: the ansible module
    :param dict[str, dict] args: the initial params of API
    :rtype: dict[str, str/list]
    """
    params = dict()
    for k, v in args.items():
        if v['nickname'] != '':
            # mapping the key of args with module argument
            s = v['nickname'].find('.')
            if s > 0:
                # key <==> suboption of module argument
                if module.params[v['nickname'][0:s]] is not None and v['nickname'][s + 1:] in module.params[v['nickname'][0:s]]:
                    input_v = module.params[v['nickname'][0:s]][v['nickname'][s + 1:]]
                else:
                    input_v = None
            else:
                # key <==> module argument
                input_v = module.params[v['nickname']]
            # mapping the value of args with module argument
            if input_v is not None and str(input_v).strip() != '':
                if 'choices' in v:
                    found = False
                    for vv in v['choices']:
                        if input_v.strip().lower() == vv.lower():
                            found = True
                            params[k] = vv
                            break
                    if found is False:
                        module.fail_json(
                            msg='Missing required argument or invalid argument: ' + v['nickname']
                            + '. The following values are valid: ' + str(v['choices']) + '.'
                        )
                else:
                    params[k] = str(input_v).strip()
            elif v['required'] is True:
                module.fail_json(msg='Missing required argument or invalid argument: ' + v['nickname'] + '.')
        elif 'default' in v:
            params[k] = v['default']
    return params


def call_file_api(module, session, api, headers):
    """
    Return the response or error message of the specific file API.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str api: the name of API
    :param dict headers: the header of HTTP request
    :rtype: dict or str
    """
    zmf_api = __get_file_api_argument_spec(api)
    zmf_api_url = __get_file_api_url(module, zmf_api['url'])
    zmf_api_params = __get_file_api_params(module, zmf_api['args'])
    return handle_request_raw(module, session, zmf_api['method'], zmf_api_url, zmf_api_params, headers)
