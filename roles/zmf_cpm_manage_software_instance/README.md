# Ansible Role: zmf_cpm_manage_software_instance

The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), referred to as `zmf_cpm_manage_software_instance`, to manage a provisioned instance of z/OS middleware/software. Various management such as starting or stopping the instance can be performed using this role. When software service instance is not required any more, it can be deprovisioned using this role.

## Role Variables

The variables used by the role are listed below:

- zmf_host: z/OSMF host name, specified via inventory file
- zmf_port: z/OSMF port number, specified via inventory file
- zmf_user: z/OSMF username, prompted when playbook is run
- zmf_password: z/OSMF password, prompted when playbook is run
- instance_action_name: Action to be performed on a provisioned software instance. for example Deprovision. Actions that can be performed on a provisioned instance are described in local record file associated with the provisioned instance. The "name" variable in "actions" array under "registry-info" identifies various actions that can be performed on the instance.
- instance_info_json_path: Path to the json file that holds provisioned instance information. Specify the file name that is generated when `zmf_cpm_provision_software_service` role was performed.
- api_polling_retry_count: Total retries number before role exit with failure waiting on instance action to complete. This variable is specified in host specific variables file in host_vars directory.
- api_polling_interval_seconds: Interval time for each polling request in seconds. This variable is specified in host specific variables file in host_vars directory.

## Requirements

None

## Dependencies

None

## Usage

Please refer to directory [examples](../../examples/README.md) for various example playbooks.

## Copyright

© Copyright IBM Corporation 2020
