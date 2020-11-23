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
module: zmf_dataset
short_description: Operates a z/OS data set or member
description:
    - Retrieve the contents of a z/OS data set or member and store the content to a local file
    - Write data to a z/OS data set or member from a local file
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
    dataset_src:
        description:
            - 
        required: true
        type: str
        default: null
    dataset_dest:
        description:
            - 
        required: true
        type: str
        default: null
    dataset_volser:
        description:
            - 
        required: false
        type: str
        default: null
    dataset_search:
        description:
            - 
        required: false
        type: str
        default: null
    dataset_search_insensitive:
        description:
            - 
        required: false
        type: bool
        default: true
    dataset_search_maxreturnsize:
        description:
            - 
        required: false
        type: int
        default: 100
    # TODO: checksum
    dataset_checksum:
        description:
            - 
        required: false
        type: str
        default: null
    dataset_validate_checksum:
        description:
            -
        required: false
        type: bool
        default: yes
    dataset_return_checksum_when_large:
        description:
            - 
        required: false
        type: bool
        default: false
    dataset_data_type:
        description:
            - 
        required: false
        type: str
        default: text
        choices:
            - text
            - binary
            - record
    dataset_migrate_recall:
        description:
            - 
        required: false
        type: str
        default: wait
        choices:
            - wait
            - nowait
            - error
    dataset_read_start:
        description:
            - 
        required: false
        type: int
        default: null
    dataset_read_end:
        description:
            - 
        required: false
        type: int
        default: null
    
requirements:
    - requests >= 2.23.0
"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if the data set is updated.
    returned: always
    type: bool
message:
    description:
        - 
    returned: on success
    type: str
    sample:
        sample1: "The data set is read successfully."
        sample2: "The data set is updated successfully."
dataset_content:
    description: The 
    returned: on success when 'state' is 'read'
    type: str 
    sample: "ABC..."
search_records:
    description: 
    returned: on success when `dataset_search` is specified
    type: list
    sample: [
        " ABC...",
        "...ABC"
    ]
checksum:
    description: 
    returned: on success
    type: str
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_util import (
    get_connect_argument_spec,
    get_connect_session
)
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_dataset_api import (
    get_request_argument_spec,
    call_dataset_api
)
from time import sleep
import json
import re
import os


def fetch_dataset(module):
    """
    Call z/OSMF REST file and data set interface to read data set or member
    """
    cmd_response = ''
    response_key = ''
    issue_result = dict(
        changed=False,
        message='',
    )

    # create session
    session = get_connect_session(module)

    # # combine custom headers
    customHeaders = dict()
    if (module.params['dataset_validate_checksum'] is not None and
            module.params['dataset_validate_checksum'] and
            module.params['dataset_checksum'] is not None and
            module.params['dataset_checksum'].strip() != ''):
        customHeaders['If-None-Match'] = module.params['dataset_checksum'].strip()

    read_start = 0
    read_end = 0
    if module.params['dataset_read_start'] is not None:
        read_start = module.params['dataset_read_start']
    if module.params['dataset_read_end'] is not None:
        read_end = module.params['dataset_read_end']
    if not (read_start == 0 and read_end == 0):
        customHeaders['X-IBM-Record-Range'] = str(read_start) + '-' + str(read_end)

    # # fetch dataset
    response_fetch = call_dataset_api(module, session, 'fetch', customHeaders)
    result_fetch = dict()
    result_fetch['changed'] = False
    status_code = response_fetch.status_code
    if status_code != 304 and status_code != 200:
        # handle response error
        response_error = response_fetch.json()
        module.fail_json(msg='Failed to fetch data set ---- Http request error: ' + str(status_code)) + ': return-code=' + str(response_error['return-code']) \
            + ' reason-code=' + str(response_error['reason-code']) + ' reason=' + response_error['reason']
    else:
        # set checksum
        print("debug6-headers: "+ str(response_fetch.headers))
        if 'Etag' in response_fetch.headers:
            checksum = response_fetch.headers['Etag']
            result_fetch['checksum'] = checksum
        if status_code == 304:
            result_fetch['message'] = 'The data set is not fetched because the checksum of source is matched with the supplied one.'
        elif status_code == 200:
            if response_fetch.headers['Content-Type'] is not None:
                content_type = response_fetch.headers['Content-Type']
                if content_type.startswith('application/json'):
                    # set search results to result_fetch
                    dataset_search = response.json()
                    result_fetch['dataset_search_result'] = dataset_search
                    result_fetch['message'] = 'The data set is fetched successfully. The search result is returned in "dataset_search_result."'
                else:
                    dest = module.params['dataset_dest'].strip()
                    if not dest.endswith('/'):
                        dest += '/'
                    if module.params['dataset_volser'] is not None and module.params['dataset_volser'].strip() != '':
                        dest = dest + module.params['dataset_volser'] + '/'

                    save_file = module.params['dataset_src'].strip()
                    save_file = save_file.replace('(', '/')
                    save_file = save_file.replace(')', '')
                    if save_file.find('/'):
                        tmp_path = save_file.split('/')
                        dest += tmp_path[0] + '/'
                        save_file = tmp_path[1]

                    print('debug7-dest: '+ dest +', file: '+ save_file)
                    if not os.path.exists(dest):
                        os.makedirs(dest, 0o755)
                    else:
                        os.chmod(dest, 0o755)

                    data_type = 'text'
                    if content_type.startswith('text/plain'):
                        # save text to file and set text to result_fetch
                        f_write = open(dest + save_file, 'w')
                        dataset_content = response_fetch.text
                        f_write.write(dataset_content)
                        f_write.close()
                        result_fetch['dataset_content'] = dataset_content
                    elif content_type.startswith(''):
                        # save binary files
                        data_type = module.params['dataset_data_type'].strip()
                        f_write = open(dest + save_file, 'wb')
                        dataset_binary = response_fetch.content
                        f_write.write(dataset_binary)
                        f_write.close()
                    
                    result_fetch['message'] = 'The data set is fetched successfully. The content is saved in: ' + dest + save_file + ' in ' + data_type + ' mode.'
            else:
                module.fail_json(msg='Failed to read data set ---- Content-Type is missing in the response.')
    
    module.exit_json(**result_fetch)


def main():
    argument_spec = dict()
    connect_argument_spec = get_connect_argument_spec()
    request_argument_spec = get_request_argument_spec()
    argument_spec.update(connect_argument_spec)
    argument_spec.update(request_argument_spec)
    argument_spec.update(
        dataset_src=dict(required=True, type='str'),
        dataset_dest=dict(required=False, type='str'),
        dataset_volser=dict(required=False, type='str'),
        dataset_checksum=dict(required=False, type='str'),
        dataset_validate_checksum=dict(required=False, type='bool'),
        dataset_read_start=dict(required=False, type='int'),
        dataset_read_end=dict(required=False, type='int'))

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )

    # # validate dataset_src
    if module.params['dataset_src'].strip() == '':
        module.fail_json(msg='Invalid "variable dataset_src", it must not be an empty string.')
    
    # # validate dataset_read_start and dataset_read_end
    if module.params['dataset_read_start'] is not None and module.params['dataset_read_start'] < 0:
        module.fail_json(msg='Invalid variable "dataset_read_start", it must be a natural number.')
    if module.params['dataset_read_end'] is not None and module.params['dataset_read_end'] < 0:
        module.fail_json(msg='Invalid variable "dataset_read_end", it must be a natural number.')
    if (module.params['dataset_read_start'] is not None and 
            module.params['dataset_read_end'] is not None and
            module.params['dataset_read_end'] < module.params['dataset_read_start']):
        module.fail_json(msg='Invalid variables, if "dataset_read_start" and "dataset_read_end" both specified' + 
            '"dataset_read_end" must larger than "dataset_read_start"')
    
    fetch_dataset(module)
        
if __name__ == '__main__':
    main()
