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
module: zmf_dataset_fetch
short_description: Operates a z/OS data set or member
description:
    - Retrieve the contents of a z/OS data set or member and store the content to a local file.
    - Write data to a z/OS data set or member from a local file.
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
            - Data set or data set member name on the remote z/OS system to fetch.
            - For example, specifying a data set like C(ZOSMF.ANSIBLE.DATA), or a data set member like C(ZOSMF.ANSIBLE.PDS(MEMBER)).
        required: true
        type: str
    dataset_dest:
        description:
            - The local directory on control node where the data set should be saved to. For example, C(/tmp/dataset).
            - This directory can be absolute or relative. The module will fail if the parent directory of I(dataset_dest) is a read-only file system.
            - The directory C({{ dataset_dest }}/{{ zmf_host }}/) will be created to save the data set, where I(zmf_host) is the hostname of the z/OSMF server.
            - If I(zmf_host=zosmf.ibm.com), a dataset named C(ZOSMF.ANSIBLE.DATA) would be saved into C({{dataset_dest}}/zosmf.ibm.com/ZOSMF.ANSIBLE.DATA).
            - If I(dataset_volser=VOL001), the above dataset would be saved into C({{dataset_dest}}/zosmf.ibm.com/VOL001/ZOSMF.ANSIBLE.DATA).
        required: true
        type: str
    dataset_volser:
        description:
            - The volume serial identify the volume to be searched for an uncataloged data set or member.
            - The length of the volume serial cannot exceed six characters. You cannot use wildcard characters for this parameter.
        required: false
        type: str
        default: null
    dataset_flat:
        description:
            - Specifies whether to override the default behavior of appending I(zmf_host) to the destination.
            - If I(dataset_flat=true), the data set will be fetched to the destination directory using its name without appending I(zmf_host).
            - For example, if I(dataset_dest=/tmp/dataset), a data set named C(ZOSMF.ANSIBLE.DATA) would be saved into C(/tmp/dataset/ZOSMF.ANSIBLE.DATA).
        required: false
        type: bool
        default: false
    dataset_search:
        description:
            - Specifies a series of parameters that are used to search the content of data set or member.
            - These parameters only take effects when I(dataset_data_type=text).
            - If this variable is specified, only the matched records in the data set will be fetched to the destination directory.
            - Records are returned starting with the first matching record. The I(dataset_range) may be used to specify the range of records to be searched.
            - The matched contents in the data set will be saved as C({{ dataset_dest }}/{{ zmf_host }}/{{ dataset_src }}.search) on control node.
            - For example, the matched contents in the dataset named C(ZOSMF.ANSIBLE.DATA) would be saved as C(/tmp/dataset/ZOSMF.ANSIBLE.DATA.search).
        required: false
        type: dict
        default: null
        suboptions:
            keyword:
                description:
                    - Specifies a string or a regular expression that is used to search the data set.
                required: false
                type: str
                default: null
            insensitive:
                description:
                    - Specifies whether the comparison of I(keyword) is case insensitive.
                    - This variable only take effects when I(keyword) is defined.
                required: false
                type: bool
                default: true
            maxreturnsize:
                description:
                    - The maximum number of records to return.
                    - This variable only take effects when I(keyword) is defined.
                required: false
                type: int
                default: 100
    dataset_data_type:
        description:
            - Specifies whether data conversion is to be performed on the returned data.
            - When I(dataset_data_type=text), data conversion is performed.
            - You can use I(dataset_encoding) to specify which encodings the fetched data set should be converted from and to.
            - If I(dataset_encoding) is not supplied, the data transfer process converts each record from C(IBM-1047) to C(ISO8859-1) by default.
            - When I(dataset_data_type=binary), no data conversion is performed. The data transfer process returns each line of data as-is.
            - When I(dataset_data_type=record), no data conversion is performed. Each logical record is preceded by the 4-byte big endian record length.
        required: false
        type: str
        default: text
        choices:
            - text
            - binary
            - record
    dataset_encoding:
        description:
            - Specifies which encodings the fetched data set should be converted from and to.
            - These parameters only take effects when I(dataset_data_type=text).
        required: false
        type: dict
        default: null
        suboptions:
            from:
                description:
                    - The character set of the source data set. Select an alternate EBCDIC code page.
                required: true
                type: str
                default: IBM-1047
            to:
                description:
                    - The destination character set for the output to be written as.
                required: true
                type: str
                default: ISO8859-1
    dataset_range:
        description:
            - Specifies a range that is used to retrieve records of the data set.
            - If this variable is specified, only the retrieved range of the data set will be fetched to the destination directory.
            - The retrieved range of the data set will be saved as C({{ dataset_dest }}/{{ zmf_host }}/{{ dataset_src }}.range) on control node.
            - For example, the retrieved range of the dat set named C(ZOSMF.ANSIBLE.DATA) would be saved as C(/tmp/dataset/ZOSMF.ANSIBLE.DATA.range).
        required: false
        type: dict
        default: null
        suboptions:
            start:
                description:
                    - This variable identifies the start record in the range to be retrieved.
                    - If this value is omitted, a tail range is returned.
                required: false
                type: int
            end:
                description:
                    - This variable identifies the end record in the range to be retrieved.
                    - If this value is omitted or is set to 0, the range extends to the end of the data set.
                required: false
                type: int
    dataset_migrate_recall:
        description:
            - Specify how a migrated data set is handled.
            - When I(dataset_migrate_recall=wait), the migrated data set is recalled synchronously.
            - When I(dataset_migrate_recall=nowait), request the migrated data set to be recalled, but do not wait.
            - When I(dataset_migrate_recall=error), do not attempt to recall the migrated data set.
        required: false
        type: str
        default: wait
        choices:
            - wait
            - nowait
            - error
    dataset_checksum:
        description:
            - Specifies the checksum to be used to verify that the data set to be fetched is not changed since the checksum was generated.
            - If the checksum is matched which means the data set is not changed, the content of the data set won't be fetched.
        required: false
        type: str
        default: null
requirements:
    - requests >= 2.23.0
"""

EXAMPLES = r"""
- name: Fetch a data set and store in /tmp/dataset/sample.ibm.com/ZOSMF.ANSIBLE.SAMPLE/MEMBER
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_dest: "/tmp/dataset"

- name: Fetch a dataset and store in /tmp/dataset/ZOSMF.ANSIBLE.SAMPLE/MEMBER
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_dest: "/tmp/dataset"
    dataset_flat: true

- name: Fetch an uncataloged dataset and store in /tmp/dataset/sample.ibm.com/ZOSMF.ANSIBLE.SAMPLE/MEMBER
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_volser: "VOLABC"
    dataset_dest: "/tmp/dataset"

- name: Fetch a data set as binary
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_dest: "/tmp/dataset"
    dataset_data_type: "binary"

- name: Fetch a data set in record format
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_dest: "/tmp/dataset"
    dataset_data_type: "record"

- name: Fetch a dataset and convert it from IBM-037 to ISO8859-1
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_dest: "/tmp/dataset"
    dataset_encoding:
        from: IBM-037
        to: ISO8859-1

- name: Fetch a range of records from a dataset (the first 500 lines)
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_dest: "/tmp/dataset"
    dataset_range:
        start: 0
        end: 499

- name: Fetch a range of records from a dataset (the final 500 lines)
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_dest: "/tmp/dataset"
    dataset_range:
        end: 500

- name: Fetch 100 lines of records from the first matched line that contains "ansible" in a dataset
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_dest: "/tmp/dataset"
    dataset_search:
        keyword: "ansible"
        maxreturnsize: 100

- name: Fetch a dataset and validate its checksum
  zmf_dataset_fetch:
    zmf_host: "sample.ibm.com"
    dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
    dataset_dest: "/tmp/dataset"
    dataset_checksum: "A4B504A7427F34B97B7E109CCC0459CA"
"""

RETURN = r"""
changed:
    description: Indicates if any change is made on managed node during the module operation.
    returned: always
    type: bool
message:
    description: The output message generated by the module to indicate whether the data set is successfully fetched.
    returned: on success
    type: str
    sample:
        sample1: "The data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is fetched successfully and saved in: /tmp/dataset/ZOSMF.ANSIBLE.SAMPLE/MEMBER."
        sample2: "The matched contents in the data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is fetched successfully and saved in: \
            /tmp/dataset/ZOSMF.ANSIBLE.SAMPLE/MEMBER.serarch."
        sample3: "The data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is not fetched since no matched contents is found with the specified search keyword."
        sample4: "A range of records in the data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is fetched successfully and saved in: \
            /tmp/dataset/ZOSMF.ANSIBLE.SAMPLE/MEMBER.range."
        sample6: "The data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is not fetched since no contents is returned in the specified range."
        sample7: "The data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is not fetched since it is not changed."
dataset_content:
    description: The retrieved content of the data set.
    returned: on success when I(dataset_data_type=text)
    type: list
    sample: [
        "First line of the data set",
        "Second line of the data set"
    ]
dataset_matched_content:
    description: The matched content in the data set with the specified search keyword.
    returned: on success when I(dataset_data_type=text) and I(dataset_search) is specified
    type: list
    sample: [
        "First line of the data set"
    ]
dataset_matched_range:
    description:
        - The range of the matched contents of the data set with the specified search keyword.
        - Return I(dataset_matched_range=p,q), where I(p) is the first matched line in the data set and I(q) is the number of lines returned.
    returned: on success when I(dataset_data_type=text) and I(dataset_search) is specified
    type: str
    sample: "0,500"
dataset_checksum:
    description: The checksum of the fetched data set, can be set in I(dataset_checksum) in next call to this module
    returned: on success when I(dataset_search) and I(dataset_range) are not specified
    type: str
    sample: "93822124D6E66E2213C64B0D10800224"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_util import (
    get_connect_argument_spec,
    get_connect_session
)
from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.zmf_dataset_api import (
    call_dataset_api
)
from time import sleep
import json
import re
import os


def validate_module_params(module):
    params = module.params
    # validate dataset_src
    if params['dataset_src'].strip() == '':
        module.fail_json(msg='Invalid variable "dataset_src", it must not be an empty string.')
    # validate dataset_dest
    if params['dataset_dest'].strip() == '':
        module.fail_json(msg='Invalid variable "dataset_dest", it must not be an empty string.')

    # validate dataset_data_type
    if 'dataset_data_type' in params:
        if params['dataset_data_type'] != 'text':
            if 'dataset_search' in params and params['dataset_search'] is not None:
                module.fail_json(msg='Variable "dataset_search" is valid only when dataset_data_type="text".')
            if 'dataset_encoding' in params and params['dataset_encoding'] is not None:
                module.fail_json(msg='Variable "dataset_encoding" is valid only when dataset_data_type="text".')

    # validate dataset_search
    if 'dataset_search' in params and params['dataset_search'] is not None:
        if isinstance(params['dataset_search'], dict):
            search = params['dataset_search']
            if ('keyword' not in search or search['keyword'].strip() == ''):
                module.fail_json(msg='Invalid variable: dataset_search. Missing required suboption or invalid suboption: keyword.')
        else:
            module.fail_json(
                msg='Invalid variable: dataset_search. It should be a dict and contain the following suboptions only: '
                    + 'keyword(required), insensitive, maxreturnsize.'
            )

    # validate dataset_encoding
    if 'dataset_encoding' in params and params['dataset_encoding'] is not None:
        if isinstance(params['dataset_encoding'], dict):
            encoding = params['dataset_encoding']
            if ('from' not in encoding or encoding['from'].strip() == ''):
                module.fail_json(msg='Invalid variable: dataset_encoding. Missing required suboption of invalid suboption: from.')
            if ('to' not in encoding or encoding['to'].strip() == ''):
                module.fail_json(msg='Invalid variable: dataset_encoding. Missing required suboption of invalid suboption: to.')
        else:
            module.fail_json(
                msg='Invalid variable: dataset_encoding. It should be a dict and contain the following suboptions only: '
                    + 'from(required), to(required).'
            )

    # validate dataset_range
    if 'dataset_range' in params and params['dataset_range'] is not None:
        if isinstance(params['dataset_range'], dict):
            range = params['dataset_range']
            start = -1
            end = -1
            if 'start' in range:
                try:
                    start = int(str(range['start']))
                    if start < 0:
                        module.fail_json(msg='Invalid variable: dataset_range. Invalid suboption: start, it must be a natural number.')
                    else:
                        module.params['dataset_range']['start'] = start
                except Exception:
                    module.fail_json(msg='Invalid variable: dataset_range. Invalid suboption: start, it must be a natural number.')
            if 'end' in range:
                try:
                    end = int(str(range['end']))
                    if end < 0:
                        module.fail_json(msg='Invalid variable: dataset_range. Invalid suboption: end, it must be a natural number.')
                    else:
                        module.params['dataset_range']['end'] = end
                except Exception:
                    module.fail_json(msg='Invalid variable: dataset_range. Invalid suboption: end, it must be a natural number.')
            if start >= 0 and end > 0 and start > end:
                module.fail_json(msg='Invalid variable: dataset_range. Invalid suboptions, end must be equal or larger than start.')
        else:
            module.fail_json(
                msg='Invalid variable: dataset_range. It should be a dict and contain the following suboptions only: '
                    + 'start, end. (Either start or end is required)'
            )


def fetch_dataset(module):
    """
    Call z/OSMF REST file and data set interface to read data set or member
    """

    # combine custom headers
    request_headers = dict()
    if module.params['dataset_data_type'] == 'text' and module.params['dataset_encoding'] is not None:
        request_headers['X-IBM-Data-Type'] = 'text;fileEncoding=' + module.params['dataset_encoding']['from']
        request_headers['Content-Type'] = 'text/plain;charset=' + module.params['dataset_encoding']['to']
    else:
        request_headers['X-IBM-Data-Type'] = module.params['dataset_data_type']

    if module.params['dataset_range'] is not None:
        range = module.params['dataset_range']
        if 'end' in range:
            end = range['end']
        else:
            end = 0
        if 'start' in range:
            range = str(range['start']) + '-' + str(end)
        else:
            range = '-' + str(end)
        request_headers['X-IBM-Record-Range'] = range

    # create session
    session = get_connect_session(module)
    # fetch dataset
    response_fetch = call_dataset_api(module, session, 'fetch', request_headers)
    dataset = module.params['dataset_src'].strip()
    fetch_result = dict()
    fetch_result['changed'] = False
    status_code = response_fetch.status_code
    if status_code == 404:
        if module.params['dataset_volser'] is not None and module.params['dataset_volser'].strip() != '':
            module.fail_json(msg='Failed to fetch the data set ---- ' + dataset + ' can not be found in ' + module.params['dataset_volser'])
        else:
            module.fail_json(msg='Failed to fetch the data set ---- ' + dataset + ' not in catalog or catalog can not be accessed.')
    elif status_code != 304 and status_code != 200:
        # handle response error
        response_error = response_fetch.json()
        if ('category' in response_error and response_error['category'] == 6
                and 'rc' in response_error and response_error['rc'] == 8
                and 'reason' in response_error and response_error['reason'] == 1046):
            # not fail - no conntents returned in the range of records (500)
            fetch_result['message'] = 'The dataset ' + dataset + ' is not fetched since no contents is returned in the specified range.'
            module.exit_json(**fetch_result)
        else:
            # fail - return JSON error report
            module.fail_json(
                msg='Failed to fetch the data set ' + dataset
                    + ' ---- Http request error: ' + str(status_code) + ': '
                    + str(response_error)
            )
    else:
        response_headers = response_fetch.headers
        if 'Etag' in response_headers:
            fetch_result['dataset_checksum'] = response_headers['Etag']
        if status_code == 304:
            fetch_result['message'] = 'The data set ' + dataset + ' is not fetched since it is not changed.'
        elif status_code == 200:
            if response_headers['Content-Type'] is not None:
                content_type = response_headers['Content-Type']

                # initialize path
                path = module.params['dataset_dest'].strip()
                host = module.params['zmf_host'].strip()

                if not path.endswith('/'):
                    path += '/'
                if module.params['dataset_flat'] is False:
                    path = path + host + '/'
                if module.params['dataset_volser'] is not None and module.params['dataset_volser'].strip() != '':
                    path = path + module.params['dataset_volser'] + '/'
                save_file = dataset.replace('(', '/').replace(')', '/')
                if save_file.find('/') != -1:
                    tmp_path = save_file.split('/')
                    path += tmp_path[0] + '/'
                    save_file = tmp_path[1]
                try:
                    if os.path.exists(path):
                        os.chmod(path, 0o755)
                    else:
                        os.makedirs(path, 0o755)
                except OSError as ex:
                    module.fail_json(msg='Failed to save the data set ' + dataset + ' ---- OS error: ' + str(ex))

                if 'X-IBM-Record-Range' in response_headers:
                    # when search
                    fetch_result['dataset_matched_range'] = response_headers['X-IBM-Record-Range']
                    if response_fetch.text != '':
                        f_write = open(path + save_file + '.search', 'w')
                        f_write.write(response_fetch.text)
                        f_write.close()
                        fetch_result['dataset_matched_content'] = response_fetch.text.split('\n')
                        fetch_result['message'] = 'The matched content in the data set ' + dataset + 'is fetched successfully and saved in: ' \
                            + path + save_file + '.search.'
                    else:
                        fetch_result['dataset_matched_content'] = []
                        fetch_result['message'] = 'The data set ' + dataset + ' is not fetched since ' \
                            + 'no matched contents is found with the specified search keyword.'

                else:
                    msg = 'The data set '
                    if 'Etag' not in response_headers:
                        # fetch with range
                        save_file += '.range'
                        msg = 'A range of records in the data set '

                    if content_type.startswith('text/plain'):
                        # text
                        f_write = open(path + save_file, 'w')
                        f_write.write(response_fetch.text)
                        f_write.close()
                        fetch_result['dataset_content'] = response_fetch.text.split('\n')
                    else:
                        # binary and record
                        f_write = open(path + save_file, 'wb')
                        f_write.write(response_fetch.content)
                        f_write.close()
                    fetch_result['message'] = msg + dataset + ' is fetched successfully and saved in: ' + path + save_file
            else:
                module.fail_json(msg='Failed to read data set ---- Content-Type is missing in the response.')
    module.exit_json(**fetch_result)


def main():
    argument_spec = dict()
    argument_spec.update(get_connect_argument_spec())
    argument_spec.update(
        dataset_src=dict(required=True, type='str'),
        dataset_dest=dict(required=False, type='str'),
        dataset_volser=dict(required=False, type='str'),
        dataset_flat=dict(required=False, type='bool', default='False'),
        dataset_data_type=dict(required=False, type='str', default='text', choices=['text', 'binary', 'record']),
        dataset_search=dict(required=False, type='dict'),
        dataset_encoding=dict(required=False, type='dict'),
        dataset_range=dict(required=False, type='dict'),
        dataset_migrate_recall=dict(required=False, type='str', default='wait', choices=['wait', 'nowait', 'error']),
        dataset_checksum=dict(required=False, type='str')
    )
    argument_spec['dataset_search']['keyword'] = dict(required=True, type='str')
    argument_spec['dataset_search']['insensitive'] = dict(required=False, type='bool', default=True)
    argument_spec['dataset_search']['maxreturnsize'] = dict(required=False, type='int', default=100)
    argument_spec['dataset_encoding']['from'] = dict(required=True, type='str')
    argument_spec['dataset_encoding']['to'] = dict(required=True, type='str')
    argument_spec['dataset_range']['start'] = dict(required=False, type='int')
    argument_spec['dataset_range']['end'] = dict(required=False, type='int')
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    validate_module_params(module)
    fetch_dataset(module)


if __name__ == '__main__':
    main()
