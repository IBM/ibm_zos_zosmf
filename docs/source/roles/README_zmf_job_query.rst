.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

zmf_job_query
=============

**IBM z/OSMF collection** provides provides an Ansible role, referred to as **zmf_job_query**, to query a job running on z/OS, check its return code and user specified content from spool files, and save the user specified spool files locally on control node.

Role Variables
--------------

zmf_host
  Hostname of the z/OSMF server, specified via inventory or vars file.

  | **required**: True
  | **type**: str

zmf_port
  Port number of the z/OSMF server, specified via inventory file or vars file.

  | **required**: False
  | **type**: int

zmf_user
  User name to be used for authenticating with z/OSMF server, prompted when playbook is run.

  Required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.

  | **required**: False
  | **type**: str

zmf_password
  Password to be used for authenticating with z/OSMF server, prompted when playbook is run.

  Required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.

  | **required**: False
  | **type**: str

zmf_crt
  Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication.

  Required when *zmf_user* and *zmf_password* are not supplied.

  | **required**: False
  | **type**: str

zmf_key
  Location of the PEM-formatted file with your private key to be used for HTTPS client authentication.

  Required when *zmf_user* and *zmf_password* are not supplied.

  | **required**: False
  | **type**: str

job_name
  Job name that identifies the job for which status is requested.

  | **required**: True
  | **type**: str

job_id
  Job ID that identifies the job for which status is requested. The value of this variable is folded to uppercase and cannot exceed eight characters. 

  | **required**: True
  | **type**: str

job_search_logic
  Specifies the logic between the check of the job return code and job output. This variable only take effects when *job_search_output* is defined.
  
  * **AND**: The role will succeed only when both the return code is matched with *job_max_rc* and the job output is matched with *job_search_output*. If the return code doesn't match with *job_max_rc*, the role will fail and the remaining tasks to check the job output will be bypassed.
  
  * **OR**: the role will succeed if either the return code is match with *job_max_rc*, or the job output is matched with *job_search_output*. Both tasks to check the return code and job output will no be bypassed no matter wether it is mismatched.

  | **required**: False
  | **type**: str
  | **default**: AND
  | **choices**: AND, OR

job_max_rc
  An integer value that specifies the maximum return code for the job that should be allowed without failing the role.

  * When *job_search_logic=AND*, the role will fail if the return code doesn't match ``CC nnnn`` where nnnn is small or equal to the maximum return code.
  
  * When *job_search_logic=OR*, the role will continue to check the job output if *job_search_output* is defined, even the return code doesn't match ``CC nnnn`` where nnnn is small or equal to the maximum return code.

  | **required**: False
  | **type**: int
  | **default**: 0

job_search_output
  A string or a regular expression specifies the matched part of job output that should be allowed without failing the role.
  
  Use *job_search_output_ddname* to specify the spool file list in which you want to do the match work.
  
  * When *job_search_logic=AND*, the role will fail if no matched output content is found.

  * When *job_search_logic=OR*, the role will succeed if either the return code is small or equal to the maximum return code, or the matched output contents are found.

  | **required**: False
  | **type**: str

job_search_output_ddname
  A list specifies the list of spool files in which the match work will be done. For example: ``["JESMSGLG", "JESJCL"]``. 
  
  This variable only take effects when *job_search_output* is defined. The spool files listed in this variable will be compared with *job_search_output*. If this variable is omitted, all spool files will be compared with *job_search_output*.

  | **required**: False
  | **type**: list

job_search_output_insensitive
  Specifies whether the comparison of *job_search_output* is case insensitive. This variable only take effects when *job_search_output* is defined.

  | **required**: False
  | **type**: bool
  | **default**: True

job_search_output_maxreturnsize
  An integer specifies how many lines of contents from the first matched line in spool file will be returned when *job_search_output* is matched in *job_search_output_ddname*.

  | **required**: False
  | **type**: int
  | **default**: 1

complete_check_times
  The maximum number of time that is used for periodic checks of the job status.

  | **required**: False
  | **type**: int
  | **default**: 10

complete_check_delay
  The interval time between periodic checks of the job status.

  | **required**: False
  | **type**: int
  | **default**: 5

job_save_output_localpath
  The local path on control node where the specified spool files should be saved to. For example: ``/tmp/job_output``. 
  
  This path can be absolute or relative. The role will fail if the parent directory of *job_save_output_localpath* is a read-only file system.
  
  The directory ``{{ job_save_output_localpath }}/{{ inventory_hostname }}/{{ job_name }}_{{ job_id }}/`` will be created to save the specified spool files.

  For example: ``/tmp/job_output/SY1/JCLSAMP1_JOB00000/``.

  Use *job_save_output_ddname* to specify the spool files that you want to save.

  | **required**: False
  | **type**: str

job_save_output_ddname
  A list specifies the list of spool files which should be saved locally on control node. For example: ``["JESYSMSG", "JESJCL"]``. 
  
  This variable only take effects when *job_save_output_localpath* is defined.
  
  The spool files listed in this variable will be saved as separate files and named as ``{{ spoolfile_name }}({{ spoolfile_id }})``.
  
  For example: ``/tmp/job_output/SY1/JCLSAMP1_JOB00000/JESYSMSG(4)``.

  If this variable is omitted, all spool files will be saved locally on control node.
  
  | **required**: False
  | **type**: list

Dependencies
------------

None

Requirements
------------

See the section `Requirements`_.

Sample Playbooks
----------------

See the sample playbook in section `Playbooks`_.


.. _Requirements:
   ../requirements_job.html
.. _Playbooks:
   ../playbooks/sample_role_job_query.html