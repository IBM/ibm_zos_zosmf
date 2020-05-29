.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_role_job_query
=====================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to query a job running on the target z/OS systems via z/OSMF.

.. code-block:: yaml

   - name: sample of querying a job running on z/OS, check its return code and user specified content from spool files
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
           name: zmf_job_query
         vars:
           job_name: "JCLSAMP1" # The name of the job for which status is requested
           job_id: "JOB00000" # The ID of the job for which status is requested. This variable should be specified in host specific variables file in host_vars directory since the same job running on different z/OS has different job ID
           # job_search_logic: 'AND' # The logic between the check of the job return code and job output. Default is AND
           # job_max_rc: 0 # The maximum return code for the job that should be allowed without failing the role. Default is 0
           # complete_check_times: 10 # The maximum number of time that is used for periodic checks of the job status. Default is 10
           # complete_check_delay: 5 # The interval time between periodic checks of the job status. Default is 5
           job_search_output: "JCLSAMP1 STARTED" # A string or a regular expression specifies the matched part of job output that should be allowed without failing the role.
           job_search_output_ddname: ["JESMSGLG"] # The list of spool files in which the match work will be done.
           # job_search_output_insensitive: True # Whether the comparison of job_search_output is case insensitive. Default is True
           # job_search_output_maxreturnsize: 1 # How many lines of contents from the first matched line in spool file will be returned when job_search_output is matched in job_search_output_ddname. Default is 1

.. note::

  To run the sample playbook, the inventory file `hosts`_ needs to be updated to identify the target z/OSMF end points.

For more details about role variables, see `zmf_job_query`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_role_job_query.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_job_query:
   ../roles/README_zmf_job_query.html