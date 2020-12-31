
:github_url: https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/zmf_dataset_copy.py

.. _zmf_dataset_copy_module:


zmf_dataset_copy -- Copy data to z/OS data set or member
========================================================



.. contents::
   :local:
   :depth: 1
   

Synopsis
--------
- Copy data from Ansible control node to a sequential data set, or a member of a partitioned data set (PDS or PDSE) on the remote z/OS system.
- If the target data set or member already exists, it can be overwritten. If the target PDS or PDSE member does not exist, it can be created.
- If the target data set does not exist, it can be created based on *dataset_model* or the size of the source.





Parameters
----------


 
     
dataset_checksum
  Specifies the checksum to be used to verify that the target data set to copy to is not changed since the checksum was generated.

  The module will fail and no data will be copied if the checksum is not matched which means the target data set has been modified.

  This variable only take effects when *dataset_force=true*.


  | **required**: False
  | **type**: str


 
     
dataset_content
  The contents to be copied to the target data set or member. This variable is used instead of *dataset_src*.

  This variable only take effects when *dataset_data_type=text*.

  Each line of the contents should be terminated with ``\n``. For example, ``Sample profile\nTZ=EST5EDT\n``.

  If *dataset_content* is supplied and *dataset_data_type=text*, *dataset_src* is ignored.


  | **required**: False
  | **type**: str


 
     
dataset_crlf
  Specifies whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF).

  If *dataset_crlf=true*, CRLF characters are used.

  This variable only take effects when *dataset_data_type=text*.


  | **required**: False
  | **type**: bool
  | **default**: false


 
     
dataset_data_type
  Specifies whether data conversion is to be performed on the data to be copied.

  When *dataset_data_type=text*, data conversion is performed.

  You can use *dataset_encoding* to specify which encodings the data to be copied should be converted from and to.

  Each line of data, delimited by a Line Feed (LF), is converted and written as a record to the target data set.

  The LF character is removed and the data is padded with the space character to the end of the record if it is a fixed record size data set.

  For variable record size data set, the record is written without padding.

  the module will fail if the record size of the data set is smaller than any line of text since not all data was written.

  If *dataset_encoding* is not supplied, the data transfer process converts each byte from ``ISO8859-1`` to ``IBM-1047`` by default.

  You can use *dataset_crlf* to control whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF).

  If *dataset_crlf* is not supplied, LF characters are left intact by default.

  You can use *dataset_diff* to specify whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command.

  If *dataset_diff* is not supplied, the input is regarded as not consisting of commands by default.

  When *dataset_data_type=binary*, no data conversion is performed.

  The data is written to the data set without respect to record boundaries. All records will be written at their maximum record length.

  For fixed length record data set, the last record will be padded with nulls if required.

  When *dataset_data_type=record*, no data conversion is performed.

  Each logical record is preceded by the 4-byte big endian record length of the record that follows. This length doesn't include the prefix length.

  For example, a zero-length record is 4 bytes of zeros with nothing following.


  | **required**: False
  | **type**: str
  | **default**: text
  | **choices**: text, binary, record


 
     
dataset_dest
  Data set or the name of the PDS or PDSE member on the remote z/OS system where the data should be copied to.

  This variable must consist of a fully qualified data set name. The length of the data set name cannot exceed 44 characters.

  If *dataset_dest* is a nonexistent data set, it will be allocated.

  For example, specifying a data set like ``ZOSMF.ANSIBLE.DATA``, or a PDS or PDSE member like ``ZOSMF.ANSIBLE.PDS(MEMBER)``.


  | **required**: True
  | **type**: str


 
     
dataset_diff
  Specifies whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command.

  These commands are used to add, replace and delete lines in the target data set. The following commands are supported.

  ``a``

  ``c``

  ``d``

  ``s/.//``

  opt ``g|<n>``, where ``g`` means global, ``n`` means search and replace ``n`` times.

  Each command may be optionally preceded by a line or line range, as allowed by the z/OS UNIX 'ed' command.

  The module will fail if an error is detected while processing a command.

  This variable only take effects when *dataset_data_type=text*.


  | **required**: False
  | **type**: bool
  | **default**: false


 
     
dataset_encoding
  Specifies which encodings the data to be copied should be converted from and to.

  These parameters only take effects when *dataset_data_type=text* and *dataset_diff=false*.


  | **required**: False
  | **type**: dict


 
     
  from
    The character set of the data to be copied.

    Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.


    | **required**: True
    | **type**: str


 
     
  to
    The destination character set for the target data set.

    Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.


    | **required**: True
    | **type**: str



 
     
dataset_force
  Specifies whether the target data set must always be overwritten.

  If *dataset_force=true* and *dataset_checksum* is not supplied, the target data set will always be overwritten.

  If *dataset_force=true* and *dataset_checksum* is supplied, the target data set will be overwritten only when the checksum is matched.

  If *dataset_force=false*, the data will only be copied if the target PDS or PDSE member does not exist.


  | **required**: False
  | **type**: bool
  | **default**: true


 
     
dataset_migrate_recall
  Specify how a migrated data set is handled.

  When *dataset_migrate_recall=wait*, the migrated data set is recalled synchronously.

  When *dataset_migrate_recall=nowait*, request the migrated data set to be recalled, but do not wait.

  When *dataset_migrate_recall=error*, do not attempt to recall the migrated data set.


  | **required**: False
  | **type**: str
  | **default**: wait
  | **choices**: wait, nowait, error


 
     
dataset_model
  When copying a local file to a non-existing PDS, PDSE or PS, specify a model data set to allocate the target data set.

  For example, specifying a data set like ``ZOSMF.ANSIBLE.DATALIB``, member name should not be provided in this parameter.

  If this parameter is not provided, the destination data set will be allocated based on the size of the local file or *dataset_content*.

  The primary extent tracks will be specified as 4 times the size of the local file or *dataset_content*.

  If *dataset_data_type=text*, then ``RECFM=FB`` and ``LRECL=80`` will be used to allocate the data set.

  If *dataset_data_type=binary* or *dataset_data_type=record*, (RECFM=U) will be used to allocate the data set.


  | **required**: False
  | **type**: str


 
     
dataset_src
  The local path on control node of the data to be copied to the target data set or member. For example, ``/tmp/dataset_input/member01``.

  This path can be absolute or relative. The module will fail if *dataset_src* has no read permission.

  The data is interpreted as one of binary, text, record or 'diff -e' format according to the value of *dataset_data_type* and *dataset_diff*.

  If *dataset_content* is supplied and *dataset_data_type=text*, *dataset_src* is ignored.


  | **required**: False
  | **type**: str


 
     
dataset_volser
  The volume serial to identify the volume to be searched for an uncataloged data set or member.

  The length of the volume serial cannot exceed six characters. Wildcard characters are not supported. Indirect volume serials are not supported.

  If this parameter is provided and *dataset_dest* is a nonexistent data set, *dataset_volser* must point to a volume on a 3390 device.


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

   
   - name: Copy a local file to data set ZOSMF.ANSIBLE.LIB
     zmf_dataset_copy:
       zmf_host: "sample.ibm.com"
       dataset_src: "/tmp/dataset_input/sample1"
       dataset_dest: "ZOSMF.ANSIBLE.LIB"

   - name: Copy a local file to PDS member ZOSMF.ANSIBLE.LIB(MEMBER01) only if it does not exist
     zmf_dataset_copy:
       zmf_host: "sample.ibm.com"
       dataset_src: "/tmp/dataset_input/member01"
       dataset_dest: "ZOSMF.ANSIBLE.LIB(MEMBER01)"
       dataset_force: false

   - name: Copy the contents to data set ZOSMF.ANSIBLE.LIB
     zmf_dataset_copy:
       zmf_host: "sample.ibm.com"
       dataset_conntent: "Sample profile\nTZ=EST5EDT\n"
       dataset_dest: "ZOSMF.ANSIBLE.LIB"

   - name: Copy a local file to uncataloged PDS member ZOSMF.ANSIBLE.LIB(MEMBER01) as binary
     zmf_dataset_copy:
       zmf_host: "sample.ibm.com"
       dataset_src: "/tmp/dataset_input/member01"
       dataset_dest: "ZOSMF.ANSIBLE.LIB(MEMBER01)"
       dataset_volser: "VOL001"
       dataset_data_type: "binary"

   - name: Copy a local file to data set ZOSMF.ANSIBLE.LIB and convert from ISO8859-1 to IBM-037
     zmf_dataset_copy:
       zmf_host: "sample.ibm.com"
       dataset_src: "/tmp/dataset_input/sample1"
       dataset_dest: "ZOSMF.ANSIBLE.LIB"
       dataset_encoding:
         from: ISO8859-1
         to: IBM-037

   - name: Copy a local file to data set ZOSMF.ANSIBLE.LIB and validate its checksum
     zmf_dataset_copy:
       zmf_host: "sample.ibm.com"
       dataset_src: "/tmp/dataset_input/sample1"
       dataset_dest: "ZOSMF.ANSIBLE.LIB"
       dataset_checksum: "93822124D6E66E2213C64B0D10800224"










Return Values
-------------

   
      
   changed
        Indicates if any change is made during the module operation.


        | **returned**: always 
        | **type**: bool


   
      
   message
        The output message generated by the module to indicate whether the data set or member is successfully copied.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "The target data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is created and updated successfully."

                  "The target data set ZOSMF.ANSIBLE.SAMPLE is updated successfully."

                  "No data is copied since the target data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) exists and dataset_force is set to False."



   
      
   dataset_checksum
        The checksum of the updated data set.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "93822124D6E66E2213C64B0D10800224"




