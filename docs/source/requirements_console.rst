.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Requirements - Operate MVS Commands
===================================

* module: `zmf_console_command`_

To use above modules and roles, it needs to ensure **z/OS console REST services** is configured in z/OSMF. Please refer to `here`_ for a quick approach to set up z/OSMF dependencies. 

Besides the `Overall Requirements`_, the following nodes require specific versions of software:

**Control Node**:

* `Requests library for Python`_: 2.23 or later

**Managed Node**:

* `z/OS Management Facility`_: V02.03.00 or later

   .. note::

      * To use the detect keywords function by regular expression in the command response or broadcast messages (by specifying `console_cmdresponse_reg=True` or `console_broadcastmsg_reg=True`) for module: `zmf_console_command`_, it also requires: **z/OSMF APAR PH24072 (PTF UI69958 for V2R3, PTF UI69959 for V2R4)**


.. _Overall Requirements:
   requirements.html
.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_console_command:
   modules/zmf_console_command.html
.. _here:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/docs/zmf_sample_conf/README.md
.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html