.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_role_job_complete
========================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to submit a job to run on the target z/OS systems via z/OSMF.

.. code-block:: yaml

   - name: sample of submitting a job to run on z/OS
     hosts: job
     gather_facts: no
     collections:
       - ibm.ibm_zos_zosmf
     vars_prompt:
       - name: zmf_user
         prompt: "Enter your zOSMF username (skip if zmf_crt and zmf_key are supplied)"
         private: no
       - name: zmf_password
         prompt: "Enter your zOSMF password (skip if zmf_crt and zmf_key are supplied)"
         private: yes
     tasks:
       - include_role:
           name: zmf_job_complete
         vars:
           job_jcl_src: "files/job_sample_jcl.jcl" # The location of file or data set containing the JCL
           # job_jcl_location: 'LOCAL' # The type of location of the JCL to be submitted. Default is LOCAL
           # job_search_logic: 'AND' # The logic between the check of the job return code and job output. Default is AND
           # job_max_rc: 0 # The maximum return code for the job that should be allowed without failing the role. Default is 0
           # complete_check_times: 10 # The maximum number of time that is used for periodic checks of the job status. Default is 10
           # complete_check_delay: 5 # The interval time between periodic checks of the job status. Default is 5
           job_search_output: "JCLSAMP1 STARTED" # A string or a regular expression specifies the matched part of job output that should be allowed without failing the role.
           job_search_output_ddname: ["JESMSGLG"] # The list of spool files in which the match work will be done.
           # job_search_output_insensitive: True # Whether the comparison of job_search_output is case insensitive. Default is True
           # job_search_output_maxreturnsize: 1 # How many lines of contents from the first matched line in spool file will be returned when job_search_output is matched in job_search_output_ddname. Default is 1
           job_save_output_localpath: "/tmp/job_output" # The local path on control node where the specified spool files will be saved to
           job_save_output_ddname: ["JESYSMSG"] # The list of spool files which will be saved on control node

.. note::

  To run the sample playbook, the inventory file `hosts`_ needs to be updated to identify the target z/OSMF end points.

For more details about role variables, see `zmf_job_complete`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_role_job_complete.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_job_complete:
   ../roles/README_zmf_job_complete.html