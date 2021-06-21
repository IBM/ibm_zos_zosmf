.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Requirements - Provision and Manage z/OS Software Instances
===========================================================

* role: `zmf_cpm_provision_software_service`_
* role: `zmf_cpm_manage_software_instance`_
* role: `zmf_cpm_remove_software_instance`_

To use above modules and roles, it needs to ensure **Cloud Provisioning & Management (CP&M)** is configured in z/OSMF. 

Besides the `Overall Requirements`_, the following nodes require specific versions of software:

**Managed Node**:

* `z/OS Management Facility`_: V02.03.00 or later

   The z/OSMF server must be installed and active on **each** managed z/OS system.

* `Cloud Provisioning & Management`_


.. _Overall Requirements:
   requirements.html
.. _zmf_cpm_provision_software_service:
   roles/README_zmf_cpm_provision_software_service.html
.. _zmf_cpm_manage_software_instance:
   roles/README_zmf_cpm_manage_software_instance.html
.. _zmf_cpm_remove_software_instance:
   roles/README_zmf_cpm_remove_software_instance.html
.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html
.. _Cloud Provisioning & Management:
   https://www.ibm.com/support/z-content-solutions/cloud-provisioning
