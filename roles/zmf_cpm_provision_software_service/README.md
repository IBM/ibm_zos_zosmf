# Ansible Role: zmf_cpm_provision_software_service

The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), referred to as `zmf_cpm_provision_software_service`, to provision a z/OS middleware/software service using Cloud Provisioning & Management (CP&M) template.

## Role Variables

The variables used by the role are listed below:

Variables:
- zmf_host: z/OSMF host name, specified via inventory file
- zmf_port: z/OSMF port number, specified via inventory file
- zmf_user: z/OSMF username, prompted when playbook is run
- zmf_password: z/OSMF password, prompted when playbook is run
- instance_record_dir: Path of the directory that provision role will use to capture various information about provisioned instance in json format. Value for this variable is specified in host specific variables file in host_vars directory.
- instance_info_json_path: Path to the file that holds provisioned instance information, `zmf_cpm_provision_software_service` role will automatically generate this variable in the format of `<instance_record_dir>/<template_name>-<instance external_name>.json`
- cpm_template_name: Template name i.e. software service to be provisioned
- domain_name: Cloud domain name associated with the template
- tenant_name: (optional) Identifies the CP&M Tenant name associated with the user that is driving this role. This variable is required if zmf_user is associated with multiple CP&M tenants.
- systems_nicknames: (optional) System nick name as identified in z/OSMF. If this variable is not specified, provisioning will take place on a system where z/OSMF is currently running.
- api_polling_retry_count: Total retries number before role exit with failure waiting on instance action to complete. This variable is specified in host specific variables file in host_vars directory.
- api_polling_interval_seconds: Interval time for each polling request in seconds. This variable is specified in host specific variables file in host_vars directory.

## Dependencies

None

## Usage

Please refer to directory [playbooks](../../playbooks/README.md) for various example playbooks.


## Copyright

© Copyright IBM Corporation 2020
