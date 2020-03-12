# Test Documentation: workflow
The collection [ibm_zos_zosmf](../../README.md) provides a directory of [Ansible playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbooks-intro) which contains various test playbooks for testing the modules and roles.


## Playbooks
### Test Modules
- [test_module_compare.yml](test_module_compare.yml) - Indicate whether the workflow instance already exists and has same definition file, variables and properties.
- [test_module_start.yml](test_module_start.yml) - Create the workflow instance if not exist and start it.
- [test_module_check.yml](test_module_check.yml) - Check status of the workflow instance.
- [test_module_delete.yml](test_module_delete.yml) - Delete the workflow instance.

### Test Roles
- [test_role_complete_workflow.yml](test_role_complete_workflow.yml) - Complete the workflow instance forcibly or idempotently:
  - `forcibly (force_complete: True)` - Delete the workflow instance if exists in z/OSMF server, create a new workflow instance and start it on each of the target z/OS systems, then priodically check its status and return final result until the workflow instance stops running.
  - `idempotently (force_complete: False)` - Create the workflow instance if not exist in z/OSMF server and start it on each of the target z/OS systems, then priodically check its status and return final result until the workflow instance stops running.


## Configuration and Setup
Before setup, please refer back to section [Installation](../../README.md#Installation) to get the installation path of collection. 

### Local Build and Installation
For local build and installation, you can clone the Git repository, build the collection archive and install locally without Galaxy.

1.  Clone the Git repository:
    ```
    git clone git@github.com:ibm/ibm_zos_zosmf.git
    ```

2.  Run local build inside the collection:
    ```
    cd ibm_zos_zosmf
    ansible-galaxy collection build
    ```

    The example output looks like:
    ```
    Created collection for ibm.ibm_zos_zosmf at /Users/user/git/ibm/ibm_zos_zosmf/ibm-ibm_zos_zosmf-1.0.0.tar.gz
    ```

3.  Install the locally built collection into `tests/workflow/collections`:
    ```
    ansible-galaxy collection install ibm-ibm_zos_zosmf-1.0.0.tar.gz -p tests/workflow/collections
    ```

    The example output looks like:
    ```
    Process install dependency map
    Starting collection install process
    Installing 'ibm.ibm_zos_zosmf:1.0.0' to '/Users/user/git/ibm/ibm_zos_zosmf/tests/workflow/collections/ansible_collections/ibm/ibm_zos_zosmf'
    ```

### Configure Ansible
This directory contains an example Ansible config [ansible.cfg](ansible.cfg) which refers to [Local Build and Installation](#Setup). You can modify the following configuration to your own installation path of collection:
```
collections_paths = collections
```

*Reference Link:* [Ansible configuration settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations)

### Inventory
This directory contains an example Ansible inventory [hosts](hosts) to manage the target z/OS systems (managed nodes) with the following template:
```
[${group_name}]
${zos_system_nickname} ansible_host=XXXXXXXX
${zos_system_nickname} ansible_host=XXXXXXXX
```

- `${group_name}` - The group name of all target z/OS systems.
- `${zos_system_nickname}` - The nickname of target z/OS system on which the workflow instance is to be performed.
- `ansible_host` - The hostname of target z/OS system.

*Reference Link:* [How to build your inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory)

### Group Vars
You can supply group variables either in the inventory file or in the separate variable file. This directory contains an example variable file [group_vars/sysplex1](group_vars/sysplex1) to supply the information of z/OSMF server and other variables with the following template:
```
zmf_host: XXXXXXXX
zmf_port: XXXXXXXX
zmf_user: XXXXXXXX
zmf_password: XXXXXXXX
zmf_crt: XXXXXXXX
zmf_key: XXXXXXXX

variables: {XXXXXXXX}
```

- `zmf_host` - The hostname of z/OSMF server.
- `zmf_port` - (Optional) The port number of z/OSMF server.
- `zmf_user` - (Optional) The username for authenticating with z/OSMF server.
- `zmf_password` - (Optional) The password for authenticating with z/OSMF server.
- `zmf_crt` - (Optional) The location of PEM formatted certificate chain file to be used for HTTPS client authentication.
- `zmf_key` - (Optional) The location of PEM formatted file that contains your private key to be used for HTTPS client authentication.
- `variables` - (Optional) The values of one or more workflow variables in JSON format.

**NOTE**: Either `zmf_user/zmf_password` or `zmf_crt/zmf_key` are required. `zmf_crt/zmf_key` will be used first if both of them are supplied.


## Running
Before running the test playbooks, ensure you are within the directory `tests/workflow` of the installed collection:
```
cd tests/workflow
```

You can use the [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command to run the test playbooks:

```
ansible-playbook test_module_compare.yml
ansible-playbook test_module_start.yml
ansible-playbook test_module_check.yml
ansible-playbook test_module_delete.yml
ansible-playbook test_role_complete_workflow.yml
```


## Copyright
© Copyright IBM Corporation 2020