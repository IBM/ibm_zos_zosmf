.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_module_dataset_fetch
===========================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to fetch data set from the remote z/OS system via z/OSMF.

.. code-block:: yaml

   - name: sample of fetching data set from z/OS
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
           zmf_host: "{{ zmf_host }}" # Authentication credentials returned by module zmf_authenticate
           zmf_port: "{{ zmf_port }}"
           zmf_user: "{{ zmf_user }}"
           zmf_password: "{{ zmf_password }}"
         register: result_auth
         delegate_to: localhost
       - zmf_dataset_fetch:
           zmf_credential: "{{ result_auth }}"
           dataset_src: "SYS1.PARMLIB(SMFPRM00)"
           dataset_dest: "/tmp/dataset_output"
           # dataset_flat: false # Whether to override the default behavior of appending hostname/path/to/file to the destination. Default is false
           # dataset_data_type: "text" # Whether data conversion is to be performed on the returned data. Default is text 
           (data conversion is performed)
           # dataset_encoding: # Which encodings the fetched data set should be converted from and to.
           #   from: IBM-1047
           #   to: ISO8859-1
           # dataset_range: # A range that is used to retrieve the data set.
           #   start: 0
           #   end: 499
           # dataset_search: # A series of parameters that are used to search the data set.
           #   keyword: "Health Checker"
           #   insensitive: true
           #   maxreturnsize: 100
           # dataset_checksum: "93822124D6E66E2213C64B0D10800224" # the ETag token to be used to verify that the  data set to be fetched is not changed since the ETag token was generated.
         register: result
         delegate_to: localhost
       - debug: var=result

.. note::

  To run the sample playbook, below preparation works are required:
  
  * ``delegate_to: localhost`` statement is required for using this module to avoid setting up an SSH connection and install Python on the target z/OS systems.

  * The inventory file `hosts`_ needs to be updated to identify the target z/OS managed node. The data set managed by each z/OS managed node can be accessed by at least one z/OSMF server. Typically, this could be done by setup one z/OSMF in the same sysplex.
  
  * Module `zmf_authenticate`_ is supported by z/OSMF APAR PH12143 (PTF UI66511 for V2R3, PTF UI66512 for V2R4). You are also allowed to authenticate with z/OSMF server in module `zmf_dataset_fetch`_ directly.

For more details about module variables, see `zmf_dataset_fetch`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_module_dataset_fetch.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_dataset_fetch:
   ../modules/zmf_dataset_fetch.html
.. _zmf_authenticate:
   ../modules/zmf_authenticate.html