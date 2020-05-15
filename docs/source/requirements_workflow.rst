.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Requirements - Operate z/OS Workflows
=====================================

To use the modules and roles which supplied to interact with **z/OSMF Workflows** in your playbook, besides the `Overall Requirements`_, the following nodes require specific versions of software:

**Control Node**:

* `Requests library for Python`_: 2.23 or later

   It is required when using:
  
   * module: `zmf_workflow`_
   * role: `zmf_workflow_complete`_


.. _Overall Requirements:
   requirements.html
.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_workflow:
   https://github.com/IBM/ibm_zos_zosmf/tree/release-v2.0.0/plugins/modules/zmf_workflow.py
.. _zmf_workflow_complete:
   roles/README_zmf_workflow_complete.html
