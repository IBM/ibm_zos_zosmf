.. ...........................................................................
.. Copyright (c) IBM Corporation 2020                                        .
.. ...........................................................................

Operate z/OS Workflows
======================

**IBM z/OSMF collection** provides capabilities to work with z/OS workflows using Ansible playbooks. There is a module as well as a role provided to interact with z/OSMF Workflows. The module uses z/OSMF workflow RESTful services to operate workflows, based on the different parameters it receives. The module provides the following final states: existed, started, deleted and check. The role is used for completing a workflow, either forcibly or idempotently.

.. note::
   
   * **Naming Rule**: It is recommended that you use the naming rule ``ansible_${workflow_name}_${zos_system_nickname}`` when you create a workflow instance.

   * **Automated Step**: Only automated steps are supported when a workflow is started.

   * **Idempotent**: The module is considered to be "weakly" idempotent. That is, the module achieves an idempotent result for the final state of the workflow instance, rather than for the target z/OS systems. A strong idempotent result for the final state of the target z/OS systems depends on the idempotency of the workflow instance steps.

   * **Check Mode**: The module does not support check mode.

Modules
-------

* `zmf_workflow`_:
   
   This module supports the following final states for working with z/OS workflows:

   * **existed**: Indicate whether a workflow instance with the given name already exists in the z/OSMF server and has the same definition file, variables and properties.

   * **started**: Create the workflow instance if it does not exist in the z/OSMF server and start it on each of the target z/OS systems.

   * **deleted**: Delete the workflow instance from the z/OSMF server.

   * **check**: Check the status of the workflow instance in the z/OSMF server.

Roles
-----

* `zmf_workflow_complete`_:

   This role is used for completing a z/OS workflow, either forcibly or idempotently:

   * **forcibly (force_complete: True)**: Delete the workflow instance if it exists in the z/OSMF server. Create a new workflow instance and start it on each of the target z/OS systems. Periodically check the workflow status and return the final result when the workflow stops running.

   * **idempotently (force_complete: False)**: Create the workflow instance if it does not exist in the z/OSMF server. Start the workflow on each of the target z/OS systems. Periodically check the workflow status and return the final result when the workflow stops running.

Requirements
------------

See the section `Requirements`_.

Sample Playbooks
----------------

See the section `Playbooks`_.


.. _zmf_workflow:
   modules/zmf_workflow.html
.. _zmf_workflow_complete:
   roles/README_zmf_workflow_complete.html
.. _Requirements:
   requirements_workflow.html
.. _Playbooks:
   playbooks.html