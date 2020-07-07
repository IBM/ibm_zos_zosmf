.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Requirements - MVS Command Operations
=====================================

To use the modules and roles which supplied to interact with **z/OS console REST services** in your playbook, besides the `Overall Requirements`_, the following nodes require specific versions of software:

**Control Node**:

* `Requests library for Python`_: 2.23 or later

   It is required when using:
  
   * module: `zmf_console_command`_


.. _Overall Requirements:
   requirements.html
.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_console_command:
   modules/zmf_console_command.html
