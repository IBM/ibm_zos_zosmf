# Ansible Role: zmf_cpm_remove_software_instance

The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), referred to as `zmf_cpm_remove_software_instance`, to remove a deprovisioned instance of z/OS middleware/software.

## Role Variables

The variables used by the role are listed below:

- zmf_host: z/OSMF host name, specified via inventory file
- zmf_port: z/OSMF port number, specified via inventory file
- zmf_user: z/OSMF username, prompted when playbook is run
- zmf_password: z/OSMF password, prompted when playbook is run
- instance_info_json_path: Path to the json file that holds provisioned instance information. Specify the file name that is generated when `zmf_cpm_provision_software_service` role was performed.

## Requirements

None

## Dependencies

None

## Usage

Please refer to directory [playbooks](../../playbooks/README.md) for various example playbooks.

## Copyright

© Copyright IBM Corporation 2020
