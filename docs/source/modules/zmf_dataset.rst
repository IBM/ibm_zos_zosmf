
:github_url: https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/zmf_dataset.py

.. _zmf_dataset_module:


zmf_dataset -- Manage z/OS data set or member
=============================================



.. contents::
   :local:
   :depth: 1
   

Synopsis
--------
- Create, delete and operate on a sequential or partitioned data set, or a member of partitioned data set (PDS or PDSE) on the remote z/OS system.
- The available operations include rename data set or member, migrate data set and recall the migrated data set.
- When forcing data set replacement, contents will not be preserved.





Parameters
----------


 
     
dataset_create
  Specifies the attributes to be used to create a sequential or partitioned data set.

  This variable only take effects when *dataset_state=present*.

  This variable only take effects when *dataset_type=PS* or *dataset_type=PDS* or *dataset_type=PDSE*.

  If both *dataset_create* and *dataset_model* are supplied, *dataset_model* is ignored.


  | **required**: False
  | **type**: dict


 
     
  alcunit
    Specifies the unit (tracks, blocks or cylinders) in which primary and secondary space allocations are to be obtained.


    | **required**: False
    | **type**: str
    | **default**: TRK
    | **choices**: TRK, BLK, CYL


 
     
  avgblk
    Specifies the average block size.


    | **required**: False
    | **type**: int


 
     
  blksize
    Specifies the maximum length of a block.


    | **required**: False
    | **type**: int


 
     
  dataclass
    Specifies the data class for an SMS-managed data set.


    | **required**: False
    | **type**: str


 
     
  dirblk
    Specifies the number of directory blocks.


    | **required**: False
    | **type**: int


 
     
  lrecl
    Specifies the length, in bytes, of each record in the data set.

    If the records are of variable-length or undefined-length, the maximum record length must be specified.


    | **required**: False
    | **type**: int
    | **default**: 80


 
     
  mgntclass
    Specifies the management class for an SMS-managed data set.


    | **required**: False
    | **type**: str


 
     
  primary
    Specifies the primary space allocation for the data set.


    | **required**: True
    | **type**: int


 
     
  recfm
    Specifies the characteristics of the records in the data set as fixed length (F), variable-length (V), ASCII variable-length (D), or undefined-length (U). Blocked records are specified as FB, VB, or DB. Spanned records are specified as VS, VBS, FS, FBS, DS, or DBS.



    | **required**: False
    | **type**: str
    | **default**: FB
    | **choices**: FB, VB, DB, F, V, D, U, VS, VBS, FS, FBS, DS, DBS


 
     
  secondary
    Specifies the secondary space allocation for the data set.

    If this value is omitted, the secondary space will be specified as 0.5 times of the primary space when *dataset_type=PS*, or as 0.2 times of the primary space when *dataset_type=PDS* or *dataset_type=PDSE*.



    | **required**: False
    | **type**: int


 
     
  storclass
    Specifies the storage class for an SMS-managed data set.


    | **required**: False
    | **type**: str


 
     
  unit
    Specifies the storage unit device type.


    | **required**: False
    | **type**: str
    | **default**: 3390



 
     
dataset_migrate_recall
  Specifies how a migrated data set is handled when *dataset_state=present*.

  If *dataset_migrate_recall=wait*, the migrated data set is recalled synchronously.

  If *dataset_migrate_recall=nowait*, request the migrated data set to be recalled, but do not wait.

  If *dataset_migrate_recall=error*, do not attempt to recall the migrated data set.

  Specifies whether wait for the completion of the request when *dataset_state=migrated* or *dataset_state=recalled*.

  If *dataset_migrate_recall=wait*, wait for the completion of the request.

  If *dataset_migrate_recall=nowait*, the request is queued.

  *dataset_migrate_recall=error* is invalid when *dataset_state=migrated* or *dataset_state=recalled*.


  | **required**: False
  | **type**: str
  | **default**: wait
  | **choices**: wait, nowait, error


 
     
dataset_model
  Specifies the model data set to be used to create a sequential or partitioned data set.

  For example, specifying a model data set like ``ZOSMF.ANSIBLE.MODEL``, member name should not be provided in this variable.

  This variable only take effects when *dataset_state=present*.

  This variable only take effects when *dataset_type=PS* or *dataset_type=PDS* or *dataset_type=PDSE*.

  If both *dataset_create* and *dataset_model* are supplied, *dataset_model* is ignored.


  | **required**: False
  | **type**: str


 
     
dataset_name
  Name of the data set or member being managed.

  This variable must consist of a fully qualified data set name. The length of the data set name cannot exceed 44 characters.

  For example, specifying a data set like ``ZOSMF.ANSIBLE.PS``, or a PDS or PDSE member like ``ZOSMF.ANSIBLE.PDS(MEMBER)``.


  | **required**: True
  | **type**: str


 
     
dataset_rename
  Specifies the new name of the data set or member.

  This variable only take effects when *dataset_state=present*.


  | **required**: False
  | **type**: str


 
     
dataset_replace
  Specifies whether the existing data set or member matching *dataset_name* will be replaced when *dataset_state=present*.

  If *dataset_replace=true*, the existing data set will be deleted, a new data set with the same name and desired attributes will be created.

  If *dataset_replace=true*, all data in the original data set will be lost.

  If *dataset_replace=true*, no data set will exist if creation of the new data set fails.

  This variable only take effects when *dataset_state=present*.


  | **required**: False
  | **type**: bool
  | **default**: false


 
     
dataset_state
  The final state desired for specified data set or member.

  If *dataset_state=present* and *dataset_name* does not exist, *dataset_name* is created, the module completes successfully with ``changed=True``.


  If *dataset_state=present* and *dataset_name* exists, when *dataset_replace=true*, the existing data set is deleted, and a new data set is created with the same name and desired attributes, the module completes successfully with ``changed=True``.


  If *dataset_state=present* and *dataset_name* exists, when *dataset_replace=false*, no action taken, the module completes successfully with ``changed=False``.


  If *dataset_state=absent* and *dataset_name* does not exist, no action taken, the module completes successfully with ``changed=False``.


  If *dataset_state=absent* and *dataset_name* exists, the existing *dataset_name* is deleted, the module completes successfully with ``changed=True``.


  If *dataset_state=migrated*, the existing *dataset_name* is migrated, the module completes successfully with ``changed=True``.


  If *dataset_state=recalled*, the migrated *dataset_name* is recalled, the module completes successfully with ``changed=True``.



  | **required**: True
  | **type**: str
  | **choices**: present, absent, migrated, recalled


 
     
dataset_type
  The type to be used when creating a data set or member.

  When *dataset_type=MEMBER*, *dataset_name* should be a member of an existing partitioned data set.

  This variable only take effects when *dataset_state=present*.


  | **required**: False
  | **type**: str
  | **default**: PS
  | **choices**: PS, PDS, PDSE, MEMBER


 
     
dataset_volser
  The volume serial to identify the volume to be searched for an uncataloged data set or member.

  The length of the volume serial cannot exceed six characters. Wildcard characters are not supported. Indirect volume serials are not supported.

  When creating a sequential or partitioned data set, this variable specifies the name of the disk volume on which the data set resides. This value is not specified for an SMS-managed data set.



  | **required**: False
  | **type**: str


 
     
zmf_credential
  Authentication credentials, returned by module ``zmf_authenticate``, for the successful authentication with z/OSMF server.

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

   
   - name: Create a sequential data set ZOSMF.ANSIBLE.PS if it does not exist
     zmf_dataset:
       zmf_host: "sample.ibm.com"
       dataset_name: "ZOSMF.ANSIBLE.PS"
       dataset_state: "present"
       dataset_type: "PS"
       dataset_create:
         primary: 10

   - name: Create a sequential data set ZOSMF.ANSIBLE.PS depending on the model data set ZOSMF.ANSIBLE.MODEL
     zmf_dataset:
       zmf_host: "sample.ibm.com"
       dataset_name: "ZOSMF.ANSIBLE.PS"
       dataset_state: "present"
       dataset_type: "PS"
       dataset_model: "ZOSMF.ANSIBLE.MODEL"

   - name: Replace a partitioned data set ZOSMF.ANSIBLE.PDS if it exists
     zmf_dataset:
       zmf_host: "sample.ibm.com"
       dataset_name: "ZOSMF.ANSIBLE.PDS"
       dataset_state: "present"
       dataset_type: "PDS"
       dataset_replace: true
       dataset_create:
         primary: 10

   - name: Create a data set member ZOSMF.ANSIBLE.PDS(MEMBER) to an existing PDS, replace if member exists
     zmf_dataset:
       zmf_host: "sample.ibm.com"
       dataset_name: "ZOSMF.ANSIBLE.PDS(MEMBER)"
       dataset_state: "present"
       dataset_type: "MEMBER"
       dataset_replace: true

   - name: Rename a data set ZOSMF.ANSIBLE.PS to ZOSMF.ANSIBLE.PS01
     zmf_dataset:
       zmf_host: "sample.ibm.com"
       dataset_name: "ZOSMF.ANSIBLE.PS"
       dataset_state: "present"
       dataset_type: "PS"
       dataset_rename: "ZOSMF.ANSIBLE.PS01"

   - name: Rename a data set member ZOSMF.ANSIBLE.PDS(MEMBER) to ZOSMF.ANSIBLE.PDS(MEMBER01)
     zmf_dataset:
       zmf_host: "sample.ibm.com"
       dataset_name: "ZOSMF.ANSIBLE.PDS(MEMBER)"
       dataset_state: "present"
       dataset_type: "MEMBER"
       dataset_rename: "ZOSMF.ANSIBLE.PDS(MEMBER01)"

   - name: Delete a data set ZOSMF.ANSIBLE.PS
     zmf_dataset:
       zmf_host: "sample.ibm.com"
       dataset_name: "ZOSMF.ANSIBLE.PS"
       dataset_state: "absent"

   - name: Migrate a data set ZOSMF.ANSIBLE.PS
     zmf_dataset:
       zmf_host: "sample.ibm.com"
       dataset_name: "ZOSMF.ANSIBLE.PS"
       dataset_state: "migrated"

   - name: Recall a data set ZOSMF.ANSIBLE.PS and wait for the completion of the request
     zmf_dataset:
       zmf_host: "sample.ibm.com"
       dataset_name: "ZOSMF.ANSIBLE.PS"
       dataset_state: "recalled"
       dataset_migrate_recall: "wait"










Return Values
-------------

   
      
   changed
        Indicates if any change is made during the module operation.


        | **returned**: always 
        | **type**: bool


   
      
   message
        The output message generated by the module to indicate whether the data set or member is successfully created, deleted, or updated.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "The data set ZOSMF.ANSIBLE.PS is created successfully."

                  "The data set member ZOSMF.ANSIBLE.PDS(MEMBER) is deleted successfully."

                  "The data set ZOSMF.ANSIBLE.PS does not exist."

                  "The data set member ZOSMF.ANSIBLE.PDS(MEMBER) already exists."

                  "The data set ZOSMF.ANSIBLE.PS is successfully renamed to /ZOSMF.ANSIBLE.PS01."

                  "The data set ZOSMF.ANSIBLE.PS is migrated successfully."

                  "The data set ZOSMF.ANSIBLE.PS is recalled successfully."



   
      
   dataset_properties
        The properties of the present data set.


        | **returned**: on success 
        | **type**: dict

        **sample**: ::

                  {"blksz": "80", "catnm": "CATALOG.SVPLEX.MASTER", "cdate": "2021/01/21", "dev": "3390", "dsname": "ZOSMF.ANSIBLE.PS", "dsorg": "PS", "edate": "None", "extx": "1", "lrecl": "80", "migr": "NO", "mvol": "N", "ovf": "NO", "rdate": "2021/01/25", "recfm": "FB", "sizex": "4", "spacu": "TRACKS", "used": "0", "vol": "VOL001", "vols": "VOL001"}


   
      
   member_properties
        The properties of the present member.


        | **returned**: on success 
        | **type**: dict

        **sample**: ::

                  {"c4date": "2021/01/21", "cnorc": 2, "inorc": 0, "m4date": "2021/01/21", "member": "MEMBER", "mnorc": 0, "mod": 2, "msec": "42", "mtime": "02:51", "sclm": "N", "user": "IBMUSER", "vers": 1}



