.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Requirements - Operate z/OS Data Sets and UNIX Files
====================================================

To use the modules and roles which supplied to interact with **z/OS data set and file REST services** in your playbook, besides the `Overall Requirements`_, the following nodes require specific versions of software:

**Managed Node**:

* `z/OS Management Facility`_: V02.03.00 or later

   The z/OS data set and USS file managed by each z/OS managed node can be accessed by at least one z/OSMF server. Typically, this could be done by setup one z/OSMF in the same sysplex.

   It is required when using:

   * module: `zmf_dataset_fetch`_
   * module: `zmf_file_fetch`_
   * module: `zmf_dataset_copy`_
   * module: `zmf_file_copy`_
   * module: `zmf_dataset`_
   * module: `zmf_file`_

   .. note::

      * To use the encoding function (by variable `dataset_encoding` or `file_encoding`) for modules: `zmf_dataset_fetch`_, `zmf_file_fetch`_, `zmf_dataset_copy`_ and `zmf_file_copy`_, it also requires: **z/OSMF APAR PH15263 (PTF UI65882 for V2R3, PTF UI65883 for V2R4)**

      * To use the create-like function (by variable `dataset_model`) for modules: `zmf_dataset_copy`_ and `zmf_dataset`_, it also requires: **z/OSMF APAR PH22030 (PTF UI68974 for V2R3, PTF UI68975 for V2R4)**


.. _Overall Requirements:
   requirements.html
.. _zmf_dataset_fetch:
   modules/zmf_dataset_fetch.html
.. _zmf_file_fetch:
   modules/zmf_file_fetch.html
.. _zmf_dataset_copy:
   modules/zmf_dataset_copy.html
.. _zmf_file_copy:
   modules/zmf_file_copy.html
.. _zmf_dataset:
   modules/zmf_dataset.html
.. _zmf_file:
   modules/zmf_file.html
.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html
