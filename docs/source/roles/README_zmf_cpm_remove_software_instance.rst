.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

zmf_cpm_remove_software_instance
================================

**IBM z/OSMF collection** provides provides an Ansible role, referred to as **zmf_cpm_remove_software_instance**, to remove a deprovisioned instance of z/OS middleware/software.

Role Variables
--------------

zmf_host
  z/OSMF host name, specified via inventory file.

  | **required**: True
  | **type**: str

zmf_port
  z/OSMF port number, specified via inventory file.

  | **required**: True
  | **type**: str

zmf_user
  z/OSMF username, prompted when playbook is run.

  | **required**: True
  | **type**: str

zmf_password
  z/OSMF password, prompted when playbook is run.

  | **required**: True
  | **type**: str

instance_info_json_path
  Path to the json file that holds provisioned instance information. 
  
  Specify the file name that is generated when `zmf_cpm_provision_software_service`_ role was performed.

  | **required**: True
  | **type**: str

Dependencies
------------

None

Requirements
------------

See the section `Requirements`_.

Sample Playbooks
----------------

See the section `Playbooks`_.


.. _zmf_cpm_provision_software_service:
   README_zmf_cpm_provision_software_service.html
.. _Requirements:
   requirements.html
.. _Playbooks:
   playbooks.html
