#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) IBM Corporation 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r"""
---
module: zmf_console_command
short_description: Ansible module for issuing a command by using a system console
description:
    - Ansible module for issuing a command by using a system console through z/OSMF console services.
version_added: "2.9"
author:
    - Yang Cao (@zosmf-Young)
    - Yun Juan Yang (@zosmf-Robyn)
options:
# TODO
requirements:
    - requests >= 2.23.0
"""

EXAMPLES = r"""
# TODO
"""

RETURN = r"""
# TODO
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_util import (
    get_connect_argument_spec,
    get_connect_session
)
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_console_api import (
    get_request_argument_spec,
    call_console_api
)
import json
import re
from time import sleep


def format_message(message):
    message = message.replace('\n', '')
    msg_list = message.split('\r')
    return msg_list

def issue_command(module):
    """
    Issue a command by using a system console.
    Return the message to indicate the command is successful.
    Return the cmd_response of the issued command.
    Return the cmdresponse_keyword_detected flag to indicate whether the specified keyword is detected in command response.
    Return the broadcastmsg_keyword_detected flag to indicate whether the specified keyword is detected in broadcast messages.
    Return the detected_broadcastmsg of the detected message in broadcast messages if broadcastmsg_keyword_detected is True.
    :param AnsibleModule module: the ansible module
    """
    cmd_response = ''
    response_key = ''
    issue_result = dict(
        changed=False,
        message='',
    )
    # create session
    session = get_connect_session(module)
    # step1 - issue a command
    response_issue = call_console_api(module, session, 'issue', module.params['console_name'])
    if isinstance(response_issue, dict):
        cmd_response = response_issue['cmd-response']
        # handle route issue
        if 'IEE618I' in cmd_response:
            module.fail_json(msg='Failed to issue a command ---- IEE618I ROUTE COMMAND REJECTED, INVALID SYSTEM NAME.')
        elif 'IEE345I' in cmd_response:
            module.fail_json(msg='Failed to issue a command ---- IEE345I ROUTE AUTHORITY INVALID, FAILED BY SECURITY PRODUCT.')
        else:
            issue_result['changed'] = True
            response_key = response_issue['cmd-response-key']
            cmd_response = format_message(cmd_response)
    else:
        module.fail_json(msg='Failed to issue a command ---- ' + response_issue)
    # step2 - detect keyword
    if module.params['console_cmdresponse_keyword'] is not None and module.params['console_cmdresponse_keyword'].strip() != '':
        issue_result['cmdresponse_keyword_detected'] = response_issue['sol-key-detected']
    if module.params['console_broadcastmsg_keyword'] is not None and module.params['console_broadcastmsg_keyword'].strip() != '':
        if response_issue['status'] == 'detected':
            issue_result['broadcastmsg_keyword_detected'] = True
            issue_result['detected_broadcastmsg'] = format_message(response_issue['msg'])
        else:
            issue_result['broadcastmsg_keyword_detected'] = False
    # step3 - retrieve the command response and detect again
    check_delay = 2
    check_times = module.params['console_cmdresponse_retrieve_times']
    while check_times > 0:
        response_getResponse = call_console_api(module, session, 'getResponse', module.params['console_name'], response_key)
        if isinstance(response_getResponse, dict):
            if response_getResponse['cmd-response'] is not None and response_getResponse['cmd-response'].strip() != '':
                # detect again
                if 'cmdresponse_keyword_detected' in issue_result and issue_result['cmdresponse_keyword_detected'] is False:
                    if module.params['console_cmdresponse_reg'] == 'Y' \
                        and re.findall(module.params['console_cmdresponse_keyword'], response_issue['cmd-response']):
                        issue_result['cmdresponse_keyword_detected'] = True
                    elif module.params['console_cmdresponse_keyword'].upper() in response_getResponse['cmd-response'].upper():
                        issue_result['cmdresponse_keyword_detected'] = True
                # append the retrieved response
                cmd_response = cmd_response + format_message(response_getResponse['cmd-response'])
                sleep(check_delay)
            check_times = check_times - 1
        else:
            module.fail_json(msg='Failed to retrieve the command response ---- ' + response_getResponse)
    issue_result['cmd_response'] = cmd_response
    # step4 - decide if detect fails or not
    if 'cmdresponse_keyword_detected' not in issue_result and 'broadcastmsg_keyword_detected' not in issue_result:
        issue_result['message'] = 'The command is successful.'
    elif 'cmdresponse_keyword_detected' in issue_result and issue_result['cmdresponse_keyword_detected'] is True:
        issue_result['message'] = 'The command is successful. The specified keyword is detected.'
    elif 'broadcastmsg_keyword_detected' in issue_result and issue_result['broadcastmsg_keyword_detected'] is True:
        issue_result['message'] = 'The command is successful. The specified keyword is detected.'
    else:
        module.fail_json(msg='The command is failed. The specified keyword is not detected.')
    module.exit_json(**issue_result)


def main():
    argument_spec = dict()
    connect_argument_spec = get_connect_argument_spec()
    request_argument_spec = get_request_argument_spec()
    argument_spec.update(connect_argument_spec)
    argument_spec.update(request_argument_spec)
    argument_spec.update(
        console_name=dict(required=False, type='str', default='defcn'),
        console_cmdresponse_retrieve_times=dict(required=False, type='int', default=1))
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    issue_command(module)


if __name__ == '__main__':
    main()
