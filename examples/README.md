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

```yml
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

- [cpm.yml](group_vars/cpm.yml) contains variables for system group `cpm`:
  - `instance_record_dir` - File path in local system where the provision result (in json) will be stored.
  - `api_polling_retry_count` - Max times of status polling before task fail and exit.
  - `api_polling_interval_seconds` - Interval in seconds between each `api_polling_retry_count` polling.


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

### [sample_role_cpm_manage_instance.yml](sample_role_cpm_manage_instance.yml)
This sample playbook shows how to perform instance action on a provisioned instance in z/OSMF CP&M:

   ```yaml
   - name: sample of managing software instance
   hosts: zosmf1 # use to match group_vars/cpm.yml
   gather_facts: no
   collections:
      - ibm.ibm_zos_zosmf
   tasks:
      - include_role:
         name: zmf_cpm_manage_software_instance
         vars:
            instance_action_name: "{{ action_name_placeholder }}"  # The value for property instance_action_name identifies which instance action user wants to perform
            instance_info_json_path: "/{{ instance_record_dir }}/{{ instanceID }}-{{ externalName }}.json"  # The value for property instance_info_json_path identifies full file path of the provisioned instance json file that is created by zmf_cpm_provision_software_service role, common format is /{{ instance_record_dir }}/{{ instanceID }}-{{ externalName }}.json
   ```

### [sample_role_cpm_provision.yml](sample_role_cpm_provision.yml)
This sample playbook shows how to provision an instance in z/OSMF CP&M:

   ```yaml
   - name: test role for zmf_cpm_provision_software_service
   hosts: zosmf1 # use to match group_vars/cpm.yml
   gather_facts: no
   collections:
      - ibm.ibm_zos_zosmf
   vars:
      - name: instance_info_json_path #will store instance json information globally thru the playbook
   vars_prompt:
      - name: zmf_user
         prompt: "Enter your zOSMF username"
         private: no

      - name: zmf_password
         prompt: "Enter your zOSMF password"
         private: yes
   tasks:
      - include_role:
         name: zmf_cpm_provision_software_service
         vars:
            cpm_template_name: "<fill-me-template-name>"   # The value for property cpm_template_name which identifies the template (software service) user wants to provision with Cloud Provisioning & Management
            domain_name: "<domain-name>" # The value for property domain_name which identifies CP&M domain in which specified template is defined
            tenant_name: "<tenant-name>" # The value for optional property tenant_name which identifies CP&M tenant that is associated with the zmf_user that is provisioning the template
            systems_nicknames: "<system-name>" # The value for optional property systems_nicknames which identifies on which system the software instance will be provisioned
   ```

### [sample_role_cpm_remove_instance.yml](sample_role_cpm_remove_instance.yml)

This sample playbook shows how to remove the deprovisioned instance in z/OSMF CP&M:

   ```yaml
      tasks:
        - include_role:
            name: zmf_cpm_remove_software_instance
          vars:
            instance_info_json_path: "<full-instance-json-file-path>"
   ```

### [sample_role_deploy_cics_application.yml](sample_role_deploy_cics_application.yml)
This sample playbook shows how to install a web application on a provisioned instance in z/OSMF CP&M. Please copy files/role_cics_wlp_install_app directory to roles directory before using this example

   ```yaml
   - name: Sample for provisioning CICS region and deploying application
   hosts: zosmf1 # use to match group_vars/cpm.yml
   gather_facts: no
   collections:
      - ibm.ibm_zos_zosmf
   vars:
      - name: instance_info_json_path #will store instance json information globally thru the playbook
   vars_prompt:
      - name: zmf_user
         prompt: "Enter your zOSMF username"
         private: no

      - name: zmf_password
         prompt: "Enter your zOSMF password"
         private: yes

      - name: application_path_input
         prompt: "Enter your application file full path"
         private: no

   tasks:
      - include_role:
         name: zmf_cpm_provision_software_service
         ...

      - include_role:
        name: cics_wlp_install_app
      vars:
        instance_info_json: "{{lookup('file', instance_info_json_path)}}" # Path of the instance json file contains cics public variables
        app_root_uri: "/CloudTestServlet" # The URI path to access the application once upload
        app_file_name: "CloudTestServlet.war" # The file name that the application file will be written to the USS file system in z/OS
        application_path: "{{ application_path_input }}" # The local absolute file path to the application binary file
   ```

**NOTE**: For CP&M roles, the inventory file is merely a placeholder for retrieving cpm group variables, you shouldn't need to modify the inventory file or change the host to something else other than cpm.


## Run the playbooks
The sample playbooks must be run from the directory `examples` of the installed collection. For example:
`~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/examples/`

You can use the [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command to run the sample playbooks as follows:

```
ansible-playbook [-i hosts] sample_role_*.yml [-e zmf_user=<username> -e zmf_password=<password>]
```

To adjust the logging verbosity, include the `-v` option with [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command. You can append more letter `v`'s, for example, `-v`, `-vv`, `-vvv`, or `-vvvv`, to obtain more details in case a connection failed. Each letter `v` increases the logging verbosity similar to the traditional logging levels, such as INFO, WARN, ERROR, or DEBUG.


## Copyright
© Copyright IBM Corporation 2020.
