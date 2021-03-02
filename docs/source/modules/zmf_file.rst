
:github_url: https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/zmf_file.py

.. _zmf_file_module:


zmf_file -- Manage z/OS USS file or directory
=============================================



.. contents::
   :local:
   :depth: 1
   

Synopsis
--------
- Create, delete and operate on a z/OS UNIX System Services (USS) file or a directory on the remote z/OS system.
- The available operations include rename, change mode, change owner and change tag.





Parameters
----------


 
     
file_mode
  Specifies the permission the resulting USS file or directory should have.

  This variable only take effects when *file_state=file* or *file_state=directory*.

  If *file_path* does not exist, this value is used in creating *file_path*. If this value is omitted, 755 is used by default.

  If *file_path* exists, this value is used in changing mode of *file_path*.


  | **required**: False
  | **type**: dict


 
     
  mode
    The value of file mode bits.

    This value could be either the POSIX symbolic form (e.g., ``RWXRW-RW-``) or octal value (e.g., ``755``).


    | **required**: True
    | **type**: str


 
     
  recursive
    This variable only take effects when *file_state=directory*.

    When *recursive=true*, the file mode bits of the directory and all files in the file hierarchy below it are changed (chmod -R).


    | **required**: False
    | **type**: bool
    | **default**: false



 
     
file_owner
  Indicates the function change owner.

  This variable only take effects when *file_state=file* or *file_state=directory*.


  | **required**: False
  | **type**: dict


 
     
  group
    The group ID or GID.


    | **required**: False
    | **type**: str


 
     
  owner
    The user ID or UID.


    | **required**: True
    | **type**: str


 
     
  recursive
    This variable only take effects when *file_state=directory*.

    When *recursive=true*, changes all the files and subdirectories in that directory to belong to the specified owner and group (chown -R).


    | **required**: False
    | **type**: bool
    | **default**: false



 
     
file_path
  Path to the USS file or directory being managed.

  This variable must consist of a fully qualified path and file or directory name. For example, ``/etc/profile``.

  The module will fail if parent directory of *file_path* does not exist or is a read-only file system.


  | **required**: True
  | **type**: str


 
     
file_rename
  Specifies the new name of the USS file or directory.

  This variable only take effects when *file_state=file* or *file_state=directory*.


  | **required**: False
  | **type**: str


 
     
file_state
  The final state desired for specified USS file or directory.

  If *file_state=file* and *file_path* does not exist, *file_path* is created as a USS file, the module completes successfully with ``changed=True``.


  If *file_state=directory* and *file_path* does not exist, *file_path* is created as a directory, the module completes successfully with ``changed=True``.


  If *file_state=file* or *file_state=directory*, and *file_path* exists, *file_path* is modified with other supplied variables (e.g., *file_mode*), the module completes successfully with ``changed=True``.


  If *file_state=file* or *file_state=directory*, and *file_path* exists, no action taken if no other variables are supplied (e.g., *file_mode*), the module completes successfully with ``changed=False``.


  If *file_state=absent* and *file_path* does not exist, no action taken, the module completes successfully with ``changed=False``.


  If *file_state=absent* and *file_path* exists, the existing *file_path* is deleted, the module completes successfully with ``changed=True``.



  | **required**: True
  | **type**: str
  | **choices**: file, directory, absent


 
     
file_tag
  Indicates the function change tag.

  This variable only take effects when *file_state=file* or *file_state=directory*.


  | **required**: False
  | **type**: dict


 
     
  codeset
    Specifies the coded character set in which text data is encoded, such as ASCII or EBCDIC.

    For example, the code set for ASCII is ISO8859–1; the code set for EBCDIC is IBM-1047.

    This variable only take effects when *tag=mixed* or *tag=text*.

    This variable is required when *tag=text*.


    | **required**: False
    | **type**: str


 
     
  recursive
    This variable only take effects when *file_state=directory*.

    When *recursive=true*, tags all the files and subdirectories in that directory (chtag -R).


    | **required**: False
    | **type**: bool
    | **default**: false


 
     
  tag
    The type of file tag.

    If *tag=absent*, any existing file tag is removed.


    | **required**: True
    | **type**: str
    | **choices**: mixed, text, binary, absent



 
     
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

   
   - name: Create a USS file /etc/profile with default mode 755
     zmf_file:
       zmf_host: "sample.ibm.com"
       file_path: "/etc/profile"
       file_state: "file"

   - name: Create a directory /etc/some_directory with mode 644
     zmf_file:
       zmf_host: "sample.ibm.com"
       file_path: "/etc/some_directory"
       file_state: "directory"
       file_mode:
           mode: "644"

   - name: Change the permissions, owner, group and tag of a USS file /etc/profile
     zmf_file:
       zmf_host: "sample.ibm.com"
       file_path: "/etc/profile"
       file_state: "file"
       file_mode:
           mode: "644"
       file_owner:
           owner: "500000"
           group: "0"
       file_tag:
           tag: "text"
           codeset: "IBM-1047"

   - name: Change the permissions of a directory /etc/some_directory, and recursively change its owner, group and tag
     zmf_file:
       zmf_host: "sample.ibm.com"
       file_path: "/etc/some_directory"
       file_state: "directory"
       file_mode:
           mode: "644"
           recursive: false
       file_owner:
           owner: "500000"
           group: "0"
           recursive: true
       file_tag:
           tag: "text"
           codeset: "IBM-1047"
           recursive: true

   - name: Rename a USS file /etc/profile to /etc/profile.bak
     zmf_file:
       zmf_host: "sample.ibm.com"
       file_path: "/etc/profile"
       file_state: "file"
       file_rename: "/etc/profile.bak"

   - name: Delete a USS file /etc/profile
     zmf_file:
       zmf_host: "sample.ibm.com"
       file_path: "/etc/profile"
       file_state: "absent"










Return Values
-------------

   
      
   changed
        Indicates if any change is made during the module operation.


        | **returned**: always 
        | **type**: bool


   
      
   message
        The output message generated by the module to indicate whether the USS file or directory is successfully created, deleted, or updated.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "The file /etc/profile is created successfully."

                  "The directory /etc/some_directory is deleted successfully."

                  "The file or directory /etc/profile does not exist."

                  "The file /etc/profile already exists."

                  "The file /etc/profile is updated successfully."

                  "The file /etc/profile is successfully renamed to /etc/profile.bak."



   
      
   file_properties
        The properties of the present USS file or directory.


        | **returned**: on success 
        | **type**: dict

        **sample**: ::

                  {"gid": 0, "group": "OPERATOR", "mode": "-rwxr-xr-x", "mtime": "2021-01-21T01:24:04", "name": "profile", "size": 0, "tag": "t IBM-1047    T=on  /etc/profile", "uid": 500000, "user": "IBMUSER"}



