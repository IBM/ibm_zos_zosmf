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
short_description: Manage z/OS data set or member
description:
    - Create, delete and operate on a sequential or partitioned data set, or a member of partitioned data set (PDS or PDSE) on z/OS system.
    - The available operations include rename data set or member, migrate data set and recall the migrated data set.
    - When forcing data set replacement, contents will not be preserved.
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
    dataset_name:
        description:
            - Name of the data set or member being managed.
            - This variable must consist of a fully qualified data set name. The length of the data set name cannot exceed 44 characters.
            - For example, specifying a data set like C(ZOSMF.ANSIBLE.PS), or a PDS or PDSE member like ``ZOSMF.ANSIBLE.PDS(MEMBER)``.
        required: true
        type: str
    dataset_volser:
        description:
            - The volume serial to identify the volume to be searched for an uncataloged data set or member.
            - The length of the volume serial cannot exceed six characters. Wildcard characters are not supported. Indirect volume serials are not supported.
            - >
              When creating a sequential or partitioned data set,
              this variable specifies the name of the disk volume on which the data set resides. This value is not specified for an SMS-managed data set.
        required: false
        type: str
        default: null
    dataset_state:
        description:
            - The final state desired for specified data set or member.
            - >
              If I(dataset_state=present) and I(dataset_name) does not exist,
              I(dataset_name) is created, the module completes successfully with C(changed=True).
            - >
              If I(dataset_state=present) and I(dataset_name) exists,
              when I(dataset_replace=true), the existing data set is deleted, and a new data set is created with the same name and desired attributes,
              the module completes successfully with C(changed=True).
            - >
              If I(dataset_state=present) and I(dataset_name) exists,
              when I(dataset_replace=false), no action taken, the module completes successfully with C(changed=False).
            - >
              If I(dataset_state=absent) and I(dataset_name) does not exist,
              no action taken, the module completes successfully with C(changed=False).
            - >
              If I(dataset_state=absent) and I(dataset_name) exists,
              the existing I(dataset_name) is deleted, the module completes successfully with C(changed=True).
            - >
              If I(dataset_state=migrated),
              the existing I(dataset_name) is migrated, the module completes successfully with C(changed=True).
            - >
              If I(dataset_state=recalled),
              the migrated I(dataset_name) is recalled, the module completes successfully with C(changed=True).
        required: true
        type: str
        choices:
            - present
            - absent
            - migrated
            - recalled
    dataset_type:
        description:
            - The type to be used when creating a data set or member.
            - When I(dataset_type=MEMBER), I(dataset_name) should be a member of an existing partitioned data set.
            - This variable only take effects when I(dataset_state=present).
        required: false
        type: str
        default: PS
        choices:
            - PS
            - PDS
            - PDSE
            - MEMBER
    dataset_replace:
        description:
            - Specifies whether the existing data set or member matching I(dataset_name) will be replaced when I(dataset_state=present).
            - If I(dataset_replace=true), the existing data set will be deleted, a new data set with the same name and desired attributes will be created.
            - If I(dataset_replace=true), all data in the original data set will be lost.
            - If I(dataset_replace=true), no data set will exist if creation of the new data set fails.
            - This variable only take effects when I(dataset_state=present).
        required: false
        type: bool
        default: false
    dataset_create_attributes:
        description:
            - Specifies the attributes to be used to create a sequential or partitioned data set.
            - This variable only take effects when I(dataset_state=present).
            - This variable only take effects when I(dataset_type=PS) or I(dataset_type=PDS) or I(dataset_type=PDSE).
            - If both I(dataset_create_attributes) and I(dataset_create_like) are supplied, I(dataset_create_like) is ignored.
        required: false
        type: dict
        default: null
        suboptions:
            recfm:
                description:
                    - >
                      Specifies the characteristics of the records in the data set as
                      fixed length (F), variable-length (V), ASCII variable-length (D), or undefined-length (U).
                      Blocked records are specified as FB, VB, or DB.
                      Spanned records are specified as VS, VBS, FS, FBS, DS, or DBS.
                required: false
                type: str
                default: FB
                choices:
                    - FB
                    - VB
                    - DB
                    - F
                    - V
                    - D
                    - U
                    - VS
                    - VBS
                    - FS
                    - FBS
                    - DS
                    - DBS
            lrecl:
                description:
                    - Specifies the length, in bytes, of each record in the data set.
                    - If the records are of variable-length or undefined-length, the maximum record length must be specified.
                required: false
                type: int
                default: 80
            alcunit:
                description:
                    - Specifies the unit (tracks, blocks or cylinders) in which primary and secondary space allocations are to be obtained.
                required: false
                type: str
                default: TRK
                choices:
                    - TRK
                    - BLK
                    - CYL
            primary:
                description:
                    - Specifies the primary space allocation for the data set.
                required: true
                type: int
            secondary:
                description:
                    - Specifies the secondary space allocation for the data set.
                    - >
                      If this value is omitted,
                      the secondary space will be specified as 0.5 times of the primary space when I(dataset_type=PS),
                      or as 0.2 times of the primary space when I(dataset_type=PDS) or I(dataset_type=PDSE).
                required: false
                type: int
                default: null
            dirblk:
                description:
                    - Specifies the number of directory blocks.
                required: false
                type: int
                default: null
            avgblk:
                description:
                    - Specifies the average block size.
                required: false
                type: int
                default: null
            blksize:
                description:
                    - Specifies the maximum length of a block.
                required: false
                type: int
                default: null
            unit:
                description:
                    - Specifies the storage unit device type.
                required: false
                type: str
                default: 3390
            storclass:
                description:
                    - Specifies the storage class for an SMS-managed data set.
                required: false
                type: str
                default: null
            mgntclass:
                description:
                    - Specifies the management class for an SMS-managed data set.
                required: false
                type: str
                default: null
            dataclass:
                description:
                    - Specifies the data class for an SMS-managed data set.
                required: false
                type: str
                default: null
    dataset_create_like:
        description:
            - Specifies the model data set to be used to create a sequential or partitioned data set.
            - For example, specifying a model data set like C(ZOSMF.ANSIBLE.MODEL), member name should not be provided in this variable.
            - This variable only take effects when I(dataset_state=present).
            - This variable only take effects when I(dataset_type=PS) or I(dataset_type=PDS) or I(dataset_type=PDSE).
            - If both I(dataset_create_attributes) and I(dataset_create_like) are supplied, I(dataset_create_like) is ignored.
        required: false
        type: str
        default: null
    dataset_new_name:
        description:
            - Specifies the new name of the data set or member.
            - This variable only take effects when I(dataset_state=present).
        required: false
        type: str
        default: null
    dataset_migrate_recall:
        description:
            - Specifies how a migrated data set is handled when I(dataset_state=present).
            - If I(dataset_migrate_recall=wait), the migrated data set is recalled synchronously.
            - If I(dataset_migrate_recall=nowait), request the migrated data set to be recalled, but do not wait.
            - If I(dataset_migrate_recall=error), do not attempt to recall the migrated data set.
            - Specifies whether wait for the completion of the request when I(dataset_state=migrated) or I(dataset_state=recalled).
            - If I(dataset_migrate_recall=wait), wait for the completion of the request.
            - If I(dataset_migrate_recall=nowait), the request is queued.
            - I(dataset_migrate_recall=error) is invalid when I(dataset_state=migrated) or I(dataset_state=recalled).
        required: false
        type: str
        default: wait
        choices:
            - wait
            - nowait
            - error
requirements:
    - requests >= 2.23.0
"""

EXAMPLES = r"""
- name: Create a sequential data set ZOSMF.ANSIBLE.PS if it does not exist
  zmf_dataset:
    zmf_host: "sample.ibm.com"
    dataset_name: "ZOSMF.ANSIBLE.PS"
    dataset_state: "present"
    dataset_type: "PS"
    dataset_create_attributes:
      primary: 10

- name: Create a sequential data set ZOSMF.ANSIBLE.PS depending on the model data set ZOSMF.ANSIBLE.MODEL
  zmf_dataset:
    zmf_host: "sample.ibm.com"
    dataset_name: "ZOSMF.ANSIBLE.PS"
    dataset_state: "present"
    dataset_type: "PS"
    dataset_create_like: "ZOSMF.ANSIBLE.MODEL"

- name: Replace a partitioned data set ZOSMF.ANSIBLE.PDS if it exists
  zmf_dataset:
    zmf_host: "sample.ibm.com"
    dataset_name: "ZOSMF.ANSIBLE.PDS"
    dataset_state: "present"
    dataset_type: "PDS"
    dataset_replace: true
    dataset_create_attributes:
      primary: 10

- name: Create a data set member ZOSMF.ANSIBLE.PDS(MEMBER) to an existing PDS, replace if member exists
  zmf_dataset:
    zmf_host: "sample.ibm.com"
    dataset_name: "ZOSMF.ANSIBLE.PDS(MEMBER)"
    dataset_state: "present"
    dataset_type: "MEMBER"
    dataset_replace: true

- name: Rename a data set ZOSMF.ANSIBLE.PS to ZOSMF.ANSIBLE.PS01
  zmf_dataset:
    zmf_host: "sample.ibm.com"
    dataset_name: "ZOSMF.ANSIBLE.PS"
    dataset_state: "present"
    dataset_type: "PS"
    dataset_new_name: "ZOSMF.ANSIBLE.PS01"

- name: Rename a data set member ZOSMF.ANSIBLE.PDS(MEMBER) to ZOSMF.ANSIBLE.PDS(MEMBER01)
  zmf_dataset:
    zmf_host: "sample.ibm.com"
    dataset_name: "ZOSMF.ANSIBLE.PDS(MEMBER)"
    dataset_state: "present"
    dataset_type: "MEMBER"
    dataset_new_name: "ZOSMF.ANSIBLE.PDS(MEMBER01)"

- name: Delete a data set ZOSMF.ANSIBLE.PS
  zmf_dataset:
    zmf_host: "sample.ibm.com"
    dataset_name: "ZOSMF.ANSIBLE.PS"
    dataset_state: "absent"

- name: Migrate a data set ZOSMF.ANSIBLE.PS
  zmf_dataset:
    zmf_host: "sample.ibm.com"
    dataset_name: "ZOSMF.ANSIBLE.PS"
    dataset_state: "migrated"

- name: Recall a data set ZOSMF.ANSIBLE.PS and wait for the completion of the request
  zmf_dataset:
    zmf_host: "sample.ibm.com"
    dataset_name: "ZOSMF.ANSIBLE.PS"
    dataset_state: "recalled"
    dataset_migrate_recall: "wait"
"""

RETURN = r"""
changed:
    description: Indicates if any change is made during the module operation.
    returned: always
    type: bool
message:
    description: The output message generated by the module to indicate whether the data set or member is successfully created, deleted, or updated.
    returned: on success
    type: str
    sample:
        sample1: "The data set ZOSMF.ANSIBLE.PS is created successfully."
        sample2: "The data set member ZOSMF.ANSIBLE.PDS(MEMBER) is deleted successfully."
        sample3: "The data set ZOSMF.ANSIBLE.PS does not exist."
        sample4: "The data set member ZOSMF.ANSIBLE.PDS(MEMBER) already exists."
        sample5: "The data set ZOSMF.ANSIBLE.PS is successfully renamed to /ZOSMF.ANSIBLE.PS01."
        sample6: "The data set ZOSMF.ANSIBLE.PS is migrated successfully."
        sample7: "The data set ZOSMF.ANSIBLE.PS is recalled successfully."
dataset_properties:
    description: The properties of the present data set.
    returned: on success
    type: dict
    sample: {
        "dsname": "ZOSMF.ANSIBLE.PS",
        "blksz": "80",
        "catnm": "CATALOG.SVPLEX.MASTER",
        "cdate": "2021/01/21",
        "dev": "3390",
        "dsorg": "PS",
        "edate": "None",
        "extx": "1",
        "lrecl": "80",
        "migr": "NO",
        "mvol": "N",
        "ovf": "NO",
        "rdate": "2021/01/25",
        "recfm": "FB",
        "sizex": "4",
        "spacu": "TRACKS",
        "used": "0",
        "vol": "VOL001",
        "vols": "VOL001"
    }
member_properties:
    description: The properties of the present member.
    returned: on success
    type: dict
    sample: {
        "c4date": "2021/01/21",
        "cnorc": 2,
        "inorc": 0,
        "m4date": "2021/01/21",
        "member": "MEMBER",
        "mnorc": 0,
        "mod": 2,
        "msec": "42",
        "mtime": "02:51",
        "sclm": "N",
        "user": "IBMUSER",
        "vers": 1
    }
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
    is_member = False
    # validate dataset_name
    if not (module.params['dataset_name'] is not None and module.params['dataset_name'].strip() != ''):
        module.fail_json(msg='Missing required argument or invalid argument: dataset_name.')
    elif module.params['dataset_name'].strip().find('(') > 0:
        is_member = True
    # validate dataset_type
    if is_member and module.params['dataset_type'] != "MEMBER":
        module.fail_json(
            msg='Invalid argument: dataset_type. dataset_name is specified as a member of partitioned data set, so dataset_type=MEMBER is expected.'
        )
    elif not is_member and module.params['dataset_type'] == "MEMBER":
        module.fail_json(
            msg='Invalid argument: dataset_type. dataset_name is specified as a sequential or partitioned data set, so dataset_type=MEMBER is invalid.'
        )
    # validate dataset_state
    if module.params['dataset_state'] == 'present':
        if is_member:
            if module.params['dataset_create_attributes'] is not None:
                module.fail_json(msg='dataset_create_attributes is valid only when dataset_type=PS or dataset_type=PDS or dataset_type=PDSE.')
            if module.params['dataset_create_like'] is not None and module.params['dataset_create_like'].strip() != '':
                module.fail_json(msg='dataset_create_like is valid only when dataset_type=PS or dataset_type=PDS or dataset_type=PDSE.')
        # validate dataset_new_name
        if module.params['dataset_new_name'] is not None and module.params['dataset_new_name'].strip() != '':
            is_rn_member = False
            if module.params['dataset_new_name'].strip().find('(') > 0:
                is_rn_member = True
            if is_member and not is_rn_member:
                module.fail_json(
                    msg='Invalid argument: dataset_new_name. '
                        + 'dataset_name is specified as a member of partitioned data set, so dataset_new_name should be the new name of the member.'
                )
            elif not is_member and is_rn_member:
                module.fail_json(
                    msg='Invalid argument: dataset_new_name. '
                        + 'dataset_name is specified as a sequential or partitioned data set, so dataset_new_name should be the new name of the data set.'
                )
    else:
        if module.params['dataset_replace'] is True:
            module.fail_json(msg='dataset_replace=True is valid only when dataset_state=present.')
        if module.params['dataset_create_attributes'] is not None:
            module.fail_json(msg='dataset_create_attributes is valid only when dataset_state=present.')
        if module.params['dataset_create_like'] is not None and module.params['dataset_create_like'].strip() != '':
            module.fail_json(msg='dataset_create_like is valid only when dataset_state=present.')
        if module.params['dataset_new_name'] is not None and module.params['dataset_new_name'].strip() != '':
            module.fail_json(msg='dataset_new_name is valid only when dataset_state=present.')
        if is_member and (module.params['dataset_state'] == 'migrated' or module.params['dataset_state'] == 'recalled'):
            module.fail_json(msg='dataset_state=migrated or dataset_state=recalled is valid only for data set.')
    # validate dataset_create_attributes
    if module.params['dataset_create_attributes'] is not None:
        if isinstance(module.params['dataset_create_attributes'], dict):
            has_recfm = False
            has_lrecl = False
            has_alcunit = False
            has_primary = False
            has_secondary = False
            has_dirblk = False
            has_avgblk = False
            has_blksize = False
            has_unit = False
            has_storclass = False
            has_mgntclass = False
            has_dataclass = False
            for k, v in module.params['dataset_create_attributes'].items():
                if k == 'recfm':
                    has_recfm = True
                    if v is not None and str(v).strip() != '':
                        if (str(v).strip().upper() == 'FB' or str(v).strip().upper() == 'VB' or str(v).strip().upper() == 'DB'
                                or str(v).strip().upper() == 'F' or str(v).strip().upper() == 'V'
                                or str(v).strip().upper() == 'D' or str(v).strip().upper() == 'U'
                                or str(v).strip().upper() == 'VS' or str(v).strip().upper() == 'VBS'
                                or str(v).strip().upper() == 'DS' or str(v).strip().upper() == 'DBS'
                                or str(v).strip().upper() == 'FS' or str(v).strip().upper() == 'FBS'):
                            module.params['dataset_create_attributes']['recfm'] = str(v).strip().upper()
                        else:
                            module.fail_json(
                                msg='Invalid argument: dataset_create_attributes. '
                                    + 'Invalid suboption: recfm, the following values are valid: '
                                    + '[FB, VB, DB, F, V, D, U, VS, VBS, FS, FBS, DS, DBS].'
                            )
                    else:
                        has_recfm = False
                elif k == 'lrecl':
                    has_lrecl = True
                    if v is not None and str(v).strip() != '':
                        try:
                            if int(str(v)) < 0:
                                module.fail_json(
                                    msg='Invalid argument: dataset_create_attributes. '
                                        + 'Invalid suboption: lrecl, it must be a interger and equal or larger than 0.'
                                )
                            else:
                                module.params['dataset_create_attributes']['lrecl'] = int(str(v))
                        except Exception:
                            module.fail_json(
                                msg='Invalid argument: dataset_create_attributes. '
                                    + 'Invalid suboption: lrecl, it must be a interger and equal or larger than 0.'
                            )
                    else:
                        has_lrecl = False
                elif k == 'alcunit':
                    has_alcunit = True
                    if v is not None and str(v).strip() != '':
                        if str(v).strip().upper() == 'TRK' or str(v).strip().upper() == 'BLK' or str(v).strip().upper() == 'CYL':
                            module.params['dataset_create_attributes']['alcunit'] = str(v).strip().upper()
                        else:
                            module.fail_json(
                                msg='Invalid argument: dataset_create_attributes. '
                                    + 'Invalid suboption: alcunit, the following values are valid: [TRK, BLK, CYL].'
                            )
                    else:
                        has_alcunit = False
                elif k == 'primary':
                    has_primary = True
                    if v is not None and str(v).strip() != '':
                        try:
                            if int(str(v)) <= 0:
                                module.fail_json(
                                    msg='Invalid argument: dataset_create_attributes. '
                                        + 'Invalid suboption: primary, it must be a interger and larger than 0.'
                                )
                            else:
                                module.params['dataset_create_attributes']['primary'] = int(str(v))
                        except Exception:
                            module.fail_json(
                                msg='Invalid argument: dataset_create_attributes. '
                                    + 'Invalid suboption: primary, it must be a interger and larger than 0.'
                            )
                    else:
                        has_primary = False
                elif k == 'secondary':
                    has_secondary = True
                    if v is not None and str(v).strip() != '':
                        try:
                            if int(str(v)) < 0:
                                module.fail_json(
                                    msg='Invalid argument: dataset_create_attributes. '
                                        + 'Invalid suboption: secondary, it must be a interger and equal or larger than 0.'
                                )
                            else:
                                module.params['dataset_create_attributes']['secondary'] = int(str(v))
                        except Exception:
                            module.fail_json(
                                msg='Invalid argument: dataset_create_attributes. '
                                    + 'Invalid suboption: secondary, it must be a interger and equal or larger than 0.'
                            )
                    else:
                        has_secondary = False
                elif k == 'dirblk':
                    has_dirblk = True
                    if v is not None and str(v).strip() != '':
                        try:
                            if int(str(v)) < 0:
                                module.fail_json(
                                    msg='Invalid argument: dataset_create_attributes. '
                                        + 'Invalid suboption: dirblk, it must be a interger and equal or larger than 0.'
                                )
                            else:
                                module.params['dataset_create_attributes']['dirblk'] = int(str(v))
                        except Exception:
                            module.fail_json(
                                msg='Invalid argument: dataset_create_attributes. '
                                    + 'Invalid suboption: dirblk, it must be a interger and equal or larger than 0.'
                            )
                    else:
                        has_dirblk = False
                elif k == 'avgblk':
                    has_avgblk = True
                    if v is not None and str(v).strip() != '':
                        try:
                            if int(str(v)) < 0:
                                module.fail_json(
                                    msg='Invalid argument: dataset_create_attributes. '
                                        + 'Invalid suboption: avgblk, it must be a interger and equal or larger than 0.'
                                )
                            else:
                                module.params['dataset_create_attributes']['avgblk'] = int(str(v))
                        except Exception:
                            module.fail_json(
                                msg='Invalid argument: dataset_create_attributes. '
                                    + 'Invalid suboption: avgblk, it must be a interger and equal or larger than 0.'
                            )
                    else:
                        has_avgblk = False
                elif k == 'blksize':
                    has_blksize = True
                    if v is not None and str(v).strip() != '':
                        try:
                            if int(str(v)) < 0:
                                module.fail_json(
                                    msg='Invalid argument: dataset_create_attributes. '
                                        + 'Invalid suboption: blksize, it must be a interger and equal or larger than 0.'
                                )
                            else:
                                module.params['dataset_create_attributes']['blksize'] = int(str(v))
                        except Exception:
                            module.fail_json(
                                msg='Invalid argument: dataset_create_attributes. '
                                    + 'Invalid suboption: blksize, it must be a interger and equal or larger than 0.'
                            )
                    else:
                        has_blksize = False
                elif k == 'unit':
                    has_unit = True
                    if v is not None and str(v).strip() != '':
                        module.params['dataset_create_attributes']['unit'] = str(v).strip()
                    else:
                        has_unit = False
                elif k == 'storclass':
                    has_storclass = True
                    if v is not None and str(v).strip() != '':
                        module.params['dataset_create_attributes']['storclass'] = str(v).strip()
                    else:
                        has_storclass = False
                elif k == 'mgntclass':
                    has_mgntclass = True
                    if v is not None and str(v).strip() != '':
                        module.params['dataset_create_attributes']['mgntclass'] = str(v).strip()
                    else:
                        has_mgntclass = False
                elif k == 'dataclass':
                    has_dataclass = True
                    if v is not None and str(v).strip() != '':
                        module.params['dataset_create_attributes']['dataclass'] = str(v).strip()
                    else:
                        has_dataclass = False
                else:
                    module.fail_json(
                        msg='Invalid argument: dataset_create_attributes. It should be a dict and contain the following suboptions only: '
                            + 'recfm, lrecl, alcunit, primary(required), secondary, '
                            + 'dirblk, avgblk, blksize, unit, storclass, mgntclass, dataclass.'
                    )
            if not has_recfm:
                module.params['dataset_create_attributes']['recfm'] = 'FB'
            if not has_lrecl:
                module.params['dataset_create_attributes']['lrecl'] = 80
            if not has_alcunit:
                module.params['dataset_create_attributes']['alcunit'] = 'TRK'
            if not has_primary:
                module.fail_json(msg='Invalid argument: dataset_create_attributes. Missing required suboption or invalid suboption: primary.')
            if 'secondary' in module.params['dataset_create_attributes'] and not has_secondary:
                module.params['dataset_create_attributes'].pop('secondary')
            if 'dirblk' in module.params['dataset_create_attributes'] and not has_dirblk:
                module.params['dataset_create_attributes'].pop('dirblk')
            if 'avgblk' in module.params['dataset_create_attributes'] and not has_avgblk:
                module.params['dataset_create_attributes'].pop('avgblk')
            if 'blksize' in module.params['dataset_create_attributes'] and not has_blksize:
                module.params['dataset_create_attributes'].pop('blksize')
            if not has_unit:
                module.params['dataset_create_attributes']['unit'] = '3390'
            if 'storclass' in module.params['dataset_create_attributes'] and not has_storclass:
                module.params['dataset_create_attributes'].pop('storclass')
            if 'mgntclass' in module.params['dataset_create_attributes'] and not has_mgntclass:
                module.params['dataset_create_attributes'].pop('mgntclass')
            if 'dataclass' in module.params['dataset_create_attributes'] and not has_dataclass:
                module.params['dataset_create_attributes'].pop('dataclass')
        else:
            module.fail_json(
                msg='Invalid argument: dataset_create_attributes. It should be a dict and contain the following suboptions only: '
                    + 'recfm, lrecl, alcunit, primary(required), secondary, '
                    + 'dirblk, avgblk, blksize, unit, storclass, mgntclass, dataclass.'
            )
    # validate dataset_migrate_recall
    if module.params['dataset_migrate_recall'] == 'error' and (module.params['dataset_state'] == 'migrated' or module.params['dataset_state'] == 'recalled'):
        module.fail_json(msg='dataset_migrate_recall=error is invalid when dataset_state=migrated or dataset_state=recalled.')


def dataset_exist(module):
    """
    Check if a data set or member already exists
    Return exist_result to indicate if a data set or member with same name already exists.
    :param AnsibleModule module: the ansible module
    """
    exist_result = dict(
        is_member=False,
        ds_exist=False,
        m_exist=False
    )
    # create session
    session = get_connect_session(module)
    target = module.params['dataset_name'].strip().upper()
    exist_result['session'] = session
    exist_result['target'] = target
    # setup data set full name, data set name and member name
    ds_full_name = ''
    ds_v_name = ''
    ds_name = ''
    m_name = ''
    v_name = ''
    if target.find('(') > 0:
        exist_result['is_member'] = True
        ds_name = target[:target.find('(')]
        m_name = target[target.find('(') + 1:target.find(')')]
    else:
        ds_name = target
    if module.params['dataset_volser'] is not None and module.params['dataset_volser'].strip() != '':
        v_name = module.params['dataset_volser'].strip().upper()
        ds_full_name = '-(' + v_name + ')/' + target
        ds_v_name = '-(' + v_name + ')/' + ds_name
    else:
        ds_full_name = target
        ds_v_name = ds_name
    module.params['ds_full_name'] = ds_full_name
    module.params['ds_v_name'] = ds_v_name
    module.params['ds_name'] = ds_name
    module.params['m_name'] = m_name
    module.params['v_name'] = v_name
    # step 1 - combine request headers
    request_headers = dict()
    request_headers['X-IBM-Attributes'] = 'base'
    # step 2 - check if the target data set with same name already exists
    res_list = call_dataset_api(module, session, 'list_ds', request_headers)
    if res_list.status_code == 200:
        res_content = json.loads(res_list.content)
        if 'returnedRows' in res_content and res_content['returnedRows'] > 0 and res_content['items'][0]['dsname'] == module.params['ds_name']:
            exist_result['ds_exist'] = True
            exist_result['dataset_properties'] = res_content['items'][0]
    # step 3 - check if the target member with same name already exists
    if exist_result['is_member'] and exist_result['ds_exist']:
        res_list = call_dataset_api(module, session, 'list_m', request_headers)
        if res_list.status_code == 200:
            res_content = json.loads(res_list.content)
            if 'returnedRows' in res_content and res_content['returnedRows'] > 0:
                exist_result['m_exist'] = True
                exist_result['member_properties'] = res_content['items'][0]
    return exist_result


def create_dataset(module, session, target, is_member):
    """
    Create a data set or member
    Return the message to indicate whether the data set or member is created successfully.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str target: the data set or member to be created
    :param bool is_member: indicate whether the target is a member or not
    """
    create_result = dict(
        changed=False,
        message='',
    )
    # create data set
    if not is_member:
        # step1 - setup request args
        request_body = dict()
        if module.params['dataset_create_attributes'] is not None:
            request_body = module.params['dataset_create_attributes']
            if module.params['dataset_type'] == 'PS':
                request_body['dsorg'] = 'PS'
            elif module.params['dataset_type'] == 'PDS':
                request_body['dsorg'] = 'PO'
                request_body['dsntype'] = 'PDS'
            elif module.params['dataset_type'] == 'PDSE':
                request_body['dsorg'] = 'PO'
                request_body['dsntype'] = 'LIBRARY'
            else:
                module.fail_json(msg='dataset_create_attributes is valid only when dataset_type=PS or dataset_type=PDS or dataset_type=PDSE.')
            if 'secondary' not in request_body:
                if module.params['dataset_type'] == 'PS':
                    request_body['secondary'] = math.ceil(0.5 * int(request_body['primary']))
                else:
                    request_body['secondary'] = math.ceil(0.2 * int(request_body['primary']))
            if module.params['dataset_volser'] is not None and module.params['dataset_volser'].strip() != '':
                request_body['volser'] = module.params['dataset_volser'].strip().upper()
        elif module.params['dataset_create_like'] is not None and module.params['dataset_create_like'].strip() != '':
            request_body['like'] = module.params['dataset_create_like'].strip()
            if module.params['dataset_volser'] is not None and module.params['dataset_volser'].strip() != '':
                request_body['volser'] = module.params['dataset_volser'].strip().upper()
                request_body['unit'] = '3390'
        else:
            module.fail_json(
                msg='Failed to create the data set ' + target
                    + ' ---- Missing required argument or invalid argument: either dataset_create_attributes or dataset_create_like is required.'
            )
        # step2 - setup request headers
        request_headers = dict()
        request_headers['Content-Type'] = 'application/json'
        # step3 - create the data set or member
        res_create = call_dataset_api(module, session, 'create', request_headers, json.dumps(request_body))
        if res_create.status_code == 201:
            create_result['changed'] = True
            create_result['message'] = 'The data set ' + target + ' is created successfully.'
        else:
            module.fail_json(
                msg='Failed to create the data set ' + target + ' ---- Http request error: '
                    + str(res_create.status_code) + ': ' + str(res_create.json())
            )
    # create member
    else:
        # step1 - setup request args
        request_body = ''
        # step2 - setup request headers
        request_headers = dict()
        request_headers['Content-Type'] = 'text/plain'
        # step3 - create the data set or member
        res_create = call_dataset_api(module, session, 'copy', request_headers, request_body)
        if res_create.status_code == 201:
            create_result['changed'] = True
            create_result['message'] = 'The data set member ' + target + ' is created successfully.'
        else:
            module.fail_json(
                msg='Failed to create the data set member ' + target + ' ---- Http request error: '
                    + str(res_create.status_code) + ': ' + str(res_create.json())
            )
    operate_result = operate_dataset(module, session, target, is_member, None, 'rename')
    if operate_result['message'] != '':
        create_result['message'] += ' ' + operate_result['message']
    if 'dataset_properties' in operate_result:
        create_result['dataset_properties'] = operate_result['dataset_properties']
    if 'member_properties' in operate_result:
        create_result['member_properties'] = operate_result['member_properties']
    if 'errors' not in operate_result:
        module.exit_json(**create_result)
    else:
        create_result['errors'] = operate_result['errors']
        module.fail_json(msg=str(create_result))


def delete_dataset(module, session, target, is_member, exist, is_replace):
    """
    Delete a data set or member
    Return the message to indicate whether the data set or member is deleted successfully.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str target: the data set or member to be deleted
    :param bool is_member: indicate whether the target is a member or not
    :param bool exist: whether the data set or member to be deleted exists or not
    :param bool is_replace: whether the existing data set or member will be replaced
    """
    delete_result = dict(
        changed=False,
        message='',
    )
    # step1 - exit if the data set or member to be deleted does not exist
    if not exist:
        if not is_member:
            delete_result['message'] = 'The data set ' + target + ' does not exist.'
        else:
            delete_result['message'] = 'The data set member ' + target + ' does not exist.'
        module.exit_json(**delete_result)
    # step2 - delete the data set or member
    res_delete = call_dataset_api(module, session, 'delete')
    if res_delete.status_code == 204:
        delete_result['changed'] = True
        if not is_member:
            delete_result['message'] = 'The data set ' + target + ' is deleted successfully.'
        else:
            delete_result['message'] = 'The data set member ' + target + ' is deleted successfully.'
        if not is_replace:
            module.exit_json(**delete_result)
    else:
        if not is_member:
            module.fail_json(
                msg='Failed to delete the data set ' + target + ' ---- Http request error: '
                    + str(res_delete.status_code) + ': ' + str(res_delete.json())
            )
        else:
            module.fail_json(
                msg='Failed to delete the data set member ' + target + ' ---- Http request error: '
                    + str(res_delete.status_code) + ': ' + str(res_delete.json())
            )


def operate_dataset(module, session, target, is_member, old_properties, action):
    """
    Operate on a data set or member
    Return the message to indicate whether the data set or member is updated successfully.
    Return the dataset_properties or member_properties of the updated data set or member.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str target: the data set or member to be operated
    :param bool is_member: indicate whether the target is a member or not
    :param dict old_properties: the old properties of the data set or member
    :param str action: the operation
    """
    operate_result = dict(
        changed=False,
        message='',
    )
    need_migrate = False
    need_recall = False
    need_rename = False
    new = ''
    # step1 - operate on the data set or member
    if action == 'hmigrate':
        need_migrate = True
        migrate = operate_dataset_action(module, session, 'hmigrate', target)
        if migrate['updated'] is True:
            operate_result['changed'] = True
        else:
            if 'errors' not in operate_result:
                operate_result['errors'] = []
            operate_result['errors'].append('Failed to migrate the data set ' + target + migrate['error'])
    elif action == 'hrecall':
        need_recall = True
        recall = operate_dataset_action(module, session, 'hrecall', target)
        if recall['updated'] is True:
            operate_result['changed'] = True
        else:
            if 'errors' not in operate_result:
                operate_result['errors'] = []
            operate_result['errors'].append('Failed to recall the data set ' + target + recall['error'])
    elif action == 'rename':
        if module.params['dataset_new_name'] is not None and module.params['dataset_new_name'].strip() != '':
            need_rename = True
            rename = operate_dataset_action(module, session, 'rename', target)
            if rename['updated'] is True:
                operate_result['changed'] = True
                new = rename['new']
            else:
                if 'errors' not in operate_result:
                    operate_result['errors'] = []
                if not is_member:
                    operate_result['errors'].append('Failed to rename the data set ' + target + rename['error'])
                else:
                    operate_result['errors'].append('Failed to rename the data set member ' + target + rename['error'])
    # step2 - return the roperties of the data set or member
    if old_properties is not None and (need_migrate is not True and need_recall is not True and need_rename is not True):
        if not is_member:
            operate_result['dataset_properties'] = old_properties
            operate_result['message'] = 'The data set ' + target + ' already exists.'
        else:
            operate_result['member_properties'] = old_properties
            operate_result['message'] = 'The data set member ' + target + ' already exists.'
        module.exit_json(**operate_result)
    else:
        request_headers = dict()
        request_headers['X-IBM-Attributes'] = 'base'
        if not is_member:
            res_list = call_dataset_api(module, session, 'list_ds', request_headers)
            if res_list.status_code == 200:
                res_content = json.loads(res_list.content)
                if 'returnedRows' in res_content and res_content['returnedRows'] > 0 and res_content['items'][0]['dsname'] == module.params['ds_name']:
                    operate_result['dataset_properties'] = res_content['items'][0]
        else:
            res_list = call_dataset_api(module, session, 'list_m', request_headers)
            if res_list.status_code == 200:
                res_content = json.loads(res_list.content)
                if 'returnedRows' in res_content and res_content['returnedRows'] > 0:
                    operate_result['member_properties'] = res_content['items'][0]
        if need_migrate is True:
            if 'errors' not in operate_result:
                operate_result['message'] = 'The data set ' + target + ' is migrated successfully. '
            else:
                operate_result['message'] = 'Failed to migrate the data set ' + target + '. '
        if need_recall is True:
            if 'errors' not in operate_result:
                operate_result['message'] = 'The data set ' + target + ' is recalled successfully. '
            else:
                operate_result['message'] = 'Failed to recall the data set ' + target + '. '
        if need_rename is True:
            if new != '':
                if not is_member:
                    operate_result['message'] += 'The data set ' + target + ' is successfully renamed to ' + new + '.'
                else:
                    operate_result['message'] += 'The data set member ' + target + ' is successfully renamed to ' + new + '.'
            else:
                if not is_member:
                    operate_result['message'] += 'Failed to rename the data set ' + target + '.'
                else:
                    operate_result['message'] += 'Failed to rename the data set member ' + target + '.'
        if old_properties is None:
            return operate_result
        else:
            if 'errors' not in operate_result:
                module.exit_json(**operate_result)
            else:
                module.fail_json(msg=str(operate_result))


def operate_dataset_action(module, session, action, target):
    """
    Operate on a data set or member
    Return operate_result_action to indicate whether each operation for the data set or member is successfully.
    :param AnsibleModule module: the ansible module
    :param Session session: the current connection session
    :param str action: the operation
    :param str target: the data set or member to be operated
    """
    operate_result_action = dict(
        updated=False,
        error=''
    )
    old_ds_full_name = module.params['ds_full_name']
    old_ds_v_name = module.params['ds_v_name']
    old_ds_name = module.params['ds_name']
    old_m_name = module.params['m_name']
    # step1 - setup request args
    request_body = dict()
    request_body['request'] = action
    if action == 'hmigrate' or action == 'hrecall':
        # migrate or recall
        if module.params['dataset_migrate_recall'] == 'wait':
            request_body['wait'] = True
        elif module.params['dataset_migrate_recall'] == 'nowait':
            request_body['wait'] = False
    elif action == 'rename':
        # rename
        new = module.params['dataset_new_name'].strip().upper()
        # setup data set full name, data set name and member name
        ds_full_name = ''
        ds_v_name = ''
        ds_name = ''
        m_name = ''
        v_name = ''
        if new.find('(') > 0:
            ds_name = new[:new.find('(')]
            m_name = new[new.find('(') + 1:new.find(')')]
        else:
            ds_name = new
        if module.params['dataset_volser'] is not None and module.params['dataset_volser'].strip() != '':
            v_name = module.params['dataset_volser'].strip().upper()
            ds_full_name = '-(' + v_name + ')/' + new
            ds_v_name = '-(' + v_name + ')/' + ds_name
        else:
            ds_full_name = new
            ds_v_name = ds_name
        module.params['ds_full_name'] = ds_full_name
        module.params['ds_v_name'] = ds_v_name
        module.params['ds_name'] = ds_name
        module.params['m_name'] = m_name
        module.params['v_name'] = v_name
        request_body['from-dataset'] = dict()
        request_body['from-dataset']['dsn'] = old_ds_name
        if old_m_name is not None and old_m_name != '':
            request_body['from-dataset']['member'] = old_m_name
    # step2 - setup request headers
    request_headers = dict()
    request_headers['Content-Type'] = 'application/json'
    # step3 - operate on the data set or member
    res_operate = call_dataset_api(module, session, 'operate', request_headers, json.dumps(request_body))
    if res_operate.status_code == 200:
        operate_result_action['updated'] = True
        if action == 'rename':
            operate_result_action['new'] = new
    else:
        # reset data set full name, data set name and member name if rename is failed
        if action == 'rename':
            module.params['ds_full_name'] = old_ds_full_name
            module.params['ds_v_name'] = old_ds_v_name
            module.params['ds_name'] = old_ds_name
            module.params['m_name'] = old_m_name
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
        dataset_name=dict(required=True, type='str'),
        dataset_volser=dict(required=False, type='str'),
        dataset_state=dict(required=True, type='str', choices=['present', 'absent', 'migrated', 'recalled']),
        dataset_type=dict(required=False, type='str', default='PS', choices=['PS', 'PDS', 'PDSE', 'MEMBER']),
        dataset_replace=dict(required=False, type='bool', default=False),
        dataset_create_attributes=dict(required=False, type='dict'),
        dataset_create_like=dict(required=False, type='str'),
        dataset_new_name=dict(required=False, type='str'),
        dataset_migrate_recall=dict(required=False, type='str', default='wait', choices=['wait', 'nowait', 'error'])
    )
    argument_spec['dataset_create_attributes']['recfm'] = dict(
        required=False, type='str', default='FB',
        choices=['FB', 'VB', 'DB', 'F', 'V', 'D', 'U', 'VS', 'VBS', 'FS', 'FBS', 'DS', 'DBS']),
    argument_spec['dataset_create_attributes']['lrecl'] = dict(required=False, type='int', default=80)
    argument_spec['dataset_create_attributes']['alcunit'] = dict(required=False, type='str', default='TRK', choices=['TRK', 'BLK', 'CYL'])
    argument_spec['dataset_create_attributes']['primary'] = dict(required=True, type='int')
    argument_spec['dataset_create_attributes']['secondary'] = dict(required=False, type='int')
    argument_spec['dataset_create_attributes']['dirblk'] = dict(required=False, type='int')
    argument_spec['dataset_create_attributes']['avgblk'] = dict(required=False, type='int')
    argument_spec['dataset_create_attributes']['blksize'] = dict(required=False, type='int')
    argument_spec['dataset_create_attributes']['unit'] = dict(required=False, type='str', default='3390')
    argument_spec['dataset_create_attributes']['storclass'] = dict(required=False, type='str')
    argument_spec['dataset_create_attributes']['mgntclass'] = dict(required=False, type='str')
    argument_spec['dataset_create_attributes']['dataclass'] = dict(required=False, type='str')
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    # validate params
    validate_module_params(module)
    # check if exists
    exist_result = dataset_exist(module)
    if exist_result['is_member']:
        if module.params['dataset_state'] == 'present':
            if not exist_result['ds_exist']:
                module.fail_json(
                    msg='Failed to create the data set member ' + exist_result['target'] + ' ---- The data set ' + module.params['ds_name'] + ' does not exist.'
                )
            elif not exist_result['m_exist']:
                create_dataset(module, exist_result['session'], exist_result['target'], True)
            else:
                if module.params['dataset_replace'] is True:
                    delete_dataset(module, exist_result['session'], exist_result['target'], True, True, True)
                    create_dataset(module, exist_result['session'], exist_result['target'], True)
                else:
                    operate_dataset(module, exist_result['session'], exist_result['target'], True, exist_result['member_properties'], 'rename')
        elif module.params['dataset_state'] == 'absent':
            delete_dataset(module, exist_result['session'], exist_result['target'], True, exist_result['m_exist'], False)
        else:
            module.fail_json(msg='dataset_state=migrated or dataset_state=recalled is valid only for data set.')
    else:
        if module.params['dataset_state'] == 'present':
            if not exist_result['ds_exist']:
                create_dataset(module, exist_result['session'], exist_result['target'], False)
            else:
                if module.params['dataset_replace'] is True:
                    delete_dataset(module, exist_result['session'], exist_result['target'], False, True, True)
                    create_dataset(module, exist_result['session'], exist_result['target'], False)
                else:
                    operate_dataset(module, exist_result['session'], exist_result['target'], False, exist_result['dataset_properties'], 'rename')
        elif module.params['dataset_state'] == 'absent':
            delete_dataset(module, exist_result['session'], exist_result['target'], False, exist_result['ds_exist'], False)
        elif module.params['dataset_state'] == 'migrated':
            if not exist_result['ds_exist']:
                module.fail_json(msg='Failed to migrate the data set ' + exist_result['target'] + ' ---- The data set does not exist.')
            else:
                operate_dataset(module, exist_result['session'], exist_result['target'], False, exist_result['dataset_properties'], 'hmigrate')
        else:
            if not exist_result['ds_exist']:
                module.fail_json(msg='Failed to recall the data set ' + exist_result['target'] + ' ---- The data set does not exist.')
            else:
                operate_dataset(module, exist_result['session'], exist_result['target'], False, exist_result['dataset_properties'], 'hrecall')


if __name__ == '__main__':
    main()
