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
module: zmf_file_fetch
short_description: Fetch USS file from z/OS
description:
    - Retrieve the contents of a z/OS UNIX System Services (USS) file from the remote z/OS system, and save them on Ansible control node.
    - USS files that already exist at I(file_dest) will be overwritten if they are different than the I(file_src).
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
            - USS file on the remote z/OS system to fetch.
            - This variable must consist of a fully qualified path and file name. For example, C(/etc/profile).
        required: true
        type: str
        default: null
    file_dest:
        description:
            - The local directory on control node where the USS file should be saved to. For example, C(/tmp/file_output).
            - This directory can be absolute or relative. The module will fail if the parent directory of I(file_dest) is a read-only file system.
            - The directory C({{ file_dest }}/{{ zmf_host }}/) will be created to save the USS file, where I(zmf_host) is the hostname of the z/OSMF server.
            - For example, if I(zmf_host=zosmf.ibm.com), a USS file named C(/etc/profile) would be saved into C(/tmp/file_output/zosmf.ibm.com/etc/profile).
        required: true
        type: str
        default: null
    file_flat:
        description:
            - Specifies whether to override the default behavior of appending hostname/path/to/file to the destination.
            - If I(file_flat=true), the USS file will be fetched to the destination directory using its basename without appending I(zmf_host).
            - For example, if I(file_dest=/tmp/file_output), a USS file named C(/etc/profile) would be saved into C(/tmp/file_output/profile).
        required: false
        type: bool
        default: false
    file_search:
        description:
            - Specifies a series of parameters that are used to search the USS file.
            - These parameters only take effects when I(file_data_type=text).
            - If this variable is specified, only the matched contents in the USS file will be fetched to the destination directory.
            - The matched contents in the USS file will be saved as C({{ file_dest }}/{{ zmf_host }}/{ file_src }}.search) on control node.
            - For example, the matched contents in the USS file named C(/etc/profile) would be saved as C(....../etc/profile.search).
        required: false
        type: dict
        default: null
        suboptions:
            keyword:
                description:
                    - Specifies a string or a regular expression that is used to search the USS file.
                    - The USS file is searched for the first line that contains the string or matches the given extended regular expression.
                required: true
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
                    - Specifies how many lines of contents from the first matched line in the USS file will be returned.
                    - This variable only take effects when I(keyword) is defined.
                required: false
                type: int
                default: 100
    file_data_type:
        description:
            - Specifies whether data conversion is to be performed on the returned data.
            - When I(file_data_type=text), data conversion is performed.
            - You can use I(file_encoding) to specify which encodings the fetched USS file should be converted from and to.
            - If I(file_encoding) is not supplied, the data transfer process converts each record from C(IBM-1047) to C(ISO8859-1) by default.
            - When I(file_data_type=binary), no data conversion is performed. The data transfer process returns each line of data as-is, without translation.
        required: false
        type: str
        default: text
        choices:
            - text
            - binary
    file_encoding:
        description:
            - Specifies which encodings the fetched USS file should be converted from and to.
            - These parameters only take effects when I(file_data_type=text).
        required: false
        type: dict
        default: null
        suboptions:
            from:
                description:
                    - The character set of the source USS file.
                    - Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.
                required: true
                type: str
            to:
                description:
                    - The destination character set for the output to be written as.
                    - Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.
                required: true
                type: str
    file_range:
        description:
            - Specifies a range that is used to retrieve the USS file.
            - If I(file_data_type=text), the module will retrieve a range of records (lines delimited by '\n') from the USS file.
            - If I(file_data_type=binary), the module will retrieve a range of bytes from the USS file.
            - If this variable is specified, only the retrieved range of the USS file will be fetched to the destination directory.
            - The retrieved range of the USS file will be saved as C({{ file_dest }}/{{ zmf_host }}/{ file_src }}.range) on control node.
            - For example, the retrieved range of the USS file named C(/etc/profile) would be saved as C(....../etc/profile.range).
        required: false
        type: dict
        default: null
        suboptions:
            start:
                description:
                    - If I(file_data_type=text), this variable identifies the start record in the range to be retrieved.
                    - If I(file_data_type=binary), this variable identifies the byte-offset of the first byte in the range to be retrieved.
                    - If this value is omitted, a tail range is returned.
                required: false
                type: int
            end:
                description:
                    - If I(file_data_type=text), this variable identifies the end record in the range to be retrieved.
                    - If I(file_data_type=binary), this variable identifies the byte-offset of the last byte in the range to be retrieved.
                    - If this value is omitted or is set to 0, the range extends to the end of the USS file.
                required: false
                type: int
    file_checksum:
        description:
            - Specifies the checksum to be used to verify that the USS file to be fetched is not changed since the checksum was generated.
        required: False
        type: str
        default: null
requirements:
    - requests >= 2.23.0
"""

EXAMPLES = r"""
- name: Fetch a USS file and store in /tmp/file_output/sample.ibm.com/etc/profile
  zmf_file_fetch:
    zmf_host: "sample.ibm.com"
    file_src: "/etc/profile"
    file_dest: "/tmp/file_output"

- name: Fetch a USS file and store in /tmp/file_output/profile
  zmf_file_fetch:
    zmf_host: "sample.ibm.com"
    file_src: "/etc/profile"
    file_dest: "/tmp/file_output"
    file_flat: true

- name: Fetch a USS file as binary
  zmf_file_fetch:
    zmf_host: "sample.ibm.com"
    file_src: "/etc/profile"
    file_dest: "/tmp/file_output"
    file_data_type: "binary"

- name: Fetch a USS file and convert from IBM-037 to ISO8859-1
  zmf_file_fetch:
    zmf_host: "sample.ibm.com"
    file_src: "/etc/profile"
    file_dest: "/tmp/file_output"
    file_encoding:
        from: IBM-037
        to: ISO8859-1

- name: Fetch a range of records from a USS file (the first 500 lines)
  zmf_file_fetch:
    zmf_host: "sample.ibm.com"
    file_src: "/etc/profile"
    file_dest: "/tmp/file_output"
    file_range:
        start: 0
        end: 499

- name: Fetch a range of records from a USS file (the final 500 lines)
  zmf_file_fetch:
    zmf_host: "sample.ibm.com"
    file_src: "/etc/profile"
    file_dest: "/tmp/file_output"
    file_range:
        end: 500

- name: Fetch 100 lines of records from the first matched line that contains "Health Checker" in a USS file
  zmf_file_fetch:
    zmf_host: "sample.ibm.com"
    file_src: "/etc/profile"
    file_dest: "/tmp/file_output"
    file_search:
        keyword: "Health Checker"

- name: Fetch a USS file and validate its checksum
  zmf_file_fetch:
    zmf_host: "sample.ibm.com"
    file_src: "/etc/profile"
    file_dest: "/tmp/file_output"
    file_checksum: "93822124D6E66E2213C64B0D10800224"
"""

RETURN = r"""
changed:
    description: Indicates if any change is made during the module operation.
    returned: always
    type: bool
message:
    description: The output message generated by the module to indicate whether the USS file is successfully fetched.
    returned: on success
    type: str
    sample:
        sample1: "The USS file /etc/profile is fetched successfully and saved in: /tmp/file_output/sample.ibm.com/etc/profile"
        sample2: "The matched contents in the USS file /etc/profile is fetched successfully and saved in: /tmp/file_output/sample.ibm.com/etc/profile.serarch"
        sample3: "The USS file /etc/profile is not fetched since no matched contents is found with the specified search keyword."
        sample4: "A range of records in the USS file /etc/profile is fetched successfully and saved in: /tmp/file_output/SY1/etc/profile.range"
        sample5: "A range of bytes in the USS file /etc/profile is fetched successfully and saved in: /tmp/file_output/SY1/etc/profile.range"
        sample6: "The USS file /etc/profile is not fetched since no contents is returned in the specified range."
        sample7: "The USS file /etc/profile is not fetched since it is not changed."
file_content:
    description: The retrieved contents of the USS file.
    returned: on success when I(file_data_type=text)
    type: list
    sample: [
        "# This is a sample profile defining system wide variables. The",
        "# variables set here may be overridden by a user's personal .profile",
        "# in their $HOME directory."
    ]
file_matched_content:
    description: The matched contents in the USS file with the specified search keyword.
    returned: on success when I(file_data_type=text) and I(file_search) is specified
    type: list
    sample: [
        "NLSPATH=/usr/lib/nls/msg/%L/%N"
    ]
file_matched_range:
    description:
        - The range of the matched contents of the USS file with the specified search keyword.
        - Return I(file_matched_range=p,q), where I(p) is the first matched line in the USS file and I(q) is the number of lines returned.
    returned: on success when I(file_data_type=text) and I(file_search) is specified
    type: str
    sample: "0,500"
file_checksum:
    description: The checksum of the fetched USS file.
    returned: on success when I(file_search) and I(file_range) are not specified
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
from time import sleep
import json
import re
import os


def validate_module_params(module):
    # validate file_src
    if not (module.params['file_src'] is not None and module.params['file_src'].strip() != ''):
        module.fail_json(msg='Missing required argument or invalid argument: file_src.')
    # validate file_dest
    if not (module.params['file_dest'] is not None and module.params['file_dest'].strip() != ''):
        module.fail_json(msg='Missing required argument or invalid argument: file_dest.')
    # validate file_data_type
    if module.params['file_data_type'] != 'text':
        if module.params['file_search'] is not None:
            module.fail_json(msg='file_search is valid only when file_data_type=text.')
        if module.params['file_encoding'] is not None:
            module.fail_json(msg='file_encoding is valid only when file_data_type=text.')
    # validate file_search
    if module.params['file_search'] is not None:
        if isinstance(module.params['file_search'], dict):
            has_keyword = False
            for k, v in module.params['file_search'].items():
                if k == 'keyword':
                    has_keyword = True
                    if v is not None and str(v).strip() != '':
                        module.params['file_search']['keyword'] = str(v).strip()
                    else:
                        module.fail_json(msg='Invalid argument: file_search. Missing required suboption or invalid suboption: keyword.')
                elif k == 'insensitive':
                    if (str(v) == '1' or str(v).lower() == 'yes' or str(v).lower() == 'y'
                            or str(v).lower() == 'true' or str(v).lower() == 't' or str(v).lower() == 'on'):
                        module.params['file_search']['insensitive'] = True
                    elif (str(v) == '0' or str(v).lower() == 'no' or str(v).lower() == 'n'
                            or str(v).lower() == 'false' or str(v).lower() == 'f' or str(v).lower() == 'off'):
                        module.params['file_search']['insensitive'] = False
                    else:
                        module.fail_json(msg='Invalid argument: file_search. Invalid suboption: insensitive, it must be a boolean.')
                elif k == 'maxreturnsize':
                    try:
                        if int(str(v)) <= 0:
                            module.fail_json(msg='Invalid argument: file_search. Invalid suboption: maxreturnsize, it must be a interger and larger than 0.')
                        else:
                            module.params['file_search']['maxreturnsize'] = int(str(v))
                    except Exception:
                        module.fail_json(msg='Invalid argument: file_search. Invalid suboption: maxreturnsize, it must be a interger and larger than 0.')
                else:
                    module.fail_json(
                        msg='Invalid argument: file_search. It should be a dict and contain the following suboptions only: '
                            + 'keyword(required), insensitive, maxreturnsize.'
                    )
            if not has_keyword:
                module.fail_json(msg='Invalid argument: file_search. Missing required suboption or invalid suboption: keyword.')
        else:
            module.fail_json(
                msg='Invalid argument: file_search. It should be a dict and contain the following suboptions only: '
                    + 'keyword(required), insensitive, maxreturnsize.'
            )
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
    # validate file_range
    if module.params['file_range'] is not None:
        if isinstance(module.params['file_range'], dict):
            for k, v in module.params['file_range'].items():
                if k == 'start':
                    try:
                        if int(str(v)) < 0:
                            module.fail_json(msg='Invalid argument: file_range. Invalid suboption: start, it must be a interger and equal or larger than 0.')
                        else:
                            module.params['file_range']['start'] = int(str(v))
                    except Exception:
                        module.fail_json(msg='Invalid argument: file_range. Invalid suboption: start, it must be a interger and equal or larger than 0.')
                elif k == 'end':
                    try:
                        if int(str(v)) < 0:
                            module.fail_json(msg='Invalid argument: file_range. Invalid suboption: end, it must be a interger and equal or larger than 0.')
                        else:
                            module.params['file_range']['end'] = int(str(v))
                    except Exception:
                        module.fail_json(msg='Invalid argument: file_range. Invalid suboption: end, it must be a interger and equal or larger than 0.')
                else:
                    module.fail_json(
                        msg='Invalid argument: file_range. It should be a dict and contain the following suboptions only: '
                            + 'start, end. (Either start or end is required)'
                    )
            if ('start' in module.params['file_range'] and 'end' in module.params['file_range']
                    and int(module.params['file_range']['end']) != 0
                    and int(module.params['file_range']['start']) > int(module.params['file_range']['end'])):
                module.fail_json(msg='Invalid argument: file_range. Invalid suboptions, end must be equal or larger than start.')
        else:
            module.fail_json(
                msg='Invalid argument: file_range. It should be a dict and contain the following suboptions only: '
                    + 'start, end. (Either start or end is required)'
            )


def fetch_file(module):
    """
    Fetch USS file from z/OS
    Return the message to indicate whether the USS file is successfully fetched.
    Return file_content of the retrieved contents.
    Return file_matched_content of the matched contents if file_search is specified.
    Return file_matched_range of the range of the matched contents if file_search is specified.
    Return file_checksum of the checksum if file_search and file_range are not specified.
    :param AnsibleModule module: the ansible module
    """
    fetch_result = dict(
        changed=False,
        message='',
    )
    # create session
    session = get_connect_session(module)
    file = module.params['file_src'].strip()
    path = module.params['file_dest'].strip()
    host = module.params['zmf_host'].strip()
    fetch_src = file
    if not fetch_src.startswith('/'):
        fetch_src = '/' + fetch_src
    # step1 - combine request headers
    request_headers = dict()
    if module.params['file_data_type'] == 'text' and module.params['file_encoding'] is not None:
        request_headers['X-IBM-Data-Type'] = 'text;fileEncoding=' + module.params['file_encoding']['from']
        request_headers['Content-Type'] = 'text/plain;charset=' + module.params['file_encoding']['to']
    else:
        request_headers['X-IBM-Data-Type'] = module.params['file_data_type']
    if module.params['file_range'] is not None:
        if 'end' in module.params['file_range']:
            end = module.params['file_range']['end']
        else:
            end = 0
        if 'start' in module.params['file_range']:
            range = str(module.params['file_range']['start']) + '-' + str(end)
        else:
            range = '-' + str(end)
        if module.params['file_data_type'] == 'text':
            request_headers['X-IBM-Record-Range'] = range
        else:
            request_headers['Range'] = 'bytes=' + range
    if module.params['file_checksum'] is not None and module.params['file_checksum'].strip() != '':
        request_headers['If-None-Match'] = module.params['file_checksum'].strip()
    # step2 - fetch USS file
    res_fetch = call_file_api(module, session, 'fetch', request_headers)
    res_cd = res_fetch.status_code
    if res_cd != 200 and res_cd != 206 and res_cd != 416 and res_cd != 304:
        # handle response error
        res_error = res_fetch.json()
        if ('category' in res_error and res_error['category'] == 6
                and 'rc' in res_error and res_error['rc'] == 8
                and 'reason' in res_error and res_error['reason'] == 1046):
            # not fail - no conntents returned in the range of records (500)
            fetch_result['message'] = 'The USS file ' + fetch_src + ' is not fetched since no contents is returned in the specified range.'
            module.exit_json(**fetch_result)
        else:
            # fail - return JSON error report
            module.fail_json(
                msg='Failed to fetch the USS file ' + fetch_src
                    + ' ---- Http request error: ' + str(res_cd) + ': '
                    + str(res_error)
            )
    else:
        # handle response
        res_hd = res_fetch.headers
        if 'Etag' in res_hd:
            fetch_result['file_checksum'] = res_hd['Etag']
        if 'X-IBM-Record-Range' in res_hd:
            fetch_result['file_matched_range'] = res_hd['X-IBM-Record-Range']
            fetch_result['file_matched_content'] = []
            if 'Content-Length' in res_hd and int(res_hd['Content-Length']) == 0:
                # no matched conntents with the specified search keyword (200)
                fetch_result['message'] = 'The USS file ' + fetch_src + ' is not fetched since no matched contents is found with the specified search keyword.'
                module.exit_json(**fetch_result)
        if res_cd == 304:
            # file not changed when file_checksum is specified (304)
            fetch_result['message'] = 'The USS file ' + fetch_src + ' is not fetched since it is not changed.'
        elif res_cd == 416:
            # no conntents returned in the range of bytes (416)
            fetch_result['message'] = 'The USS file ' + fetch_src + ' is not fetched since no contents is returned in the specified range.'
        else:
            # save the returned conntents to local (200/206)
            if file.startswith('/'):
                file = file[1:]
            if not path.endswith('/'):
                path += '/'
            if module.params['file_flat'] is False:
                path += host + '/' + file[0:file.rfind('/') + 1]
            file = file[file.rfind('/') + 1:]
            try:
                if not os.path.exists(path):
                    os.makedirs(path, 0o755)
                else:
                    os.chmod(path, 0o755)
            except OSError as ex:
                module.fail_json(msg='Failed to fetch the USS file ' + fetch_src + ' ---- OS error: ' + str(ex))
            if res_cd == 206:
                # binary contents returned in the specified range of bytes (206)
                f_write = open(path + file + '.range', 'wb')
                f_write.write(res_fetch.content)
                f_write.close()
                fetch_result['message'] = 'A range of bytes in the USS file ' + fetch_src + ' is fetched successfully and saved in: ' \
                    + path + file + '.range'
            elif 'file_matched_range' in fetch_result:
                # matched text contents returned with the specified search keyword (200)
                f_write = open(path + file + '.search', 'w')
                f_write.write(res_fetch.text)
                f_write.close()
                fetch_result['file_matched_content'] = res_fetch.text.split('\n')
                fetch_result['message'] = 'The matched contents in the USS file ' + fetch_src + ' is fetched successfully and saved in: ' \
                    + path + file + '.search'
            elif 'file_checksum' not in fetch_result:
                # text contents returned in the specified range of records (200)
                f_write = open(path + file + '.range', 'w')
                f_write.write(res_fetch.text)
                f_write.close()
                fetch_result['file_content'] = res_fetch.text.split('\n')
                fetch_result['message'] = 'A range of records in the USS file ' + fetch_src + ' is fetched successfully and saved in: ' \
                    + path + file + '.range'
            else:
                # all contents returned (200)
                if res_hd['Content-Type'].find('text/plain') > -1:
                    # text contents returned
                    f_write = open(path + file, 'w')
                    f_write.write(res_fetch.text)
                    f_write.close()
                    fetch_result['file_content'] = res_fetch.text.split('\n')
                else:
                    # binary contents returned
                    f_write = open(path + file, 'wb')
                    f_write.write(res_fetch.content)
                    f_write.close()
                fetch_result['message'] = 'The USS file ' + fetch_src + ' is fetched successfully and saved in: ' + path + file
        module.exit_json(**fetch_result)


def main():
    argument_spec = dict()
    argument_spec.update(get_connect_argument_spec())
    argument_spec.update(
        file_src=dict(required=True, type='str'),
        file_dest=dict(required=True, type='str'),
        file_flat=dict(required=False, type='bool', default=False),
        file_data_type=dict(required=False, type='str', default='text', choices=['text', 'binary']),
        file_search=dict(required=False, type='dict'),
        file_encoding=dict(required=False, type='dict'),
        file_range=dict(required=False, type='dict'),
        file_checksum=dict(required=False, type='str')
    )
    argument_spec['file_search']['keyword'] = dict(required=True, type='str')
    argument_spec['file_search']['insensitive'] = dict(required=False, type='bool', default=True)
    argument_spec['file_search']['maxreturnsize'] = dict(required=False, type='int', default=100)
    argument_spec['file_encoding']['from'] = dict(required=True, type='str')
    argument_spec['file_encoding']['to'] = dict(required=True, type='str')
    argument_spec['file_range']['start'] = dict(required=False, type='int')
    argument_spec['file_range']['end'] = dict(required=False, type='int')
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    validate_module_params(module)
    fetch_file(module)


if __name__ == '__main__':
    main()
