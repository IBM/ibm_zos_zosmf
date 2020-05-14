# Playbook documentation
The collection [ibm_zos_zosmf](../README.md) provides a directory of [Ansible playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbooks-intro), which contains various sample playbooks to demonstrate the use of modules and roles.


## Configuration and setup
Before setup, obtain the installation path for the collection, see the section [Installation](../README.md#Installation).

### Ansible config
This directory contains an example Ansible config [ansible.cfg](ansible.cfg), which refers to the default installation path for the collection:
`~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf`.

You can modify the following configuration statement to refer to your own installation path for the collection:

```
collections_paths = ~/.ansible/collections:/usr/share/ansible/collections
```

*Reference Link:* [Ansible configuration settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations)

### Inventory
This directory contains an example Ansible inventory [hosts](hosts), which is used to manage the target z/OS systems (managed nodes). Information is specified in the following format:

```yml
[workflow]
SY1
[cpm]
zosmf1 zmf_host=hostname_of_zos_system zmf_port=zosmf_port
```

- `workflow` - host grouping for z/OSMF Workflows
   - `SY1` - Nickname for the target z/OS system. You can modify it to refer to your own z/OS system.
- `cpm` - host grouping for Cloud Provisioning & Management
   - `zosmf1` - Host nickname for the target z/OS system. You can modify it to refer to your own z/OS system. When the nickname is modified, make sure host specific variables file is defined as described in "Group vars".
   - `zmf_host` - Hostname of the target z/OS system where z/OSMF is running. You need to specify the correct host name to reach out to z/OSMF end point, for example: `zmf_host=pev076.pok.ibm.com`
   - `zmf_port` - Port number associated with the z/OSMF server on the target z/OS system. You need to specify the correct port number to reach out to z/OSMF end point, for example: `zmf_port=443`

*Reference Link:* [How to build your inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#intro-inventory)

### Group vars
You can supply group variables in either the inventory file or the separate group specific variable file. This directory contains some example variable files in the directory [group_vars](group_vars/).

- [workflow.yml](group_vars/workflow.yml) contains the variables for system group `workflow`:
   - `zmf_host` - Hostname of the z/OSMF server.
   - `zmf_port` - Port number of the z/OSMF server.

   **NOTE**: This is an easy example to use username and password for authenticating with z/OSMF server. `zmf_user` and `zmf_password` are prompted to input when running a playbook. Actually, client-certificate authorization is recommended. You can use `zmf_crt` and `zmf_key` to specify the certificate chain file and key file to be used for HTTPS client authentication.

### Host vars
You can supply host variables in either the inventory file or the separate host specific variable file. This directory contains some example variables files in the directory [host_vars](host_vars/) matching the example host names used in the sample inventory [hosts](hosts).

- [zosmf1.yml](host_vars/zosmf1.yml) contains variables for z/OSMF host 'zosmf1' in system group `cpm`:
  - `instance_record_dir` - File path in local system where the provision result (in json) will be stored.
  - `api_polling_retry_count` - Max times of status polling before task fail and exit.
  - `api_polling_interval_seconds` - Interval in seconds between each `api_polling_retry_count` polling.


## Sample playbooks
The sections that follow explain how to use the sample playbooks.

### [sample_role_workflow_complete.yml](sample_role_workflow_complete.yml)
This sample playbook shows how to invoke role [zmf_workflow_complete](../roles/zmf_workflow_complete/README.md) to complete a z/OS workflow on the target z/OS systems via z/OSMF. To run the sample playbook, below preparation works are required:

- In this sample playbook, the workflow definition file [workflow_sample_automation_steps.xml](files/workflow_sample_automation_steps.xml) is used to create the workflow instance. You need to manually upload it to the z/OS file system. For example, you can upload it to the directory `/var/zosmf/workflow_def/`. Then modify the value of variable `workflow_file` in the sample playbook to refer to the location of the workflow definition file.

   ```yaml
   tasks:
   - include_role:
         name: zmf_workflow_complete
      vars:
         force_complete: False
         workflow_name: "ansible_sample_workflow_{{ inventory_hostname }}"
         # modify the location of the workflow definition file on the z/OS file system
         workflow_file: "/var/zosmf/workflow_def/workflow_sample_automation_steps.xml"
   ```

- In the inventory file, the nickname `SY1` for the target z/OS system, which is configured as managed node, is used to create the workflow instance. You can modify it to refer to your own z/OS system. You need to ensure the z/OS system `SY1` or your own z/OS system is configured in z/OSMF **Systems** task.

   ```
   [workflow]
   SY1
   ```

### [sample_role_cpm_manage_instance.yml](sample_role_cpm_manage_instance.yml)
This sample playbook shows how to perform instance specific action on a provisioned instance in z/OSMF CP&M:

   ```yaml
   - name: sample of managing software instance
   hosts: zosmf1 # need to match host nick name specified in hosts inventory file
   gather_facts: no
   collections:
      - ibm.ibm_zos_zosmf
   vars_prompt:
      - name: zmf_user
         prompt: "Enter your zOSMF username"
         private: no

      - name: zmf_password
         prompt: "Enter your zOSMF password"
         private: yes
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
   hosts: zosmf1 # need to match host nick name specified in hosts inventory file
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
   - name: sample of managing software instance
   hosts: zosmf1 # need to match host nick name specified in hosts inventory file
   gather_facts: no
   collections:
      - ibm.ibm_zos_zosmf
   vars_prompt:
      - name: zmf_user
         prompt: "Enter your zOSMF username"
         private: no

      - name: zmf_password
         prompt: "Enter your zOSMF password"
         private: yes
   tasks:
      - include_role:
         name: zmf_cpm_remove_software_instance
         vars:
            instance_info_json_path: "/{{ instance_record_dir }}/{{ instanceID }}-{{ externalName }}.json""<full-instance-json-file-path>" # The value for property instance_info_json_path identifies full file path of the provisioned instance json file that is created by zmf_cpm_provision_software_service role, common format is /{{ instance_record_dir }}/{{ instanceID }}-{{ externalName }}.json
   ```

### [sample_role_deploy_cics_application.yml](sample_role_deploy_cics_application.yml)
This sample playbook shows how to install a web application on a provisioned CICS instance in z/OSMF CP&M. Please copy files/role_cics_wlp_install_app directory to roles directory before using this example

   ```yaml
   - name: Sample for provisioning CICS region and deploying application
   hosts: zosmf1 # need to match host nick name specified in hosts inventory file
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

**NOTE**: For CP&M roles, the inventory file needs to be updated to identify the target z/OSMF end points.


## Run the playbooks
The sample playbooks must be run from the directory `playbooks` of the installed collection. For example:
`~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks/`

You can use the [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command to run the sample playbooks as follows:

```
ansible-playbook [-i hosts] sample_role_*.yml [-e zmf_user=<username> -e zmf_password=<password>]
```

To adjust the logging verbosity, include the `-v` option with [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command. You can append more letter `v`'s, for example, `-v`, `-vv`, `-vvv`, or `-vvvv`, to obtain more details in case a connection failed. Each letter `v` increases the logging verbosity similar to the traditional logging levels, such as INFO, WARN, ERROR, or DEBUG.


## Copyright
© Copyright IBM Corporation 2020.
