#!/usr/bin/python

# Copyright (c) IBM Corporation 2020
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: workflow
short_description: Ansible module for running z/OS workflows
description:
    - "Ansible module for running z/OS workflows by issuing z/OSMF workflow RESTful services."
version_added: "2.9"
author: "Yang Cao (@zosmf-Young), Yun Juan Yang (@zosmf-Robyn)"
requirements: []
options:
    action:
        description:
            - Action to be performed by the module.
        required: true
        type: str
        choices: ['compare', 'start', 'check', 'delete']
    zmf_host:
        description:
            - Hostname of the z/OSMF server.
        required: true
        type: str
    zmf_port:
        description:
            - Port number of the z/OSMF server.
        required: false
        type: int
    zmf_user:
        description:
            - User name to be used for authenticating with z/OSMF server.
            - If zmf_crt and zmf_key are supplied, zmf_user and zmf_password are ignored.
        required: false
        type: str
    zmf_password:
        description:
            - Password to be used for authenticating with z/OSMF server.
            - If zmf_crt and zmf_key are supplied, zmf_user and zmf_password are ignored.
        required: false
        type: str
    zmf_crt:
        description:
            - Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication.
        required: false
        type: str
    zmf_key:
        description:
            - Location of the PEM-formatted file with your private key to be used for HTTPS client authentication.
        required: false
        type: str
    zos_workflow_name:
        description:
            - Descriptive name of the workflow.
            - It is recommended that you use the naming rule ansible_workflowName_{{ zos_workflow_host }}.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_file:
        description:
            - Location of the workflow definition file.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_host:
        description:
            - Nickname of the system on which the workflow is to be performed.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_owner:
        description:
            - User name of the workflow owner.
            - If this value is omitted, zmf_user is used as workflow owner.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_file_system:
        description:
            - Nickname of the system on which the specified workflow definition file and any related files reside.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_vars_file:
        description:
            - Location of the optional properties file to be used to pre-specify the values of one or more variables
              that are defined in workflow definition file.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_vars:
        description:
            - Values of one or more workflow variables in JSON format.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: dict
    zos_workflow_resolve_global_conflict_by_using:
        description:
            - Version of the variable to be used if the supplied workflow variable conflicts with an existing global variable in z/OSMF Workflows task.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
        choices: ['global', 'input']
    zos_workflow_comments:
        description:
            - User-specified information to be associated with the workflow at creation time.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_assign_to_owner:
        description:
            - Specifies whether the workflow steps are assigned to the workflow owner when the workflow is created.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: bool
    zos_workflow_access_type:
        description:
            - Access type for the workflow when the workflow is created.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
        choices: ['Public', 'Restricted', 'Private']
    zos_workflow_account_info:
        description:
            - For a workflow that submits a batch job, this variable specifies the account information for the JCL JOB statement.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_job_statement:
        description:
            - For a workflow that submits a batch job, this variable specifies the JOB statement JCL for the job.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_delete_completed_jobs:
        description:
            - For a workflow that submits a batch job, this variable specifies whether the job is deleted from the JES spool after it completes.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: bool
    zos_workflow_resolve_conflict_by_using:
        description:
            - Specifies how to handle variable conflicts if any are detected at workflow creation time.
            - Such conflicts can be found when z/OSMF Workflows task reads the output file from a step that runs a REXX exec or UNIX shell script.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
        choices: ['outputFileValue', 'existingValue', 'leaveConflict']
    zos_workflow_step_name:
        description:
            - Name of the workflow step at which automation processing is to begin when the workflow is started.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_perform_subsequent:
        description:
            - Specifies whether the subsequent automated steps are performed when the workflow is started.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: bool
    zos_workflow_notification_url:
        description:
            - URL to be used for notification when the workflow is started.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_category:
        description:
            - Category for the workflow.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
        choices: ['general', 'configuration']
    zos_workflow_vender:
        description:
            - Name of the vendor that provided the workflow definition file.
            - For more information, see the documentation for the z/OSMF workflow REST services.
        required: false
        type: str
    zos_workflow_key:
        description:
            - Generated key to uniquely identify the workflow instance.
        required: false
        type: str
'''

EXAMPLES = '''
'''

RETURN = '''
changed:
    description:
        - (action compare) Always be false.
        - (action start) Indicate whether the workflow instance is created and started.
        - (action check) Always be false.
        - (action delete) Indicate whether the workflow instance is deleted.
    returned: always
    type: bool
message:
    description:
        - (action compare) Indicate whether the workflow instance does not exist, or exists with same or different definition file, variables and properties.
        - (action start) Indicate whether the workflow instance is started.
        - (action check) Indicate whether the workflow instance is completed, is not completed, or is still in progress.
        - (action delete) Indicate whether the workflow instance does not exist or is deleted.
    returned: success
    type: str
exist_workflow_key:
    description:
        - (action compare) Key for the existing workflow instance.
    returned: success
    type: str
same_workflow_instance:
    description:
        - (action compare) Indicate whether the existing workflow instance has the same or different definition file, variables and properties.
    returned: success
    type: bool
workflow_completed:
    description:
        - (action compare) Indicate whether the existing workflow instance has been completed.
    returned: success
    type: bool
workflow_key:
    description:
        - (action start) Key for the started workflow instance.
    returned: success
    type: str
waiting:
    description:
        - (action check) Indicate whether it needs to wait and check again because the workflow instance is still in progress.
    returned: success
    type: bool
completed:
    description:
        - (action check) Indicate whether the workflow instance is completed.
    returned: success
    type: bool
deleted:
    description:
        - (action delete) Indicate whether the workflow instance is deleted.
    returned: success
    type: bool
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.workflow_util import get_connect_argument_spec
except ImportError:
    def get_connect_argument_spec():
        return dict()
try:
    from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.workflow_api import get_request_argument_spec
except ImportError:
    def get_request_argument_spec():
        return dict()
try:
    from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.workflow_util import get_connect_session
except ImportError:
    get_connect_session = None
try:
    from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.workflow_api import call_workflow_api
except ImportError:
    call_workflow_api = None
try:
    from ansible_collections.ibm.ibm_zos_zosmf.plugins.module_utils.workflow_util import cmp_list
except ImportError:
    def cmp_list(list1, list2):
        return True
import json


def get_next_step_name(module, current_step_number, response_retrieveP):
    """
    Return the next step name
    :param AnsibleModule module: the ansible module
    :param str current_step_number: the current step number
    :param dict response_retrieveP: the response of the workflow API to retrieve the properties of a z/OSMF workflow instance
    :rtype: str
    """
    next_step_name = ''
    nextList = []
    curList = current_step_number.split('.')
    level = len(curList)
    prefix = ''
    count = 1
    steps = response_retrieveP['steps']
    while steps is not None and count <= level:
        found = False
        index = 0
        while index <= len(steps) - 1:
            if steps[index]['stepNumber'] == prefix + curList[count - 1]:
                found = True
                if count == level:
                    if index != len(steps) - 1:
                        nextList.append(steps[index + 1])
                else:
                    if index != len(steps) - 1:
                        nextList.append(steps[index + 1])
                    steps = steps[index]['steps']
                break
            index += 1
        if found is False:
            steps = None
        prefix += curList[count - 1] + '.'
        count += 1
    while len(nextList) > 0:
        step = nextList.pop()
        if step['steps'] is None:
            next_step_name = step['name']
            break
        nextList.append(step['steps'][0])
    return next_step_name


def is_same_workflow_instance(module, argument_spec_mapping, response_retrieveP, response_retrieveD):
    """
    Compare two workflow instances to see whether they have same definition files, variables and properties
    :param AnsibleModule module: the ansible module
    :param dict[str, dict] argument_spec_mapping: the mapping between arguments of ansible module and params of all workflow APIs
    :param dict response_retrieveP: the response of the workflow API to retrieve the properties of a z/OSMF workflow instance
    :param dict response_retrieveD: the response of the workflow API to retrieve the contents of a z/OSMF workflow definition from a z/OS system
    :returns: True/False if the given two workflow instances have same/different definition files, None if cannot compare since no definition file is supplied
    :returns: True/False if the given two workflow instances have same/different variables, None if cannot compare since no definition file is supplied to get
              default value or cannot get the content of supplied var file
    :returns: True/False if the given two workflow instances have same/different properties
    :returns: diff_name of the different variable or property
    :returns: diff_value of the different variable or property
    :rtype: (bool, bool, bool, str, str)
    """
    sameD = True
    sameV = True
    sameP = True
    diff_name = ''
    diff_value = ''
    conflict_by_input = False
    input_file_defined = False
    default_list_vars = []
    res_list_vars = []
    module_vars = dict()
    default_vars = dict()
    # compare definition files
    if 'workflowDefinitionFileMD5Value' in response_retrieveD and 'workflowDefinitionFileMD5Value' in response_retrieveP:
        if response_retrieveD['workflowDefinitionFileMD5Value'] != response_retrieveP['workflowDefinitionFileMD5Value']:
            return (False, sameV, sameP, diff_name, diff_value)
    else:
        sameD = None
    # compare variables
    if (module.params['zos_workflow_resolve_global_conflict_by_using'] is not None
            and module.params['zos_workflow_resolve_global_conflict_by_using'].strip().lower() == 'input'):
        conflict_by_input = True
    if (module.params['zos_workflow_vars_file'] is not None
            and module.params['zos_workflow_vars_file'].strip() != ''):
        input_file_defined = True
    if (module.params['zos_workflow_vars'] is not None
            and len(module.params['zos_workflow_vars']) > 0):
        module_vars = module.params['zos_workflow_vars']
        for k, v in module_vars.items():
            if v is None or str(v).strip() == '':
                module_vars.pop(k)
    if 'variables' in response_retrieveD and len(response_retrieveD['variables']) > 0:
        default_list_vars = response_retrieveD['variables']
        for v in default_list_vars:
            default_vars[v['name']] = v['default']
    if 'variables' in response_retrieveP and len(response_retrieveP['variables']) > 0:
        res_list_vars = response_retrieveP['variables']
    skip = False
    for v in res_list_vars:
        if v['scope'] == 'global' and conflict_by_input is False:
            # same since the supplied value will be ignored and the current global value will be used.
            continue
        if v['scope'] != 'global' and v['value'] is None:
            if v['name'] not in default_vars:
                # skip: cannot get current value since it will use default value
                skip = True
                continue
            v['value'] == default_vars[v['name']]
        if v['name'] in module_vars:
            if v['type'] == 'array' and v['value'] is not None:
                if isinstance(module_vars[v['name']], list) and cmp_list(json.loads(v['value']), module_vars[v['name']]) is True:
                    # same since the supplied value is exactly same as the current value
                    continue
                return (sameD, False, sameP, v['name'], v['value'])
            else:
                if str(v['value']).strip().lower() == str(module_vars[v['name']]).strip().lower():
                    # same since the supplied value is exactly same as the current value
                    continue
                return (sameD, False, sameP, v['name'], v['value'])
        elif input_file_defined is True:
            # skip: cannot get the content of input file
            skip = True
            continue
        elif v['name'] in default_vars:
            if v['type'] == 'array' and v['value'] is not None and default_vars[v['name']] is not None:
                if cmp_list(json.loads(v['value']), json.loads(default_vars[v['name']])) is True:
                    # same since the default value is exactly same as the current value
                    continue
                return (sameD, False, sameP, v['name'], v['value'])
            else:
                if str(v['value']).strip().lower() == str(default_vars[v['name']]).strip().lower():
                    # same since the default value is exactly same as the current value
                    continue
                return (sameD, False, sameP, v['name'], v['value'])
        else:
            # skip: cannot get the supplied value since it will use default value
            skip = True
            continue
    if skip is True:
        sameV = None
    # compare properties
    for k, v in module.params.items():
        if k in argument_spec_mapping and argument_spec_mapping[k]['name'] in response_retrieveP:
            res_v = response_retrieveP[argument_spec_mapping[k]['name']]
            if k == 'zos_workflow_host':
                if res_v.find('(') > -1 and res_v.find(')') > -1:
                    res_v = res_v[res_v.index('(') + 1:res_v.rindex(')')]
                elif res_v.find('.') > -1:
                    res_v = res_v[res_v.rindex('.') + 1:]
            elif k == 'zos_workflow_owner' and (v is None or str(v).strip() == ''):
                v = module.params['zmf_user']
            elif v is None and 'default' in argument_spec_mapping[k]:
                v = argument_spec_mapping[k]['default']
            if (isinstance(v, str) and v.strip() != '') or isinstance(v, bool):
                if str(v).strip().lower() != str(res_v).strip().lower():
                    return (sameD, sameV, False, k, res_v)
    return (sameD, sameV, sameP, diff_name, diff_value)


def action_compare(module, argument_spec_mapping):
    """
    Indicate whether the workflow instance specified by zos_workflow_name already exists
    If the workflow instance already exists, indicate whether they have same definition files, variables and properties
    Return the message to indicate whether the workflow instance does not exist, or exists with same or different definition file, variables and properties
    Return the exist_workflow_key of the existing workflow instance
    Return the same_workflow_instance flag to indicate whether the existing workflow instance has same or different definition file, variables and properties
    Return the workflow_completed flag to indicate whether the existing workflow instance with same definition file, variables and properties has been completed
    :param AnsibleModule module: the ansible module
    :param dict[str, dict] argument_spec_mapping: the mapping between arguments of ansible module and params of all workflow APIs
    """
    workflow_key = ''
    compare_result = dict(
        changed=False,
        exist_workflow_key='',
        same_workflow_instance=False,
        workflow_completed=False,
        message=''
    )
    # create session
    session = get_connect_session(module)
    # step1 - find workflow instance by name
    response_list = call_workflow_api(module, session, 'list', workflow_key)
    if isinstance(response_list, dict):
        if 'workflows' in response_list and len(response_list['workflows']) > 0:
            workflow_key = response_list['workflows'][0]['workflowKey']
        else:
            compare_result['message'] = 'No workflow instance named: ' + module.params['zos_workflow_name'] + ' is found.'
            module.exit_json(**compare_result)
    else:
        module.fail_json(msg='Failed to find workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_list)
    # step2 - compare the properties and definition files
    response_retrieveP = call_workflow_api(module, session, 'retrieveProperties', workflow_key)
    if isinstance(response_retrieveP, str):
        module.fail_json(
            msg='Failed to get properties of workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_retrieveP
        )
    response_retrieveD = dict()
    if module.params['zos_workflow_file'] is not None and module.params['zos_workflow_file'].strip() != '':
        response_retrieveD = call_workflow_api(module, session, 'retrieveDefinition', workflow_key)
        if isinstance(response_retrieveD, str):
            module.fail_json(
                msg='Failed to get definition file of workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_retrieveD
            )
    (sameD, sameV, sameP, diff_name, diff_value) = is_same_workflow_instance(module, argument_spec_mapping, response_retrieveP, response_retrieveD)
    if sameD is False:
        compare_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] + ' with different definition file is found.'
    elif sameV is False:
        compare_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] + ' with different variable: ' \
            + diff_name + ' = ' + str(diff_value) + ' is found.'
    elif sameP is False:
        compare_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] + ' with different property: ' \
            + diff_name + ' = ' + str(diff_value) + ' is found.'
    elif sameD is None or sameV is None:
        compare_result['same_workflow_instance'] = True
        compare_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] \
            + ' is found. While it could not be compared since the argument: zos_workflow_file is required,' \
            + ' and please supply variables by the argument: zos_workflow_vars rather than the argument: zos_workflow_vars_file.'
    else:
        compare_result['same_workflow_instance'] = True
        compare_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] \
            + ' with same definition file, variables and properties is found.'
    if compare_result['same_workflow_instance'] is not False and response_retrieveP['statusName'] == 'complete':
        compare_result['workflow_completed'] = True
    compare_result['exist_workflow_key'] = workflow_key
    module.exit_json(**compare_result)


def action_start(module):
    """
    Start the workflow instance specified by zos_workflow_key
    If zos_workflow_key is not supplied, create the workflow instance specified by zos_workflow_name if not exist and then start it
    Return the message to indicate the workflow instance is started
    Return the workflow_key of the started workflow instance
    :param AnsibleModule module: the ansible module
    """
    workflow_key = ''
    start_by_key = False
    start_result = dict(
        changed=False,
        workflow_key='',
        message=''
    )
    # create session
    session = get_connect_session(module)
    # decide if start by name or key
    if module.params['zos_workflow_key'] is not None and module.params['zos_workflow_key'].strip() != '':
        workflow_key = module.params['zos_workflow_key']
        start_by_key = True
    # step1 - find workflow instance by name
    if workflow_key == '':
        if module.params['zos_workflow_name'] is None or module.params['zos_workflow_name'].strip() == '':
            module.fail_json(msg='A valid argument of either zos_workflow_name or zos_workflow_key is required.')
        response_list = call_workflow_api(module, session, 'list', workflow_key)
        if isinstance(response_list, dict):
            if 'workflows' in response_list and len(response_list['workflows']) > 0:
                workflow_key = response_list['workflows'][0]['workflowKey']
        else:
            module.fail_json(msg='Failed to find workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_list)
    # step2 - create workflow instance if needed
    if workflow_key == '':
        response_create = call_workflow_api(module, session, 'create', workflow_key)
        if isinstance(response_create, dict):
            if 'workflowKey' in response_create and response_create['workflowKey'] != '':
                workflow_key = response_create['workflowKey']
            else:
                module.fail_json(msg='Failed to create workflow instance named: ' + module.params['zos_workflow_name'] + '.')
        else:
            module.fail_json(msg='Failed to create workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_create)
    # step3 - start workflow instance
    response_start = call_workflow_api(module, session, 'start', workflow_key)
    if isinstance(response_start, dict):
        start_result['changed'] = True
        start_result['workflow_key'] = workflow_key
        if start_by_key is True:
            start_result['message'] = 'Workflow instance with key: ' + workflow_key + ' is started, you can use check action to check its final status.'
        else:
            start_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] \
                + ' is started, you can use check action to check its final status.'
        module.exit_json(**start_result)
    else:
        # handle start issue caused by non-automated step
        next_step_message = ''
        if response_start.find('IZUWF5007E') > 0:
            next_step_message = ' You can manually complete this step in z/OSMF Workflows task,' \
                + ' and start this workflow instance again with next step name specified in argument: zos_workflow_step_name.'
        if start_by_key is True:
            module.fail_json(
                msg='Failed to start workflow instance with key: ' + workflow_key + ' ---- ' + response_start + next_step_message
            )
        else:
            module.fail_json(
                changed=True,
                msg='Failed to start workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_start + next_step_message
            )


def action_check(module):
    """
    Check status of the workflow instance specified by zos_workflow_key
    If zos_workflow_key is not supplied, check status of the workflow instance specified by zos_workflow_name
    Return the message to indicate whether the workflow instance is completed, is not completed, or is still in progress
    Return the waiting flag to indicate whether it needs to wait and check again since the workflow instance is still in progress
    :param AnsibleModule module: the ansible module
    """
    workflow_key = ''
    check_by_key = False
    next_step_name = ''
    check_result = dict(
        changed=False,
        waiting=True,
        completed=False,
        message=''
    )
    # create session
    session = get_connect_session(module)
    # decide if check by name or key
    if module.params['zos_workflow_key'] is not None and module.params['zos_workflow_key'].strip() != '':
        workflow_key = module.params['zos_workflow_key']
        check_by_key = True
    # step1 - find workflow instance by name if needed
    if workflow_key == '':
        if module.params['zos_workflow_name'] is None or module.params['zos_workflow_name'].strip() == '':
            module.fail_json(msg='A valid argument of either zos_workflow_name or zos_workflow_key is required.')
        response_list = call_workflow_api(module, session, 'list', workflow_key)
        if isinstance(response_list, dict):
            if 'workflows' in response_list and len(response_list['workflows']) > 0:
                workflow_key = response_list['workflows'][0]['workflowKey']
            else:
                module.fail_json(msg='No workflow instance named: ' + module.params['zos_workflow_name'] + ' is found.')
        else:
            module.fail_json(msg='Failed to find workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_list)
    # step2 - get workflow properties
    response_retrieveP = call_workflow_api(module, session, 'retrieveProperties', workflow_key)
    if isinstance(response_retrieveP, dict):
        if 'statusName' in response_retrieveP:
            status = response_retrieveP['statusName']
            if status == 'automation-in-progress':
                if check_by_key is True:
                    check_result['message'] = 'Workflow instance with key: ' + workflow_key + ' is still in progress.'
                else:
                    check_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] + ' is still in progress.'
                module.exit_json(**check_result)
            elif status == 'complete':
                check_result['waiting'] = False
                check_result['completed'] = True
                if check_by_key is True:
                    check_result['message'] = 'Workflow instance with key: ' + workflow_key + ' is completed.'
                else:
                    check_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] + ' is completed.'
                module.exit_json(**check_result)
            else:
                step_status = response_retrieveP['automationStatus']
                check_result['waiting'] = False
                if step_status is None:
                    if check_by_key is True:
                        check_result['message'] = 'Workflow instance with key: ' + workflow_key + ' is not completed: No step is started.'
                    else:
                        check_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] + ' is not completed: No step is started.'
                else:
                    current_step_message = ''
                    next_step_message = ''
                    if step_status['currentStepNumber'] is not None:
                        current_step_message = 'In step ' + step_status['currentStepNumber'] + ' ' + step_status['currentStepTitle'] + ': '
                    # handle specific start issues
                    if step_status['messageID'] == 'IZUWF0145E' and step_status['currentStepNumber'] is not None:
                        next_step_name = get_next_step_name(module, step_status['currentStepNumber'], response_retrieveP)
                        if next_step_name != '':
                            next_step_message = ' You can manually complete this step in z/OSMF Workflows task,' \
                                + ' and start this workflow instance again with next step name: ' \
                                + next_step_name + ' specified in argument: zos_workflow_step_name.'
                    if step_status['messageID'] == 'IZUWF0162I':
                        next_step_message = ' While one or more steps may be skipped.'
                    if check_by_key is True:
                        check_result['message'] = 'Workflow instance with key: ' + workflow_key + ' is not completed: ' \
                            + current_step_message + step_status['messageText'] + next_step_message
                    else:
                        check_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] + ' is not completed: ' \
                            + current_step_message + step_status['messageText'] + next_step_message
                module.exit_json(**check_result)
        else:
            if check_by_key is True:
                module.fail_json(msg='Failed to get properties of workflow instance with key: ' + workflow_key + '.')
            else:
                module.fail_json(msg='Failed to get properties of workflow instance named: ' + module.params['zos_workflow_name'] + '.')
    else:
        if check_by_key is True:
            module.fail_json(msg='Failed to get properties of workflow instance with key: ' + workflow_key + ' ---- ' + response_retrieveP)
        else:
            module.fail_json(msg='Failed to get properties of workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_retrieveP)


def action_delete(module):
    """
    Delete the workflow instance specified by zos_workflow_key
    If zos_workflow_key is not supplied, delete the workflow instance specified by zos_workflow_name
    Return the message to indicate whether the workflow instance does not exist or is deleted
    :param AnsibleModule module: the ansible module
    """
    workflow_key = ''
    delete_by_key = False
    delete_result = dict(
        changed=False,
        deleted=False,
        message=''
    )
    # create session
    session = get_connect_session(module)
    # decide if delete by name or key
    if module.params['zos_workflow_key'] is not None and module.params['zos_workflow_key'].strip() != '':
        workflow_key = module.params['zos_workflow_key']
        delete_by_key = True
    # step1 - find workflow instance by name if needed
    if workflow_key == '':
        if module.params['zos_workflow_name'] is None or module.params['zos_workflow_name'].strip() == '':
            module.fail_json(msg='A valid argument of either zos_workflow_name or zos_workflow_key is required.')
        response_list = call_workflow_api(module, session, 'list', workflow_key)
        if isinstance(response_list, dict):
            if 'workflows' in response_list and len(response_list['workflows']) > 0:
                workflow_key = response_list['workflows'][0]['workflowKey']
            else:
                delete_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] + ' does not exist.'
                module.exit_json(**delete_result)
        else:
            module.fail_json(msg='Failed to find workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_list)
    # step2 - delete workflow instance
    response_delete = call_workflow_api(module, session, 'delete', workflow_key)
    if isinstance(response_delete, dict):
        delete_result['changed'] = True
        delete_result['deleted'] = True
        if delete_by_key is True:
            delete_result['message'] = 'Workflow instance with key: ' + workflow_key + ' is deleted.'
        else:
            delete_result['message'] = 'Workflow instance named: ' + module.params['zos_workflow_name'] + ' is deleted.'
        module.exit_json(**delete_result)
    else:
        if delete_by_key is True:
            module.fail_json(msg='Failed to delete workflow instance with key: ' + workflow_key + ' ---- ' + response_delete)
        else:
            module.fail_json(msg='Failed to delete workflow instance named: ' + module.params['zos_workflow_name'] + ' ---- ' + response_delete)


def main():
    argument_spec = dict()
    (argument_spec_mapping, request_argument_spec) = get_request_argument_spec()
    argument_spec.update(get_connect_argument_spec())
    argument_spec.update(request_argument_spec)
    argument_spec.update(
        action=dict(required=True, type='str', choices=['compare', 'start', 'check', 'delete']),
        zos_workflow_key=dict(required=False, type='str'))
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False
    )
    # validation for import from module_utils
    if get_connect_session is None or call_workflow_api is None:
        module.fail_json(msg='ImportError: cannot import from ibm.ibm_zos_zosmf.plugins.module_utils')
    # validation for action
    if module.params['action'].strip().lower() == 'compare':
        if module.params['zos_workflow_name'] is None or module.params['zos_workflow_name'].strip() == '':
            module.fail_json(msg='Missing required argument or invalid argument: zos_workflow_name')
        action_compare(module, argument_spec_mapping)
    elif module.params['action'].strip().lower() == 'start':
        action_start(module)
    elif module.params['action'].strip().lower() == 'check':
        action_check(module)
    elif module.params['action'].strip().lower() == 'delete':
        action_delete(module)
    else:
        module.fail_json(msg='Wrong action')


if __name__ == '__main__':
    main()
