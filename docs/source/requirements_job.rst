.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Requirements - Operate z/OS Jobs
================================

* role: `zmf_job_complete`_
* role: `zmf_job_query`_

To use above modules and roles, it needs to ensure **z/OS jobs REST services** is configured in z/OSMF. Please refer to `here`_ for a quick approach to set up z/OSMF dependencies. 

Besides the `Overall Requirements`_, the following nodes require specific versions of software:

**Managed Node**:

* `z/OS Management Facility`_: V02.03.00 or later

   The z/OSMF server must be installed and active on **each** managed z/OS system.

   .. note::

      * To use the search job output function (by variable `job_search_output`) for roles: `zmf_job_complete`_ and `zmf_job_query`_, it also requires: **z/OSMF APAR PH23046 (PTF UI69412 for V2R3, PTF UI69413 for V2R4)**


.. _Overall Requirements:
   requirements.html
.. _zmf_job_complete:
   roles/README_zmf_job_complete.html
.. _zmf_job_query:
   roles/README_zmf_job_query.html
.. _here:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/docs/zmf_sample_conf/README.md
.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html
