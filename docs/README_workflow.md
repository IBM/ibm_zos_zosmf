# Manipulating z/OS workflows
The collection provides a module `workflow` and a role [complete_workflow](../roles/complete_workflow/README.md) for working with z/OS workflows. The module uses z/OSMF workflow RESTful services to manipulate a workflow, based on the different parameters it receives. The module provides the following functions: compare, start, check and delete. The role is used for completing a workflow, either forcibly or idempotently. 

**NOTE**:
- `delegate_to` - The **“delegate_to: localhost”** statement is required for using the module in your playbook task. This statement is hard-coded within the role. The statement causes the module to run locally in control node. With this setting in effect, it is not necessary for you to set up an SSH connection and install Python on the target z/OS systems. Instead, the module creates HTTPS connections with the z/OSMF server.

- `Naming Rule` - It is recommended that you use the naming rule ***ansible_${workflow_name}_${zos_system_nickname}*** when you create a workflow instance.

- `Automated Step` - Only automated steps are supported when a workflow is started.

- `Idempotent` - The module is considered to be "weakly" idempotent. That is, the module achieves an idempotent result for the final state of the workflow instance, rather than for the target z/OS systems. A strong idempotent result for the final state of the target z/OS systems depends on the idempotency of the workflow instance steps.

- `Check Mode` - The module does not support check mode.


## Modules
- `workflow` - This module supports the following actions for working with z/OS workflows:
  - `compare` - Indicate whether the workflow instance already exists in the z/OSMF server and has the same definition file, variables and properties.
  - `start` - Create the workflow instance if it does not exist in the z/OSMF server and start it on each of the target z/OS systems.
  - `check` - Check the status of the workflow instance in the z/OSMF server.
  - `delete` - Delete the workflow instance from the z/OSMF server.

### Module documentation
For information about the modules, use the [ansible-doc](https://docs.ansible.com/ansible/latest/cli/ansible-doc.html) command:

```
ansible-doc ibm.ibm_zos_zosmf.workflow
```


## Roles
- [complete_workflow](../roles/complete_workflow/README.md) - This role is used for completing a z/OS workflow, either forcibly or idempotently:
  - `forcibly (force_complete: True)` - Delete the workflow instance if it exists in the z/OSMF server. Create a new workflow instance and start it on each of the target z/OS systems. Periodically check the workflow status and return the final result when the workflow stops running.
  - `idempotently (force_complete: False)` - Create the workflow instance if it does not exist in the z/OSMF server. Start the workflow on each of the target z/OS systems. Periodically check the workflow status and return the final result when the workflow stops running.


## Requirements
Observe the following requirements.

### Control node
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) - 2.9 or later.
- [Python](https://www.python.org/downloads/release/latest) -  3.7 or later.
- [Requests library for Python](https://requests.readthedocs.io/en/latest/) - 2.23 or later.

### Managed node
- [z/OS](https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html) - 2.3 or later.


## Usage
The collection provides various sample playbooks to demonstrate the use of modules and roles in the directory [examples](../examples/README.md).


## Test
See the section [Test documentation: workflow](../tests/workflow/README.md).


## Copyright
© Copyright IBM Corporation 2020.