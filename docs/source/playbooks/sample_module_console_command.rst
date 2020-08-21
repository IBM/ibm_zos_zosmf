.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

sample_module_console_command
=============================

For configuration and setup, see `Playbook Documentation`_. 

This `sample playbook`_ shows how to issue MVS command by using a system console via z/OSMF.

.. code-block:: yaml

   - name: sample of issuing MVS command by using a system console
     hosts: console
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
       - zmf_console_command:
           zmf_credential: "{{ result_auth }}"
           console_cmd: "start pegasus"
           console_system: "{{ inventory_hostname }}"
           # console_cmdresponse_keyword: "SLP registration initiated" # The keyword that you want to detect in the command response. The module will fail if no specified keywords are detected in neither the command response nor broadcast messages
           # console_cmdresponse_reg: "N" # Whether console_cmdresponse_keyword represents a regular expression. Default is 'N'
           # console_broadcastmsg_keyword: "started CIM server" # The keyword that you want to detect in broadcast messages. The module will fail if no specified keywords are detected in neither the command response nor broadcast messages
           # console_broadcastmsg_reg: "N" # Whether console_broadcastmsg_keyword represents a regular expression. Default is 'N'
           # console_broadcastmsg_detect_timeout: 30 # How long, in seconds, the console attempts to detect the value of console_broadcastmsg_keyword in the broadcast messages. Default is 30
           # console_cmdresponse_retrieve_times: 1 # How many times the console attempts to retrieve the command response. Default is 1
           console_save_output_localpath: "/tmp/cmd_output" # The local path on control node where the command response will be saved to
         register: result
         delegate_to: localhost
       - debug: var=result

.. note::

  To run the sample playbook, below preparation works are required:
  
  * ``delegate_to: localhost`` statement is required for using this module to avoid setting up an SSH connection and install Python on the target z/OS systems.

  * In the inventory file `hosts`_, the name of Ansible managed node should be the same with the system name of target z/OS system. You can update it to your own z/OS system name.

  * In the inventory file `hosts`_, each z/OS managed node typically needs to specify its serving z/OSMF via variable ``zmf_host`` and ``zmf_port``. For z/OS managed nodes in the same sysplex, it's recommended to specify the same serving z/OSMF host since z/OSMF is sysplex scope typically. Otherwise if you have different serving z/OSMF specified for multiple z/OS managed nodes which are in the same sysplex, you need to specify the variable ``console_name`` in host specific variable file under host_vars directory so that each z/OS managed node uses an unique console name.
  
For more details about module variables, see `zmf_console_command`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_module_console_command.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_console_command:
   ../modules/zmf_console_command.html