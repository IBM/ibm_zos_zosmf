.. ...........................................................................
.. © Copyright IBM Corporation 2020                                          .
.. ...........................................................................

Releases
========

Version 2.2.0
-------------

`v2.2.0`_

Added
  * add modules: `zmf_authenticate`
  * support to save job output locally on control node for roles: `zmf_job_complete`, `zmf_job_query`
  * support to save command response locally on control node for module: `zmf_console_command`

Availability
  * Galaxy
  * github

Version 2.1.0
-------------

`v2.1.0`_

Added
  * add modules: `zmf_console_command`

Availability
  * Galaxy
  * github

Reference
  * Supported by z/OSMF APAR PH24072 (PTF UI69958 for V2R3, PTF UI69959 for V2R4)

Version 2.0.1
-------------

`v2.0.1`_

Added
  * support to search job output for roles: `zmf_job_complete`, `zmf_job_query`

Availability
  * Galaxy
  * github

Reference
  * Supported by z/OSMF APAR PH23046 (PTF UI69412 for V2R3, PTF UI69413 for V2R4)

Version 2.0.0
-------------

`v2.0.0`_

Added
  * add roles: `zmf_job_complete`, `zmf_job_query`
  * support a doc site for collection

Refined
  * refine and rename module `workflow` to `zmf_workflow`
  * rename role `complete_workflow` to `zmf_workflow_complete`
  * rename role `provision_software_service` to `zmf_cpm_provision_software_service`
  * rename role `manage_software_instance` to `zmf_cpm_manage_software_instance`
  * rename role `remove_software_instance` to `zmf_cpm_remove_software_instance`

Fixed
  * cleanup sanity test checks
  * add tags

Availability
  * Galaxy
  * github

Version 1.0.3
-------------

`v1.0.3`_

Fixed
  * cleanup ansible_lint checks
  * cleanup sanity test checks

Availability
  * Galaxy
  * github

Version 1.0.2
-------------

`v1.0.2`_

Fixed
  * cleanup ansible_lint checks
  * fix bug for cmp roles: instance variable is not correctly parsed in the role

Availability
  * Galaxy
  * github

Version 1.0.1
-------------

`v1.0.1`_

Fixed
  * cleanup ansible_lint checks
  * fix README links on Galaxy webpage
  * add tags

Availability
  * Galaxy
  * github

Version 1.0.0
-------------

`v1.0.0`_

Added
  * initial **ibm_zos_zosmf** collection
  * add modules: `workflow`
  * add roles: `complete_workflow`, `provision_software_service`, `manage_software_instance`, `remove_software_instance`

Availability
  * Galaxy
  * github


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