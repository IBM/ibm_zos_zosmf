# Copyright (c) IBM Corporation 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_util import handle_request
import json
import re


def __get_console_apis():
    """
    Return the details of all z/OS console services APIs.
    :rtype: dict[str, dict]
    """
    return dict(
        # issue a command by using a system console
        issue=dict(
            method='put',
            header={'Content-Type': 'application/json'},
            url='https://{zmf_host}:{zmf_port}/zosmf/restconsoles/consoles/{console_name}',
            args={
                'cmd': dict(required=True, type='str', nickname='console_cmd'),
                'sol-key': dict(required=False, type='str', nickname='console_cmdresponse_keyword'),
                'unsol-key': dict(required=False, type='str', nickname='console_broadcastmsg_keyword'),
                'solKeyReg': dict(
                    required=False, type='str', default='N', nickname='console_cmdresponse_reg',
                    choices=['Y', 'N']
                ),
                'unsolKeyReg': dict(
                    required=False, type='str', default='N', nickname='console_broadcastmsg_reg',
                    choices=['Y', 'N']
                ),
                'async': dict(required=False, type='str', default='N', nickname=''),
                'unsol-detect-sync': dict(required=False, type='str', default='Y', nickname=''),
                'detect-time': dict(required=False, type='int', default='30', nickname='console_broadcastmsg_detect_timeout'),
                'unsol-detect-timeout': dict(required=False, type='int', default='30', nickname='console_broadcastmsg_detect_timeout'),
                'system': dict(required=True, type='str', nickname='console_system')
            },
            ok_rcode=200
        ),
        # get the detect result for broadcast messages after a command is issued
        getDetection=dict(
            method='get',
            url='https://{zmf_host}:{zmf_port}/zosmf/restconsoles/consoles/{console_name}/detections/{detection_key}',
            args=dict(),
            ok_rcode=200
        ),
        # get the command response after a command is issued
        getResponse=dict(
            method='get',
            url='https://{zmf_host}:{zmf_port}/zosmf/restconsoles/consoles/{console_name}/solmsgs/{response_key}',
            args=dict(),
            ok_rcode=200
        )
    )


def __get_console_api_argument_spec(api):
    """
    Return the details of the specific console API.
    :param str api: the name of API
    :rtype: dict[str, str/int/dict]
    """
    console_apis = __get_console_apis()
    if api in console_apis:
        return console_apis[api]


def __get_console_api_url(module, url, response_key=None, detection_key=None):
    """
    Return the parsed URL of the specific console API.
    :param AnsibleModule module: the ansible module
    :param str url: the initial URL of API
    :param str response_key: the response key that can be used to retrieve the command response
    :param str detection_key: the detection key that can be used to retrieve the detect result for broadcast messages
    :rtype: str
    """
    # format the input for zmd_port
    if module.params['zmf_port'] is None:
        module.params['zmf_port'] = ''
    else:
        module.params['zmf_port'] = str(module.params['zmf_port']).strip()
    if module.params['console_name'] is None or module.params['console_name'].strip() == '':
        module.params['console_name'] = 'defcn'
    matchObj = re.findall('{(.+?)}', url)
    for x in matchObj:
        if ((x == 'detection_key' and (detection_key is None or detection_key.strip() == ''))
                or (x == 'response_key' and (response_key is None or response_key.strip() == ''))):
            module.fail_json(msg='Missing required argument or invalid argument: ' + x + '.')
        if x == 'zmf_port' and module.params[x] == '':
            url = re.sub(':{' + x + '}', module.params[x], url)
        elif x == 'response_key':
            url = re.sub('{' + x + '}', response_key.strip(), url)
        elif x == 'detection_key':
            url = re.sub('{' + x + '}', detection_key.strip(), url)
        else:
            url = re.sub('{' + x + '}', module.params[x].strip(), url)
    return url


def __get_console_api_params(module, args):
    """
    Return the parsed params of the specific console API.
    :param AnsibleModule module: the ansible module
    :param dict[str, dict] args: the initial params of API
    :rtype: dict[str, str/list]
    """
    params = dict()
    for k, v in args.items():
        if v['nickname'] != '' and module.params[v['nickname']] is not None and str(module.params[v['nickname']]).strip() != '':
            # format the input for params with choices
            if 'choices' in v:
                found = False
                for vv in v['choices']:
                    if module.params[v['nickname']].strip().lower() == vv.lower():
                        found = True
                        params[k] = vv
                        break
                if found is False:
                    module.fail_json(
                        msg='Missing required argument or invalid argument: ' + v['nickname'] + '. The following values are valid: ' + str(v['choices']) + '.'
                    )
            else:
                params[k] = str(module.params[v['nickname']]).strip()
        elif v['nickname'] != '' and v['required'] is True:
            module.fail_json(msg='Missing required argument or invalid argument: ' + v['nickname'] + '.')
        elif 'default' in v:
            params[k] = v['default']
    if 'solKeyReg' in params and params['solKeyReg'] == 'N':
        params.pop('solKeyReg')
    if 'unsolKeyReg' in params and params['unsolKeyReg'] == 'N':
        params.pop('unsolKeyReg')
    return params


def call_console_api(module, session, api, response_key=None, detection_key=None):
    """
    Return the response or error message of the specific console API.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str api: the name of API
    :param str response_key: the response key that can be used to retrieve the command response
    :param str detection_key: the detection key that can be used to retrieve the detect result for broadcast messages
    :rtype: dict or str
    """
    zmf_api = __get_console_api_argument_spec(api)
    zmf_api_url = __get_console_api_url(module, zmf_api['url'], response_key, detection_key)
    zmf_api_params = __get_console_api_params(module, zmf_api['args'])
    if 'detect-time' in zmf_api_params and int(zmf_api_params['detect-time']) >= 30:
        timeout = int(zmf_api_params['detect-time']) + 5
    else:
        timeout = 30
    if 'header' in zmf_api:
        return handle_request(module, session, zmf_api['method'], zmf_api_url, zmf_api_params, zmf_api['ok_rcode'], zmf_api['header'], timeout)
    else:
        return handle_request(module, session, zmf_api['method'], zmf_api_url, zmf_api_params, zmf_api['ok_rcode'], None, timeout)


def get_request_argument_spec():
    """
    Return the arguments of ansible module used for console APIs.
    :rtype: (dict[str, dict])
    """
    argument_spec = dict()
    console_apis = __get_console_apis()
    for k, v in console_apis.items():
        for kk, vv in v['args'].items():
            if vv['nickname'] != '':
                argument_spec[vv['nickname']] = dict(required=False, type=vv['type'])
                if 'choices' in vv:
                    argument_spec[vv['nickname']].update(choices=vv['choices'])
                if 'default' in vv:
                    argument_spec[vv['nickname']].update(default=vv['default'])
    return argument_spec
