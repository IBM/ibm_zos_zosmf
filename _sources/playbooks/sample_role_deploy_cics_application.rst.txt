.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_role_deploy_cics_application
===================================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to install a web application on a provisioned CICS instance in z/OSMF Cloud Provisioning & Management (CP&M).

Before run the sample playbook, please copy role `role_cics_wlp_install_app`_ in ``playbooks/files/cpm/`` directory to ``roles/`` directory.

.. code-block:: yaml

   - name: sample of provisioning CICS region and deploying application
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
       - name: application_path_input
         prompt: "Enter your application file full path"
         private: no
     tasks:
       - include_role:
           name: zmf_cpm_provision_software_service
         vars:
           cpm_template_name: "<fill-me-template-name>" # The value for property cpm_template_name which identifies the template (software service) user wants to provision with Cloud Provisioning & Management
           domain_name: "<domain-name>" # The value for property domain_name which identifies CP&M domain in which specified template is defined
           tenant_name: "<tenant-name>" # The value for optional property tenant_name which identifies CP&M tenant that is associated with the zmf_user that is provisioning the template
           systems_nicknames: "<system-name>" # The value for optional property systems_nicknames which identifies on which system the software instance will be provisioned
       - include_role:
           name: cics_wlp_install_app
         vars:
           instance_info_json: "{{lookup('file', instance_info_json_path)}}" # Path of the instance json file contains cics public variables
           app_root_uri: "/CloudTestServlet" # The URI path to access the application once upload
           app_file_name: "CloudTestServlet.war" # The file name that the application file will be written to the USS file system in z/OS
           application_path: "{{ application_path_input }}" # The local absolute file path to the application binary file

.. note::

  For CP&M roles, the inventory file `hosts`_ needs to be updated to identify the target z/OSMF end points.

For more details about role variables, see `zmf_cpm_provision_software_service`_ and `role_cics_wlp_install_app`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_role_deploy_cics_application.yml
.. _role_cics_wlp_install_app:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/files/cpm/cics_wlp_install_app/
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_cpm_provision_software_service:
   ../roles/README_zmf_cpm_provision_software_service.html