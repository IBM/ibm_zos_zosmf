.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Operate z/OS Data Sets and UNIX Files
=====================================

**IBM z/OSMF collection** provides several modules to work with z/OS data sets and UNIX files. You can use these modules to fetch z/OS data sets and UNIX files from the remote z/OS system to Ansible control node, copy z/OS data sets and UNIX files from Ansible control node to the remote z/OS system, and manage z/OS data sets and UNIX files on the remote z/OS system.

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
   This module also can be used to copy file or data set from the remote z/OS system to a data set or member on the remote z/OS system.

* `zmf_file_copy`_:
   
   This module can be used to copy data from Ansible control node to a z/OS UNIX System Services (USS) file on the remote z/OS system.

* `zmf_dataset`_:
   
   This module can be used to create, delete and operate on a sequential or partitioned data set, or a member of partitioned data set (PDS or PDSE) on the remote z/OS system. The available operations include rename data set or member, migrate data set and recall the migrated data set.

* `zmf_file`_:
   
   This module can be used to create, delete and operate on a z/OS UNIX System Services (USS) file or a directory on the remote z/OS system. The available operations include rename, change mode, change owner and change tag.

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
.. _zmf_dataset:
   modules/zmf_dataset.html
.. _zmf_file:
   modules/zmf_file.html
.. _Requirements:
   requirements_dataset_file.html
.. _Playbooks:
   playbooks.html