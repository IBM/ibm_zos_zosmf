.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Provision and Manage z/OS Softwares
===================================

**IBM z/OSMF collection** provides capabilities to provision and manage z/OS middlewares/softwares using Ansible playbooks. There are three roles provided to interact with z/OSMF Cloud Provisioning & Management (CP&M). These roles drive z/OSMF RESTful services provided by CP&M to provision and manage software services.

Roles
-----

* `provision_software_service`_: This role can be used to provision a z/OS software service. The provision role will create a local record file of instance information that is responded from registry API in json format, and this file will be served to other CP&M roles such like ``manage_software_instance`` and ``remove_software_instance``.

* `manage_software_instance`_: This role can be used to manage a provisioned software service instance. Various actions can be performed on a provisioned instance using this role.

* `remove_software_instance`_: This role can be used to remove a deprovisioned software service instance.

Requirements
------------

See the section `Requirements`_.


.. _provision_software_service:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/provision_software_service/
.. _manage_software_instance:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/manage_software_instance/
.. _remove_software_instance:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/remove_software_instance/
.. _Requirements:
   requirements.html