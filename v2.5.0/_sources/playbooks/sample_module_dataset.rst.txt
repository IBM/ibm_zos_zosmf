.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_module_dataset
=====================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to manage z/OS data set or member on z/OS system via z/OSMF.

.. code-block:: yaml

   - name: sample of managing z/OS data set or member
     hosts: dataset
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
       - zmf_dataset:
           zmf_credential: "{{ result_auth }}" # Authentication credentials returned by module zmf_authenticate
           dataset_name: "ZOSMF.ANSIBLE.PS" # Name of the data set or member being managed
           dataset_state: "present" # The final state desired for specified data set or member
           # dataset_volser: "VOL001" # The volume serial to identify the volume to be searched for an uncataloged data set or member
           # dataset_type: "PS" # The type to be used when creating a data set or member. Default is PS
           # dataset_replace: false # Whether the existing data set or member will be replaced. Default is false
           # dataset_create_attributes: # The attributes to be used to create a sequential or partitioned data set
           #   recfm: "FB"
           #   lrecl: 80
           #   alcunit: "TRK"
           #   primary: 10
           #   secondary: 5
           #   unit: "3390"
           # dataset_create_like: "ZOSMF.ANSIBLE.MODEL" # The model data set to be used to create a sequential or partitioned data set. If both dataset_create_attributes and dataset_create_like are supplied, dataset_create_like is ignored
           # dataset_new_name: "ZOSMF.ANSIBLE.PS01" # The new name of the data set or member
           # dataset_migrate_recall: "wait" # How a migrated data set is handled. Default is wait
         register: result
         delegate_to: localhost
       - debug: var=result

.. note::

  To run the sample playbook, below preparation works are required:
  
  * ``delegate_to: localhost`` statement is required for using this module to avoid setting up an SSH connection and install Python on the target z/OS systems.

  * The inventory file `hosts`_ needs to be updated to identify the target z/OS managed node. The data set managed by each z/OS managed node can be accessed by at least one z/OSMF server. Typically, this could be done by setup one z/OSMF in the same sysplex.
  
  * Module `zmf_authenticate`_ is supported by z/OSMF APAR PH12143 (PTF UI66511 for V2R3, PTF UI66512 for V2R4). You are also allowed to authenticate with z/OSMF server in module `zmf_dataset`_ directly.

For more details about module variables, see `zmf_dataset`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_module_dataset.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_dataset:
   ../modules/zmf_dataset.html
.. _zmf_authenticate:
   ../modules/zmf_authenticate.html