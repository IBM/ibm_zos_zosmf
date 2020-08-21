.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_module_workflow
======================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to start a z/OS workflow on the target z/OS systems via z/OSMF.

.. code-block:: yaml

   - name: sample of starting a z/OS workflow
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
       - zmf_authenticate:
           zmf_host: "{{ zmf_host }}"
           zmf_port: "{{ zmf_port }}"
           zmf_user: "{{ zmf_user }}"
           zmf_password: "{{ zmf_password }}"
         register: result_auth
         delegate_to: localhost
       - zmf_workflow:
           state: "started"
           zmf_credential: "{{ result_auth }}"
           workflow_name: "ansible_sample_workflow_{{ inventory_hostname }}" # The name of the workflow
           workflow_file: "/var/zosmf/workflow_def/workflow_sample_automation_steps.xml" # The location of the workflow definition file
           workflow_host: "{{ inventory_hostname }}" # Nickname of the target z/OS system on which the workflow is to be performed
           workflow_owner: "{{ zmf_user }}" # User name of the workflow owner
         register: result
         delegate_to: localhost
       - debug: var=result

.. note::

  To run the sample playbook, below preparation works are required:
   
  * In this sample playbook, the workflow definition file `workflow_sample_automation_steps.xml`_ is used to create the workflow instance. You need to manually upload it to the z/OS file system. For example, you can upload it to the directory ``/var/zosmf/workflow_def/``. Then modify the value of variable ``workflow_file`` in the sample playbook to refer to the location of the workflow definition file.
   
  * In the inventory file `hosts`_, the nickname ``workflowHost1`` for the target z/OS system, which is configured as managed node, is used to create the workflow instance. You can modify it to refer to your own z/OS system. You need to ensure the z/OS system ``workflowHost1`` or your own z/OS system is configured in **z/OSMF Systems** plugin.

For more details about module variables, see `zmf_workflow`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_module_workflow.yml
.. _workflow_sample_automation_steps.xml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/files/workflow_sample_automation_steps.xml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_workflow:
   ../modules/zmf_workflow.html