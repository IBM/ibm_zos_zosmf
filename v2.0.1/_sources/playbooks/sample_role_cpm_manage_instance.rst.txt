.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_role_cpm_manage_instance
===============================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to perform instance specific action on a provisioned instance in z/OSMF Cloud Provisioning & Management (CP&M).

.. code-block:: yaml

   - name: sample of managing software instance
     hosts: zosmf1
     gather_facts: no
     collections:
       - ibm.ibm_zos_zosmf
     vars_prompt:
       - name: zmf_user
         prompt: "Enter your zOSMF username"
         private: no
       - name: zmf_password
         prompt: "Enter your zOSMF password"
         private: yes
     tasks:
       - include_role:
           name: zmf_cpm_manage_software_instance
         vars:
           instance_action_name: "<action-name>" # The value for property instance_action_name identifies which instance action user wants to perform
           instance_info_json_path: "<full-instance-json-file-path>" # The value for property instance_info_json_path identifies full file path of the provisioned instance json file that is created by zmf_cpm_provision_software_service role, common format is /{{ instance_record_dir }}/{{ instanceID }}-{{ externalName }}.json

.. note::

  For CP&M roles, the inventory file `hosts`_ needs to be updated to identify the target z/OSMF end points.

For more details about role variables, see `zmf_cpm_manage_software_instance`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_role_cpm_manage_instance.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_cpm_manage_software_instance:
   ../roles/README_zmf_cpm_manage_software_instance.html