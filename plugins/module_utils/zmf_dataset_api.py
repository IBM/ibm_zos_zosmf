# Copyright (c) IBM Corporation 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_util import handle_request_raw
import json
import re


def __get_dataset_apis():
    """
    Return the details of all z/OS dataset services APIs.
    :rtype: dict[str, dict]
    """
    return dict(
        # read a data set or member
        fetch=dict(
            method='get',
            # header={'Content-Type': 'application/json'},
            url='https://{zmf_host}:{zmf_port}/zosmf/restfiles/ds/{dataset_name}',
            args={ 
                'research': dict(required=False, type='str', nickname='dataset_search.keyword'),
                'insensitive': dict(required=False, type='bool', nickname='dataset_search.insensitive'),
                'maxreturnsize': dict(required=False, type='int', nickname='dataset_search.maxreturnsize')
            },
            headers={
                'X-IBM-Data-Type': dict(
                    required=False, 
                    type='str', 
                    choices=['text','binary','record'],
                    nickname='dataset_data_type', 
                    default='text'),
                'X-IBM-Return-Etag': dict(required=False, type='bool', nickname='dataset_return_checksum_when_large'),
                'X-IBM-Migrated-Recall': dict(
                    required=False, 
                    type='str', 
                    choices=['wait','nowait','error'],
                    nickname='dataset_migrate_recall'),
                'If-None-Match': dict(required=False, type='str', nickname='dataset_checksum')
                # 'X-IBM-Record-Range': dict(required=False, type='str')
            },
            ok_rcode=200
        )
    )


def __get_dataset_api_argument_spec(api):
    """
    Return the details of the specific dataset API.
    :param str api: the name of API
    :rtype: dict[str, str/int/dict]
    """
    dataset_apis = __get_dataset_apis()
    if api in dataset_apis:
        return dataset_apis[api]


def __get_dataset_api_url(module, url):
    """
    Return the parsed URL of the specific dataset API.
    :param AnsibleModule module: the ansible module
    :param str url: the initial URL of API
    :param str response_key: the response key that can be used to retrieve the command response
    :param str detection_key: the detection key that can be used to retrieve the detect result for broadcast messages
    :rtype: str
    """
    # format the input for zmf_port
    port = ''
    if module.params['zmf_port'] is None:
        module.params['zmf_port'] = ''
    else:
        module.params['zmf_port'] = str(module.params['zmf_port']).strip()
    
    # set up full name of data set
    dataset_name = ''
    if module.params['dataset_volser'] is not None and module.params['dataset_volser'].strip() != '':
        dataset_name = '-(' + module.params['dataset_volser'].strip() + ')/' + module.params['dataset_src'].strip()
    else:
        dataset_name = module.params['dataset_src'].strip()

    matchObj = re.findall('{(.+?)}', url)
    for x in matchObj:
        if x == 'zmf_port' and module.params[x] == '':
            url = re.sub(':{' + x + '}', module.params[x], url)
        elif x == 'dataset_name':
            url = re.sub('{' + x + '}', dataset_name, url)
        else:
            url = re.sub('{' + x + '}', module.params[x].strip(), url)

    return url


def __get_dataset_api_params(module, args):
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


def call_dataset_api(module, session, api, customHeaders):
    """
    Return the response or error message of the specific dataset API.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str api: the name of API
    :rtype: dict or str
    """
    zmf_api = __get_dataset_api_argument_spec(api)
    zmf_api_url = __get_dataset_api_url(module, zmf_api['url'])
    zmf_api_params = None
    zmf_api_headers = None
    if 'args' in zmf_api:
        zmf_api_params = __get_dataset_api_params(module, zmf_api['args'])
    if 'headers' in zmf_api:
        zmf_api_headers = __get_dataset_api_params(module, zmf_api['headers'])  

    if customHeaders is not None:
        zmf_api_headers.update(customHeaders)

    print("debug-3: "+ str(zmf_api_params))
    print("debug-4: "+ str(zmf_api_headers))
    return handle_request_raw(module, session, zmf_api['method'], zmf_api_url, zmf_api_params, zmf_api_headers)


def get_request_argument_spec():
    """
    Return the arguments of ansible module used for dataset APIs.
    :rtype: (dict[str, dict])
    """
    argument_spec = dict()
    dataset_apis = __get_dataset_apis()
    for k, v in dataset_apis.items(): 
        variables = dict()
        if v['args'] is not None:
            variables.update(v['args'])
        if 'headers' in v.keys() and v['headers'] is not None:
            variables.update(v['headers'])
        for kk, vv in variables.items():
            if 'nickname' in vv and vv['nickname'] is not None and vv['nickname'] != '':
                argument_spec[vv['nickname']] = dict(required=False, type=vv['type'])
                if 'choices' in vv:
                    argument_spec[vv['nickname']].update(choices=vv['choices'])
                if 'default' in vv:
                    argument_spec[vv['nickname']].update(default=vv['default'])
            
    return argument_spec
