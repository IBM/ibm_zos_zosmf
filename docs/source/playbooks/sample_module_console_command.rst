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
       - zmf_console_command:
           zmf_host: "{{ zmf_host }}"
           zmf_port: "{{ zmf_port }}"
           zmf_user: "{{ zmf_user }}"
           zmf_password: "{{ zmf_password }}"
           console_cmd: "start pegasus"
           console_system: "{{ inventory_hostname }}"
           # console_cmdresponse_keyword: "SLP registration initiated"
           # console_cmdresponse_reg: "N" # Whether console_cmdresponse_keyword represents a regular expression. Default is 'N'
           # console_broadcastmsg_keyword: "started CIM server"
           # console_broadcastmsg_reg: "N" # Whether console_broadcastmsg_keyword represents a regular expression. Default is 'N'
           # console_broadcastmsg_detect_timeout: 30 # How long, in seconds, the console attempts to detect the value of console_broadcastmsg_keyword in the broadcast messages. Default is 30
           # console_cmdresponse_retrieve_times: 1 # How many times the console attempts to retrieve the command response. Default is 1
         register: result
         delegate_to: localhost
       - debug: var=result

.. note::

  To run the sample playbook, below preparation works are required:
   
  * In the inventory file `hosts`_, the nickname ``consoleHost1`` for the target z/OS system, which is configured as managed node, indicates the system in the same sysplex that the command is routed to. You can modify it to refer to your own z/OS system. You need to ensure the z/OS system ``consoleHost1`` or your own z/OS system is configured in **z/OSMF Systems** plugin.

For more details about module variables, see `zmf_console_command`_.


.. _Playbook Documentation:
   ../playbooks.html
.. _sample playbook:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_module_console_command.yml
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _zmf_console_command:
   ../modules/zmf_console_command.html