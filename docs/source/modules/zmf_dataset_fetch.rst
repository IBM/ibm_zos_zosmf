
:github_url: https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/zmf_dataset_fetch.py

.. _zmf_dataset_fetch_module:


zmf_dataset_fetch -- Operates a z/OS data set or member
=======================================================



.. contents::
   :local:
   :depth: 1
   

Synopsis
--------
- Retrieve the contents of a z/OS data set or member and store the content to a local file.
- Write data to a z/OS data set or member from a local file.





Parameters
----------


 
     
dataset_checksum
  Specifies the checksum to be used to verify that the data set to be fetched is not changed since the checksum was generated.

  If the checksum is matched which means the data set is not changed, the content of the data set won't be fetched.


  | **required**: False
  | **type**: str


 
     
dataset_data_type
  Specifies whether data conversion is to be performed on the returned data.

  When *dataset_data_type=text*, data conversion is performed.

  You can use *dataset_encoding* to specify which encodings the fetched data set should be converted from and to.

  If *dataset_encoding* is not supplied, the data transfer process converts each record from ``IBM-1047`` to ``ISO8859-1`` by default.

  When *dataset_data_type=binary*, no data conversion is performed. The data transfer process returns each line of data as-is.

  When *dataset_data_type=record*, no data conversion is performed. Each logical record is preceded by the 4-byte big endian record length.


  | **required**: False
  | **type**: str
  | **default**: text
  | **choices**: text, binary, record


 
     
dataset_dest
  The local directory on control node where the data set should be saved to. For example, ``/tmp/dataset``.

  This directory can be absolute or relative. The module will fail if the parent directory of *dataset_dest* is a read-only file system.

  The directory ``{{ dataset_dest }}/{{ zmf_host }}/`` will be created to save the data set, where *zmf_host* is the hostname of the z/OSMF server.

  If *zmf_host=zosmf.ibm.com*, a dataset named ``ZOSMF.ANSIBLE.DATA`` would be saved into ``{{dataset_dest}}/zosmf.ibm.com/ZOSMF.ANSIBLE.DATA``.

  If *dataset_volser=VOL001*, the above dataset would be saved into ``{{dataset_dest}}/zosmf.ibm.com/VOL001/ZOSMF.ANSIBLE.DATA``.


  | **required**: True
  | **type**: str


 
     
dataset_encoding
  Specifies which encodings the fetched data set should be converted from and to.

  These parameters only take effects when *dataset_data_type=text*.


  | **required**: False
  | **type**: dict


 
     
  from
    The character set of the source data set. Select an alternate EBCDIC code page.


    | **required**: True
    | **type**: str
    | **default**: IBM-1047


 
     
  to
    The destination character set for the output to be written as.


    | **required**: True
    | **type**: str
    | **default**: ISO8859-1



 
     
dataset_flat
  Specifies whether to override the default behavior of appending *zmf_host* to the destination.

  If *dataset_flat=true*, the data set will be fetched to the destination directory using its name without appending *zmf_host*.

  For example, if *dataset_dest=/tmp/dataset*, a data set named ``ZOSMF.ANSIBLE.DATA`` would be saved into ``/tmp/dataset/ZOSMF.ANSIBLE.DATA``.


  | **required**: False
  | **type**: bool
  | **default**: false


 
     
dataset_migrate_recall
  Specify how a migrated data set is handled.

  When *dataset_migrate_recall=wait*, the migrated data set is recalled synchronously.

  When *dataset_migrate_recall=nowait*, request the migrated data set to be recalled, but do not wait.

  When *dataset_migrate_recall=error*, do not attempt to recall the migrated data set.


  | **required**: False
  | **type**: str
  | **default**: wait
  | **choices**: wait, nowait, error


 
     
dataset_range
  Specifies a range that is used to retrieve records of the data set.

  If this variable is specified, only the retrieved range of the data set will be fetched to the destination directory.

  The retrieved range of the data set will be saved as ``{{ dataset_dest }}/{{ zmf_host }}/{{ dataset_src }}.range`` on control node.

  For example, the retrieved range of the dat set named ``ZOSMF.ANSIBLE.DATA`` would be saved as ``/tmp/dataset/ZOSMF.ANSIBLE.DATA.range``.


  | **required**: False
  | **type**: dict


 
     
  end
    This variable identifies the end record in the range to be retrieved.

    If this value is omitted or is set to 0, the range extends to the end of the data set.


    | **required**: False
    | **type**: int


 
     
  start
    This variable identifies the start record in the range to be retrieved.

    If this value is omitted, a tail range is returned.


    | **required**: False
    | **type**: int



 
     
dataset_search
  Specifies a series of parameters that are used to search the content of data set or member.

  These parameters only take effects when *dataset_data_type=text*.

  If this variable is specified, only the matched records in the data set will be fetched to the destination directory.

  Records are returned starting with the first matching record. The *dataset_range* may be used to specify the range of records to be searched.

  The matched contents in the data set will be saved as ``{{ dataset_dest }}/{{ zmf_host }}/{{ dataset_src }}.search`` on control node.

  For example, the matched contents in the dataset named ``ZOSMF.ANSIBLE.DATA`` would be saved as ``/tmp/dataset/ZOSMF.ANSIBLE.DATA.search``.


  | **required**: False
  | **type**: dict


 
     
  insensitive
    Specifies whether the comparison of *keyword* is case insensitive.

    This variable only take effects when *keyword* is defined.


    | **required**: False
    | **type**: bool
    | **default**: true


 
     
  keyword
    Specifies a string or a regular expression that is used to search the data set.


    | **required**: False
    | **type**: str


 
     
  maxreturnsize
    The maximum number of records to return.

    This variable only take effects when *keyword* is defined.


    | **required**: False
    | **type**: int
    | **default**: 100



 
     
dataset_src
  Data set or data set member name on the remote z/OS system to fetch.

  For example, specifying a data set like ``ZOSMF.ANSIBLE.DATA``, or a data set member like ``ZOSMF.ANSIBLE.PDS(MEMBER``).


  | **required**: True
  | **type**: str


 
     
dataset_volser
  The volume serial identify the volume to be searched for an uncataloged data set or member.

  The length of the volume serial cannot exceed six characters. You cannot use wildcard characters for this parameter.


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

   
   - name: Fetch a data set and store in /tmp/dataset/sample.ibm.com/ZOSMF.ANSIBLE.SAMPLE/MEMBER
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_dest: "/tmp/dataset"

   - name: Fetch a dataset and store in /tmp/dataset/ZOSMF.ANSIBLE.SAMPLE/MEMBER
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_dest: "/tmp/dataset"
       dataset_flat: true

   - name: Fetch an uncataloged dataset and store in /tmp/dataset/sample.ibm.com/ZOSMF.ANSIBLE.SAMPLE/MEMBER
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_volser: "VOLABC"
       dataset_dest: "/tmp/dataset"

   - name: Fetch a data set as binary
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_dest: "/tmp/dataset"
       dataset_data_type: "binary"

   - name: Fetch a data set in record format
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_dest: "/tmp/dataset"
       dataset_data_type: "record"

   - name: Fetch a dataset and convert it from IBM-037 to ISO8859-1
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_dest: "/tmp/dataset"
       dataset_encoding:
           from: IBM-037
           to: ISO8859-1

   - name: Fetch a range of records from a dataset (the first 500 lines)
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_dest: "/tmp/dataset"
       dataset_range:
           start: 0
           end: 499

   - name: Fetch a range of records from a dataset (the final 500 lines)
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_dest: "/tmp/dataset"
       dataset_range:
           end: 500

   - name: Fetch 100 lines of records from the first matched line that contains "ansible" in a dataset
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_dest: "/tmp/dataset"
       dataset_search:
           keyword: "ansible"
           maxreturnsize: 100

   - name: Fetch a dataset and validate its checksum
     zmf_dataset_fetch:
       zmf_host: "sample.ibm.com"
       dataset_src: "ZOSMF.ANSIBLE.SAMPLE(MEMBER)"
       dataset_dest: "/tmp/dataset"
       dataset_checksum: "A4B504A7427F34B97B7E109CCC0459CA"










Return Values
-------------

   
      
   changed
        Indicates if any change is made on managed node during the module operation.


        | **returned**: always 
        | **type**: bool


   
      
   message
        The output message generated by the module to indicate whether the data set is successfully fetched.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "The data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is fetched successfully and saved in: /tmp/dataset/ZOSMF.ANSIBLE.SAMPLE/MEMBER."

                  "The matched contents in the data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is fetched successfully and saved in: /tmp/dataset/ZOSMF.ANSIBLE.SAMPLE/MEMBER.serarch."

                  "The data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is not fetched since no matched contents is found with the specified search keyword."

                  "A range of records in the data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is fetched successfully and saved in: /tmp/dataset/ZOSMF.ANSIBLE.SAMPLE/MEMBER.range."

                  "The data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is not fetched since no contents is returned in the specified range."

                  "The data set ZOSMF.ANSIBLE.SAMPLE(MEMBER) is not fetched since it is not changed."



   
      
   dataset_content
        The retrieved content of the data set.


        | **returned**: on success when I(dataset_data_type=text) 
        | **type**: list

        **sample**: ::

                  ["First line of the data set", "Second line of the data set"]


   
      
   dataset_matched_content
        The matched content in the data set with the specified search keyword.


        | **returned**: on success when I(dataset_data_type=text) and I(dataset_search) is specified 
        | **type**: list

        **sample**: ::

                  ["First line of the data set"]


   
      
   dataset_matched_range
        The range of the matched contents of the data set with the specified search keyword.

        Return *dataset_matched_range=p,q*, where *p* is the first matched line in the data set and *q* is the number of lines returned.


        | **returned**: on success when I(dataset_data_type=text) and I(dataset_search) is specified 
        | **type**: str

        **sample**: ::

                  "0,500"



   
      
   dataset_checksum
        The checksum of the fetched data set, can be set in *dataset_checksum* in next call to this module


        | **returned**: on success when I(dataset_search) and I(dataset_range) are not specified 
        | **type**: str

        **sample**: ::

                  "93822124D6E66E2213C64B0D10800224"




