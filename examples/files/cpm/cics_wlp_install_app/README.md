
# Ansible Role: cics_wlp_install_app

This is a sample role provided to support sample playbook provided with CP&M.  This role uses z/OSMF file REST APIs to transfer file to zFS file system file associated with the provisioned middleware instance.  This role can be used to copy application binary files from local system to target directory of the provisioned instance on the z/OS system.

In order to use this role in any playbook, cics_wlp_install_app directory needs to be copied into collections/roles/ibm/ibm_zos_zosmf/roles

## Role Variables

The variables used by the role are listed below:

Variables:

- zmf_host: z/OSMF host name
- zmf_port: z/OSMF port number
- zmf_user: z/OSMF username
- zmf_password: z/OSMF password
- instance_info_json: JSON record of provisioned instance
- application_path: location of application file on local workstation

## Dependencies

None

## Usage

Please refer to directory [examples](../../examples/README.md) for various example playbooks.

## Examples

Please refer to the test playbook [sample_role_deploy_cics_application.yml](../../../sample_role_deploy_cics_application.yml) in the directory [/examples](../../../README.md).

## Copyright
