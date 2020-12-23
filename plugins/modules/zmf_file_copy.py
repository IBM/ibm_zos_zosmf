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
module: zmf_file_copy
short_description: Copy data to z/OS USS file
description:
    - Copy data from Ansible control node to a z/OS UNIX System Services (USS) file on the remote z/OS system.
    - If the target USS file already exists, it can be overwritten. If the target USS file does not exist, it can be created with mode 644.
version_added: "2.9"
author:
    - Yang Cao (@zosmf-Young)
    - Yun Juan Yang (@zosmf-Robyn)
options:
    zmf_credential:
        description:
            - Authentication credentials, returned by module C(zmf_authenticate), for the successful authentication with z/OSMF server.
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
    file_src:
        description:
            - The local path on control node of the data to be copied to the target USS file. For example, C(/tmp/file_input/profile).
            - This path can be absolute or relative. The module will fail if I(file_src) has no read permission.
            - The data is interpreted as one of binary, text or 'diff -e' format according to the value of I(file_data_type) and I(file_diff).
            - If I(file_content) is supplied and I(file_data_type=text), I(file_src) is ignored.
        required: false
        type: str
        default: null
    file_content:
        description:
            - The contents to be copied to the target USS file. This variable is used instead of I(file_src).
            - This variable only take effects when I(file_data_type=text).
            - Each line of the contents should be terminated with C(\n). For example, C(Sample profile\nTZ=EST5EDT\n).
            - If I(file_content) is supplied and I(file_data_type=text), I(file_src) is ignored.
        required: false
        type: str
        default: null
    file_dest:
        description:
            - USS file on the remote z/OS system where the data should be copied to.
            - This variable must consist of a fully qualified path and file name. For example, C(/etc/profile).
        required: true
        type: str
        default: null
    file_force:
        description:
            - Specifies whether the target USS file must always be overwritten.
            - If I(file_force=true), the target USS file will always be overwritten.
            - If I(file_force=false), the data will only be copied if the target USS file does not exist.
        required: false
        type: bool
        default: true
    file_data_type:
        description:
            - Specifies whether data conversion is to be performed on the data to be copied.
            - When I(file_data_type=text), data conversion is performed.
            - You can use I(file_encoding) to specify which encodings the data to be copied should be converted from and to.
            - If I(file_encoding) is not supplied, the data transfer process converts each byte from C(ISO8859-1) to C(IBM-1047) by default.
            - You can use I(file_crlf) to control whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF).
            - If I(file_crlf) is not supplied, LF characters are left intact by default.
            - You can use I(file_diff) to specify whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command.
            - If I(file_diff) is not supplied, the input is regarded as not consisting of commands by default.
            - When I(file_data_type=binary), no data conversion is performed.
        required: false
        type: str
        default: text
        choices:
            - text
            - binary
    file_encoding:
        description:
            - Specifies which encodings the data to be copied should be converted from and to.
            - These parameters only take effects when I(file_data_type=text) and I(file_diff=false).
        required: false
        type: dict
        default: null
        suboptions:
            from:
                description:
                    - The character set of the data to be copied.
                    - Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.
                required: true
                type: str
            to:
                description:
                    - The destination character set for the target USS file.
                    - Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.
                required: true
                type: str
    file_crlf:
        description:
            - Specifies whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF).
            - This variable only take effects when I(file_data_type=text).
        required: false
        type: bool
        default: false
    file_diff:
        description:
            - Specifies whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command.
            - These commands are used to add, replace and delete lines in the target USS file. The following commands are supported.
            - C(a)
            - C(c)
            - C(d)
            - C(s/.//)
            - opt C(g|<n>), where C(g) means global, C(n) means search and replace C(n) times.
            - Each command may be optionally preceded by a line or line range, as allowed by the z/OS UNIX 'ed' command.
            - The module will fail if an error is detected while processing a command.
            - This variable only take effects when I(file_data_type=text).
        required: false
        type: bool
        default: false
    file_checksum:
        description:
            - Specifies the checksum to be used to verify that the target USS file to copy to is not changed since the checksum was generated.
            - If the checksum is not matched which means the target USS file has been modified, the data won't be copied to the target USS file.
            - This variable only take effects when I(file_force=true).
        required: False
        type: str
        default: null
requirements:
    - requests >= 2.23.0
"""

EXAMPLES = r"""
- name: Copy a local file to USS file /etc/profile
  zmf_file_copy:
    zmf_host: "sample.ibm.com"
    file_src: "/tmp/file_input/profile"
    file_dest: "/etc/profile"

- name: Copy a local file to USS file /etc/profile only if it does not exist
  zmf_file_copy:
    zmf_host: "sample.ibm.com"
    file_src: "/tmp/file_input/profile"
    file_dest: "/etc/profile"
    file_force: false

- name: Copy the contents to USS file /etc/profile
  zmf_file_copy:
    zmf_host: "sample.ibm.com"
    file_conntent: "Sample profile\nTZ=EST5EDT\n"
    file_dest: "/etc/profile"

- name: Copy a local file to USS file /etc/profile as binary
  zmf_file_copy:
    zmf_host: "sample.ibm.com"
    file_src: "/tmp/file_input/profile"
    file_dest: "/etc/profile"
    file_data_type: "binary"

- name: Copy a local file to USS file /etc/profile and convert from ISO8859-1 to IBM-037
  zmf_file_copy:
    zmf_host: "sample.ibm.com"
    file_src: "/tmp/file_input/profile"
    file_dest: "/etc/profile"
    file_encoding:
      from: ISO8859-1
      to: IBM-037

- name: Copy a local file to USS file /etc/profile and validate its checksum
  zmf_file_copy:
    zmf_host: "sample.ibm.com"
    file_src: "/tmp/file_input/profile"
    file_dest: "/etc/profile"
    file_checksum: "93822124D6E66E2213C64B0D10800224"
"""

RETURN = r"""
changed:
    description: Indicates if any change is made during the module operation.
    returned: always
    type: bool
message:
    description: The output message generated by the module to indicate whether the USS file is successfully copied.
    returned: on success
    type: str
    sample:
        sample1: "The target USS file /etc/profile is created and updated successfully."
        sample2: "The target USS file /etc/profile is updated successfully."
        sample7: "No data is copied since the target USS file /etc/profile exists and file_force is set to False."
file_checksum:
    description: The checksum of the updated USS file.
    returned: on success
    type: str
    sample: "93822124D6E66E2213C64B0D10800224"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_util import (
    get_connect_argument_spec,
    get_connect_session
)
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_file_api import (
    call_file_api
)


def validate_module_params(module):
    # validate file_src and file_content
    if ((module.params['file_src'] is None or module.params['file_src'].strip() == '')
            and (module.params['file_content'] is None or module.params['file_content'].strip() == '')):
        module.fail_json(msg='Missing required argument or invalid argument: either file_src or file_content is required.')
    # validate file_dest
    if not (module.params['file_dest'] is not None and module.params['file_dest'].strip() != ''):
        module.fail_json(msg='Missing required argument or invalid argument: file_dest.')
    # validate file_force and file_checksum
    if module.params['file_force'] is False and module.params['file_checksum'] is not None and module.params['file_checksum'].strip() != '':
        module.fail_json(msg='file_checksum is valid only when file_force=true.')
    # validate file_data_type
    if module.params['file_data_type'] != 'text':
        if module.params['file_encoding'] is not None:
            module.fail_json(msg='file_encoding is valid only when file_data_type=text.')
        if module.params['file_crlf'] is True:
            module.fail_json(msg='file_crlf is valid only when file_data_type=text.')
        if module.params['file_diff'] is True:
            module.fail_json(msg='file_diff is valid only when file_data_type=text.')
        if not (module.params['file_src'] is not None and module.params['file_src'].strip() != ''):
            module.fail_json(msg='file_src is required when file_data_type=binary.')
    # validate file_encoding
    if module.params['file_encoding'] is not None:
        if isinstance(module.params['file_encoding'], dict):
            has_from = False
            has_to = False
            for k, v in module.params['file_encoding'].items():
                if k == 'from':
                    has_from = True
                    if v is not None and str(v).strip() != '':
                        module.params['file_encoding']['from'] = str(v).strip()
                    else:
                        module.fail_json(msg='Invalid argument: file_encoding. Missing required suboption or invalid suboption: from.')
                elif k == 'to':
                    has_to = True
                    if v is not None and str(v).strip() != '':
                        module.params['file_encoding']['to'] = str(v).strip()
                    else:
                        module.fail_json(msg='Invalid argument: file_encoding. Missing required suboption or invalid suboption: to.')
                else:
                    module.fail_json(
                        msg='Invalid argument: file_encoding. It should be a dict and contain the following suboptions only: '
                            + 'from(required), to(required).'
                    )
            if not has_from:
                module.fail_json(msg='Invalid argument: file_encoding. Missing required suboption or invalid suboption: from.')
            if not has_to:
                module.fail_json(msg='Invalid argument: file_encoding. Missing required suboption or invalid suboption: to.')
        else:
            module.fail_json(
                msg='Invalid argument: file_encoding. It should be a dict and contain the following suboptions only: '
                    + 'from(required), to(required).'
            )
        if module.params['file_diff'] is True:
            module.fail_json(msg='file_encoding is valid only when file_diff=false.')


def copy_file(module):
    """
    Copy data to a USS file
    Return the message to indicate whether the USS file is successfully copied.
    Return file_checksum of the checksum of the USS file.
    :param AnsibleModule module: the ansible module
    """
    copy_result = dict(
        changed=False,
        message='',
    )
    # create session
    session = get_connect_session(module)
    copy_dest = module.params['file_dest'].strip()
    if not copy_dest.startswith('/'):
        copy_dest = '/' + copy_dest
    copy_src = None
    if module.params['file_src'] is not None and module.params['file_src'].strip() != '':
        copy_src = module.params['file_src'].strip()
    # step1 - check if the target USS file exists when file_force=false
    if module.params['file_force'] is False:
        res_list = call_file_api(module, session, 'list')
        res_cd = res_list.status_code
        if res_list.status_code == 200:
            # not fail - no data is copied since the target USS file exists
            copy_result['message'] = 'No data is copied since the target USS file ' + copy_dest + ' exists and file_force is set to False.'
            module.exit_json(**copy_result)
    # step2 - read file_src or file_content
    f_read = None
    request_body = None
    if module.params['file_data_type'] != 'text':
        try:
            f_read = open(copy_src, 'rb')
            request_body = f_read.read()
        except OSError as ex:
            module.fail_json(msg='Failed to copy data to the target USS file ' + copy_dest + ' ---- OS error: ' + str(ex))
    else:
        if module.params['file_content'] is not None and module.params['file_content'].strip() != '':
            request_body = module.params['file_content']
        else:
            try:
                f_read = open(copy_src, 'r')
                request_body = f_read.read()
            except OSError as ex:
                module.fail_json(msg='Failed to copy data to the target USS file ' + copy_dest + ' ---- OS error: ' + str(ex))
    if f_read is not None:
        f_read.close()
    # step3 - combine request headers
    request_headers = dict()
    request_headers['X-IBM-Data-Type'] = module.params['file_data_type']
    request_headers['Content-Type'] = 'text/plain'
    if module.params['file_data_type'] == 'text':
        if module.params['file_diff'] is True:
            request_headers['Content-Type'] = 'application/x-ibm-diff-e'
        if module.params['file_encoding'] is not None:
            request_headers['X-IBM-Data-Type'] += ';fileEncoding=' + module.params['file_encoding']['to']
            request_headers['Content-Type'] += ';charset=' + module.params['file_encoding']['from']
        if module.params['file_crlf'] is True:
            request_headers['X-IBM-Data-Type'] += ';crlf=true'
    if module.params['file_checksum'] is not None and module.params['file_checksum'].strip() != '':
        request_headers['If-Match'] = module.params['file_checksum'].strip()
    # step4 - copy data to the target USS file
    res_copy = call_file_api(module, session, 'copy', request_headers, request_body)
    res_cd = res_copy.status_code
    if res_cd != 201 and res_cd != 204:
        # handle response error
        if res_cd == 412:
            # fail - file has been modified when file_checksum is specified (412)
            module.fail_json(
                msg='Failed to copy data to the target USS file ' + copy_dest + ' ---- the target USS file has been modified and its checksum is: '
                + res_copy.headers['Etag']
            )
        else:
            # fail - return JSON error report
            res_error = res_copy.json()
            module.fail_json(
                msg='Failed to copy data to the target USS file ' + copy_dest + ' ---- Http request error: '
                + str(res_cd) + ': ' + str(res_error)
            )
    else:
        # handle response
        copy_result['changed'] = True
        copy_result['file_checksum'] = res_copy.headers['Etag']
        if res_cd == 201:
            # success - a new USS file is created (201)
            copy_result['message'] = 'The target USS file ' + copy_dest + ' is created and updated successfully.'
        else:
            # success - an existing USS file is updated (204)
            copy_result['message'] = 'The target USS file ' + copy_dest + ' is updated successfully.'
        module.exit_json(**copy_result)


def main():
    argument_spec = dict()
    argument_spec.update(get_connect_argument_spec())
    argument_spec.update(
        file_src=dict(required=False, type='str'),
        file_content=dict(required=False, type='str'),
        file_dest=dict(required=True, type='str'),
        file_force=dict(required=False, type='bool', default=True),
        file_data_type=dict(required=False, type='str', default='text', choices=['text', 'binary']),
        file_encoding=dict(required=False, type='dict'),
        file_crlf=dict(required=False, type='bool', default=False),
        file_diff=dict(required=False, type='bool', default=False),
        file_checksum=dict(required=False, type='str')
    )
    argument_spec['file_encoding']['from'] = dict(required=True, type='str')
    argument_spec['file_encoding']['to'] = dict(required=True, type='str')
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    validate_module_params(module)
    copy_file(module)


if __name__ == '__main__':
    main()
