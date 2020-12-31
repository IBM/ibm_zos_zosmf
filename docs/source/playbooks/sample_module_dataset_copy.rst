.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_module_dataset_copy
==========================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to copy data to a z/OS data set or member on the remote z/OS system via z/OSMF.

.. code-block:: yaml

   - name: sample of copying data to a z/OS data set or member
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
       - zmf_dataset_copy:
           zmf_credential: "{{ result_auth }}" # Authentication credentials returned by module zmf_authenticate
           dataset_src: "/tmp/dataset_input/member01"
           # dataset_content: "Sample profile\nTZ=EST5EDT\n"
           dataset_dest: "ZOSMF.ANSIBLE.LIB(MEMBER01)"
           # dataset_volser: "VOL001" # The volume to be searched for an uncataloged data set or member
           # dataset_force: true # Whether the target data set must always be overwritten. Default is true
           # dataset_data_type: "text" # Whether data conversion is to be performed on the data to be copied. Default is text (data conversion is performed)
           # dataset_encoding: # Which encodings the data to be copied should be converted from and to
           #   from: ISO8859-1
           #   to: IBM-1047
           # dataset_crlf: false # Whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF)
           # dataset_diff: false # Whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command
           # dataset_migrate_recall: "wait" # How a migrated data set is handled. Default is wait
           # dataset_checksum: "93822124D6E66E2213C64B0D10800224" # The checksum to be used to verify that the target data set to copy to is not changed since the checksum was generated
         register: result
         delegate_to: localhost
       - debug: var=result

.. note::

  To run the sample playbook, below preparation works are required:
  
  * ``delegate_to: localhost`` statement is required for using this module to avoid setting up an SSH connection and install Python on the target z/OS systems.

  * The inventory file `hosts`_ needs to be updated to identify the target z/OS managed node. The data set managed by each z/OS managed node can be accessed by at least one z/OSMF server. Typically, this could be done by setup one z/OSMF in the same sysplex.
  
  * Module `zmf_authenticate`_ is supported by z/OSMF APAR PH12143 (PTF UI66511 for V2R3, PTF UI66512 for V2R4). You are also allowed to authenticate with z/OSMF server in module `zmf_dataset_copy`_ directly.

For more details about module variables, see `zmf_dataset_copy`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_module_dataset_copy.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_dataset_copy:
   ../modules/zmf_dataset_copy.html
.. _zmf_authenticate:
   ../modules/zmf_authenticate.html