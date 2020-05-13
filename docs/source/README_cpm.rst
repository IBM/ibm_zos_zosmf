.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Provision and Manage z/OS Software Instances
============================================

**IBM z/OSMF collection** provides capabilities to provision and manage z/OS middlewares/softwares using Ansible playbooks, for example CICS, Db2, IMS, WLP etc. There are three roles provided to interact with z/OSMF Cloud Provisioning & Management (CP&M). These roles drive z/OSMF RESTful services provided by CP&M to provision and manage software services.

Roles
-----

* `zmf_cpm_provision_software_service`_:
   
   This role can be used to provision a z/OS software service. The provision role will create a local record file of instance information that is responded from registry API in json format, and this file will be served to other CP&M roles such like `zmf_cpm_manage_software_instance`_ and `zmf_cpm_remove_software_instance`_. The local record file is generated in the directory specified via ``instance_record_dir`` variable defined in a host specific variable files under "host_vars". By default location is ``/tmp/"host-name"`` which can be changed by updating ``instance_record_dir`` variable.

* `zmf_cpm_manage_software_instance`_: 

   This role can be used to manage a provisioned software service instance. Various actions can be performed on a provisioned instance using this role. Actions that can be performed on a provisioned instance are described in local record file associated with the provisioned instance. The ``name`` variable in ``actions`` array under ``registry-info`` identifies various actions that can be performed on the instance.

* `zmf_cpm_remove_software_instance`_: 

   This role can be used to remove a deprovisioned software service instance.

Requirements
------------

See the section `Requirements`_.

Sample Playbooks
----------------

See the section `Playbooks`_.


.. _zmf_cpm_provision_software_service:
   roles/README_zmf_cpm_provision_software_service.html
.. _zmf_cpm_manage_software_instance:
   roles/README_zmf_cpm_manage_software_instance.html
.. _zmf_cpm_remove_software_instance:
   roles/README_zmf_cpm_remove_software_instance.html
.. _Requirements:
   requirements.html
.. _Playbooks:
   playbooks.html