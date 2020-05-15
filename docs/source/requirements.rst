.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Requirements
============

**Control node** is any machine with Ansible installed. From the control node, you can run commands and playbooks from a laptop, desktop, or server machine. However, you cannot run **IBM z/OSMF collection** on a Windows machine.

**Managed node** is often referred to as a target node, or host, and is the node that is managed by Ansible. Ansible does not need to be installed on a managed node.

Overall Requirements
--------------------

To use this collection, the following nodes require specific versions of software:

**Control Node**:

* `Ansible`_: 2.9 or later
* `Python`_: 2.7 or later

**Managed Node**:

* `z/OS`_: V02.03.00 or later

   The target z/OS systems should be configured as the target hosts (managed nodes) in your playbook. It is not necessary to set up an SSH connection and install Python on the target z/OS systems. Instead, the modules and roles in this collection will create HTTPS connections with the z/OSMF server. Therefore ``delegate_to: localhost`` statement is required for using the modules in your playbook task. This statement is hard-coded within the roles.

* `z/OS Management Facility`_: V02.03.00 or later

   The z/OSMF server must be installed and active on **at least one** z/OS system in the same sysplex. Information about the z/OSMF server must be configured in the inventory ``hosts`` file or in the ``vars`` file, such as the hostname, port number, and authentication info. The authentication info to connect to the z/OSMF server is provided when running playbook or it will be prompted during playbook run.

Specific Requirements
---------------------

.. toctree::
   :maxdepth: 1
   :glob:

   requirements_workflow
   requirements_cpm
   requirements_job


.. _Ansible:
   https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
.. _Python:
.. _z/OS:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html
.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html