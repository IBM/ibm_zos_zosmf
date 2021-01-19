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
module: zmf_dataset_copy
short_description: Copy data to z/OS data set or member
description:
    - Copy data from Ansible control node to a sequential data set, or a member of a partitioned data set (PDS or PDSE) on the remote z/OS system.
    - If the target data set or member already exists, it can be overwritten. If the target PDS or PDSE member does not exist, it can be created.
    - If the target data set does not exist, it can be created based on I(dataset_model) or the size of the source.
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
            - The local path on control node of the data to be copied to the target data set or member. For example, C(/tmp/dataset_input/member01).
            - This path can be absolute or relative. The module will fail if I(dataset_src) has no read permission.
            - The data is interpreted as one of binary, text, record or 'diff -e' format according to the value of I(dataset_data_type) and I(dataset_diff).
            - If I(dataset_content) is supplied and I(dataset_data_type=text), I(dataset_src) is ignored.
        required: false
        type: str
        default: null
    dataset_content:
        description:
            - The contents to be copied to the target data set or member. This variable is used instead of I(dataset_src).
            - This variable only take effects when I(dataset_data_type=text).
            - Each line of the contents should be terminated with C(\n). For example, C(Sample profile\nTZ=EST5EDT\n).
            - If I(dataset_content) is supplied and I(dataset_data_type=text), I(dataset_src) is ignored.
        required: false
        type: str
        default: null
    dataset_dest:
        description:
            - Data set or the name of the PDS or PDSE member on the remote z/OS system where the data should be copied to.
            - This variable must consist of a fully qualified data set name. The length of the data set name cannot exceed 44 characters.
            - If I(dataset_dest) is a nonexistent data set, it will be allocated.
            - For example, specifying a data set like C(ZOSMF.ANSIBLE.DATA), or a PDS or PDSE member like ``ZOSMF.ANSIBLE.PDS(MEMBER)``.
        required: true
        type: str
        default: null
    dataset_volser:
        description:
            - The volume serial to identify the volume to be searched for an uncataloged data set or member.
            - The length of the volume serial cannot exceed six characters. Wildcard characters are not supported. Indirect volume serials are not supported.
            - If this parameter is provided and I(dataset_dest) is a nonexistent data set, I(dataset_volser) must point to a volume on a 3390 device.
        required: false
        type: str
        default: null
    dataset_force:
        description:
            - Specifies whether the target data set must always be overwritten.
            - If I(dataset_force=true) and I(dataset_checksum) is not supplied, the target data set will always be overwritten.
            - If I(dataset_force=true) and I(dataset_checksum) is supplied, the target data set will be overwritten only when the checksum is matched.
            - If I(dataset_force=false), the data will only be copied if the target PDS or PDSE member does not exist.
        required: false
        type: bool
        default: true
    dataset_model:
        description:
            - When copying a local file to a non-existing PDS, PDSE or PS, specify a model data set to allocate the target data set.
            - For example, specifying a data set like C(ZOSMF.ANSIBLE.DATALIB), member name should not be provided in this parameter.
            - If this parameter is not provided, the destination data set will be allocated based on the size of the local file or I(dataset_content).
            - The primary extent tracks will be specified as 4 times the size of the local file or I(dataset_content).
            - If I(dataset_data_type=text), then C(RECFM=FB) and C(LRECL=80) will be used to allocate the data set.
            - If I(dataset_data_type=binary) or I(dataset_data_type=record), (RECFM=U) will be used to allocate the data set.
        required: False
        type: str
        default: null
    dataset_data_type:
        description:
            - Specifies whether data conversion is to be performed on the data to be copied.
            - When I(dataset_data_type=text), data conversion is performed.
            - You can use I(dataset_encoding) to specify which encodings the data to be copied should be converted from and to.
            - Each line of data, delimited by a Line Feed (LF), is converted and written as a record to the target data set.
            - The LF character is removed and the data is padded with the space character to the end of the record if it is a fixed record size data set.
            - For variable record size data set, the record is written without padding.
            - the module will fail if the record size of the data set is smaller than any line of text since not all data was written.
            - If I(dataset_encoding) is not supplied, the data transfer process converts each byte from C(ISO8859-1) to C(IBM-1047) by default.
            - You can use I(dataset_crlf) to control whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF).
            - If I(dataset_crlf) is not supplied, LF characters are left intact by default.
            - You can use I(dataset_diff) to specify whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command.
            - If I(dataset_diff) is not supplied, the input is regarded as not consisting of commands by default.
            - When I(dataset_data_type=binary), no data conversion is performed.
            - The data is written to the data set without respect to record boundaries. All records will be written at their maximum record length.
            - For fixed length record data set, the last record will be padded with nulls if required.
            - When I(dataset_data_type=record), no data conversion is performed.
            - Each logical record is preceded by the 4-byte big endian record length of the record that follows. This length doesn't include the prefix length.
            - For example, a zero-length record is 4 bytes of zeros with nothing following.
        required: false
        type: str
        default: text
        choices:
            - text
            - binary
            - record
    dataset_encoding:
        description:
            - Specifies which encodings the data to be copied should be converted from and to.
            - These parameters only take effects when I(dataset_data_type=text) and I(dataset_diff=false).
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
                    - The destination character set for the target data set.
                    - Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.
                required: true
                type: str
    dataset_crlf:
        description:
            - Specifies whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF).
            - If I(dataset_crlf=true), CRLF characters are used.
            - This variable only take effects when I(dataset_data_type=text).
        required: false
        type: bool
        default: false
    dataset_diff:
        description:
            - Specifies whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command.
            - These commands are used to add, replace and delete lines in the target data set. The following commands are supported.
            - C(a)
            - C(c)
            - C(d)
            - C(s/.//)
            - opt C(g|<n>), where C(g) means global, C(n) means search and replace C(n) times.
            - Each command may be optionally preceded by a line or line range, as allowed by the z/OS UNIX 'ed' command.
            - The module will fail if an error is detected while processing a command.
            - This variable only take effects when I(dataset_data_type=text).
        required: false
        type: bool
        default: false
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
            - Specifies the checksum to be used to verify that the target data set to copy to is not changed since the checksum was generated.
            - The module will fail and no data will be copied if the checksum is not matched which means the target data set has been modified.
            - This variable only take effects when I(dataset_force=true).
        required: False
        type: str
        default: null
requirements:
    - requests >= 2.23.0
"""

EXAMPLES = r"""
- name: Copy a local file to data set ZOSMF.ANSIBLE.LIB
  zmf_dataset_copy:
    zmf_host: "sample.ibm.com"
    dataset_src: "/tmp/dataset_input/sample1"
    dataset_dest: "ZOSMF.ANSIBLE.LIB"

- name: Copy a local file to PDS member ZOSMF.ANSIBLE.LIB(MEMBER01) only if it does not exist
  zmf_dataset_copy:
    zmf_host: "sample.ibm.com"
    dataset_src: "/tmp/dataset_input/member01"
    dataset_dest: "ZOSMF.ANSIBLE.LIB(MEMBER01)"
    dataset_force: false

- name: Copy the contents to data set ZOSMF.ANSIBLE.LIB
  zmf_dataset_copy:
    zmf_host: "sample.ibm.com"
    dataset_conntent: "Sample profile\nTZ=EST5EDT\n"
    dataset_dest: "ZOSMF.ANSIBLE.LIB"

- name: Copy a local file to uncataloged PDS member ZOSMF.ANSIBLE.LIB(MEMBER01) as binary
  zmf_dataset_copy:
    zmf_host: "sample.ibm.com"
    dataset_src: "/tmp/dataset_input/member01"
    dataset_dest: "ZOSMF.ANSIBLE.LIB(MEMBER01)"
    dataset_volser: "VOL001"
    dataset_data_type: "binary"

- name: Copy a local file to data set ZOSMF.ANSIBLE.LIB and convert from ISO8859-1 to IBM-037
  zmf_dataset_copy:
    zmf_host: "sample.ibm.com"
    dataset_src: "/tmp/dataset_input/sample1"
    dataset_dest: "ZOSMF.ANSIBLE.LIB"
    dataset_encoding:
      from: ISO8859-1
      to: IBM-037

- name: Copy a local file to data set ZOSMF.ANSIBLE.LIB and validate its checksum
  zmf_dataset_copy:
    zmf_host: "sample.ibm.com"
    dataset_src: "/tmp/dataset_input/sample1"
    dataset_dest: "ZOSMF.ANSIBLE.LIB"
    dataset_checksum: "93822124D6E66E2213C64B0D10800224"
"""

RETURN = r"""
changed:
    description: Indicates if any change is made during the module operation.
    returned: always
    type: bool
message:
    description: The output message generated by the module to indicate whether the data set or member is successfully copied.
    returned: on success
    type: str
    sample:
        sample1: "The target data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is created and updated successfully."
        sample2: "The target data set ZOSMF.ANSIBLE.SAMPLE is updated successfully."
        sample7: "No data is copied since the target data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) already exists and dataset_force is set to False."
dataset_checksum:
    description: The checksum of the updated data set.
    returned: on success
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
import json
import os
import math


def validate_module_params(module):
    # validate dataset_src and dataset_content
    if ((module.params['dataset_src'] is None or module.params['dataset_src'].strip() == '')
            and (module.params['dataset_content'] is None or module.params['dataset_content'].strip() == '')):
        module.fail_json(msg='Missing required argument or invalid argument: either dataset_src or dataset_content is required.')
    elif module.params['dataset_src'] is not None and module.params['dataset_src'].strip() != '':
        try:
            if not os.path.isfile(module.params['dataset_src'].strip()):
                module.fail_json(msg='dataset_src should be a path of a file.')
        except OSError as ex:
            module.fail_json(msg='Failed to read content of dataset_src ' + module.params['dataset_src'].strip() + ' ---- OS error: ' + str(ex))
    # validate dataset_dest
    if not (module.params['dataset_dest'] is not None and module.params['dataset_dest'].strip() != ''):
        module.fail_json(msg='Missing required argument or invalid argument: dataset_dest.')
    # validate dataset_force and dataset_checksum
    if module.params['dataset_force'] is False and module.params['dataset_checksum'] is not None and module.params['dataset_checksum'].strip() != '':
        module.fail_json(msg='dataset_checksum is valid only when dataset_force=true.')
    # validate dataset_data_type
    if module.params['dataset_data_type'] != 'text':
        if module.params['dataset_encoding'] is not None:
            module.fail_json(msg='dataset_encoding is valid only when dataset_data_type=text.')
        if module.params['dataset_crlf'] is True:
            module.fail_json(msg='dataset_crlf is valid only when dataset_data_type=text.')
        if module.params['dataset_diff'] is True:
            module.fail_json(msg='dataset_diff is valid only when dataset_data_type=text.')
        if not (module.params['dataset_src'] is not None and module.params['dataset_src'].strip() != ''):
            module.fail_json(msg='dataset_src is required when dataset_data_type=binary or dataset_data_type=record.')
        if module.params['dataset_content'] is not None and module.params['dataset_content'].strip() != '':
            module.fail_json(msg='dataset_content is valid only when dataset_data_type=text.')
    # validate dataset_encoding
    if module.params['dataset_encoding'] is not None:
        if isinstance(module.params['dataset_encoding'], dict):
            has_from = False
            has_to = False
            for k, v in module.params['dataset_encoding'].items():
                if k == 'from':
                    has_from = True
                    if v is not None and str(v).strip() != '':
                        module.params['dataset_encoding']['from'] = str(v).strip()
                    else:
                        module.fail_json(msg='Invalid argument: dataset_encoding. Missing required suboption or invalid suboption: from.')
                elif k == 'to':
                    has_to = True
                    if v is not None and str(v).strip() != '':
                        module.params['dataset_encoding']['to'] = str(v).strip()
                    else:
                        module.fail_json(msg='Invalid argument: dataset_encoding. Missing required suboption or invalid suboption: to.')
                else:
                    module.fail_json(
                        msg='Invalid argument: dataset_encoding. It should be a dict and contain the following suboptions only: '
                            + 'from(required), to(required).'
                    )
            if not has_from:
                module.fail_json(msg='Invalid argument: dataset_encoding. Missing required suboption or invalid suboption: from.')
            if not has_to:
                module.fail_json(msg='Invalid argument: dataset_encoding. Missing required suboption or invalid suboption: to.')
        else:
            module.fail_json(
                msg='Invalid argument: dataset_encoding. It should be a dict and contain the following suboptions only: '
                    + 'from(required), to(required).'
            )
        if module.params['dataset_diff'] is True:
            module.fail_json(msg='dataset_encoding is valid only when dataset_diff=false.')


def copy_dataset(module):
    """
    Copy data to a data set or member
    Return the message to indicate whether the data set or member is successfully copied.
    Return dataset_checksum of the checksum of the data set or member.
    :param AnsibleModule module: the ansible module
    """
    copy_result = dict(
        changed=False,
        message='',
    )
    # create session
    session = get_connect_session(module)
    dataset = module.params['dataset_dest'].strip().upper()
    # setup data set full name, data set name and member name
    ds_full_name = ''
    ds_v_name = ''
    ds_name = ''
    m_name = ''
    has_volser = False
    is_member = False
    ds_exist = True
    if dataset.find('(') > 0:
        ds_name = dataset[:dataset.find('(')]
        m_name = dataset[dataset.find('(') + 1:dataset.find(')')]
    else:
        ds_name = dataset
    if module.params['dataset_volser'] is not None and module.params['dataset_volser'].strip() != '':
        has_volser = True
        ds_full_name = '-(' + module.params['dataset_volser'].strip().upper() + ')/' + dataset
        ds_v_name = '-(' + module.params['dataset_volser'].strip().upper() + ')/' + ds_name
    else:
        ds_full_name = dataset
        ds_v_name = ds_name
    module.params['ds_full_name'] = ds_full_name
    module.params['ds_v_name'] = ds_v_name
    module.params['ds_name'] = ds_name
    module.params['m_name'] = m_name
    copy_src = None
    if module.params['dataset_src'] is not None and module.params['dataset_src'].strip() != '':
        copy_src = module.params['dataset_src'].strip()

    # step 1 - check if the target data set or member exists when dataset_force=false
    if module.params['m_name'] is not None and module.params['m_name'].strip() != '':
        is_member = True
        res_list = call_dataset_api(module, session, 'list_m')
    else:
        res_list = call_dataset_api(module, session, 'list_ds')
    if res_list.status_code == 200:
        # PDS exists if dest is a member of PDS
        res_content = json.loads(res_list.content)
        if 'returnedRows' in res_content and res_content['returnedRows'] == 0 and not is_member:
            ds_exist = False
        elif 'returnedRows' in res_content and res_content['returnedRows'] != 0 and module.params['dataset_force'] is False:
            # not fail - no data is copied since the target data set or member exists
            copy_result['message'] = 'No data is copied since the target data set ' + dataset + ' already exists and dataset_force is set to False.'
            module.exit_json(**copy_result)
    elif res_list.status_code == 404:
        if 'Content-Type' in res_list.headers and res_list.headers['Content-Type'].startswith('application/json'):
            res_json = res_list.json()
            if ('category' in res_json and 'rc' in res_json and 'reason' in res_json
                    and res_json['category'] == 4 and res_json['rc'] == 8 and res_json['reason'] == 0):
                # PDS doesn't exist if dest is a member of PDS
                ds_exist = False

    # step 2 - create the DS or PDS if not exist
    create_vars = dict()
    if not ds_exist:
        create_headers = dict()
        create_headers['Content-Type'] = 'application/json'
        if module.params['dataset_model'] is not None and module.params['dataset_model'].strip() != '':
            create_vars['like'] = module.params['dataset_model'].strip()
        else:
            file_size_byte = 0
            if module.params['dataset_data_type'] == 'text':
                create_vars['recfm'] = 'FB'
                create_vars['lrecl'] = 80
                if module.params['dataset_content'] is not None and module.params['dataset_content'].strip() != '':
                    file_size_byte = len(module.params['dataset_content'].encode())
            else:
                create_vars['recfm'] = 'U'
            if file_size_byte == 0:
                try:
                    file_size_byte = os.path.getsize(copy_src)
                except OSError as ex:
                    module.fail_json(msg='Failed to copy data to the target data set ' + dataset + ' ---- OS error: ' + str(ex))
            primary_num = 0
            secondary_num = 0
            trk_size = 56664
            cyl_size = 849960
            if file_size_byte >= 5 * cyl_size:
                alc_unit = 'CYL'
                primary_num = math.ceil(float(file_size_byte) / cyl_size)
            else:
                alc_unit = 'TRK'
                primary_num = math.ceil(float(file_size_byte) / trk_size)

            primary_num *= 4
            if is_member:
                secondary_num = math.ceil(0.2 * primary_num)
                create_vars['dsorg'] = 'PO'
                create_vars['dsntype'] = 'LIBRARY'
            else:
                secondary_num = math.ceil(0.5 * primary_num)
                create_vars['dsorg'] = 'PS'
            create_vars['alcunit'] = alc_unit
            create_vars['primary'] = primary_num
            create_vars['secondary'] = secondary_num
        create_vars['unit'] = '3390'
        if has_volser:
            create_vars['volser'] = module.params['dataset_volser'].strip().upper()
        res_create = call_dataset_api(module, session, 'create', create_headers, json.dumps(create_vars))
        if res_create.status_code != 201:
            module.fail_json(
                msg='Failed to create the target date set ' + ds_name + ' ---- Http request error: '
                    + str(res_create.status_code) + ': ' + str(res_create.content)
            )

    # step 3 - read dataset_src or dataset_content
    f_read = None
    request_body = None
    if module.params['dataset_data_type'] != 'text':
        try:
            f_read = open(copy_src, 'rb')
            request_body = f_read.read()
        except OSError as ex:
            module.fail_json(msg='Failed to copy data to the target data set ' + dataset + ' ---- OS error: ' + str(ex))
    else:
        if module.params['dataset_content'] is not None and module.params['dataset_content'].strip() != '':
            request_body = module.params['dataset_content']
        else:
            try:
                f_read = open(copy_src, 'r')
                request_body = f_read.read()
            except OSError as ex:
                module.fail_json(msg='Failed to copy data to the target data set ' + dataset + ' ---- OS error: ' + str(ex))
    if f_read is not None:
        f_read.close()
    # step 4 - combine request headers
    request_headers = dict()
    request_headers['X-IBM-Data-Type'] = module.params['dataset_data_type']
    request_headers['Content-Type'] = 'text/plain'
    if module.params['dataset_data_type'] == 'text':
        if module.params['dataset_diff'] is True:
            request_headers['Content-Type'] = 'application/x-ibm-diff-e'
        if module.params['dataset_encoding'] is not None:
            request_headers['X-IBM-Data-Type'] += ';fileEncoding=' + module.params['dataset_encoding']['to']
            request_headers['Content-Type'] += ';charset=' + module.params['dataset_encoding']['from']
        if module.params['dataset_crlf'] is True:
            request_headers['X-IBM-Data-Type'] += ';crlf=true'
    # step 5 - copy data to the target data set
    res_copy = call_dataset_api(module, session, 'copy', request_headers, request_body)
    res_cd = res_copy.status_code
    if res_cd != 201 and res_cd != 204:
        # handle response error
        if res_cd == 412:
            # fail - data set has been modified when dataset_checksum is specified (412)
            module.fail_json(
                msg='Failed to copy data to the target data set ' + dataset + ' ---- the target data set has been modified and its checksum is: '
                    + res_copy.headers['Etag']
            )
        else:
            # fail - return JSON error report
            res_error = res_copy.json()
            module.fail_json(
                msg='Failed to copy data to the target data set ' + dataset + ' ---- Http request error: '
                    + str(res_cd) + ': ' + str(res_error) + json.dumps(create_vars)
            )
    else:
        # handle response
        copy_result['changed'] = True
        copy_result['dataset_checksum'] = res_copy.headers['Etag']
        if res_cd == 201:
            # success - a new member is created (201)
            copy_result['message'] = 'The target data set ' + dataset + ' is created and updated successfully.'
        else:
            # success - an existing data set is updated (204)
            copy_result['message'] = 'The target data set ' + dataset + ' is updated successfully.'
        module.exit_json(**copy_result)


def main():
    argument_spec = dict()
    argument_spec.update(get_connect_argument_spec())
    argument_spec.update(
        dataset_src=dict(required=False, type='str'),
        dataset_content=dict(required=False, type='str'),
        dataset_dest=dict(required=True, type='str'),
        dataset_volser=dict(required=False, type='str'),
        dataset_force=dict(required=False, type='bool', default=True),
        dataset_model=dict(required=False, type='str'),
        dataset_data_type=dict(required=False, type='str', default='text', choices=['text', 'binary', 'record']),
        dataset_encoding=dict(required=False, type='dict'),
        dataset_crlf=dict(required=False, type='bool', default=False),
        dataset_diff=dict(required=False, type='bool', default=False),
        dataset_migrate_recall=dict(required=False, type='str', default='wait', choices=['wait', 'nowait', 'error']),
        dataset_checksum=dict(required=False, type='str')
    )
    argument_spec['dataset_encoding']['from'] = dict(required=True, type='str')
    argument_spec['dataset_encoding']['to'] = dict(required=True, type='str')
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    validate_module_params(module)
    copy_dataset(module)


if __name__ == '__main__':
    main()
