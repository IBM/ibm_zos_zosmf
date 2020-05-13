.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Quickstart
==========

Access Collection
-----------------

After **IBM z/OSMF collection** is installed following the section `Installation`_, you can access the collection content for a playbook by referencing the namespace ``ibm`` and collection's fully qualified name ``ibm_zos_zosmf``, for example:

.. code-block:: yaml

   - hosts: all
     tasks:
       - ibm.ibm_zos_zosmf.zmf_workflow:

In Ansible 2.9, the ``collections`` keyword was added and reduces the need to refer to the collection repeatedly, for example:

.. code-block:: yaml

    - hosts: all
      collections:
        - ibm.ibm_zos_zosmf
      tasks:
        - zmf_workflow:

.. code-block:: yaml

    - hosts: all
      collections:
        - ibm.ibm_zos_zosmf
      tasks:
        - include_role:
            name: zmf_workflow_complete

Contents
--------

.. toctree::
   :maxdepth: 3
   :glob:

   README_workflow
   README_cpm
   README_job



.. _Installation:
   installation.html