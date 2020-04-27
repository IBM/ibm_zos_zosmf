.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Roles
=======

Roles are ways of automatically loading certain vars_files, tasks, and handlers based on a known file structure. Grouping content by roles also allows easy sharing of roles with other users.

Role Reference
--------------

**IBM z/OSMF collection** provides several roles. Reference material for each role contains documentation on how to use certain roles in your playbook.

* `zmf_workflow_complete`_: This role is used for completing a z/OS workflow, either forcibly or idempotently.

* `provision_software_service`_: This role can be used to provision a z/OS software service. The provision role will create a local record file of instance information that is responded from registry API in json format, and this file will be served to other CP&M roles such like ``manage_software_instance`` and ``remove_software_instance``.

* `manage_software_instance`_: This role can be used to manage a provisioned software service instance. Various actions can be performed on a provisioned instance using this role.

* `remove_software_instance`_: This role can be used to remove a deprovisioned software service instance.


.. _zmf_workflow_complete:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/zmf_workflow_complete/
.. _provision_software_service:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/provision_software_service/
.. _manage_software_instance:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/manage_software_instance/
.. _remove_software_instance:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/remove_software_instance/
