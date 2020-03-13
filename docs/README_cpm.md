# Provison z/OS middlewares, for example CICS, Db2, IMS, WLP etc. 

This collection also provide capabilities to provision and manage z/OS middlewares/softwares using Ansible playbooks. There are two roles provided to interact with z/OSMF Cloud Provisioning & Management (CP&M). These roles drive z/OSMF RESTful services provided by CP&M to provision and manage software services.

- [provision_software_service](../roles/provision_software_service/README.md) : Provisions an instance of a specific middleware/software by driving a software template defined in CP&M software catalog. 

- [manage_software_instance](../roles/manage_software_instance): Performs a specific action on a provisioned software instance. This role can be used to deprovision the software service instance when no longer requireed. 

**NOTE**:

- `delegate_to` - The “delegate_to: localhost” statement is required when using the module in your playbook's task, which makes the module run locally (in control node), so that it does not need to set up SSH connection and install Python on all of the target z/OS systems. Instead, the module will set up HTTPS connections with z/OSMF server. The “delegate_to: localhost” statement is hard-coded inside the role.

- `Check Mode` - The module does not support check mode. (dry run or test run)

## Roles Specification

- [provision_software_service](../roles/provision_software_service): This role can be used to provision a z/OS software service. 

Variables:
  - instance_record_dir: Path of the directory that provision role will use to capture various information about provisioned instance in json format.
  - zmf_username: z/OSMF username  
  - zmf_password: z/OSMF password
  - instance_info_json_path: Path to the file that holds provisioned instance information, `provison_software_service` role will automatically generate this variable in the foramt of `<instance_record_dir>/<template_name>-<instance external_name>.json`
  - zmf_host: z/OSMF host uri, excluding https, including port
  - cpm_template_name: Template name i.e. software service to be provisioned
  - domain_name: Cloud domain name associated with the template
  - tenant_name: (optional) Identifies the CP&M Tenant name associated with the user that is driving this role
  - systems_nicknames: System nick name, no multi-sysplex support at current stage
  - api_polling_retry_count: Total retries number before role exit with failure waiting on provisioning to complete
  - api_polling_interval_seconds: Interval time for each polling request in seconds

- [manage_software_instance](../roles/manage_software_instance): This role can be used to manage a provisioned software service instance. Various actions can be performed on a provisioned instance using this role. 

Variables:
  - zmf_host: z/OSMF host uri, excluding https, including port
  - zmf_username: z/OSMF username  
  - zmf_password: z/OSMF password
  - instance_action_name: Action to be performed on a provisioned software instance. for example Deprovision 
  - instance_info_json_path: Path to the json file that holds provisioned instance information. Specify the file name that is generated when provision_software_service role was performed.
  - api_polling_retry_count: Total retries number before role exit with failure waiting on instance action to complete
  - api_polling_interval_seconds: Interval time for each polling request in seconds.

## Requirements

### Control Node

- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) - 2.9 or later.
- [Python](https://www.python.org/downloads/release/latest) -  3.7 or later.
- [Requests library for Python](https://requests.readthedocs.io/en/latest/) - 2.23 or later.

### provision_software_service

Addtional required Python library listed [here](../roles/provision_software_service/requirement.txt)

### Managed Node

- [z/OS](https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html) - 2.3 or later.

## Usage

Please refer to directory [examples](../examples/README.md) for various example playbooks.

## Test

Please refer to directory [tests/cpm](../tests/cpm/README.md).

## Copyright

© Copyright IBM Corporation 2020
