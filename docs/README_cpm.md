# Provision z/OS middlewares, for example CICS, Db2, IMS, WLP etc.

This collection also provide capabilities to provision and manage z/OS middlewares/softwares using Ansible playbooks. There are three roles provided to interact with z/OSMF Cloud Provisioning & Management (CP&M). These roles drive z/OSMF RESTful services provided by CP&M to provision and manage software services.

- [provision_software_service](../roles/provision_software_service) : Provisions an instance of a specific middleware/software by driving a software template defined in CP&M software catalog.

- [manage_software_instance](../roles/manage_software_instance): Performs a specific action on a provisioned software instance. This role can be used to deprovision the software service instance when no longer required.

- [remove_software_instance](../roles/remove_software_instance): Removes a deprovisioned software instance. This role can be used to remove the software service instance from z/OSMF after deprovisioning the instance.

**NOTE**:

- `delegate_to` - The “delegate_to: localhost” statement is required when using the module in your playbook's task, which makes the module run locally (in control node), so that it does not need to set up SSH connection and install Python on all of the target z/OS systems. Instead, the module will set up HTTPS connections with z/OSMF server. The “delegate_to: localhost” statement is hard-coded inside the role.

- `Check Mode` - The module does not support check mode. (dry run or test run)

## Roles-Specification

- [provision_software_service](../roles/provision_software_service/README.md): This role can be used to provision a z/OS software service. The provision role will create a local record file of instance information that is responsed from registry API in json format, and this file will be served to other CP&M roles such like manage_software_instance and
remove_software_instance.

- [manage_software_instance](../roles/manage_software_instance/README.md): This role can be used to manage a provisioned software service instance. Various actions can be performed on a provisioned instance using this role.

- [remove_software_instance](../roles/remove_software_instance/README.md): This role can be used to remove a deprovisioned software service instance.

## Requirements

None

### Control Node

- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) - 2.9 or later.

### Managed Node

- [z/OS](https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html) - 2.3 or later.
- [Cloud Provisioning & Management](https://www.ibm.com/support/z-content-solutions/cloud-provisioning)

## Usage

Please refer to directory [examples](../examples/README.md) for various example playbooks.

## Copyright

© Copyright IBM Corporation 2020
