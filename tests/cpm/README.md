# CPM test playbook

## Example run

1. Fill in variable value in to the `test_xxxx` playbook under this directory
2. Run `$ ansible-playbook path_to_test_xxxx.yml -i path_to/tests/cpm/hosts`

# Test Documentation: Cloud Provisioning & Management
The collection [ibm_zos_zosmf](../../README.md) provides a directory of [Ansible playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbooks-intro) which contains various test playbooks for testing roles provided for Cloud Provisioning and Management.


## Playbooks
### Test Roles
- [test_role_cpm_provision.yml](test_role_cpm_provision.yml) - Provisions a z/OS middleware e.g. CICS, Db2, WLP, IMS
- [test_role_cpm_action.yml](test_role_cpm_action.yml) - Performs actions on the provisioned software instance for example deprovision action
- [test_role_cpm_remove_instance.yml](test_role_cpm_remove_instance.yml) - Removes a deprovisioned software instance from z/OSMF
- [test_role_deploy_cics_application.yml](test_role_deploy_cics_application.yml) - Provisions a CICS region and then deploys a CICS applicaiton file from local workstaion to CICS instance directory.

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

3.  Install the locally built collection into `tests/cpm/collections`:
    ```
    ansible-galaxy collection install ibm-ibm_zos_zosmf-1.0.0.tar.gz -p tests/cpm/collections
    ```

    The example output looks like:
    ```
    Process install dependency map
    Starting collection install process
    Installing 'ibm.ibm_zos_zosmf:1.0.0' to '/Users/user/git/ibm/ibm_zos_zosmf/tests/cpm/collections/ansible_collections/ibm/ibm_zos_zosmf'
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
```

- `${group_name}` - The group name of all target z/OS systems.
- `${zos_system_nickname}` - The nickname of target z/OS system on which the workflow instance is to be performed.
- `ansible_host` - The hostname of target z/OS system.

*Reference Link:* [How to build your inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory)

### Group Vars
You can supply group variables either in the inventory file or in the separate variable file. This directory contains an example variable file [group_vars/any](group_vars/any) to supply the information of z/OSMF server and other variables with the following template:
```
zmf_host: XXXXXXXX
zmf_port: XXXXXXXX
zmf_user: XXXXXXXX
zmf_password: XXXXXXXX
zmf_crt: XXXXXXXX
zmf_key: XXXXXXXX

- `zmf_host` - The hostname of z/OSMF server.
- `zmf_port` - (Optional) The port number of z/OSMF server.
- `zmf_user` - (Optional) The username for authenticating with z/OSMF server.
- `zmf_password` - (Optional) The password for authenticating with z/OSMF server.


**NOTE**: Either `zmf_user/zmf_password` or `zmf_crt/zmf_key` are required. 


## Running
Before running the test playbooks, ensure you are within the directory `tests/cpm` of the installed collection:
```
cd tests/cpm
```

You can use the [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command to run the test playbooks:

```

ansible-playbook test_role_cpm_provision.yml -i hosts
ansible-playbook test_role_cpm_action.yml -i hosts
ansible-playbook test_role_cpm_remove_instance.yml -i hosts
ansible-playbook test_role_deploy_cics_application.yml -i hosts
```


## Copyright
© Copyright IBM Corporation 2020
