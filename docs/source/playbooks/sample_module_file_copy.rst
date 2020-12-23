.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_module_file_copy
=======================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to copy data to a USS file on the remote z/OS system via z/OSMF.

.. code-block:: yaml

   - name: sample of copying data to a z/OS USS file
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
       - zmf_file_copy:
           zmf_credential: "{{ result_auth }}" # Authentication credentials returned by module zmf_authenticate
           file_src: "/tmp/file_input/profile"
           # file_content: "Sample profile\nTZ=EST5EDT\n"
           file_dest: "/etc/profile"
           # file_force: true # Whether the target USS file must always be overwritten. Default is true
           # file_data_type: "text" # Whether data conversion is to be performed on the data to be copied. Default is text (data conversion is performed)
           # file_encoding: # Which encodings the data to be copied should be converted from and to
           #   from: ISO8859-1
           #   to: IBM-1047
           # file_crlf: false # Whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF)
           # file_diff: false # Whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command
           # file_checksum: "93822124D6E66E2213C64B0D10800224" # The checksum to be used to verify that the target USS file to copy to is not changed since the checksum was generated
         register: result
         delegate_to: localhost
       - debug: var=result

.. note::

  To run the sample playbook, below preparation works are required:
  
  * ``delegate_to: localhost`` statement is required for using this module to avoid setting up an SSH connection and install Python on the target z/OS systems.

  * The inventory file `hosts`_ needs to be updated to identify the target z/OS managed node. The USS file managed by each z/OS managed node can be accessed by at least one z/OSMF server. Typically, this could be done by setup one z/OSMF in the same sysplex.
  
  * Module `zmf_authenticate`_ is supported by z/OSMF APAR PH12143 (PTF UI66511 for V2R3, PTF UI66512 for V2R4). You are also allowed to authenticate with z/OSMF server in module `zmf_file_copy`_ directly.

For more details about module variables, see `zmf_file_copy`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_module_file_copy.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_file_copy:
   ../modules/zmf_file_copy.html
.. _zmf_authenticate:
   ../modules/zmf_authenticate.html