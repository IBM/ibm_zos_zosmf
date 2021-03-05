
:github_url: https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/zmf_file_copy.py

.. _zmf_file_copy_module:


zmf_file_copy -- Copy data to z/OS USS file
===========================================



.. contents::
   :local:
   :depth: 1
   

Synopsis
--------
- Copy data from Ansible control node to a z/OS UNIX System Services (USS) file on z/OS system.
- If the target USS file already exists, it can be overwritten. If the target USS file does not exist, it can be created with mode 644.





Parameters
----------


 
     
file_checksum
  Specifies the checksum to be used to verify that the target USS file to copy to is not changed since the checksum was generated.

  The module will fail and no data will be copied if the checksum is not matched which means the target data set has been modified.

  This variable only take effects when *file_force=true*.


  | **required**: False
  | **type**: str


 
     
file_content
  The contents to be copied to the target USS file. This variable is used instead of *file_src*.

  This variable only take effects when *file_data_type=text*.

  Each line of the contents should be terminated with ``\n``. For example, ``Sample profile\nTZ=EST5EDT\n``.

  If *file_content* is supplied and *file_data_type=text*, *file_src* is ignored.


  | **required**: False
  | **type**: str


 
     
file_crlf
  Specifies whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF).

  If *file_crlf=true*, CRLF characters are used.

  This variable only take effects when *file_data_type=text*.


  | **required**: False
  | **type**: bool
  | **default**: false


 
     
file_data_type
  Specifies whether data conversion is to be performed on the data to be copied.

  When *file_data_type=text*, data conversion is performed.

  You can use *file_encoding* to specify which encodings the data to be copied should be converted from and to.

  If *file_encoding* is not supplied, the data transfer process converts each byte from ``ISO8859-1`` to ``IBM-1047`` by default.

  You can use *file_crlf* to control whether each input text line is terminated with a carriage return line feed (CRLF) or a line feed (LF).

  If *file_crlf* is not supplied, LF characters are left intact by default.

  You can use *file_diff* to specify whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command.

  If *file_diff* is not supplied, the input is regarded as not consisting of commands by default.

  When *file_data_type=binary*, no data conversion is performed.


  | **required**: False
  | **type**: str
  | **default**: text
  | **choices**: text, binary


 
     
file_dest
  USS file on z/OS system where the data should be copied to.

  This variable must consist of a fully qualified path and file name. For example, ``/etc/profile``.


  | **required**: True
  | **type**: str


 
     
file_diff
  Specifies whether the input consists of commands in the same format as produced by the z/OS UNIX 'diff -e' command.

  These commands are used to add, replace and delete lines in the target USS file. The following commands are supported.

  ``a``

  ``c``

  ``d``

  ``s/.//``

  opt ``g|<n>``, where ``g`` means global, ``n`` means search and replace ``n`` times.

  Each command may be optionally preceded by a line or line range, as allowed by the z/OS UNIX 'ed' command.

  The module will fail if an error is detected while processing a command.

  This variable only take effects when *file_data_type=text*.


  | **required**: False
  | **type**: bool
  | **default**: false


 
     
file_encoding
  Specifies which encodings the data to be copied should be converted from and to.

  This variable only take effects when *file_data_type=text* and *file_diff=false*.


  | **required**: False
  | **type**: dict


 
     
  from
    The character set of the data to be copied.

    Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.


    | **required**: True
    | **type**: str


 
     
  to
    The destination character set for the target USS file.

    Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.


    | **required**: True
    | **type**: str



 
     
file_force
  Specifies whether the target USS file must always be overwritten.

  If *file_force=true* and *file_checksum* is not supplied, the target USS file will always be overwritten.

  If *file_force=true* and *file_checksum* is supplied, the target USS file will be overwritten only when the checksum is matched.

  If *file_force=false*, the data will only be copied if the target USS file does not exist.


  | **required**: False
  | **type**: bool
  | **default**: true


 
     
file_src
  The local path on control node of the data to be copied to the target USS file. For example, ``/tmp/file_input/profile``.

  This path can be absolute or relative. The module will fail if *file_src* has no read permission.

  The data is interpreted as one of binary, text or 'diff -e' format according to the value of *file_data_type* and *file_diff*.

  If *file_content* is supplied and *file_data_type=text*, *file_src* is ignored.


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

   
   - name: Copy a local file to USS file /etc/profile
     zmf_file_copy:
       zmf_host: "sample.ibm.com"
       file_src: "/tmp/file_input/profile"
       file_dest: "/etc/profile"

   - name: Copy a local file to USS file /etc/profile only if it does not exist
     zmf_file_copy:
       zmf_host: "sample.ibm.com"
       file_src: "/tmp/file_input/profile"
       file_dest: "/etc/profile"
       file_force: false

   - name: Copy the contents to USS file /etc/profile
     zmf_file_copy:
       zmf_host: "sample.ibm.com"
       file_conntent: "Sample profile\nTZ=EST5EDT\n"
       file_dest: "/etc/profile"

   - name: Copy a local file to USS file /etc/profile as binary
     zmf_file_copy:
       zmf_host: "sample.ibm.com"
       file_src: "/tmp/file_input/profile"
       file_dest: "/etc/profile"
       file_data_type: "binary"

   - name: Copy a local file to USS file /etc/profile and convert from ISO8859-1 to IBM-037
     zmf_file_copy:
       zmf_host: "sample.ibm.com"
       file_src: "/tmp/file_input/profile"
       file_dest: "/etc/profile"
       file_encoding:
         from: ISO8859-1
         to: IBM-037

   - name: Copy a local file to USS file /etc/profile and validate its checksum
     zmf_file_copy:
       zmf_host: "sample.ibm.com"
       file_src: "/tmp/file_input/profile"
       file_dest: "/etc/profile"
       file_checksum: "93822124D6E66E2213C64B0D10800224"










Return Values
-------------

   
      
   changed
        Indicates if any change is made during the module operation.


        | **returned**: always 
        | **type**: bool


   
      
   message
        The output message generated by the module to indicate whether the USS file is successfully copied.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "The target USS file /etc/profile is created and updated successfully."

                  "The target USS file /etc/profile is updated successfully."

                  "No data is copied since the target USS file /etc/profile already exists and file_force is set to False."



   
      
   file_checksum
        The checksum of the updated USS file.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "93822124D6E66E2213C64B0D10800224"




