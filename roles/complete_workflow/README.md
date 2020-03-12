# Ansible Role: complete_workflow
The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), referred to as `complete_workflow`, to complete a z/OS workflow forcibly or idempotently.


## Role Variables
The available role variables include the following two parts:

### Specified by Role
The variables specified by role are listed below, you can get their default values in [defaults/main.yml](defaults/main.yml):

- `force_complete` - Specify whether complete the workflow instance forcibly or idempotently:
  - `forcibly (force_complete: True)` - Delete the workflow instance if exists in z/OSMF server, create a new workflow instance and start it on each of the target z/OS systems, then priodically check its status and return final result until the workflow instance stops running.
  - `idempotently (force_complete: False)` - Create the workflow instance if not exist in z/OSMF server and start it on each of the target z/OS systems, then priodically check its status and return final result until the workflow instance stops running.
- `complete_check_times` - The maximum times for the priodically checking of the workflow instance status.
- `complete_check_delay` - The interval time between two of the priodically checking of the workflow instance status.

### Specified by Module
The variables specified by the involved module `workflow` can be found using the [ansible-doc](https://docs.ansible.com/ansible/latest/cli/ansible-doc.html) command:
```
ansible-doc ibm.ibm_zos_zosmf.workflow
```


## Requirements
Please refer to section [Requirements](../../docs/README_workflow.md#Requirements). 


## Dependencies
None


## Usage
Please refer to directory [examples](../../examples/README.md) for various example playbooks.


## Test
Please refer to the test playbook [test_role_complete_workflow.yml](../../tests/workflow/test_role_complete_workflow.yml) in the directory [tests/workflow](../../tests/workflow/README.md).


## Copyright
© Copyright IBM Corporation 2020