.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Operate z/OS Data Sets and UNIX Files
=====================================

**IBM z/OSMF collection** provides several modules to work with z/OS data sets and UNIX files. You can use these modules to fetch z/OS data sets and UNIX files from the remote z/OS system to Ansible control node, and copy z/OS data sets and UNIX files from Ansible control node to the remote z/OS system.

.. **IBM z/OSMF collection** provides several modules to work with z/OS data sets and UNIX files. You can use these modules to fetch z/OS data sets and UNIX files from the remote z/OS system to Ansible control node, copy z/OS data sets and UNIX files from Ansible control node to the remote z/OS system, and manage z/OS data sets and UNIX files on the remote z/OS system (create, delete and set attributes).

.. note::

   * **Check Mode**: These modules do not support check mode.

Modules
-------

* `zmf_dataset_fetch`_:
   
   This module can be used to retrieve the contents of a sequential data set, or a member of a partitioned data set (PDS or PDSE) from the remote z/OS system, and save them on Ansible control node.

* `zmf_file_fetch`_:
   
   This module can be used to retrieve the contents of a z/OS UNIX System Services (USS) file from the remote z/OS system, and save them on Ansible control node.

* `zmf_dataset_copy`_:
   
   This module can be used to copy data from Ansible control node to a sequential data set, or a member of a partitioned data set (PDS or PDSE) on the remote z/OS system.

* `zmf_file_copy`_:
   
   This module can be used to copy data from Ansible control node to a z/OS UNIX System Services (USS) file on the remote z/OS system.

Requirements
------------

See the section `Requirements`_.

Sample Playbooks
----------------

See the section `Playbooks`_.


.. _zmf_dataset_fetch:
   modules/zmf_dataset_fetch.html
.. _zmf_file_fetch:
   modules/zmf_file_fetch.html
.. _zmf_dataset_copy:
   modules/zmf_dataset_copy.html
.. _zmf_file_copy:
   modules/zmf_file_copy.html
.. _Requirements:
   requirements_dataset_file.html
.. _Playbooks:
   playbooks.html