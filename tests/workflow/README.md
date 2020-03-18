# Test documentation: workflow
The collection [ibm_zos_zosmf](../../README.md) provides a directory of [Ansible playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbooks-intro), which contains various test playbooks that you can use for testing modules and testing roles.


## Playbooks
The sections that follow explain how to use the test playbooks. 

### Test modules
- [test_module_compare.yml](test_module_compare.yml) - Determine whether the workflow instance already exists and includes the same definition file, variables and properties.

- [test_module_start.yml](test_module_start.yml) - Create the workflow instance if it does not exist and start it.

- [test_module_check.yml](test_module_check.yml) - Check the status of the workflow instance.

- [test_module_delete.yml](test_module_delete.yml) - Delete the workflow instance.

### Test roles
- [test_role_complete_workflow.yml](test_role_complete_workflow.yml) - Complete the workflow instance forcibly or idempotently:
  - `forcibly (force_complete: True)` - Delete the workflow instance if it exists in the z/OSMF server. Create a new workflow instance and start it on each of the target z/OS systems. Periodically check the workflow status and return the final result when the workflow stops running.
  - `idempotently (force_complete: False)` - Create the workflow instance if it does not exist in the z/OSMF server. Start the workflow on each of the target z/OS systems. Periodically check the workflow status and return the final result when the workflow stops running.


## Configuration and setup
Before setup, obtain the installation path for the collection, see the section [Installation](../../README.md#Installation).

### Local test
For local test, you can build the collection archive, and install the locally built collection into `tests/workflow/collections`.

1.  Run a local build inside the collection:

    ```
    cd ibm_zos_zosmf
    ansible-galaxy collection build
    ```

    The example output looks like this:

    ```
    Created collection for ibm.ibm_zos_zosmf at ~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/ibm-ibm_zos_zosmf-1.0.0.tar.gz
    ```

2.  Install the locally built collection into `tests/workflow/collections`:

    ```
    ansible-galaxy collection install ibm-ibm_zos_zosmf-1.0.0.tar.gz -p tests/workflow/collections
    ```

    The example output looks like this:

    ```
    Process install dependency map
    Starting collection install process
    Installing 'ibm.ibm_zos_zosmf:1.0.0' to '~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/workflow/collections/ansible_collections/ibm/ibm_zos_zosmf'
    ```

### Ansible config
This directory contains an example Ansible config [ansible.cfg](ansible.cfg), which refers to the installation path for the collection as [Local test](#local-test):  
`~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/workflow/collections/ansible_collections/ibm/ibm_zos_zosmf`

You can modify the following configuration statement to refer to your own installation path for the collection:

```
collections_paths = collections
```

*Reference Link:* [Ansible configuration settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations)

### Inventory
This directory contains an example Ansible inventory [hosts](hosts), which is used to manage the target z/OS systems (managed nodes). Information is specified in the following format:

```
[${group_name}]
${zos_system_nickname} ansible_host=XXXXXXXX
```

- `${group_name}` - Group name for the target z/OS systems.
- `${zos_system_nickname}` - Nickname for the target z/OS system on which the workflow instance is to be performed.
- `ansible_host` - Hostname of the target z/OS system.

*Reference Link:* [How to build your inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory)

### Group vars
You can supply group variables in either the inventory file or the separate variable file. This directory contains an example variable file [sysplex1](group_vars/sysplex1), which is used for specifying information about the z/OSMF server and workflow variables. Information is specified in the following format:

```
zmf_host: XXXXXXXX
zmf_port: XXXXXXXX
zmf_user: XXXXXXXX
zmf_password: XXXXXXXX
zmf_crt: XXXXXXXX
zmf_key: XXXXXXXX
variables: {XXXXXXXX}
```

- `zmf_host` - Hostname of the z/OSMF server. This value is required.
- `zmf_port` - Port number of the z/OSMF server.
- `zmf_user` - User name to be used for authenticating with z/OSMF server (see note).
- `zmf_password` - Password to be used for authenticating with z/OSMF server (see note).
- `zmf_crt` - Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication (see note).
- `zmf_key` - Location of the PEM-formatted file with your private key to be used for HTTPS client authentication (see note). 
- `variables` - Values of one or more workflow variables (in JSON format).

**NOTE**: You must specify an authentication method - either `zmf_user` and `zmf_password` or `zmf_crt` and `zmf_key`. If both methods are specified, `zmf_crt` and `zmf_key` is used.


## Run the playbooks
The test playbooks must be run from the directory `tests/workflow` of the installed collection. For example:  
`~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/workflow`

You can use the [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command to run the test playbooks as follows:

```
ansible-playbook test_module_compare.yml
ansible-playbook test_module_start.yml
ansible-playbook test_module_check.yml
ansible-playbook test_module_delete.yml
ansible-playbook test_role_complete_workflow.yml
```


## Copyright
© Copyright IBM Corporation 2020.