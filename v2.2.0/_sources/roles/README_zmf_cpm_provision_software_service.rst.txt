.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

zmf_cpm_provision_software_service
==================================

**IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_cpm_provision_software_service**, to provision a z/OS middleware/software service using Cloud Provisioning & Management (CP&M) template.

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

instance_record_dir
  Path of the directory that provision role will use to capture various information about provisioned instance in json format. 
  
  Value for this variable is specified in host specific variables file in *host_vars* directory.

  | **required**: True
  | **type**: str
  | **default**: default value set in host_vars file is /tmp

instance_info_json_path
  Path to the file that holds provisioned instance information, `zmf_cpm_provision_software_service`_ role will automatically generate this variable in the format of ``<instance_record_dir>/<template_name>-<instance external_name>.json``

  | **required**: False
  | **type**: str

cpm_template_name
  Template name, i.e. software service to be provisioned.

  | **required**: True
  | **type**: str

domain_name
  Cloud domain name associated with the template.

  | **required**: True
  | **type**: str

tenant_name
  Identifies the CP&M Tenant name associated with the user that is driving this role. 
  
  This variable is required if *zmf_user* is associated with multiple CP&M tenants.

  | **required**: True
  | **type**: str

systems_nicknames
  System nick name as identified in z/OSMF. 
  
  If this variable is not specified, provisioning will take place on a system where z/OSMF is currently running.

  | **required**: False
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
   ../playbooks/sample_role_cpm_provision.html
