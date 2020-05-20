.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_role_cpm_provision
=========================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to provision an instance in z/OSMF Cloud Provisioning & Management (CP&M).

.. code-block:: yaml

   - name: sample of provisioning software instance
     hosts: zosmf1
     gather_facts: no
     collections:
       - ibm.ibm_zos_zosmf
     vars:
       - name: instance_info_json_path # will store instance json information globally thru the playbook
     vars_prompt:
       - name: zmf_user
         prompt: "Enter your zOSMF username"
         private: no
       - name: zmf_password
         prompt: "Enter your zOSMF password"
         private: yes
     tasks:
       - include_role:
           name: zmf_cpm_provision_software_service
         vars:
           cpm_template_name: "<fill-me-template-name>" # The value for property cpm_template_name which identifies the template (software service) user wants to provision with Cloud Provisioning & Management
           domain_name: "<domain-name>" # The value for property domain_name which identifies CP&M domain in which specified template is defined
           tenant_name: "<tenant-name>" # The value for optional property tenant_name which identifies CP&M tenant that is associated with the zmf_user that is provisioning the template
           systems_nicknames: "<system-name>" # The value for optional property systems_nicknames which identifies on which system the software instance will be provisioned

.. note::

  For CP&M roles, the inventory file `hosts`_ needs to be updated to identify the target z/OSMF end points.
  
For more details about role variables, see `zmf_cpm_provision_software_service`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/release-v2.0.0/playbooks/sample_role_cpm_provision.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/release-v2.0.0/playbooks/hosts
.. _zmf_cpm_provision_software_service:
   ../roles/README_zmf_cpm_provision_software_service.html