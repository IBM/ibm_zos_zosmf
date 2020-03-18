# Ansible role: complete_workflow
The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), which is referred to as `complete_workflow`. This role is used for completing a z/OS workflow, either forcibly or idempotently.


## Role variables
The available role variables are described as follows.

### Defined by role
The following variables are defined by role. For the default values, see [defaults/main.yml](defaults/main.yml).

- `force_complete` - Specify whether to complete the workflow instance forcibly or idempotently:
  - `forcibly (force_complete: True)` - Delete the workflow instance if it exists in the z/OSMF server. Create a new workflow instance and start it on each of the target z/OS systems. Periodically check the workflow status and return the final result when the workflow stops running.
  - `idempotently (force_complete: False)` - Create the workflow instance if it does not exist in the z/OSMF server. Start the workflow on each of the target z/OS systems. Periodically check the workflow status and return the final result when the workflow stops running.

- `complete_check_times` - The maximum number of time that is used for periodic checks of the workflow status.

- `complete_check_delay` - The interval time between periodic checks of the workflow status.

### Defined by module
To see the variables that are defined by the module `workflow`, use the [ansible-doc](https://docs.ansible.com/ansible/latest/cli/ansible-doc.html) command:

```
ansible-doc ibm.ibm_zos_zosmf.workflow
```


## Requirements
See the section [Requirements](../../docs/README_workflow.md#Requirements). 


## Dependencies
None


## Usage
For a sample playbook, see [sample_role_complete_workflow.yml](../../examples/sample_role_complete_workflow.yml) in the directory [examples](../../examples/README.md).


## Test
For a test playbook, see [test_role_complete_workflow.yml](../../tests/workflow/test_role_complete_workflow.yml) in the directory [tests/workflow](../../tests/workflow/README.md).


## Copyright
© Copyright IBM Corporation 2020.