.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_role_job_complete
========================

For configuration and setup, see `Playbook Documentation`_. 

This sample playbook shows how to submit a job to run on the target z/OS systems via z/OSMF.

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
           job_jcl_src: "files/job_sample_jcl.jcl" # The detail location of file or data set containing the JCL


.. _Playbook Documentation:
   ../playbooks.html
.. _sample_role_job_complete.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/release-v2.0.0/playbooks/sample_role_job_complete.yml