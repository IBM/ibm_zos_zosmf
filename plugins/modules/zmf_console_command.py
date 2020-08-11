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
short_description: Issue MVS command
description:
    - Issue MVS command by using a system console through z/OS console RESTful services.
    - Retrieve command response and define success condition based on specified keywords in the command response or broadcast messages.
    - Save the command response locally on control node.
version_added: "2.9"
author:
    - Yang Cao (@zosmf-Young)
    - Yun Juan Yang (@zosmf-Robyn)
options:
    zmf_credential:
        description:
            - Authentication credentials, returned by module C(zmf_authenticate), for the successfully authentication with z/OSMF server.
            - If I(zmf_credential) is supplied, I(zmf_host), I(zmf_port), I(zmf_user), I(zmf_password), I(zmf_crt) and I(zmf_key) are ignored.
        required: false
        type: dict
        default: null
        suboptions:
            LtpaToken2:
                description:
                    - The value of Lightweight Third Party Access (LTPA) token, which supports strong encryption.
                    - If I(jwtToken) is not supplied, I(LtpaToken2) is required.
                required: false
                type: str
                default: null
            jwtToken:
                description:
                    - The value of JSON Web token, which supports strong encryption.
                    - If I(LtpaToken2) is not supplied, I(jwtToken) is required.
                required: false
                type: str
                default: null
            zmf_host:
                description: Hostname of the z/OSMF server.
                required: true
                type: str
                default: null
            zmf_port:
                description: Port number of the z/OSMF server.
                required: false
                type: int
                default: null
    zmf_host:
        description:
            - Hostname of the z/OSMF server.
            - If I(zmf_credential) is supplied, I(zmf_host) is ignored.
            - If I(zmf_credential) is not supplied, I(zmf_host) is required.
        required: false
        type: str
        default: null
    zmf_port:
        description:
            - Port number of the z/OSMF server.
            - If I(zmf_credential) is supplied, I(zmf_port) is ignored.
        required: false
        type: int
        default: null
    zmf_user:
        description:
            - User name to be used for authenticating with z/OSMF server.
            - If I(zmf_credential) is supplied, I(zmf_user) is ignored.
            - If I(zmf_credential) is not supplied, I(zmf_user) is required when I(zmf_crt) and I(zmf_key) are not supplied.
            - If I(zmf_credential) is not supplied and I(zmf_crt) and I(zmf_key) are supplied, I(zmf_user) and I(zmf_password) are ignored.
        required: false
        type: str
        default: null
    zmf_password:
        description:
            - Password to be used for authenticating with z/OSMF server.
            - If I(zmf_credential) is supplied, I(zmf_password) is ignored.
            - If I(zmf_credential) is not supplied, I(zmf_password) is required when I(zmf_crt) and I(zmf_key) are not supplied.
            - If I(zmf_credential) is not supplied and I(zmf_crt) and I(zmf_key) are supplied, I(zmf_user) and I(zmf_password) are ignored.
        required: false
        type: str
        default: null
    zmf_crt:
        description:
            - Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication.
            - If I(zmf_credential) is supplied, I(zmf_crt) is ignored.
            - If I(zmf_credential) is not supplied, I(zmf_crt) is required when I(zmf_user) and I(zmf_password) are not supplied.
        required: false
        type: str
        default: null
    zmf_key:
        description:
            - Location of the PEM-formatted file with your private key to be used for HTTPS client authentication.
            - If I(zmf_credential) is supplied, I(zmf_key) is ignored.
            - If I(zmf_credential) is not supplied, I(zmf_key) is required when I(zmf_user) and I(zmf_password) are not supplied.
        required: false
        type: str
        default: null
    console_cmd:
        description:
            - Specifies the command to issue.
            - For more information, see the documentation for the z/OS console REST services.
        required: true
        type: str
        default: null
    console_system:
        description:
            - Nickname of the target z/OS system in the same sysplex that the command is routed to.
            - This variable should be specified as C({{ inventory_hostname }}), and its value should be specified in the inventory file as a managed node.
            - For more information, see the documentation for the z/OS console REST services.
        required: true
        type: str
        default: null
    console_name:
        description:
            - Name of the EMCS console that is used to issue the command.
            - If this value is omitted, the console name is generated by adding CN to the logon user ID.
            - For more information, see the documentation for the z/OS console REST services.
        required: false
        type: str
        default: null
    console_cmdresponse_keyword:
        description:
            - Specifies a keyword that you want to detect in the command response. Case is not significant.
            - This value can be a string or a regular expression. To use a regular expression, you must also set I(console_cmdresponse_reg=Y).
            - This parameter is designed to help user determine whether the command response matches with user's expectation.
            - If I(console_broadcastmsg_keyword) is not specified, the module will fail if the specified keyword can not be detected from the command response.
            - Otherwise, the module will fail if the specified keywords can not be detected from both command response and broadcast messages.
            - For more information, see the documentation for the z/OS console REST services.
        required: false
        type: str
        default: null
    console_cmdresponse_reg:
        description:
            - If I(console_cmdresponse_keyword) is specified, this variable specifies whether I(console_cmdresponse_keyword) represents a regular expression.
            - For more information, see the documentation for the z/OS console REST services.
        required: false
        type: str
        default: N
        choices:
            - Y
            - N
    console_broadcastmsg_keyword:
        description:
            - Specifies a keyword that you want to detect in broadcast messages. Case is not significant.
            - This value can be a string or a regular expression. To use a regular expression, you must also set I(console_broadcastmsg_reg=Y).
            - This parameter is designed to help user determine whether the broadcast messages issued after the command matches with user's expectation.
            - If I(console_cmdresponse_keyword) is not specified, the module will fail if the specified keyword can not be detected from broadcast messages.
            - Otherwise, the module will fail if the specified keywords can not be detected from both command response and broadcast messages.
            - For more information, see the documentation for the z/OS console REST services.
        required: false
        type: str
        default: null
    console_broadcastmsg_reg:
        description:
            - If I(console_broadcastmsg_keyword) is specified, this variable specifies whether I(console_broadcastmsg_keyword) represents a regular expression.
            - For more information, see the documentation for the z/OS console REST services.
        required: false
        type: str
        default: N
        choices:
            - Y
            - N
    console_broadcastmsg_detect_timeout:
        description:
            - Specifies how long, in seconds, the console attempts to detect the value of I(console_broadcastmsg_keyword) in broadcast messages.
            - For more information, see the documentation for the z/OS console REST services.
        required: false
        type: int
        default: 30
    console_cmdresponse_retrieve_times:
        description:
            - Specifies how many times the console attempts to retrieve the command response.
            - If the command response contains a large volume of messages, it will not arrive within a certain time interval.
            - In this case you might retrieve again several times to ensure that all messages related to the command are retrieved.
            - For more information, see the documentation for the z/OS console REST services.
        required: false
        type: int
        default: 1
    console_save_output_localpath:
        description:
            - The local path on control node where the command response should be saved to. For example, C(/tmp/cmd_output).
            - This path can be absolute or relative. The module will fail if parent directory of I(console_save_output_localpath) is a read-only file system.
            - The directory C({{ console_save_output_localpath }}/{{ inventory_hostname }}/) will be created to save the command response.
            - For example, C(/tmp/cmd_output/SY1/).
            - The command response will be saved as separate file and named as C({{ console_cmd }}).
            - For example, C(/tmp/cmd_output/SY1/display_a_l).
        required: false
        type: str
        default: null
requirements:
    - requests >= 2.23.0
"""

EXAMPLES = r"""
- name: Issue command to display active jobs
  zmf_console_command:
    zmf_host: "sample.ibm.com"
    console_cmd: "display a,l"
    console_system: "{{ inventory_hostname }}"

- name: Issue command to display active jobs and save the command response
  zmf_console_command:
    zmf_host: "sample.ibm.com"
    console_cmd: "display a,l"
    console_system: "{{ inventory_hostname }}"
    console_save_output_localpath: "/tmp/cmd_output"

- name: Issue command to start CIM server and detect if it is started successfully or not
  zmf_console_command:
    zmf_host: "sample.ibm.com"
    console_cmd: "start pegasus"
    console_system: "{{ inventory_hostname }}"
    console_cmdresponse_keyword: "SLP registration initiated"

- name: Issue command to start CIM server and detect if it is started successfully or not
  zmf_console_command:
    zmf_host: "sample.ibm.com"
    console_cmd: "start pegasus"
    console_system: "{{ inventory_hostname }}"
    console_broadcastmsg_keyword: "started CIM server"
"""

RETURN = r"""
changed:
    description: Indicates if any change is made during the module operation.
    returned: always
    type: bool
message:
    description:
        - The output message generated by the module to indicate whether the command is successful.
        - If either `console_cmdresponse_keyword` or `console_broadcastmsg_keyword` is specified, indicate whether the specified keyword is detected.
        - If `console_save_output_localpath` is specified, indicate whether the command response is saved locally.
    returned: on success
    type: str
    sample:
        sample1: "The command is issued successfully."
        sample2: "The command is issued successfully. The specified keyword is detected in the command response."
        sample3: "The command is issued successfully. The specified keyword is detected in broadcast messages."
        sample4: "The command is issued successfully. The command response is saved in: /tmp/output/SY1/display_a_l"
cmd_response:
    description: The command response.
    returned: on success
    type: list
    sample: [
        " CNZ4105I 04.32.31 DISPLAY ACTIVITY 458",
        "  JOBS     M/S    TS USERS    SYSAS    INITS   ACTIVE/MAX VTAM     OAS",
        " 00002    00015    00002      00032    00005    00001/00020       00011",
        "  VLF      VLF      VLF      NSW  S  IGVDGNPP IGVDGNPP PRIMEPSA OWT  S",
        "  VTAM44   VTAM44   VTAM     NSW  S  RACF     RACF     RACF     NSW  S",
        "  GRSSTMON GRSSTMON STEP1    OWT  S  SDSF23   SDSF23   SDSF     NSW  S",
        "  HZR      HZR      IEFPROC  NSW  S  JES2     JES2     IEFPROC  NSW  S",
        "  SDSFAUX  SDSFAUX  SDSFAUX  NSW  S  TCAS     TCAS     TSO      OWT  S",
        "  TCPIP    TCPIP    TCPIP    NSW  SO RESOLVER RESOLVER EZBREINI NSW  SO",
        "  RRS      RRS      RRS      NSW  S  OMPROUTE OMPROUTE OMPROUTE NSW  SO",
        "  INETD1   STEP1    INETD    OWT  AO FTPDEV1  STEP1    FTPD     OWT  AO",
        "  PEGASUS  PEGASUS  *OMVSEX  IN   SO",
        " IBMUSER  OWT      ZOSMFAD  IN   O"
    ]
cmdresponse_keyword_detected:
    description: Indicate whether the specified keyword is detected in the command response.
    returned: on success when `console_cmdresponse_keyword` is specified
    type: bool
broadcastmsg_keyword_detected:
    description: Indicate whether the specified keyword is detected in broadcast messages.
    returned: on success when `console_broadcastmsg_keyword` is specified
    type: bool
detected_broadcastmsg:
    description: The message that contains the specified keyword that was detected in broadcast messages.
    returned: on success when `console_broadcastmsg_keyword` is specified
    type: list
    sample: [
        " BPXM023I (ZOSMFAD) CFZ10030I: Started CIM Server version 2.14.2."
    ]
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
from time import sleep
import json
import re
import os


def format_message_to_list(message):
    message = message.replace('\n', '')
    msg_list = message.split('\r')
    return msg_list


def format_message_to_file(msg_list):
    for i in range(len(msg_list)):
        msg_list[i] = msg_list[i] + '\n'
    return msg_list


def format_cmd_to_str(cmd):
    cmd = cmd.replace(',', ' ')
    cmd = cmd.replace('=', ' ')
    cmd_list = cmd.split(' ')
    cmd_str = ''
    for i in range(len(cmd_list)):
        v = cmd_list[i].replace('"', '').replace("'", '').replace('(', '').replace(')', '')
        if v.strip() != '':
            if i == 0:
                cmd_str = v
            else:
                cmd_str = cmd_str + '_' + v
    return cmd_str


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
    response_issue = call_console_api(module, session, 'issue')
    if isinstance(response_issue, dict):
        if 'cmd-response' in response_issue:
            cmd_response = response_issue['cmd-response']
            # handle route issue
            if 'IEE618I' in cmd_response:
                module.fail_json(msg='Failed to issue the command ---- IEE618I ROUTE COMMAND REJECTED, INVALID SYSTEM NAME.')
            elif 'IEE345I' in cmd_response:
                module.fail_json(msg='Failed to issue the command ---- IEE345I ROUTE AUTHORITY INVALID, FAILED BY SECURITY PRODUCT.')
            else:
                issue_result['changed'] = True
                response_key = response_issue['cmd-response-key']
                cmd_response = format_message_to_list(cmd_response)
        else:
            module.fail_json(msg='Failed to issue the command ---- No response is returned.')
    else:
        module.fail_json(msg='Failed to issue the command ---- ' + response_issue)
    # step2 - detect keyword
    if module.params['console_cmdresponse_keyword'] is not None and module.params['console_cmdresponse_keyword'].strip() != '':
        issue_result['cmdresponse_keyword_detected'] = response_issue['sol-key-detected']
    if module.params['console_broadcastmsg_keyword'] is not None and module.params['console_broadcastmsg_keyword'].strip() != '':
        if response_issue['status'] == 'detected':
            issue_result['broadcastmsg_keyword_detected'] = True
            issue_result['detected_broadcastmsg'] = format_message_to_list(response_issue['msg'])
        else:
            issue_result['broadcastmsg_keyword_detected'] = False
    # step3 - retrieve the command response and detect again
    check_delay = 2
    check_times = module.params['console_cmdresponse_retrieve_times']
    while check_times > 0:
        response_getResponse = call_console_api(module, session, 'getResponse', response_key)
        if isinstance(response_getResponse, dict):
            if 'cmd-response' in response_getResponse and response_getResponse['cmd-response'].strip() != '':
                # detect again
                if 'cmdresponse_keyword_detected' in issue_result and issue_result['cmdresponse_keyword_detected'] is False:
                    if (module.params['console_cmdresponse_reg'] == 'Y'
                            and re.findall(module.params['console_cmdresponse_keyword'], response_issue['cmd-response'])):
                        issue_result['cmdresponse_keyword_detected'] = True
                    elif module.params['console_cmdresponse_keyword'].upper() in response_getResponse['cmd-response'].upper():
                        issue_result['cmdresponse_keyword_detected'] = True
                # append the retrieved response
                cmd_response = cmd_response + format_message_to_list(response_getResponse['cmd-response'])
                sleep(check_delay)
            check_times = check_times - 1
        else:
            module.fail_json(msg='Failed to retrieve the command response ---- ' + response_getResponse)
    issue_result['cmd_response'] = cmd_response
    # step4 - save to local if console_save_output_localpath is defined
    save_message = ''
    if module.params['console_save_output_localpath'] is not None and module.params['console_save_output_localpath'].strip() != '':
        if module.params['console_save_output_localpath'].endswith('/'):
            save_path = module.params['console_save_output_localpath'] + module.params['console_system'] + '/'
        else:
            save_path = module.params['console_save_output_localpath'] + '/' + module.params['console_system'] + '/'
        if not os.path.exists(save_path):
            os.makedirs(save_path, 0o755, True)
        else:
            os.chmod(save_path, 0o755)
        save_file = format_cmd_to_str(module.params['console_cmd'])
        f_write = open(save_path + save_file, 'w')
        f_write.writelines(format_message_to_file(cmd_response))
        f_write.close()
        save_message = ' The command response is saved in: ' + save_path + save_file
    # step5 - decide if detect fails or not
    if 'cmdresponse_keyword_detected' not in issue_result and 'broadcastmsg_keyword_detected' not in issue_result:
        issue_result['message'] = 'The command is issued successfully.' + save_message
    elif 'cmdresponse_keyword_detected' in issue_result and issue_result['cmdresponse_keyword_detected'] is True:
        issue_result['message'] = 'The command is issued successfully. The specified keyword is detected in the command response.' + save_message
    elif 'broadcastmsg_keyword_detected' in issue_result and issue_result['broadcastmsg_keyword_detected'] is True:
        issue_result['message'] = 'The command is issued successfully. The specified keyword is detected in broadcast messages.' + save_message
    else:
        module.fail_json(
            cmd_response=cmd_response,
            msg='The command is issued successfully. But no specified keywords are detected in neither the command response nor broadcast messages.'
                + save_message
        )
    module.exit_json(**issue_result)


def main():
    argument_spec = dict()
    connect_argument_spec = get_connect_argument_spec()
    request_argument_spec = get_request_argument_spec()
    argument_spec.update(connect_argument_spec)
    argument_spec.update(request_argument_spec)
    argument_spec.update(
        console_name=dict(required=False, type='str'),
        console_cmdresponse_retrieve_times=dict(required=False, type='int', default=1),
        console_save_output_localpath=dict(required=False, type='str'))
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    issue_command(module)


if __name__ == '__main__':
    main()
