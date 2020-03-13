# Playbook documentation
The collection [ibm_zos_zosmf](../README.md) provides a directory of [Ansible playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbooks-intro), which contains various sample playbooks to demonstrate the use of modules and roles.


## Configuration and setup
Before setup, obtain the installation path for the collection, see the section [Installation](../README.md#Installation).

### Ansible config
This directory contains an example Ansible config [ansible.cfg](ansible.cfg), which refers to the default installation path for the collection:  
`~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf`. 

You can modify the following configuration statement to refer to your own installation path for the collection:

```
collections_paths = ../../../../../collections
```

*Reference Link:* [Ansible configuration settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations)

### Inventory
This directory contains an example Ansible inventory [hosts](hosts), which is used to manage the target z/OS systems (managed nodes). Information is specified in the following format:

```
[zsystems]
SY1 ansible_host=hostname_of_zos_system
```

- `SY1` - Nickname for the target z/OS system. You can modify it to refer to your own z/OS system.
- `ansible_host` - Hostname of the target z/OS system. You can modify it to refer to your own z/OS system, for example: `ansible_host=pev076.pok.ibm.com`

*Reference Link:* [How to build your inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory)

### Group vars
You can supply group variables in either the inventory file or the separate variable file. This directory contains some example variable files in the directory [group_vars](group_vars/).

- [all.yml](group_vars/all.yml) contains the variables for all groups of the target z/OS systems:
   - `zmf_host` - Hostname of the z/OSMF server.
   - `zmf_port` - Port number of the z/OSMF server.
   - `zmf_user` - User name to be used for authenticating with z/OSMF server (see note).
   - `zmf_password` - Password to be used for authenticating with z/OSMF server (see note).
   
   **NOTE**: This is an easy example to use username and password for authenticating with z/OSMF server. Actually, client-certificate authorization is recommended. You can use `zmf_crt` and `zmf_key` to specify the certificate chain file and key file to be used for HTTPS client authentication.


## Run the playbooks
The sample playbooks must be run from the directory `examples` of the installed collection. For example:  
`~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/examples/`  

You can use the [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command to run the sample playbooks as follows:

```
ansible-playbook -i hosts sample_role_complete_workflow.yml
```

To adjust the logging verbosity, include the `-v` option with [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command. You can append more letter `v`'s, for example, `-v`, `-vv`, `-vvv`, or `-vvvv`, to obtain more details in case a connection failed. Each letter `v` increases the logging verbosity similar to the traditional logging levels, such as INFO, WARN, ERROR, or DEBUG.


## Sample playbooks
The sections that follow explain how to use the sample playbooks. 

### [sample_role_complete_workflow.yml](sample_role_complete_workflow.yml)
This sample playbook shows how to invoke role [complete_workflow](../roles/complete_workflow/README.md) to complete a z/OS workflow on the target z/OS systems via z/OSMF. To run the sample playbook, below preparation works are required:

- In this sample playbook, the workflow definition file [workflow_sample_automation_steps.xml](files/workflow_sample_automation_steps.xml) is used to create the workflow instance. You need to manually upload it to the z/OS file system. For example, you can upload it to the directory `/var/zosmf/workflow_def/`. Then modify the value of variable `zos_workflow_file` in the sample playbook to refer to the location of the workflow definition file.

   ```yaml
   tasks:
   - include_role:
         name: complete_workflow
      vars:
         force_complete: False
         zos_workflow_name: "ansible_sample_workflow_{{ inventory_hostname }}"
         # modify the location of the workflow definition file on the z/OS file system
         zos_workflow_file: "/var/zosmf/workflow_def/workflow_sample_automation_steps.xml"
   ```

- In the inventory file, the nickname `SY1` for the target z/OS system, which is configured as managed node, is used to create the workflow instance. You can modify it to refer to your own z/OS system. You need to ensure the z/OS system `SY1` or your own z/OS system is configured in z/OSMF **Systems** task.

   ```
   [zsystems]
   SY1 ansible_host=hostname_of_zos_system
   ```


## Copyright
© Copyright IBM Corporation 2020.