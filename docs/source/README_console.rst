.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

MVS Command Operations
======================

**IBM z/OSMF collection** provides a module to work with z/OS console. You can use this module to issue MVS command, retrieve command response and easily define success condition based on specified keywords in the command response or broadcast messages, and save the command response on Ansible control node.

.. note::

   * **Configure Console Services**: The module is driving z/OSMF "REST z/OS console services". So you might need to ensure the z/OSMF console services have been setup correctly before you use this ansible module. For more details, see `Configure Console Services`_.

   * **Check Mode**: The module does not support check mode.

Modules
-------

* `zmf_console_command`_:
   
   This module can be used to issue MVS command, retrieve command response and easily define success condition based on specified keywords in the command response or broadcast messages, and save the command response on Ansible control node.

Requirements
------------

See the section `Requirements`_.

Sample Playbooks
----------------

See the section `Playbooks`_.


.. _Configure Console Services:
   https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.4.0/com.ibm.zos.v2r4.izua300/izulite_Consoles_setup.htm
.. _zmf_console_command:
   modules/zmf_console_command.html
.. _Requirements:
   requirements_console.html
.. _Playbooks:
   playbooks.html