.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Playbooks
=========

An `Ansible Playbook`_ consists of organized instructions that define work for a managed node (hosts) to be managed with Ansible.

Playbook Documentation
----------------------

**IBM z/OSMF collection** provides a `playbooks directory`_, which contains various sample playbooks to demonstrate the use of modules and roles. 

You can find the playbook content that is included with the collection where the collection was installed, please refer back to the section `Installation`_ to obtain the installation path for the collection. In the following examples, this document will refer to the installation path as ``~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf``.

Ansible Config
--------------

Ansible config file ``ansible.cfg`` can override nearly all ``ansible-playbook`` configurations. 

Included in the `playbooks directory`_ is a sample `ansible.cfg`_ that with little modification can supplement ``ansible-playbook``.

You can modify the following configuration statement to refer to your own installation path for the collection:

.. code-block:: yaml

   collections_paths = ../../../../../collections

For more information about available configurations for ``ansible.cfg``, see `Ansible Configuration Settings`_.

Inventory
---------

Ansible works with multiple managed nodes (hosts) at the same time, using a list or group of lists know as an `inventory`_. Once the inventory is defined, you can use `patterns`_ to select the hosts, or groups, you want Ansible to run against.

Included in the `playbooks directory`_ is a sample inventory file `hosts`_ that with little modification can be used to manage the target z/OS systems. This inventory file should be included when running the sample playbook.

.. code-block:: yaml

   [zsystems]
   SY1 ansible_host=hostname_of_zos_system

* **SY1**: Nickname for the target z/OS system. You can modify it to refer to your own z/OS system.
* **ansible_host**: The value of this property is the hostname of the target z/OS system. You can modify it to refer to your own z/OS system, for example: ``ansible_host=pev076.pok.ibm.com``.

Group Vars
----------

You can supply group variables in either the inventory file or the separate variable file. Storing separate host
and group variables files may help you organize your variable values more easily. 

Included in the `playbooks directory`_ is some sample variables files in the directory `group_vars`_.

* `workflow.yml`_: It contains the variables for system group ``workflow``:

  .. code-block:: yaml
  
     zmf_host: your.host.name
     zmf_port: port_number
     # zmf_user:
     # zmf_password:
     # zmf_crt:
     # zmf_key:

  * **zmf_host**: Hostname of the z/OSMF server, for example: ``zmf_host: pev076.pok.ibm.com``
  * **zmf_port**: Port number of the z/OSMF server, for example: ``zmf_port: 443``

  .. note::
     
     This is an easy example to use username and password for authenticating with z/OSMF server. ``zmf_user`` and ``zmf_password`` will be prompted to input when running the sample playbooks. Actually, client-certificate authorization is recommended. You can use ``zmf_crt`` and ``zmf_key`` to specify the certificate chain file and key file to be used for HTTPS client authentication.

* `cpm.yml`_: It contains the variables for system group ``cpm``:

  .. code-block:: yaml

     instance_record_dir: "/tmp"
     api_polling_retry_count: 30
     api_polling_interval_seconds: 10

  * **instance_record_dir**: File path in local system where the provision result (in json) will be stored.
  * **api_polling_retry_count**: Max times of status polling before task fail and exit.
  * **api_polling_interval_seconds**: Interval in seconds between each ``api_polling_retry_count`` polling.

Sample Playbooks
----------------

* `sample_role_workflow_complete.yml`_: This sample playbook shows how to complete a z/OS workflow on the target z/OS systems via z/OSMF. To run the sample playbook, below preparation works are required:
   
   1. In this sample playbook, the workflow definition file `workflow_sample_automation_steps.xml`_ is used to create the workflow instance. You need to manually upload it to the z/OS file system. For example, you can upload it to the directory ``/var/zosmf/workflow_def/``. Then modify the value of variable ``workflow_file`` in the sample playbook to refer to the location of the workflow definition file.
   
   2. In the inventory file, the nickname ``SY1`` for the target z/OS system, which is configured as managed node, is used to create the workflow instance. You can modify it to refer to your own z/OS system. You need to ensure the z/OS system ``SY1`` or your own z/OS system is configured in z/OSMF **Systems** task.

* `sample_role_cpm_manage_instance.yml`_: This sample playbook shows how to perform instance action on a provisioned instance in z/OSMF CP&M.

* `sample_role_cpm_provision.yml`_: This sample playbook shows how to provision an instance in z/OSMF CP&M.

* `sample_role_cpm_remove_instance.yml`_: This sample playbook shows how to remove the deprovisioned instance in z/OSMF CP&M.

* `sample_role_deploy_cics_application.yml`_: This sample playbook shows how to install a web application on a provisioned instance in z/OSMF CP&M. Please copy ``files/role_cics_wlp_install_app`` directory to roles directory before using this example.

.. note::
   
   * For CP&M roles, the inventory file is merely a placeholder for retrieving cpm group variables, you shouldn't need to modify the inventory file or change the host to something else other than ``cpm``.

Run the Playbooks
-----------------

The sample playbooks must be run from the `playbooks directory`_ of the installed collection: ``~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks/``

You can use the `ansible-playbook`_ command to run the sample playbooks as follows:

.. code-block:: sh

   $ ansible-playbook [-i hosts] sample_role_*.yml [-e zmf_user=<username> -e zmf_password=<password>]

To adjust the logging verbosity, include the ``-v`` option with `ansible-playbook`_ command. You can append more letter ``v``'s, for example, ``-v``, ``-vv``, ``-vvv``, or ``-vvvv``, to obtain more details in case a connection failed. Each letter ``v`` increases the logging verbosity similar to the traditional logging levels, such as INFO, WARN, ERROR, or DEBUG.


.. _Ansible Playbook:
   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbooks-intro
.. _playbooks directory:
   https://github.com/ansible-collections/ibm_zos_core/tree/master/playbooks/
.. _Installation:
   installation.html
.. _ansible.cfg:
   https://github.com/ansible-collections/ibm_zos_core/tree/master/playbooks/ansible.cfg
.. _Ansible Configuration Settings:
   https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations
.. _inventory:
   https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html
.. _patterns:
   https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html#intro-patterns
.. _hosts:
   https://github.com/ansible-collections/ibm_zos_core/tree/master/playbooks/hosts
.. _group_vars:
   https://github.com/ansible-collections/ibm_zos_core/tree/master/playbooks/group_vars/
.. _workflow.yml:
   https://github.com/ansible-collections/ibm_zos_core/tree/master/playbooks/group_vars/workflow.yml
.. _cpm.yml:
   https://github.com/ansible-collections/ibm_zos_core/tree/master/playbooks/group_vars/cpm.yml
.. _sample_role_workflow_complete.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_role_workflow_complete.yml
.. _workflow_sample_automation_steps.xml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/files/workflow_sample_automation_steps.xml
.. _sample_role_cpm_manage_instance.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_role_cpm_manage_instance.yml
.. _sample_role_cpm_provision.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_role_cpm_provision.yml
.. _sample_role_cpm_remove_instance.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_role_cpm_remove_instance.yml
.. _sample_role_deploy_cics_application.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/sample_role_deploy_cics_application.yml
.. _ansible-playbook:
   https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html
