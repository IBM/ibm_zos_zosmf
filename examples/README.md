# Playbook Documentation
The collection [ibm_zos_zosmf](../README.md) provides a directory of [Ansible playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbooks-intro) which consists of organized instructions that define work for a managed node (hosts) to be managed with Ansible.

First, please refer back to section [Installation](../README.md#Installation) to get the installation path of collection. In the following examples, it will refer to the default installation path as `~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf`.

## Configuration and Setup

### Ansible Config

Ansible config `ansible.cfg` can override nearly all `ansible-playbook` configurations. Also included in this directory is a sample [ansible.cfg](ansible.cfg) that with little modificaton can supplement `ansible-playbook`.

*Reference Link:* [Ansible configuration settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations)

### Inventory

Ansible works with multiple managed nodes (hosts) at the same time, using a list or group of lists know as an [inventory](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html). Once the inventory is defined, you can use [patterns](https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html#intro-patterns) to select the hosts, or groups, you want Ansible to run against.

Included in this directory is a sample inventory file called [hosts](hosts). This inventory file should be included when running the sample playbooks.

```yml
[zsystems]
SY1 ansible_host=hostname_of_zos_system
```

The value for property __ansible_host__ is the hostname of the manage node, for example:
`ansible_host: pev076.pok.ibm.com`

### Group Vars

Included in this directory are sample variable files located in directory [group_vars](group_vars/).

- `all.yml` contains variables for all groups of systems:
  - The value for property __zmf_host__ is the hostname of the system on which z/OSMF server is running on.
  - The value for property __zmf_port__ is the port number of z/OSMF server.
  - The value for property __zmf_user__ is your username of z/OSMF.
  - The value for property __zmf_password__ is the password of your username of z/OSMF. Actually, client certificate is the recommanded way to do the authentication, you can use __zmf_crt__ and __zmf_key__ to specify the certificate file and key file to be used in authentication. But it's easier to try the examples by using username/password system here.

- `cpm.yml` contians variables for all groups for sample_role(s)_*.yml:
  - The value for property cpm_template_name is the template name in CP&M user want to provision
  - The value for property domain_name where the template under
  - The value for property tenant_name is for which tenant that is associated with the template under domain_name
  - The value for property systems_nicknames is for system nickname
  - The value for property instance_record_dir is for the file path in local system where the provision result (in json) will be stored
  - The value for property api_polling_retry_count is for max times of status polling before task fail and exit
  - The value for property api_polling_interval_seconds is for interval in seconds between each api_polling_retry_count polling
  - The value for property instance_action_name is the name which instance action user want to perform provision_software_service role, common format is /{{ instance_record_dir }}/{{ instanceID }}-{{ externalName }}.json
  - The value for property instance_info_json_path is the full file path of the provision json file that is created by

## Sample Playbooks

### [sample_role_complete_workflow.yml](sample_role_complete_workflow.yml)

This sample playbook shows how to invoke role complete_workflow to complete (create/start/check) a z/OS workflow on target z/OS systems via z/OSMF. To run the playbook, below preparation works are required:

- In this sample playbook, workflow definition file [workflow_sample_automation_steps.xml](files/workflow_sample_automation_steps.xml) is used to create the workflow. You need to manually upload it to the z/OS file system. For example, you can upload it to `/var/zosmf/workflow_def/`. Then change the value of variable `zos_workflow_file` to the location of the workflow definition file on target z/OS system.

   ```yaml
   tasks:
      - include_role:
         name: complete_workflow
         vars:
            force_complete: False
            zos_workflow_name: "ansible_sample_workflow_{{ inventory_hostname }}"
            # change the location of workflow definition file.
            zos_workflow_file: "/var/zosmf/workflow_def/workflow_sample_automation_steps.xml"
   ```

- In the inventory file, the z/OS target system is configured as managed node like below:

   ```yml
   [zsystems]
   SY1 ansible_host=hostname_of_zos_system
   ```

   `SY1` is the nickname of z/OS system, you can replace it with yours. To try this sample playbook, the system `SY1` (or your system name) should be configured in the z/OSMF __Systems__ task, or the playbook will be failed.

### [sample_role_cpm_action.yml](sample_role_cpm_action.yml)

This sample playbook shows how to perform instance action on a provisioned instance in z/OSMF CP&M:

   ```yaml
   tasks:
      - include_role:
         name: manage_software_instance
         vars:
            instance_action_name: "{{ action_name_placeholder }}"
            instance_info_json_path: "/{{ instance_record_dir }}/{{ instanceID }}-{{ externalName }}.json"
            api_polling_retry_count: 10
            api_polling_interval_seconds: 7
   ```

### [sample_role_cpm_provision.yml](sample_role_cpm_provision.yml)

This sample playbook shows how to provision an instance in z/OSMF CP&M:

   ```yaml
   tasks:
      - include_role:
         name: provision_software_service
         vars:
            cpm_template_name: "<template-name>"
            domain_name: "default"
            tenant_name: "default"
            systems_nicknames: "SY1"
            instance_record_dir: "/tmp"
            api_polling_retry_count: 10
            api_polling_interval_seconds: 3
   ```

### [sample_roles_cpm_cics_full_cycle.yml](sample_roles_cpm_cics_full_cycle.yml)

This sample playbook shows how to install a web application on a provisioned instance in z/OSMF CP&M, and then deprovision the instance once it's done:

   ```yaml
   tasks:
      - include_role:
         name: provision_software_service
         ...

      - include_role:
        name: cics_wlp_install_app
      vars:
        instance_info_json: "{{lookup('file', instance_info_json_path)}}"
        app_root_uri: "/CloudTestServlet"
        app_file_name: "./files/cpm/CloudTestServlet.war"
        application_path: "{{ application_path_input }}"

      - include_role:
          name: manage_software_instance
        vars:
          instance_action_name: "deprovision"
          ...
   ```

- In the inventory file, the z/OS target system is configured as managed node like below:

   ```yml
   [cpmsystem]
   SY1 ansible_host=hostname_of_zos_system
   ```

   `SY1` is the nickname of z/OS system, you can replace it with yours. To try this sample playbook, the system `SY1` (or your system name) should be configured in the z/OSMF __Systems__ task, or the playbook will be failed.

## Running

Before running the sample playbooks, ensure you are within the directory `examples` of the installed collection where the sample playbooks are included:
`~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/examples/`

You can use the [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html) command to run the sample playbooks. The command syntax is `ansible-playbook -i <inventory> <playbook>`, for example:
`ansible-playbook -i hosts sample_role_complete_workflow.yml`

Optionally, during playbook execution, logging to the console verbosity can be configured. This is helpful in situations where communication is failing and you want more detail. To adjust logging verbosity, append more letter `v`'s, for example: `-v`, `-vv`, `-vvv`, or `-vvvv`. Each letter `v` increases logging vebosity similar to traditional logging levels INFO, WARN, ERROR, DEBUG.

## Copyright

© Copyright IBM Corporation 2020
