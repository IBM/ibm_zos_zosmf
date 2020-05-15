.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_role_workflow_complete
=============================

For configuration and setup, see `Playbook Documentation`_. 

This sample playbook shows how to complete a z/OS workflow on the target z/OS systems via z/OSMF.

.. code-block:: yaml

   - name: sample of completing a z/OS workflow
     hosts: workflow
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
           name: zmf_workflow_complete
         vars:
           workflow_name: "ansible_sample_workflow_{{ inventory_hostname }}"
           workflow_file: "/var/zosmf/workflow_def/workflow_sample_automation_steps.xml"
       - debug: var=result

To run the sample playbook, below preparation works are required:
   
* In this sample playbook, the workflow definition file `workflow_sample_automation_steps.xml`_ is used to create the workflow instance. You need to manually upload it to the z/OS file system. For example, you can upload it to the directory ``/var/zosmf/workflow_def/``. Then modify the value of variable ``workflow_file`` in the sample playbook to refer to the location of the workflow definition file.
   
* In the inventory file `hosts`_, the nickname ``SY1`` for the target z/OS system, which is configured as managed node, is used to create the workflow instance. You can modify it to refer to your own z/OS system. You need to ensure the z/OS system ``SY1`` or your own z/OS system is configured in **z/OSMF Systems** plugin.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample_role_workflow_complete.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/release-v2.0.0/playbooks/sample_role_workflow_complete.yml
.. _workflow_sample_automation_steps.xml:
   https://github.com/IBM/ibm_zos_zosmf/tree/release-v2.0.0/playbooks/files/workflow_sample_automation_steps.xml
.. _hosts:
   https://github.com/ansible-collections/ibm_zos_core/tree/release-v2.0.0/playbooks/hosts