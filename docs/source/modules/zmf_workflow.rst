
:github_url: https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/zmf_workflow.py

.. _zmf_workflow_module:


zmf_workflow -- Operate z/OS workflows
======================================



.. contents::
   :local:
   :depth: 1
   

Synopsis
--------
- Operate z/OS workflows by issuing z/OSMF workflow RESTful services.
- This module supports to compare, start, delete and check a workflow.





Parameters
----------


 
     
state
  Final state desired for the specified workflow.

  If *state=existed*, indicate whether a workflow with the given name does not exist, or exists with same or different definition file, variables and properties.


  If *state=started*, create a workflow if it does not exist, and start it.


  If *state=deleted*, delete a workflow if it exists.


  If *state=check*, check the status of a workflow.



  | **required**: True
  | **type**: str
  | **choices**: existed, started, deleted, check


 
     
workflow_access_type
  Access type for the workflow when the workflow is created.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str
  | **default**: Public
  | **choices**: Public, Restricted, Private


 
     
workflow_account_info
  For a workflow that submits a batch job, this variable specifies the account information for the JCL JOB statement.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_assign_to_owner
  Specifies whether the workflow steps are assigned to the workflow owner when the workflow is created.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: bool
  | **default**: True


 
     
workflow_category
  Category for the workflow.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str
  | **choices**: general, configuration


 
     
workflow_comments
  User-specified information to be associated with the workflow at creation time.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_delete_completed_jobs
  For a workflow that submits a batch job, this variable specifies whether the job is deleted from the JES spool after it completes.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: bool


 
     
workflow_file
  Location of the workflow definition file.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_file_system
  Nickname of the system on which the specified workflow definition file and any related files reside.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_host
  Nickname of the target z/OS system on which the workflow is to be performed.

  This variable should be specified as ``{{ inventory_hostname }}``, and its value should be specified in the inventory file as a managed node.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_job_statement
  For a workflow that submits a batch job, this variable specifies the JOB statement JCL for the job.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_key
  Generated key to uniquely identify the workflow instance.

  Either *workflow_name* or *workflow_key* is required when *state=started/deleted/check*.


  | **required**: False
  | **type**: str


 
     
workflow_name
  Descriptive name of the workflow.

  It is recommended that you use the naming rule ``ansible_workflowName_{{ workflow_host }}`` when *state=started*.

  Required when *state=existed*.

  Either *workflow_name* or *workflow_key* is required when *state=started/deleted/check*.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_notification_url
  URL to be used for notification when the workflow is started.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_owner
  User name of the workflow owner.

  If this value is omitted, *zmf_user* is used as workflow owner.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_perform_subsequent
  Specifies whether the subsequent automated steps are performed when the workflow is started.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: bool
  | **default**: True


 
     
workflow_resolve_conflict_by_using
  Specifies how to handle variable conflicts if any are detected at workflow creation time.

  Such conflicts can be found when z/OSMF Workflows task reads the output file from a step that runs a REXX exec or UNIX shell script.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str
  | **default**: outputFileValue
  | **choices**: outputFileValue, existingValue, leaveConflict


 
     
workflow_resolve_global_conflict_by_using
  Version of the variable to be used if the supplied workflow variable conflicts with an existing global variable in z/OSMF Workflows task.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str
  | **default**: global
  | **choices**: global, input


 
     
workflow_step_name
  Name of the workflow step at which automation processing is to begin when the workflow is started.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_vars
  Values of one or more workflow variables in JSON format.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: dict


 
     
workflow_vars_file
  Location of the optional properties file to be used to pre-specify the values of one or more variables that are defined in workflow definition file.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
workflow_vendor
  Name of the vendor that provided the workflow definition file.

  For more information, see the documentation for the z/OSMF workflow REST services.


  | **required**: False
  | **type**: str


 
     
zmf_credential
  Authentication credentials, returned by module ``zmf_authenticate``, for the successfully authentication with z/OSMF server.

  If *zmf_credential* is supplied, *zmf_host*, *zmf_port*, *zmf_user*, *zmf_password*, *zmf_crt* and *zmf_key* are ignored.


  | **required**: False
  | **type**: dict


 
     
  jwtToken
    The value of JSON Web token, which supports strong encryption.

    If *LtpaToken2* is not supplied, *jwtToken* is required.


    | **required**: False
    | **type**: str


 
     
  LtpaToken2
    The value of Lightweight Third Party Access (LTPA) token, which supports strong encryption.

    If *jwtToken* is not supplied, *LtpaToken2* is required.


    | **required**: False
    | **type**: str


 
     
  zmf_host
    Hostname of the z/OSMF server.


    | **required**: True
    | **type**: str


 
     
  zmf_port
    Port number of the z/OSMF server.


    | **required**: False
    | **type**: int



 
     
zmf_crt
  Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication.

  If *zmf_credential* is supplied, *zmf_crt* is ignored.

  If *zmf_credential* is not supplied, *zmf_crt* is required when *zmf_user* and *zmf_password* are not supplied.


  | **required**: False
  | **type**: str


 
     
zmf_host
  Hostname of the z/OSMF server.

  If *zmf_credential* is supplied, *zmf_host* is ignored.

  If *zmf_credential* is not supplied, *zmf_host* is required.


  | **required**: False
  | **type**: str


 
     
zmf_key
  Location of the PEM-formatted file with your private key to be used for HTTPS client authentication.

  If *zmf_credential* is supplied, *zmf_key* is ignored.

  If *zmf_credential* is not supplied, *zmf_key* is required when *zmf_user* and *zmf_password* are not supplied.


  | **required**: False
  | **type**: str


 
     
zmf_password
  Password to be used for authenticating with z/OSMF server.

  If *zmf_credential* is supplied, *zmf_password* is ignored.

  If *zmf_credential* is not supplied, *zmf_password* is required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_credential* is not supplied and *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 
     
zmf_port
  Port number of the z/OSMF server.

  If *zmf_credential* is supplied, *zmf_port* is ignored.


  | **required**: False
  | **type**: int


 
     
zmf_user
  User name to be used for authenticating with z/OSMF server.

  If *zmf_credential* is supplied, *zmf_user* is ignored.

  If *zmf_credential* is not supplied, *zmf_user* is required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_credential* is not supplied and *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Compare whether a workflow with the given name already exists and has the same definition file, variables and properties
     zmf_workflow:
       state: "existed"
       zmf_host: "sample.ibm.com"
       workflow_name: "ansible_sample_workflow_SY1"
       workflow_file: "/var/zosmf/workflow_def/workflow_sample_automation_steps.xml"
       workflow_host: "SY1"

   - name: Create a workflow if it does not exist, and start it
     zmf_workflow:
       state: "started"
       zmf_host: "sample.ibm.com"
       workflow_name: "ansible_sample_workflow_{{ inventory_hostname }}"
       workflow_file: "/var/zosmf/workflow_def/workflow_sample_automation_steps.xml"
       workflow_host: "{{ inventory_hostname }}"

   - name: Delete a workflow if it exists
     zmf_workflow:
       state: "deleted"
       zmf_host: "sample.ibm.com"
       workflow_name: "ansible_sample_workflow_SY1"

   - name: Check the status of a workflow
     zmf_workflow:
       state: "check"
       zmf_host: "sample.ibm.com"
       workflow_name: "ansible_sample_workflow_SY1"










Return Values
-------------

   
      
   changed
        Indicates if any change is made during the module operation.

        If `state=existed/check`, always return false.

        If `state=started` and the workflow is started, return true.

        If `state=deleted` and the workflow is deleted, return true.


        | **returned**: always 
        | **type**: bool


   
      
   message
        The output message generated by the module.

        If `state=existed`, indicate whether a workflow with the given name does not exist, or exists with same or different definition file, variables and properties.

        If `state=started`, indicate whether the workflow is started.

        If `state=deleted`, indicate whether the workflow to be deleted does not exist or is deleted.

        If `state=check`, indicate whether the workflow is completed, is not completed, or is still in progress.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "Workflow instance named: ansible_sample_workflow_SY1 with same definition file, variables and properties is found."

                  "Workflow instance named: ansible_sample_workflow_SY1 with different definition file is found."

                  "Workflow instance named: ansible_sample_workflow_SY1 is started, you can use state=check to check its final status."

                  "Workflow instance named: ansible_sample_workflow_SY1 is still in progress."

                  "Workflow instance named: ansible_sample_workflow_SY1 is completed"

                  "Workflow instance named: ansible_sample_workflow_SY1 is deleted."

                  "Workflow instance named: ansible_sample_workflow_SY1 does not exist."



   
      
   workflow_key
        Generated key to uniquely identify the existing or started workflow.


        | **returned**: on success when `state=existed/started` 
        | **type**: str

        **sample**: ::

                  "2535b19e-a8c3-4a52-9d77-e30bb920f912"



   
      
   same_workflow_instance
        Indicate whether the existing workflow has the same or different definition file, variables and properties.


        | **returned**: on success when `state=existed` 
        | **type**: bool


   
      
   waiting
        Indicate whether it needs to wait and check again because the workflow is still in progress.


        | **returned**: on success when `state=check` 
        | **type**: bool


   
      
   completed
        Indicate whether the workflow is completed.


        | **returned**: on success when `state=existed/check` 
        | **type**: bool


   
      
   deleted
        Indicate whether the workflow is deleted.


        | **returned**: on success when `state=deleted` 
        | **type**: bool



