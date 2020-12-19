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

   collections_paths = ~/.ansible/collections:/usr/share/ansible/collections

For more information about available configurations for ``ansible.cfg``, see `Ansible Configuration Settings`_.

Inventory
---------

Ansible works with multiple managed nodes (hosts) at the same time, using a list or group of lists know as an `inventory`_. Once the inventory is defined, you can use `patterns`_ to select the hosts, or groups, you want Ansible to run against.

Included in the `playbooks directory`_ is a sample inventory file `hosts`_ that with little modification can be used to manage the target z/OS systems. This inventory file should be included when running the sample playbook.

.. code-block:: yaml

   [workflow]
   workflowHost1
   workflowHost2

   [cpm]
   cpmHost1 zmf_host=zosmf1.ibm.com zmf_port=443
   cpmHost2 zmf_host=zosmf2.ibm.com zmf_port=443

   [job]
   jobHost1 zmf_host=zosmf1.ibm.com zmf_port=443
   jobHost2 zmf_host=zosmf2.ibm.com zmf_port=443

   [console]
   consoleHost1
   consoleHost2

   [dataset]
   datasetHost1 zmf_host=zosmf1.ibm.com zmf_port=443
   datasetHost2 zmf_host=zosmf2.ibm.com zmf_port=443

   [file]
   fileHost1 zmf_host=zosmf1.ibm.com zmf_port=443
   fileHost2 zmf_host=zosmf2.ibm.com zmf_port=443


* **workflow**: Host grouping for z/OSMF Workflows.

   * **workflowHost1**: Nickname for the target z/OS system. You can modify it to refer to your own z/OS system. It is configured in **z/OSMF Systems** plugin.

* **cpm**: Host grouping for Cloud Provisioning & Management (CP&M).

   * **cpmHost1**: Nickname for the target z/OS system. You can modify it to refer to your own z/OS system. When the nickname is modified, make sure host specific variables file is defined as described in `Host Vars`_.

   * **zmf_host**: The value of this property identifies the hostname of the z/OS system on which z/OSMF server is running on. For example: ``zmf_host=pev076.pok.ibm.com``.

   * **zmf_port**: The value of this property identifies the port number of z/OSMF server.

* **job**: Host grouping for z/OS Jobs.

   * **jobHost1**: Nickname for the target z/OS system. You can modify it to refer to your own z/OS system. When the nickname is modified, make sure host specific variables file is defined as described in `Host Vars`_.

   * **zmf_host**: The value of this property identifies the hostname of the z/OS system on which z/OSMF server is running on. For example: ``zmf_host=pev076.pok.ibm.com``.

   * **zmf_port**: The value of this property identifies the port number of z/OSMF server.

* **console**: Host grouping for z/OS Consoles.

   * **consoleHost1**: Nickname for the target z/OS system. You can modify it to refer to your own z/OS system. It is configured in **z/OSMF Systems** plugin.

* **dataset**: Host grouping for z/OS Data Sets.

   * **datasetHost1**: Nickname for the target z/OS system. You can modify it to refer to your own z/OS system. When the nickname is modified, make sure host specific variables file is defined as described in `Host Vars`_.

   * **zmf_host**: The value of this property identifies the hostname of the z/OS system on which z/OSMF server is running on. For example: ``zmf_host=pev076.pok.ibm.com``.

   * **zmf_port**: The value of this property identifies the port number of z/OSMF server.

* **file**: Host grouping for z/OS USS File.

   * **datasetHost1**: Nickname for the target z/OS system. You can modify it to refer to your own z/OS system. When the nickname is modified, make sure host specific variables file is defined as described in `Host Vars`_.

   * **zmf_host**: The value of this property identifies the hostname of the z/OS system on which z/OSMF server is running on. For example: ``zmf_host=pev076.pok.ibm.com``.

   * **zmf_port**: The value of this property identifies the port number of z/OSMF server.

Host Vars
---------

You can supply host variables in either the inventory file or the separate variable file. Storing separate host and group variables files may help you organize your variable values more easily.

Included in the `playbooks directory`_ is some sample variables files in the directory `host_vars`_.

* `cpmHost1.yml`_: It contains the variables for host ``cpmHost1`` in group ``cpm``:

   .. code-block:: yaml

      instance_record_dir: "/tmp"
      api_polling_retry_count: 50
      api_polling_interval_seconds: 10

   * **instance_record_dir**: The value of this property identifies the file path in local system where the provision result (in json) will be stored.
     
   * **api_polling_retry_count**: The value of this property identifies max times of status polling before task fail and exit.

   * **api_polling_interval_seconds**: The value of this property identifies interval in seconds between each *api_polling_retry_count* polling.

* `jobHost1.yml`_: It contains the variables for host ``jobHost1`` in group ``job``:

   .. code-block:: yaml

      # zmf_user:
      # zmf_password:
      # zmf_crt:
      # zmf_key:
      job_name: JCLSAMP1
      job_id: JOB00000

   * **zmf_user**: The value of this property identifies the username to be used for authenticating with z/OSMF server.

   * **zmf_password**: The value of this property identifies the password to be used for authenticating with z/OSMF server.

   * **zmf_crt**: The value of this property identifies the location of the PEM-formatted certificate chain file to be used for HTTPS client authentication with z/OSMF server.

   * **zmf_key**: The value of this property identifies the location of the PEM-formatted file with private key to be used for HTTPS client authentication with z/OSMF server.

   * **job_name**: The value of this property identifies the job name to be used for role ``zmf_job_query`` to query a job running on different z/OS.
  
   * **job_id**: The value of this property identifies the job ID to be used for role ``zmf_job_query`` to query a job running on different z/OS.

* `datasetHost1.yml`_: It contains the variables for host ``datasetHost1`` in group ``dataset``:

   .. code-block:: yaml

      # zmf_user:
      # zmf_password:
      # zmf_crt:
      # zmf_key:

   * **zmf_user**: The value of this property identifies the username to be used for authenticating with z/OSMF server.

   * **zmf_password**: The value of this property identifies the password to be used for authenticating with z/OSMF server.

   * **zmf_crt**: The value of this property identifies the location of the PEM-formatted certificate chain file to be used for HTTPS client authentication with z/OSMF server.

   * **zmf_key**: The value of this property identifies the location of the PEM-formatted file with private key to be used for HTTPS client authentication with z/OSMF server.

* `fileHost1.yml`_: It contains the variables for host ``fileHost1`` in group ``file``:

   .. code-block:: yaml

      # zmf_user:
      # zmf_password:
      # zmf_crt:
      # zmf_key:

   * **zmf_user**: The value of this property identifies the username to be used for authenticating with z/OSMF server.

   * **zmf_password**: The value of this property identifies the password to be used for authenticating with z/OSMF server.

   * **zmf_crt**: The value of this property identifies the location of the PEM-formatted certificate chain file to be used for HTTPS client authentication with z/OSMF server.

   * **zmf_key**: The value of this property identifies the location of the PEM-formatted file with private key to be used for HTTPS client authentication with z/OSMF server.

.. note::
   
   This is an easy example to use username and password for authenticating with z/OSMF server. ``zmf_user`` and ``zmf_password`` will be prompted to input when running the sample playbooks. Actually, client-certificate authorization is recommended. You can use ``zmf_crt`` and ``zmf_key`` to specify the client-certificate authorization. If both methods are specified, the system attempts to use client-certificate authentication.

Group Vars
----------

You can supply group variables in either the inventory file or the separate variable file. Storing separate host and group variables files may help you organize your variable values more easily.

Included in the `playbooks directory`_ is some sample variables files in the directory `group_vars`_.

* `workflow.yml`_: It contains the variables for group ``workflow``:

   .. code-block:: yaml
  
      zmf_host: your.host.name
      zmf_port: port_number
      # zmf_user:
      # zmf_password:
      # zmf_crt:
      # zmf_key:

   * **zmf_host**: The value of this property identifies the hostname of the z/OS system on which z/OSMF server is running on. For example: ``zmf_host=pev076.pok.ibm.com``.

   * **zmf_port**: The value of this property identifies the port number of z/OSMF server.

   * **zmf_user**: The value of this property identifies the username to be used for authenticating with z/OSMF server.

   * **zmf_password**: The value of this property identifies the password to be used for authenticating with z/OSMF server.

   * **zmf_crt**: The value of this property identifies the location of the PEM-formatted certificate chain file to be used for HTTPS client authentication with z/OSMF server.

   * **zmf_key**: The value of this property identifies the location of the PEM-formatted file with private key to be used for HTTPS client authentication with z/OSMF server.

* `console.yml`_: It contains the variables for group ``console``:

   .. code-block:: yaml
  
      zmf_host: your.host.name
      zmf_port: port_number
      # zmf_user:
      # zmf_password:
      # zmf_crt:
      # zmf_key:

   * **zmf_host**: The value of this property identifies the hostname of the z/OS system on which z/OSMF server is running on. For example: ``zmf_host=pev076.pok.ibm.com``.

   * **zmf_port**: The value of this property identifies the port number of z/OSMF server.

   * **zmf_user**: The value of this property identifies the username to be used for authenticating with z/OSMF server.

   * **zmf_password**: The value of this property identifies the password to be used for authenticating with z/OSMF server.

   * **zmf_crt**: The value of this property identifies the location of the PEM-formatted certificate chain file to be used for HTTPS client authentication with z/OSMF server.

   * **zmf_key**: The value of this property identifies the location of the PEM-formatted file with private key to be used for HTTPS client authentication with z/OSMF server.

.. note::
   
   This is an easy example to use username and password for authenticating with z/OSMF server. ``zmf_user`` and ``zmf_password`` will be prompted to input when running the sample playbooks. Actually, client-certificate authorization is recommended. You can use ``zmf_crt`` and ``zmf_key`` to specify the client-certificate authorization. If both methods are specified, the system attempts to use client-certificate authentication.

Sample Playbooks
----------------

.. toctree::
   :maxdepth: 1
   :glob:

   playbooks/sample_module_workflow
   playbooks/sample_role_workflow_complete
   playbooks/sample_role_cpm_manage_instance
   playbooks/sample_role_cpm_provision
   playbooks/sample_role_cpm_remove_instance
   playbooks/sample_role_deploy_cics_application
   playbooks/sample_role_job_complete
   playbooks/sample_role_job_query
   playbooks/sample_module_console_command
   playbooks/sample_module_dataset_fetch
   playbooks/sample_module_file_fetch

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
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/
.. _Installation:
   installation.html
.. _ansible.cfg:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/ansible.cfg
.. _Ansible Configuration Settings:
   https://docs.ansible.com/ansible/latest/reference_appendices/config.html#ansible-configuration-settings-locations
.. _inventory:
   https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html
.. _patterns:
   https://docs.ansible.com/ansible/latest/user_guide/intro_patterns.html#intro-patterns
.. _Host Vars:
   #host-vars
.. _hosts:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/hosts
.. _host_vars:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/host_vars/
.. _group_vars:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/group_vars/
.. _workflow.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/group_vars/workflow.yml
.. _console.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/group_vars/console.yml
.. _cpmHost1.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/host_vars/cpmHost1.yml
.. _jobHost1.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/host_vars/jobHost1.yml
.. _datasetHost1.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/host_vars/datasetHost1.yml
.. _fileHost1.yml:
   https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/host_vars/fileHost1.yml
.. _ansible-playbook:
   https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html
