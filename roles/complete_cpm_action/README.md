# Ansible Role: manage_software_instance
The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), referred to as `manage_software_instance`, to manage a provisioned instance of z/OS middleware/software. Various management such as starting or stopping the instance can be performed using this role. When software service instance is not required any more, it can be deprovisioned using this role. 

## Role Variables
The variables used by the role are listed below:

- 'zmf_host' - z/OSMF host uri, excluding https, including port
- 'zmf_username' - z/OSMF username  
- 'zmf_password' - z/OSMF password
- 'instance_info_json_path' - Path to the file that holds provisioned instance information. Refer to `provison_software_service` role to determine what value should be assigned to this variable
- 'instance_action_name' - Action to be performed on a provisioned software instance. for example Deprovision 
- 'api_polling_retry_count' - Total retries number before role exit with failure waiting on provisioning to complete
- 'api_polling_interval_seconds' -  Interval time for each polling request in seconds

## Requirements
Please refer to section [Requirements](requirements.txt). 


## Dependencies
None


## Usage
Please refer to directory [examples](../../examples/cpm/README.md) for various example playbooks.


## Test
Please refer to the test playbook [test_role_deprovision_cics.yml](../../tests/cpm/test_role_provision_cics.yml) in the directory [tests/cpm](../../tests/cpm/README.md).


## Copyright
© Copyright IBM Corporation 2020