.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Requirements - Operate z/OS Workflows
=====================================

* module: `zmf_workflow`_
* role: `zmf_workflow_complete`_

To use above modules and roles, it needs to ensure **z/OSMF Workflows** is configured in z/OSMF. Please refer to `here`_ for a quick approach to set up z/OSMF dependencies. 

Besides the `Overall Requirements`_, the following nodes require specific versions of software:

**Control Node**:

* `Requests library for Python`_: 2.23 or later


.. _Overall Requirements:
   requirements.html
.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_workflow:
   modules/zmf_workflow.html
.. _zmf_workflow_complete:
   roles/README_zmf_workflow_complete.html
.. _here:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/docs/zmf_sample_conf/README.md