.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Installation
============

**IBM z/OSMF collection** can be installed by several options, including Ansible Galaxy and a local build.

.. **IBM z/OSMF collection** can be installed by several options, including Ansible Galaxy, Ansible Automation Hub, and a local build.

For more information on installing collections, see `Using Collections`_.

Ansible Galaxy
--------------

Galaxy enables to quickly configure the automation project with content from the Ansible community. Galaxy provides prepackaged units of work known as collections.

**IBM z/OSMF collection** is distributed through `Ansible Galaxy Community`_. You can use the `ansible-galaxy`_ command with the option ``install`` to install the collection on your control node, as follows:

.. code-block:: sh

   $ ansible-galaxy collection install ibm.ibm_zos_zosmf

By default, the collection is installed in ``~/.ansible/collections``. The output looks like this:

.. code-block:: sh

   Process install dependency map
   Starting collection install process
   Installing 'ibm.ibm_zos_zosmf:1.0.0' to '/Users/user/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf'

To specify the installation path, include the ``-p`` option with the `ansible-galaxy`_ command:

.. code-block:: sh

   $ ansible-galaxy collection install ibm.ibm_zos_zosmf -p /myAnsible/collections

After installation, the collection content will resemble this hierarchy:

.. code-block:: sh

   ├── collections/
   │  ├── ansible_collections/
   │      ├── ibm/
   │          ├── ibm_zos_zosmf/
   │              ├── docs/
   │              ├── tests/
   │              ├── playbooks/
   │              ├── roles/
   │              ├── plugins/
   │                  ├── module_utils/
   │                  └── modules/

For more information on installing collections with Ansible Galaxy, see `Installing Collections`_.

Local Build
-----------

To build your own collection, you must clone the Git repository, build the collection archive, and install the locally built collection. The ``ansible-galaxy collection build`` command packages the collection into an archive that can later be installed locally without having to use Hub or Galaxy. Then you can use the ``ansible-galaxy collection install`` command to install a collection built from source.

1. Clone the Git repository:

   .. code-block:: sh

      $ git clone git@github.com:ibm/ibm_zos_zosmf.git

   .. note::
      
      * Collection archive names will change depending on the release version.
      
      * They adhere to this convention ``<namespace>-<collection>-<version>.tar.gz``, for example, ``ibm-ibm_zos_zosmf-1.0.0.tar.gz``.

2. Run a local build inside the collection:

   .. code-block:: sh
   
      $ cd ibm_zos_zosmf
      $ ansible-galaxy collection build

   The example output looks like this:

   .. code-block:: sh
   
      Created collection for ibm.ibm_zos_zosmf at /Users/user/git/ibm/ibm_zos_zosmf/ibm-ibm_zos_zosmf-1.0.0.tar.gz

3. Install the locally built collection:

   .. code-block:: sh

      $ ansible-galaxy collection install ibm-ibm_zos_zosmf-1.0.0.tar.gz

   The example output looks like this:
    
   .. code-block:: sh

      Process install dependency map
      Starting collection install process
      Installing 'ibm.ibm_zos_zosmf:1.0.0' to '/Users/user/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf'

   To specify the installation path, include the ``-p`` option with the `ansible-galaxy`_ command:

   .. code-block:: sh

      $ ansible-galaxy collection install ibm-ibm_zos_zosmf-1.0.0.tar.gz -p /myAnsible/collections


.. _Using Collections:
   https://docs.ansible.com/ansible/latest/user_guide/collections_using.html
.. _Ansible Galaxy Community:
   https://galaxy.ansible.com/
.. _ansible-galaxy:
   https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html
.. _Installing Collections:
   https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#installing-collections-with-ansible-galaxy
