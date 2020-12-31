
:github_url: https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/zmf_file_fetch.py

.. _zmf_file_fetch_module:


zmf_file_fetch -- Fetch USS file from z/OS
==========================================



.. contents::
   :local:
   :depth: 1
   

Synopsis
--------
- Retrieve the contents of a z/OS UNIX System Services (USS) file from the remote z/OS system, and save them on Ansible control node.
- USS file that already exists at *file_dest* will be overwritten if it is different than the *file_src*.





Parameters
----------


 
     
file_checksum
  Specifies the checksum to be used to verify that the USS file to be fetched is not changed since the checksum was generated.

  If the checksum is matched which means the USS file is not changed, the USS file won't be fetched.


  | **required**: False
  | **type**: str


 
     
file_data_type
  Specifies whether data conversion is to be performed on the returned data.

  When *file_data_type=text*, data conversion is performed.

  You can use *file_encoding* to specify which encodings the fetched USS file should be converted from and to.

  If *file_encoding* is not supplied, the data transfer process converts each record from ``IBM-1047`` to ``ISO8859-1`` by default.

  When *file_data_type=binary*, no data conversion is performed. The data transfer process returns each line of data as-is, without translation.


  | **required**: False
  | **type**: str
  | **default**: text
  | **choices**: text, binary


 
     
file_dest
  The local directory on control node where the USS file should be saved to. For example, ``/tmp/file_output``.

  This directory can be absolute or relative. The module will fail if the parent directory of *file_dest* is a read-only file system.

  The directory ``{{ file_dest }}/{{ zmf_host }}/`` will be created to save the USS file, where *zmf_host* is the hostname of the z/OSMF server.

  For example, if *zmf_host=zosmf.ibm.com*, a USS file named ``/etc/profile`` would be saved into ``/tmp/file_output/zosmf.ibm.com/etc/profile``.


  | **required**: True
  | **type**: str


 
     
file_encoding
  Specifies which encodings the fetched USS file should be converted from and to.

  These parameters only take effects when *file_data_type=text*.


  | **required**: False
  | **type**: dict


 
     
  from
    The character set of the source USS file.

    Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.


    | **required**: True
    | **type**: str


 
     
  to
    The destination character set for the output to be written as.

    Supported character sets rely on the charset conversion utility (iconv) version. The most common character sets are supported.


    | **required**: True
    | **type**: str



 
     
file_flat
  Specifies whether to override the default behavior of appending hostname/path/to/file to the destination.

  If *file_flat=true*, the USS file will be fetched to the destination directory using its basename without appending *zmf_host*.

  For example, if *file_dest=/tmp/file_output*, a USS file named ``/etc/profile`` would be saved into ``/tmp/file_output/profile``.


  | **required**: False
  | **type**: bool
  | **default**: false


 
     
file_range
  Specifies a range that is used to retrieve the USS file.

  If *file_data_type=text*, the module will retrieve a range of records (lines delimited by '\n') from the USS file.

  If *file_data_type=binary*, the module will retrieve a range of bytes from the USS file.

  If this variable is specified, only the retrieved range of the USS file will be fetched to the destination directory.

  The retrieved range of the USS file will be saved as ``{{ file_dest }}/{{ zmf_host }}/{ file_src }}.range`` on control node.

  For example, the retrieved range of the USS file named ``/etc/profile`` would be saved as ``....../etc/profile.range``.


  | **required**: False
  | **type**: dict


 
     
  end
    If *file_data_type=text*, this variable identifies the end record in the range to be retrieved.

    If *file_data_type=binary*, this variable identifies the byte-offset of the last byte in the range to be retrieved.

    If this value is omitted or is set to 0, the range extends to the end of the USS file.


    | **required**: False
    | **type**: int


 
     
  start
    If *file_data_type=text*, this variable identifies the start record in the range to be retrieved.

    If *file_data_type=binary*, this variable identifies the byte-offset of the first byte in the range to be retrieved.

    If this value is omitted, a tail range is returned.


    | **required**: False
    | **type**: int



 
     
file_search
  Specifies a series of parameters that are used to search the USS file.

  These parameters only take effects when *file_data_type=text*.

  If this variable is specified, only the matched contents in the USS file will be fetched to the destination directory.

  The matched contents in the USS file will be saved as ``{{ file_dest }}/{{ zmf_host }}/{ file_src }}.search`` on control node.

  For example, the matched contents in the USS file named ``/etc/profile`` would be saved as ``....../etc/profile.search``.


  | **required**: False
  | **type**: dict


 
     
  insensitive
    Specifies whether the comparison of *keyword* is case insensitive.

    This variable only take effects when *keyword* is defined.


    | **required**: False
    | **type**: bool
    | **default**: true


 
     
  keyword
    Specifies a string or a regular expression that is used to search the USS file.

    The USS file is searched for the first line that contains the string or matches the given extended regular expression.


    | **required**: True
    | **type**: str


 
     
  maxreturnsize
    Specifies how many lines of contents from the first matched line in the USS file will be returned.

    This variable only take effects when *keyword* is defined.


    | **required**: False
    | **type**: int
    | **default**: 100



 
     
file_src
  USS file on the remote z/OS system to fetch.

  This variable must consist of a fully qualified path and file name. For example, ``/etc/profile``.


  | **required**: True
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

   
   - name: Fetch a USS file and store in /tmp/file_output/sample.ibm.com/etc/profile
     zmf_file_fetch:
       zmf_host: "sample.ibm.com"
       file_src: "/etc/profile"
       file_dest: "/tmp/file_output"

   - name: Fetch a USS file and store in /tmp/file_output/profile
     zmf_file_fetch:
       zmf_host: "sample.ibm.com"
       file_src: "/etc/profile"
       file_dest: "/tmp/file_output"
       file_flat: true

   - name: Fetch a USS file as binary
     zmf_file_fetch:
       zmf_host: "sample.ibm.com"
       file_src: "/etc/profile"
       file_dest: "/tmp/file_output"
       file_data_type: "binary"

   - name: Fetch a USS file and convert from IBM-037 to ISO8859-1
     zmf_file_fetch:
       zmf_host: "sample.ibm.com"
       file_src: "/etc/profile"
       file_dest: "/tmp/file_output"
       file_encoding:
           from: IBM-037
           to: ISO8859-1

   - name: Fetch a range of records from a USS file (the first 500 lines)
     zmf_file_fetch:
       zmf_host: "sample.ibm.com"
       file_src: "/etc/profile"
       file_dest: "/tmp/file_output"
       file_range:
           start: 0
           end: 499

   - name: Fetch a range of records from a USS file (the final 500 lines)
     zmf_file_fetch:
       zmf_host: "sample.ibm.com"
       file_src: "/etc/profile"
       file_dest: "/tmp/file_output"
       file_range:
           end: 500

   - name: Fetch 100 lines of records from the first matched line that contains "Health Checker" in a USS file
     zmf_file_fetch:
       zmf_host: "sample.ibm.com"
       file_src: "/etc/profile"
       file_dest: "/tmp/file_output"
       file_search:
           keyword: "Health Checker"

   - name: Fetch a USS file and validate its checksum
     zmf_file_fetch:
       zmf_host: "sample.ibm.com"
       file_src: "/etc/profile"
       file_dest: "/tmp/file_output"
       file_checksum: "93822124D6E66E2213C64B0D10800224"










Return Values
-------------

   
      
   changed
        Indicates if any change is made during the module operation.


        | **returned**: always 
        | **type**: bool


   
      
   message
        The output message generated by the module to indicate whether the USS file is successfully fetched.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "The USS file /etc/profile is fetched successfully and saved in: /tmp/file_output/sample.ibm.com/etc/profile"

                  "The matched contents in the USS file /etc/profile is fetched successfully and saved in: /tmp/file_output/sample.ibm.com/etc/profile.serarch"

                  "The USS file /etc/profile is not fetched since no matched contents is found with the specified search keyword."

                  "A range of records in the USS file /etc/profile is fetched successfully and saved in: /tmp/file_output/SY1/etc/profile.range"

                  "A range of bytes in the USS file /etc/profile is fetched successfully and saved in: /tmp/file_output/SY1/etc/profile.range"

                  "The USS file /etc/profile is not fetched since no contents is returned in the specified range."

                  "The USS file /etc/profile is not fetched since it is not changed."



   
      
   file_content
        The retrieved contents of the USS file.


        | **returned**: on success when I(file_data_type=text) 
        | **type**: list

        **sample**: ::

                  ["# This is a sample profile defining system wide variables. The", "# variables set here may be overridden by a user\u0027s personal .profile", "# in their $HOME directory."]


   
      
   file_matched_content
        The matched contents in the USS file with the specified search keyword.


        | **returned**: on success when I(file_data_type=text) and I(file_search) is specified 
        | **type**: list

        **sample**: ::

                  ["NLSPATH=/usr/lib/nls/msg/%L/%N"]


   
      
   file_matched_range
        The range of the matched contents of the USS file with the specified search keyword.

        Return *file_matched_range=p,q*, where *p* is the first matched line in the USS file and *q* is the number of lines returned.


        | **returned**: on success when I(file_data_type=text) and I(file_search) is specified 
        | **type**: str

        **sample**: ::

                  "0,500"



   
      
   file_checksum
        The checksum of the fetched USS file.


        | **returned**: on success when I(file_search) and I(file_range) are not specified 
        | **type**: str

        **sample**: ::

                  "93822124D6E66E2213C64B0D10800224"




