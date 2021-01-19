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
module: zmf_file
short_description: Manage z/OS USS file or directory
description:
    - Create, delete and operate on a z/OS UNIX System Services (USS) file or a directory on the remote z/OS system.
    - The available operations include rename, change mode, change owner and change tag.
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
    file_path:
        description:
            - Path to the USS file or directory being managed.
            - This variable must consist of a fully qualified path and file or directory name. For example, C(/etc/profile).
            - The module will fail if parent directory of I(file_path) does not exist or is a read-only file system.
        required: true
        type: str
    file_state:
        description:
            - The final state desired for specified USS file or directory.
            - >
              If I(state=file) and I(file_path) does not exist,
              I(file_path) is created as a USS file, the module completes successfully with C(changed=True).
            - >
              If I(state=directory) and I(file_path) does not exist,
              I(file_path) is created as a directory, the module completes successfully with C(changed=True).
            - >
              If I(state=file) or I(state=directory), and I(file_path) exists,
              I(file_path) is modified with other supplied variables (e.g., I(file_mode)), the module completes successfully with C(changed=True).
            - >
              If I(state=file) or I(state=directory), and I(file_path) exists,
              no action taken if no other variables are supplied (e.g., I(file_mode)), the module completes successfully with C(changed=False).
            - >
              If I(state=absent) and I(file_path) does not exist,
              no action taken, the module completes successfully with C(changed=False).
            - >
              If I(state=absent) and I(file_path) exists,
              the existing I(file_path) is deleted, the module completes successfully with C(changed=True).
        required: true
        type: str
        choices:
            - file
            - directory
            - absent
    file_rename:
        description:
            - Specifies the new name of the USS file or directory.
            - This variable only take effects when I(state=file) or I(state=directory).
        required: false
        type: str
        default: null
    file_mode:
        description:
            - Specifies the permission the resulting USS file or directory should have.
            - This variable only take effects when I(state=file) or I(state=directory).
            - If I(file_path) does not exist, this value is used in creating I(file_path). If this value is omitted, 755 is used by default.
            - If I(file_path) exists, this value is used in changing mode of I(file_path).
        required: false
        type: dict
        default: null
        suboptions:
            mode:
                description:
                    - The value of file mode bits.
                    - This value could be either the POSIX symbolic form (e.g., C(RWXRW-RW-)) or octal value (e.g., C(755)).
                required: true
                type: str
            recursive:
                description:
                    - This variable only take effects when I(state=directory).
                    - When I(recursive=true), the file mode bits of the directory and all files in the file hierarchy below it are changed (chmod -R).
                required: false
                type: bool
                default: false
    file_owner:
        description:
            - Indicates the function change owner.
            - This variable only take effects when I(state=file) or I(state=directory).
        required: false
        type: dict
        default: null
        suboptions:
            owner:
                description: The user ID or UID.
                required: true
                type: str
            group:
                description: The group ID or GID.
                required: false
                type: str
                default: null
            recursive:
                description:
                    - This variable only take effects when I(state=directory).
                    - When I(recursive=true), changes all the files and subdirectories in that directory to belong to the specified owner and group (chown -R).
                required: false
                type: bool
                default: false
    file_tag:
        description:
            - Indicates the function change tag.
            - This variable only take effects when I(state=file) or I(state=directory).
        required: false
        type: dict
        default: null
        suboptions:
            tag:
                description:
                    - The type of file tag.
                    - If I(tag=absent), any existing file tag is removed.
                required: true
                type: str
                choices:
                    - mixed
                    - text
                    - binary
                    - absent
            codeset:
                description:
                    - Specifies the coded character set in which text data is encoded, such as ASCII or EBCDIC.
                    - For example, the code set for ASCII is ISO8859–1; the code set for EBCDIC is IBM-1047.
                    - This variable only take effects when I(tag=mixed) or I(tag=text).
                    - This variable is required when I(tag=text).
                required: false
                type: str
                default: null
            recursive:
                description:
                    - This variable only take effects when I(state=directory).
                    - When I(recursive=true), tags all the files and subdirectories in that directory (chtag -R).
                required: false
                type: bool
                default: false
requirements:
    - requests >= 2.23.0
"""

EXAMPLES = r"""
- name: Create a USS file /etc/profile with default mode 755
  zmf_file:
    zmf_host: "sample.ibm.com"
    file_path: "/etc/profile"
    file_state: "file"

- name: Create a directory /etc/some_directory with mode 644
  zmf_file:
    zmf_host: "sample.ibm.com"
    file_path: "/etc/some_directory"
    file_state: "directory"
    file_mode:
        mode: "644"

- name: Change the permissions, owner, group and tag of a USS file /etc/profile
  zmf_file:
    zmf_host: "sample.ibm.com"
    file_path: "/etc/profile"
    file_state: "file"
    file_mode:
        mode: "644"
    file_owner:
        owner: "ibmuser"
        group: "ibmuser"
    file_tag:
        tag: "text"
        codeset: "IBM-1047"

- name: Change the permissions of a directory /etc/some_directory, and recursively change its owner, group and tag
  zmf_file:
    zmf_host: "sample.ibm.com"
    file_path: "/etc/some_directory"
    file_state: "directory"
    file_mode:
        mode: "644"
        recursive: false
    file_owner:
        owner: "ibmuser"
        group: "ibmuser"
        recursive: true
    file_tag:
        tag: "text"
        codeset: "IBM-1047"
        recursive: true

- name: Rename a USS file /etc/profile to /etc/profile.bak
  zmf_file:
    zmf_host: "sample.ibm.com"
    file_path: "/etc/profile"
    file_state: "file"
    file_rename: "/etc/profile.bak"

- name: Delete a USS file /etc/profile
  zmf_file:
    zmf_host: "sample.ibm.com"
    file_path: "/etc/profile"
    file_state: "absent"
"""

RETURN = r"""
changed:
    description: Indicates if any change is made during the module operation.
    returned: always
    type: bool
message:
    description: The output message generated by the module to indicate whether the USS file or directory is successfully created, deleted, or updated.
    returned: on success
    type: str
    sample:
        sample1: "The file /etc/profile is created successfully."
        sample2: "The directory /etc/some_directory is deleted successfully."
        sample3: "The file or directory /etc/profile does not exist."
        sample4: "The file /etc/profile already exists."
        sample5: "The file /etc/profile is updated successfully."
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_util import (
    get_connect_argument_spec,
    get_connect_session
)
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_file_api import (
    call_file_api
)
import json
import re


def format_mode(module, mode, to_octal):
    # validate mode
    matchChar = re.findall('^[-rwxRWX]{9}$', mode)
    matchNum = re.findall('^[0-7]{3}$', mode)
    if len(matchChar) == 0 and len(matchNum) == 0:
        module.fail_json(
            msg='Invalid argument: file_mode. Invalid suboption: mode, it should be either '
                + 'the POSIX symbolic form (e.g., RWXRW-RW-) or octal value (e.g., 755).'
        )
    # format mode
    if to_octal is None:
        return mode
    elif to_octal is True:
        if len(matchNum) > 0:
            return matchNum[0]
        else:
            m = matchChar[0]
            b = re.sub(r'[rwx]', '1', re.sub('-', '0', m))
            o = oct(int(b, 2))[2:]
            return o.zfill(3)
    else:
        if len(matchChar) > 0:
            return matchChar[0]
        else:
            m = matchNum[0]
            r = 'rwxrwxrwx'
            s = ''
            for i in range(8, -1, -1):
                if ((int('0o' + m, 8) >> i) & 1) == 1:
                    s = s + r[8 - i]
                else:
                    s = s + '-'
            return s


def validate_module_params(module):
    # validate file_path
    if not (module.params['file_path'] is not None and module.params['file_path'].strip() != '' and not module.params['file_path'].strip().endswith('/')):
        module.fail_json(msg='Missing required argument or invalid argument: file_path.')
    # validate file_state
    if module.params['file_state'] == 'absent':
        if module.params['file_rename'] is not None and module.params['file_rename'].strip() != '':
            module.fail_json(msg='file_rename is valid only when file_state=file or file_state=directory.')
        if module.params['file_mode'] is not None:
            module.fail_json(msg='file_mode is valid only when file_state=file or file_state=directory.')
        if module.params['file_owner'] is not None:
            module.fail_json(msg='file_owner is valid only when file_state=file or file_state=directory.')
        if module.params['file_tag'] is not None:
            module.fail_json(msg='file_tag is valid only when file_state=file or file_state=directory.')
    # validate file_mode
    if module.params['file_mode'] is not None:
        if isinstance(module.params['file_mode'], dict):
            has_mode = False
            for k, v in module.params['file_mode'].items():
                if k == 'mode':
                    has_mode = True
                    if v is not None and str(v).strip() != '':
                        module.params['file_mode']['mode'] = format_mode(module, str(v).strip().lower(), None)
                    else:
                        module.fail_json(msg='Invalid argument: file_mode. Missing required suboption or invalid suboption: mode.')
                elif k == 'recursive':
                    if (str(v) == '1' or str(v).lower() == 'yes' or str(v).lower() == 'y'
                            or str(v).lower() == 'true' or str(v).lower() == 't' or str(v).lower() == 'on'):
                        module.params['file_mode']['recursive'] = True
                    elif (str(v) == '0' or str(v).lower() == 'no' or str(v).lower() == 'n'
                            or str(v).lower() == 'false' or str(v).lower() == 'f' or str(v).lower() == 'off'):
                        module.params['file_mode']['recursive'] = False
                    else:
                        module.fail_json(msg='Invalid argument: file_mode. Invalid suboption: recursive, it must be a boolean.')
                else:
                    module.fail_json(
                        msg='Invalid argument: file_mode. It should be a dict and contain the following suboptions only: '
                            + 'mode(required), recursive.'
                    )
            if not has_mode:
                module.fail_json(msg='Invalid argument: file_mode. Missing required suboption or invalid suboption: mode.')
        else:
            module.fail_json(
                msg='Invalid argument: file_mode. It should be a dict and contain the following suboptions only: '
                    + 'mode(required), recursive.'
            )
    # validate file_owner
    if module.params['file_owner'] is not None:
        if isinstance(module.params['file_owner'], dict):
            has_owner = False
            for k, v in module.params['file_owner'].items():
                if k == 'owner':
                    has_owner = True
                    if v is not None and str(v).strip() != '':
                        module.params['file_owner']['owner'] = str(v).strip()
                    else:
                        module.fail_json(msg='Invalid argument: file_owner. Missing required suboption or invalid suboption: owner.')
                elif k == 'group':
                    if v is not None and str(v).strip() != '':
                        module.params['file_owner']['group'] = str(v).strip()
                elif k == 'recursive':
                    if (str(v) == '1' or str(v).lower() == 'yes' or str(v).lower() == 'y'
                            or str(v).lower() == 'true' or str(v).lower() == 't' or str(v).lower() == 'on'):
                        module.params['file_owner']['recursive'] = True
                    elif (str(v) == '0' or str(v).lower() == 'no' or str(v).lower() == 'n'
                            or str(v).lower() == 'false' or str(v).lower() == 'f' or str(v).lower() == 'off'):
                        module.params['file_owner']['recursive'] = False
                    else:
                        module.fail_json(msg='Invalid argument: file_owner. Invalid suboption: recursive, it must be a boolean.')
                else:
                    module.fail_json(
                        msg='Invalid argument: file_owner. It should be a dict and contain the following suboptions only: '
                            + 'owner(required), group, recursive.'
                    )
            if not has_owner:
                module.fail_json(msg='Invalid argument: file_owner. Missing required suboption or invalid suboption: owner.')
        else:
            module.fail_json(
                msg='Invalid argument: file_owner. It should be a dict and contain the following suboptions only: '
                    + 'owner(required), group, recursive.'
            )
    # validate file_tag
    if module.params['file_tag'] is not None:
        if isinstance(module.params['file_tag'], dict):
            has_tag = False
            for k, v in module.params['file_tag'].items():
                if k == 'tag':
                    has_tag = True
                    if (v is not None and str(v).strip() != ''
                            and (str(v).strip() == 'mixed' or str(v).strip() == 'text' or str(v).strip() == 'binary' or str(v).strip() == 'absent')):
                        module.params['file_tag']['tag'] = str(v).strip()
                    else:
                        module.fail_json(
                            msg='Invalid argument: file_tag. Missing required suboption or invalid suboption: tag, the following values are valid: '
                                + '[mixed, text, binary, absent].'
                        )
                elif k == 'codeset':
                    if v is not None and str(v).strip() != '':
                        module.params['file_tag']['codeset'] = str(v).strip()
                elif k == 'recursive':
                    if (str(v) == '1' or str(v).lower() == 'yes' or str(v).lower() == 'y'
                            or str(v).lower() == 'true' or str(v).lower() == 't' or str(v).lower() == 'on'):
                        module.params['file_tag']['recursive'] = True
                    elif (str(v) == '0' or str(v).lower() == 'no' or str(v).lower() == 'n'
                            or str(v).lower() == 'false' or str(v).lower() == 'f' or str(v).lower() == 'off'):
                        module.params['file_tag']['recursive'] = False
                    else:
                        module.fail_json(msg='Invalid argument: file_tag. Invalid suboption: recursive, it must be a boolean.')
                else:
                    module.fail_json(
                        msg='Invalid argument: file_tag. It should be a dict and contain the following suboptions only: '
                            + 'tag(required), codeset, recursive.'
                    )
            if not has_tag:
                module.fail_json(msg='Invalid argument: file_tag. Missing required suboption or invalid suboption: tag.')
            if module.params['file_tag']['tag'] == 'text':
                if not ('codeset' in module.params['file_tag'] and module.params['file_tag']['codeset'].strip() != ''):
                    module.fail_json(msg='Invalid argument: file_tag. Invalid suboption: codeset, it is required when tag=text.')
            elif module.params['file_tag']['tag'] == 'binary':
                if 'codeset' in module.params['file_tag'] and module.params['file_tag']['codeset'].strip() != '':
                    module.fail_json(msg='Invalid argument: file_tag. Invalid suboption: codeset, it is valid only when tag=mixed or tag=text.')
        else:
            module.fail_json(
                msg='Invalid argument: file_tag. It should be a dict and contain the following suboptions only: '
                    + 'tag(required), codeset, recursive.'
            )


def file_exist(module):
    """
    Check if a USS file or directory already exists
    Return exist_result to indicate if a USS file or directory with same name already exists.
    :param AnsibleModule module: the ansible module
    """
    exist_result = dict(
        type=None
    )
    # create session
    session = get_connect_session(module)
    target = module.params['file_path'].strip()
    if not target.startswith('/'):
        target = '/' + target
    exist_result['session'] = session
    exist_result['target'] = target
    # setup file parent path and file name
    f_path = target[:target.rfind('/')]
    f_name = target[target.rfind('/') + 1:]
    if f_path.startswith('/'):
        f_path = f_path[1:]
    module.params['f_path'] = f_path
    module.params['f_name'] = f_name
    # step1 - check if the target USS file or directory with same name already exists
    res_list = call_file_api(module, session, 'list')
    if res_list.status_code == 200:
        res_content = json.loads(res_list.content)
        if 'returnedRows' in res_content and res_content['returnedRows'] == 1:
            exist_result['properties'] = res_content['items'][0]
            if res_content['items'][0]['mode'].startswith('d'):
                exist_result['type'] = 'directory'
            else:
                exist_result['type'] = 'file'
            # list tag of the target USS file or directory
            request_body = dict()
            request_body['request'] = 'chtag'
            request_body['action'] = 'list'
            request_headers = dict()
            request_headers['Content-Type'] = 'application/json'
            res_operate = call_file_api(module, session, 'operate', request_headers, json.dumps(request_body))
            if res_operate.status_code == 200:
                res_content = json.loads(res_operate.content)
                if 'stdout' in res_content:
                    exist_result['properties']['tag'] = res_content['stdout'][0]
    else:
        res_json = res_list.json()
        if (res_list.status_code == 404 and 'category' in res_json and 'rc' in res_json and 'reason' in res_json
                and res_json['category'] == 1 and res_json['rc'] == 4 and res_json['reason'] == 8):
            # parent path not found
            exist_result['type'] = 'error'
    return exist_result


def create_file(module, session, target):
    """
    Create a USS file or directory
    Return the message to indicate whether the USS file or directory is created successfully.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str target: the USS file or directory to be created
    """
    create_result = dict(
        changed=False,
        message='',
    )
    # step1 - setup request args
    module.params['f_create_type'] = module.params['file_state']
    if module.params['file_mode'] is not None:
        module.params['f_create_mode'] = format_mode(module, module.params['file_mode']['mode'], False)
    else:
        module.params['f_create_mode'] = 'rwxr-xr-x'
    # step2 - setup request headers
    request_headers = dict()
    request_headers['Content-Type'] = 'application/json'
    # step3 - create the USS file or directory
    res_create = call_file_api(module, session, 'create', request_headers)
    if res_create.status_code == 201:
        create_result['changed'] = True
        create_result['message'] = 'The ' + module.params['file_state'] + ' ' + target + ' is created successfully.'
        operate_result = operate_file(module, session, target, None)
        if operate_result['message'] != '':
            create_result['message'] += ' ' + operate_result['message']
        if 'properties' in operate_result:
            create_result['properties'] = operate_result['properties']
        if 'errors' not in operate_result:
            module.exit_json(**create_result)
        else:
            create_result['errors'] = operate_result['errors']
            module.fail_json(msg=str(create_result))
    else:
        module.fail_json(
            msg='Failed to create ' + module.params['file_state'] + ' ' + target + ' ---- Http request error: '
                + str(res_create.status_code) + ': ' + str(res_create.json())
        )


def delete_file(module, session, target, exist):
    """
    Delete a USS file or directory
    Return the message to indicate whether the USS file or directory is deleted successfully.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str target: the USS file or directory to be deleted
    :param bool exist: whether the USS file or directory to be deleted exists or not
    """
    delete_result = dict(
        changed=False,
        message='',
    )
    # step1 - exit if the USS file or directory to be deleted does not exist
    if not exist:
        delete_result['message'] = 'The file or directory ' + target + ' does not exist.'
        module.exit_json(**delete_result)
    # step2 - setup request headers
    request_headers = dict()
    request_headers['X-IBM-Option'] = 'recursive'
    # step3 - delete the USS file or directory
    res_delete = call_file_api(module, session, 'delete', request_headers)
    if res_delete.status_code == 204:
        delete_result['changed'] = True
        delete_result['message'] = 'The file or directory ' + target + ' is deleted successfully.'
        module.exit_json(**delete_result)
    else:
        module.fail_json(
            msg='Failed to delete ' + target + ' ---- Http request error: '
                + str(res_delete.status_code) + ': ' + str(res_delete.json())
        )


def operate_file(module, session, target, old_properties):
    """
    Operate on a USS file or directory
    Return the message to indicate whether the USS file or directory is updated successfully.
    Return the properties of the updated USS file or directory.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str target: the USS file or directory to be operated
    :param dict old_properties: the old properties of the USS file or directory
    """
    operate_result = dict(
        changed=False,
        message='',
    )
    need_update = False
    need_rename = False
    new = ''
    # step1 - operate on the USS file or directory
    if old_properties is not None and module.params['file_mode'] is not None:
        need_update = True
        chmod = operate_file_action(module, session, 'chmod', target)
        if chmod['updated'] is True:
            operate_result['changed'] = True
        else:
            if 'errors' not in operate_result:
                operate_result['errors'] = []
            operate_result['errors'].append('Failed to change mode for the ' + module.params['file_state'] + ' ' + target + chmod['error'])
    if module.params['file_owner'] is not None:
        need_update = True
        chown = operate_file_action(module, session, 'chown', target)
        if chown['updated'] is True:
            operate_result['changed'] = True
        else:
            if 'errors' not in operate_result:
                operate_result['errors'] = []
            operate_result['errors'].append('Failed to change owner for the ' + module.params['file_state'] + ' ' + target + chown['error'])
    if module.params['file_tag'] is not None:
        need_update = True
        chtag = operate_file_action(module, session, 'chtag', target)
        if chtag['updated'] is True:
            operate_result['changed'] = True
        else:
            if 'errors' not in operate_result:
                operate_result['errors'] = []
            operate_result['errors'].append('Failed to change tag for the ' + module.params['file_state'] + ' ' + target + chtag['error'])
    if module.params['file_rename'] is not None and module.params['file_rename'].strip() != '':
        need_rename = True
        rename = operate_file_action(module, session, 'move', target)
        if rename['updated'] is True:
            operate_result['changed'] = True
            new = rename['new']
        else:
            if 'errors' not in operate_result:
                operate_result['errors'] = []
            operate_result['errors'].append('Failed to rename for the ' + module.params['file_state'] + ' ' + target + rename['error'])
    # step2 - return the roperties of the USS file or directory
    if old_properties is not None and (need_update is not True and need_rename is not True):
        operate_result['properties'] = old_properties
        operate_result['message'] = 'The ' + module.params['file_state'] + ' ' + target + ' already exists.'
        module.exit_json(**operate_result)
    else:
        res_list = call_file_api(module, session, 'list')
        if res_list.status_code == 200:
            res_content = json.loads(res_list.content)
            if 'returnedRows' in res_content and res_content['returnedRows'] == 1:
                operate_result['properties'] = res_content['items'][0]
                # list tag of the target USS file or directory
                request_body = dict()
                request_body['request'] = 'chtag'
                request_body['action'] = 'list'
                request_headers = dict()
                request_headers['Content-Type'] = 'application/json'
                res_operate = call_file_api(module, session, 'operate', request_headers, json.dumps(request_body))
                if res_operate.status_code == 200:
                    res_content = json.loads(res_operate.content)
                    if 'stdout' in res_content:
                        operate_result['properties']['tag'] = res_content['stdout'][0]
        if need_update is True:
            if 'errors' not in operate_result:
                operate_result['message'] = 'The ' + module.params['file_state'] + ' ' + target + ' is updated successfully. '
            else:
                operate_result['message'] = 'Failed to update the ' + module.params['file_state'] + ' ' + target + '. '
        if need_rename is True:
            if new != '':
                operate_result['message'] += 'The ' + module.params['file_state'] + ' ' + target + ' is successfully renamed to ' + new + '.'
            else:
                operate_result['message'] += 'Failed to rename the ' + module.params['file_state'] + ' ' + target + '.'
        if old_properties is None:
            return operate_result
        else:
            if 'errors' not in operate_result:
                module.exit_json(**operate_result)
            else:
                module.fail_json(msg=str(operate_result))


def operate_file_action(module, session, action, target):
    """
    Operate on a USS file or directory
    Return operate_result_action to indicate whether each operation for the USS file or directory is successfully.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str action: the operation
    :param str target: the USS file or directory to be operated
    """
    operate_result_action = dict(
        updated=False,
        error=''
    )
    old_f_path = module.params['f_path']
    old_f_name = module.params['f_name']
    # step1 - setup request args
    request_body = dict()
    request_body['request'] = action
    if action == 'chmod':
        # chmod
        request_body['mode'] = format_mode(module, module.params['file_mode']['mode'], True)
        if 'recursive' in module.params['file_mode']:
            request_body['recursive'] = module.params['file_mode']['recursive']
    elif action == 'chown':
        # chown
        request_body['owner'] = module.params['file_owner']['owner']
        if 'group' in module.params['file_owner']:
            request_body['group'] = module.params['file_owner']['group']
        if 'recursive' in module.params['file_owner']:
            request_body['recursive'] = module.params['file_owner']['recursive']
    elif action == 'chtag':
        # chtag
        if module.params['file_tag']['tag'] == 'absent':
            request_body['action'] = 'remove'
        else:
            request_body['action'] = 'set'
            request_body['type'] = module.params['file_tag']['tag']
        if 'codeset' in module.params['file_tag']:
            request_body['codeset'] = module.params['file_tag']['codeset']
        if 'recursive' in module.params['file_tag']:
            request_body['recursive'] = module.params['file_tag']['recursive']
    elif action == 'move':
        # rename
        new = module.params['file_rename'].strip()
        if not new.startswith('/'):
            new = '/' + new
        # setup file parent path and file name
        f_path = new[:new.rfind('/')]
        f_name = new[new.rfind('/') + 1:]
        if f_path.startswith('/'):
            f_path = f_path[1:]
        module.params['f_path'] = f_path
        module.params['f_name'] = f_name
        request_body['from'] = target
    # step2 - setup request headers
    request_headers = dict()
    request_headers['Content-Type'] = 'application/json'
    # step3 - operate on the USS file or directory
    res_operate = call_file_api(module, session, 'operate', request_headers, json.dumps(request_body))
    if res_operate.status_code == 200:
        operate_result_action['updated'] = True
        if action == 'move':
            operate_result_action['new'] = new
    else:
        # reset file parent path and file name if rename is failed
        if action == 'move':
            module.params['f_path'] = old_f_path
            module.params['f_name'] = old_f_name
        try:
            res_content = res_operate.json()
        except Exception:
            res_content = res_operate.content
        operate_result_action['error'] = ' ---- Http request error: ' + str(res_operate.status_code) + ': ' + str(res_content)
    return operate_result_action


def main():
    argument_spec = dict()
    argument_spec.update(get_connect_argument_spec())
    argument_spec.update(
        file_path=dict(required=True, type='str'),
        file_state=dict(required=True, type='str', choices=['file', 'directory', 'absent']),
        file_rename=dict(required=False, type='str'),
        file_mode=dict(required=False, type='dict'),
        file_owner=dict(required=False, type='dict'),
        file_tag=dict(required=False, type='dict')
    )
    argument_spec['file_mode']['mode'] = dict(required=True, type='str')
    argument_spec['file_mode']['recursive'] = dict(required=False, type='bool', default=False)
    argument_spec['file_owner']['owner'] = dict(required=True, type='str')
    argument_spec['file_owner']['group'] = dict(required=False, type='str')
    argument_spec['file_owner']['recursive'] = dict(required=False, type='bool', default=False)
    argument_spec['file_tag']['tag'] = dict(required=True, type='str', choices=['mixed', 'text', 'binary', 'absent'])
    argument_spec['file_tag']['codeset'] = dict(required=False, type='str')
    argument_spec['file_tag']['recursive'] = dict(required=False, type='bool', default=False)
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    # validate params
    validate_module_params(module)
    # check if exists
    exist_result = file_exist(module)
    if exist_result['type'] == 'file':
        if module.params['file_state'] == 'absent':
            delete_file(module, exist_result['session'], exist_result['target'], True)
        elif module.params['file_state'] == 'file':
            operate_file(module, exist_result['session'], exist_result['target'], exist_result['properties'])
        else:
            module.fail_json(msg='Failed to create directory ' + exist_result['target'] + ' ---- A file with same name already exists.')
    elif exist_result['type'] == 'directory':
        if module.params['file_state'] == 'absent':
            delete_file(module, exist_result['session'], exist_result['target'], True)
        elif module.params['file_state'] == 'directory':
            operate_file(module, exist_result['session'], exist_result['target'], exist_result['properties'])
        else:
            module.fail_json(msg='Failed to create file ' + exist_result['target'] + ' ---- A directory with same name already exists.')
    elif exist_result['type'] == 'error':
        if module.params['file_state'] == 'absent':
            delete_file(module, exist_result['session'], exist_result['target'], False)
        else:
            module.fail_json(msg='Failed to create ' + module.params['file_state'] + ' ' + exist_result['target'] + ' ---- Parent path not found.')
    else:
        if module.params['file_state'] == 'absent':
            delete_file(module, exist_result['session'], exist_result['target'], False)
        else:
            create_file(module, exist_result['session'], exist_result['target'])


if __name__ == '__main__':
    main()
