.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

zmf_cpm_manage_software_instance
=================================

**IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_cpm_manage_software_instance**, to manage a provisioned instance of z/OS middleware/software. Various management such as starting or stopping the instance can be performed using this role. When software service instance is not required any more, it can be deprovisioned using this role.

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
  z/OSMF username, prompted when playbook is run or can be specified on playbook run command.


  | **required**: True
  | **type**: str

zmf_password
  z/OSMF password, prompted when playbook is run or can be specified on playbook run command.

  | **required**: True
  | **type**: str

instance_action_name
  Action to be performed on a provisioned software instance, for example: Deprovision.
  
  Actions that can be performed on a provisioned instance are described in local record file associated with the provisioned instance. The *name* variable in *actions* array under *registry-info* identifies various actions that can be performed on the instance.

  | **required**: True
  | **type**: str

instance_info_json_path
  Path to the json file that holds provisioned instance information. 
  
  Specify the file name that is generated when `zmf_cpm_provision_software_service`_ role was performed.

  | **required**: True
  | **type**: str

api_polling_retry_count
  Total retries number before role exit with failure waiting on instance action to complete. 
  
  This variable is specified in host specific variables file in *host_vars* directory.

  | **required**: True
  | **type**: int
  | **default**: default value set in host_vars file is 50

api_polling_interval_seconds
  Interval time for each polling request in seconds. 
  
  This variable is specified in host specific variables file in *host_vars* directory.

  | **required**: True
  | **type**: int
  | **default**: default value set in host_vars file is 10

Dependencies
------------

None

Requirements
------------

See the section `Requirements`_.

Sample Playbooks
----------------

See the sample playbook in section `Playbooks`_.


.. _zmf_cpm_provision_software_service:
   README_zmf_cpm_provision_software_service.html
.. _Requirements:
   ../requirements_cpm.html
.. _Playbooks:
   ../playbooks/sample_role_cpm_manage_instance.html
