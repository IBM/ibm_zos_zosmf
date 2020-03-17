# Ansible Role: remove_software_instance

The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), referred to as `remove_software_instance`, to remove a deprovisioned instance of z/OS middleware/software.

## Role Variables

The variables used by the role are listed below:

    - zmf_host: z/OSMF host name
    - zmf_port: z/OSMF port number
    - zmf_user: z/OSMF username
    - zmf_password: z/OSMF password
    - instance_info_json_path: Path to the json file that holds provisioned instance information. Specify the file name that is generated when provision_software_service role was performed.

## Requirements

None

## Dependencies

None

## Usage

Please refer to directory [examples](../examples/README.md) for various example playbooks.

## Test

Please refer to the test playbook [test_role_cpm_remove_instance.yml](../tests/cpm/test_role_cpm_remove_instance.yml) in the directory [tests/cpm](../tests/cpm/README.md).

## Copyright

© Copyright IBM Corporation 2020
