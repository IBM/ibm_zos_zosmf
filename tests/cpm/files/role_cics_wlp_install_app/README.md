# How to use for testing

To use this role, copy this folder to `project-root/roles`

# Ansible Role: cics_wlp_install_app

The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), referred to as `cics_wlp_install_app`, to deploy application from local workstation to the target file of provisioned CICS instance.

## Role Variables

The variables used by the role are listed below:

    - zmf_host: z/OSMF host name
    - zmf_port: z/OSMF port number
    - zmf_user: z/OSMF username
    - zmf_password: z/OSMF password
    - instance_info_json: JSON record associaaed with provisioned instance information
    - application_path: Location of application file on local work station

## Requirements

None

## Dependencies

None

## Usage

Please refer to directory [examples](../examples/README.md) for various example playbooks.

## Test

Please refer to the test playbook [test_roles_deploy_cics_application.yml](../tests/cpm/test_roles_deploy_cics_application.yml) in the directory [tests/cpm](../tests/cpm/README.md).

## Copyright

© Copyright IBM Corporation 2020

