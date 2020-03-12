# Manipulate z/OS Workflows
This collection provides a module `workflow` as well as a role [complete_workflow](../roles/complete_workflow/README.md) to work with z/OS workflows based on z/OSMF workflow RESTful services. The module will communicate with z/OSMF workflow RESTful services to manipulate workflow based on different parameters it receives.

**NOTE**:
- `delegate_to` - The “delegate_to: localhost” statement is required when using the module in your playbook's task, which makes the module run locally (in control node), so that it does not need to set up SSH connection and install Python on all of the target z/OS systems. Instead, the module will set up HTTPS connections with z/OSMF server. The “delegate_to: localhost” statement is hard-coded inside the role.
- `Naming Rule` - The naming rule *ansible_${workflow_name}_${zos_system_nickname}* is recommended when create a workflow instance.
- `Automated Step` - Due to the limitaion of z/OSMF workflow RESTful services, only automated steps are supported when start a workflow instance.
- `Idempotent` - The module is weakly idempotent. It achives the idempotent for the final state of the workflow instance, rather than that of the target z/OS systems. The strong idempotent for the final state of the target z/OS systems depends on the idempotency of the workflow instance steps.
- `Check Mode` - The module does not support check mode.


## Modules
- `workflow` - This module supports 4 actions to work with z/OS workflows:
  - `compare` - Indicate whether the workflow instance already exists in z/OSMF server and has same definition file, variables and properties.
  - `start` - Create the workflow instance if not exist in z/OSMF server and start it on each of the target z/OS systems.
  - `check` - Check status of the workflow instance in z/OSMF server.
  - `delete` - Delete the workflow instance from z/OSMF server.

### Module Documentation
You can use the [ansible-doc](https://docs.ansible.com/ansible/latest/cli/ansible-doc.html) command to get the information of modules:
```
ansible-doc ibm.ibm_zos_zosmf.workflow
```


## Roles
- [complete_workflow](../roles/complete_workflow/README.md) - This role supports to complete a z/OS workflow forcibly or idempotently:
  - `forcibly (force_complete: True)` - Delete the workflow instance if exists in z/OSMF server, create a new workflow instance and start it on each of the target z/OS systems, then priodically check its status and return final result until the workflow instance stops running.
  - `idempotently (force_complete: False)` - Create the workflow instance if not exist in z/OSMF server and start it on each of the target z/OS systems, then priodically check its status and return final result until the workflow instance stops running.


## Requirements
### Control Node
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) - 2.9 or later.
- [Python](https://www.python.org/downloads/release/latest) -  3.7 or later.
- [Requests library for Python](https://requests.readthedocs.io/en/latest/) - 2.23 or later.

### Managed Node
- [z/OS](https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html) - 2.3 or later.


## Usage
Please refer to directory [examples](../examples/README.md) for various example playbooks.


## Test
Please refer to directory [tests/workflow](../tests/workflow/README.md).


## Copyright
© Copyright IBM Corporation 2020