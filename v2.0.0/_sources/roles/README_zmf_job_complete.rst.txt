.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

zmf_job_complete
================

**IBM z/OSMF collection** provides provides an Ansible role, referred to as **zmf_job_complete**, to submit a job to run on z/OS, and check its return code.

.. **IBM z/OSMF collection** provides provides an Ansible role, referred to as **zmf_job_complete**, to submit a job to run on z/OS, check its return code and specific contents in spool files.

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

job_jcl_src
  Specifies the detail location of file or data set containing the JCL.

  * When *job_jcl_location=LOCAL*, this variable should be the absolute path of the JCL file on control node. For example: ``/tmp/job1.jcl``.

  * When *job_jcl_location=DATASET*, this variable should be the full name of the data set or the member. For example: ``USER.TEST.JCLLIB`` or ``USER.TEST.JCLLIB(JCL1)``.

  * When *job_jcl_location=USS*, this variable should be the absolute path of the JCL file in USS file system on managed z/OS node. For example: ``/var/data/jcl/job1.jcl``.

  | **required**: True
  | **type**: str

job_jcl_location
  An option to specify the location of the JCL to be submitted.
  
  * **LOCAL**: Specifies that the JCL residents in local, the role will try to load the JCL file from control node.

  * **DATASET**: Specifies that the JCL is contained in a data set or s data set member on managed z/OS node. Note that the specified data set must be cataloged

  * **USS**: Specifies that the JCL residents in USS file system on managed z/OS node.

  | **required**: False
  | **type**: str
  | **default**: LOCAL
  | **choices**: LOCAL, DATASET, USS

job_internal_reader_class
  A single character that specifies the internal reader class to define the default message class (MSGCLASS) for the job.

  | **required**: False
  | **type**: str
  | **default**: A

job_internal_reader_recfm
  A single character that specifies the internal reader record format: ``F`` or ``V``.  
  
  * When submitting a job from a data set, you can omit this header. Otherwise, this value must match the record format of the data set.
  
  * When not submitting a job from a data set, if you omit this header or specify a value other than ``F`` or ``V``, the default of ``F`` is used.

  | **required**: False
  | **type**: str
  
job_internal_reader_lrecl
  An integer value that specifies the internal reader logical record length (LRECL).
  
  * When submitting a job from a data set, you can omit this header. Otherwise, this value must match the LRECL of the data set.
  
  * When not submitting a job from a data set, if you omit this header or specify a non-integer value, the default of 80 is used.

  | **required**: False
  | **type**: int

job_internal_reader_mode
  A keyword that specifies the format of the input job.

  * **RECORD**: When submitting a job from a data set, you can ether omit this variable or set it to ``RECORD``.
  
  * **TEXT**: When not submitting a job from a data set, ``TEXT`` is default value.
  
  * **BINARY**: When set this variable to ``BINARY``, *job_internal_reader_lrecl* must be omitted or set to ``F``.

  | **required**: False
  | **type**: str
  | **choices**: RECORD, TEXT, BINARY

job_user_correlator
  Specifies the user portion of the job correlator. 
  
  In z/OS, a job correlator can be used to associate each job with a unique 64-character value. The correlator provides you with a means to query a job in the system and track it through execution.  
  A job correlator consists of a 31-byte system-defined portion and a colon character ``:``, followed by a 32-byte user portion. 
  
  This value is 1 – 32 characters in length, where the first character must be uppercase alphabetic (A-Z) or special ($, #, @). The remaining characters (up to 31) can be any combination of uppercase alphabetic, numeric (0-9), or special. Blank characters are not supported.

  | **required**: False
  | **type**: str
  
job_symbols
  This variable is a dictionary which specifies the name and value for JCL symbols.

  A symbol name is 1 – 8 characters, where the first character must be uppercase alphabetic (A-Z) or special ($, #, @). The remaining characters (up to 7) can be any combination of uppercase alphabetic, numeric (0-9), or special.

  A symbol value is limited to 255 characters. Multiple symbol names and values can be specified, up to a limit of 128.

  For example:

  .. code-block:: sh
     
     {
       "symbol1": "value1",
       "symbol2": "value2"
     }

  | **required**: False
  | **type**: dict

.. job_search_logic
..   Specifies the logic between the check of the job return code and job output. This variable only take effects when *job_search_output* is defined.
  
..   * **AND**: The role will succeed only when both the return code is matched with *job_max_rc* and the job output is matched with *job_search_output*. If the return code doesn't match with *job_max_rc*, the role will fail and the remaining tasks to check the job output will be bypassed.
  
..   * **OR**: the role will succeed if either the return code is match with *job_max_rc*, or the job output is matched with *job_search_output*. Both tasks to check the return code and job output will no be bypassed no matter wether it is mismatched.

..   | **required**: False
..   | **type**: str
..   | **default**: AND
..   | **choices**: AND, OR

job_max_rc
  An integer value that specifies the maximum return code for the job that should be allowed without failing the role.

  The role will fail if the return code doesn't match ``CC nnnn`` where nnnn is small or equal to the maximum return code.

  | **required**: False
  | **type**: int
  | **default**: 0

.. job_max_rc
..   An integer value that specifies the maximum return code for the job that should be allowed without failing the role.

..   * When *job_search_logic=AND*, the role will fail if the return code doesn't match ``CC nnnn`` where nnnn is small or equal to the maximum return code.
  
..   * When *job_search_logic=OR*, the role will continue to check the job output if *job_search_output* is defined, even the return code doesn't match ``CC nnnn`` where nnnn is small or equal to the maximum return code.

..   | **required**: False
..   | **type**: int
..   | **default**: 0

.. job_search_output
..   A string or a regular expression specifies the matched part of job output that should be allowed without failing the role.
  
..   Use *job_search_output_ddname* to specify the spool file list in which you want to do the match work.
  
..   * When *job_search_logic=AND*, the role will fail if no matched output content is found.

..   * When *job_search_logic=OR*, the role will succeed if either the return code is small or equal to the maximum return code, or the matched output contents are found.

..   | **required**: False
..   | **type**: str

.. job_search_output_ddname
..   A list specifies the list of spool files in which the match work will be done. For example: ``["JESMSGLG", "JESJCL"]``. 
  
..   This variable only take effects when *job_search_output* is defined. The spool files listed in this variable will be compared with *job_search_output*. If this variable is omitted, all spool files will be compared with *job_search_output*.

..   | **required**: False
..   | **type**: list

.. job_search_output_insensitive
..   Specifies whether the comparison of *job_search_output* is case insensitive. This variable only take effects when *job_search_output* is defined.

..   | **required**: False
..   | **type**: bool
..   | **default**: True

.. job_search_output_maxreturnsize
..   An integer specifies how many lines of contents from the first matched line in spool file will be returned when *job_search_output* is matched in *job_search_output_ddname*.

..   | **required**: False
..   | **type**: int
..   | **default**: 1

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
   ../playbooks/sample_role_job_complete.html