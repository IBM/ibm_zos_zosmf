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

   .. note::

      * To use the detect keywords function by regular expression in the command response or broadcast messages (by specifying `console_cmdresponse_reg=True` or `console_broadcastmsg_reg=True`) for module: `zmf_console_command`_, it also requires: **z/OSMF APAR PH24072 (PTF UI69958 for V2R3, PTF UI69959 for V2R4)**


.. _Overall Requirements:
   requirements.html
.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_console_command:
   modules/zmf_console_command.html
