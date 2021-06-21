.. ...........................................................................
.. © Copyright IBM Corporation 2020                                          .
.. ...........................................................................

========
Releases
========

Version 3.0.0
=============

`v3.0.0`_

Removed
-------

  * remove module: `zmf_workflow`: use `ibm.ibm_zosmf.zmf_workflow` instead
  * remove role: `zmf_cpm_provision_software_service`: use `ibm.ibm_zosmf.zmf_cpm_provision_software_service` instead
  * remove role: `zmf_cpm_manage_software_instance`: use `ibm.ibm_zosmf.zmf_cpm_manage_software_instance` instead
  * remove role: `zmf_cpm_remove_software_instance`: use `ibm.ibm_zosmf.zmf_cpm_remove_software_instance` instead

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Version 2.5.0
=============

`v2.5.0`_

Added
-----
  * add modules: `zmf_dataset`, `zmf_file`
  * enhance for module: `zmf_dataset_copy`: support to copy file or data set from z/OS system
  * enhance for role: `zmf_cpm_provision_software_service`: add input_vars parameter for CPM provision role, add zmf_body parameter for using playbook in full automation

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Reference
---------
  * Supported by z/OSMF APAR PH22030 (PTF UI68974 for V2R3, PTF UI68975 for V2R4)

Version 2.4.0
=============

`v2.4.0`_

Added
-----
  * add modules: `zmf_dataset_copy`, `zmf_file_copy`

Fixed
-----
  * fix for role `zmf_workflow_complete`: refine final_result
  * fix for module `zmf_console_command`: console_cmdresponse_reg and console_broadcastmsg_reg should be bool type

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Reference
---------
  * Supported by z/OSMF APAR PH22030 (PTF UI68974 for V2R3, PTF UI68975 for V2R4)

Version 2.3.0
=============

`v2.3.0`_

Added
-----
  * add modules: `zmf_dataset_fetch`, `zmf_file_fetch`

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Reference
---------
  * Supported by z/OSMF APAR PH15263 (PTF UI65882 for V2R3, PTF UI65883 for V2R4)

Version 2.2.1
=============

`v2.2.1`_

Fixed
-----
  * fix for module `zmf_console_command`: conflict route params
  * fix for module `zmf_console_command`: os issue when save output to local with python2.7
  * fix for roles `zmf_job_complete`, `zmf_job_query`: overridden matched contents

Availability
------------
  * `Galaxy`_
  * `GitHub`_
  
Version 2.2.0
=============

`v2.2.0`_

Added
-----
  * add modules: `zmf_authenticate`
  * support to save job output on Ansible control node for roles: `zmf_job_complete`, `zmf_job_query`
  * support to save command response on Ansible control node for module: `zmf_console_command`

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Reference
---------
  * Module `zmf_authenticate` is supported by z/OSMF APAR PH12143 (PTF UI66511 for V2R3, PTF UI66512 for V2R4)

Version 2.1.0
=============

`v2.1.0`_

Added
-----
  * add modules: `zmf_console_command`

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Reference
---------
  * Supported by z/OSMF APAR PH24072 (PTF UI69958 for V2R3, PTF UI69959 for V2R4)

Version 2.0.1
=============

`v2.0.1`_

Added
-----
  * support to search job output for roles: `zmf_job_complete`, `zmf_job_query`

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Reference
---------
  * Supported by z/OSMF APAR PH23046 (PTF UI69412 for V2R3, PTF UI69413 for V2R4)

Version 2.0.0
=============

`v2.0.0`_

Added
-----
  * add roles: `zmf_job_complete`, `zmf_job_query`
  * support a doc site for collection

Refined
-------
  * refine and rename module `workflow` to `zmf_workflow`
  * rename role `complete_workflow` to `zmf_workflow_complete`
  * rename role `provision_software_service` to `zmf_cpm_provision_software_service`
  * rename role `manage_software_instance` to `zmf_cpm_manage_software_instance`
  * rename role `remove_software_instance` to `zmf_cpm_remove_software_instance`

Fixed
-----
  * cleanup sanity test checks
  * add tags

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Version 1.0.3
=============

`v1.0.3`_

Fixed
-----
  * cleanup ansible_lint checks
  * cleanup sanity test checks

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Version 1.0.2
=============

`v1.0.2`_

Fixed
-----
  * cleanup ansible_lint checks
  * fix bug for cmp roles: instance variable is not correctly parsed in the role

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Version 1.0.1
=============

`v1.0.1`_

Fixed
-----
  * cleanup ansible_lint checks
  * fix README links on Galaxy webpage
  * add tags

Availability
------------
  * `Galaxy`_
  * `GitHub`_

Version 1.0.0
=============

`v1.0.0`_

Added
-----
  * initial **ibm_zos_zosmf** collection
  * add modules: `workflow`
  * add roles: `complete_workflow`, `provision_software_service`, `manage_software_instance`, `remove_software_instance`

Availability
------------
  * `Galaxy`_
  * `GitHub`_


.. _Galaxy:
   https://galaxy.ansible.com/ibm/ibm_zos_zosmf
.. _GitHub:
   https://github.com/IBM/ibm_zos_zosmf
.. _v1.0.0:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v1.0.0
.. _v1.0.1:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v1.0.1
.. _v1.0.2:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v1.0.2
.. _v1.0.3:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v1.0.3
.. _v2.0.0:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.0.0
.. _v2.0.1:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.0.1
.. _v2.1.0:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.1.0
.. _v2.2.0:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.2.0
.. _v2.2.1:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.2.1
.. _v2.3.0:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.3.0
.. _v2.4.0:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.4.0
.. _v2.5.0:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.5.0
.. _v3.0.0:
    https://github.com/IBM/ibm_zos_zosmf/releases/tag/v3.0.0