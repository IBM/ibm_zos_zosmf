.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Requirements
============

**Control node** is any machine with Ansible installed. From the control node, you can run commands and playbooks from a laptop, desktop, or server machine. However, you cannot run **IBM z/OSMF collection** on a Windows machine.

**Managed node** is often referred to as a target node, or host, and is the node that is managed by Ansible. Ansible does not need to be installed on a managed node.

The following nodes require specific versions of software:

Control Node
------------

* `Ansible`_: 2.9 or later
* `Python`_: 2.7 or later
* `Requests library for Python`_: 2.23 or later

.. note::
   
   * ``Requests library for Python`` is required only when using:

      * modules: `zmf_workflow`_
      * roles: `zmf_workflow_complete`_

Managed Node
------------

* `z/OS`_: V02.03.00 or later
* `Cloud Provisioning & Management`_

.. note::
   
   * ``Cloud Provisioning & Management`` is required only when using:
   
      * roles: `provision_software_service`_, `manage_software_instance`_, `remove_software_instance`_

Target z/OS
-----------

**"delegate_to: localhost"** statement is required for using the module in your playbook task. The statement causes the module to run locally in control node. With this setting in effect, it is not necessary to set up an SSH connection and install Python on the target z/OS systems. Instead, the module creates HTTPS connections with the z/OSMF server. This statement is hard-coded within the roles.

z/OSMF on z/OS
--------------

The target z/OS systems should be configured as the target hosts (managed nodes) in your playbook. It is not necessary for a z/OSMF server to be installed on every target z/OS system. However, a z/OSMF server must be installed and active on *at least one* z/OS system in the same sysplex. For the configuration of z/OSMF server, see `IBM z/OSMF Configuration Guide`_.

Information about the z/OSMF server must be configured in the `vars` file, such as the hostname, port number, and authentication info. Either username and password or client-certificate authorization can be used for authenticating with the z/OSMF server.  If both methods are specified, the system attempts to use client-certificate authentication.


.. _Ansible:
   https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
.. _Python:
   https://www.python.org/downloads/release/latest
.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_workflow:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/zmf_workflow.py
.. _zmf_workflow_complete:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/zmf_workflow_complete/
.. _provision_software_service:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/provision_software_service/
.. _manage_software_instance:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/manage_software_instance/
.. _remove_software_instance:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/remove_software_instance/
.. _z/OS:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html
.. _Cloud Provisioning & Management:
   https://www.ibm.com/support/z-content-solutions/cloud-provisioning
.. _IBM z/OSMF Configuration Guide:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html
