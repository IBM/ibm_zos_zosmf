.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_module_file
==================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to manage USS file or directory on the remote z/OS system via z/OSMF.

.. code-block:: yaml

   - name: sample of managing z/OS USS file or directory
     hosts: file
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
       - zmf_file:
           zmf_credential: "{{ result_auth }}" # Authentication credentials returned by module zmf_authenticate
           file_path: "/etc/profile" # Path to the USS file or directory being managed
           file_state: "file" # The final state desired for specified USS file or directory
           # file_mode: # The permission the resulting USS file or directory should have
           #   mode: "755"
           #   recursive: false
           # file_owner: # Indicates the function change owner
           #   owner: "500000"
           #   group: "0"
           #   recursive: false
           # file_tag: # Indicates the function change tag
           #   tag: "mixed"
           #   codeset: "IBM-1047"
           #   recursive: false
           # file_rename: "/etc/profile.bak" # The new name of the USS file or directory
         register: result
         delegate_to: localhost
       - debug: var=result

.. note::

  To run the sample playbook, below preparation works are required:
  
  * ``delegate_to: localhost`` statement is required for using this module to avoid setting up an SSH connection and install Python on the target z/OS systems.

  * The inventory file `hosts`_ needs to be updated to identify the target z/OS managed node. The USS file managed by each z/OS managed node can be accessed by at least one z/OSMF server. Typically, this could be done by setup one z/OSMF in the same sysplex.
  
  * Module `zmf_authenticate`_ is supported by z/OSMF APAR PH12143 (PTF UI66511 for V2R3, PTF UI66512 for V2R4). You are also allowed to authenticate with z/OSMF server in module `zmf_file`_ directly.

For more details about module variables, see `zmf_file`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_module_file.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_file:
   ../modules/zmf_file.html
.. _zmf_authenticate:
   ../modules/zmf_authenticate.html