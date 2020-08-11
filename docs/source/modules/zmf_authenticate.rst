
:github_url: https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/zmf_authenticate.py

.. _zmf_authenticate_module:


zmf_authenticate -- Authenticate with z/OSMF server
===================================================



.. contents::
   :local:
   :depth: 1
   

Synopsis
--------
- Authenticate with z/OSMF server by either username/password or HTTPS client authentication.
- Return the authentication credentials for the successfully authentication with z/OSMF server.





Parameters
----------


 
     
zmf_crt
  Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication.

  Required when *zmf_user* and *zmf_password* are not supplied.


  | **required**: False
  | **type**: str


 
     
zmf_host
  Hostname of the z/OSMF server.


  | **required**: True
  | **type**: str


 
     
zmf_key
  Location of the PEM-formatted file with your private key to be used for HTTPS client authentication.

  Required when *zmf_user* and *zmf_password* are not supplied.


  | **required**: False
  | **type**: str


 
     
zmf_password
  Password to be used for authenticating with z/OSMF server.

  Required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 
     
zmf_port
  Port number of the z/OSMF server.


  | **required**: False
  | **type**: int


 
     
zmf_user
  User name to be used for authenticating with z/OSMF server.

  Required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Authenticate with z/OSMF server by username/password
     zmf_authenticate:
       zmf_host: "sample.ibm.com"
       zmf_user: "your_username"
       zmf_password: "your_password"

   - name: Authenticate with z/OSMF server by HTTPS client authentication
     zmf_authenticate:
       zmf_host: "sample.ibm.com"
       zmf_crt: "/file_with_your_certificate_chain.crt"
       zmf_key: "/file_with_your_private_key.key"










Return Values
-------------

   
      
   changed
        Indicates if any change is made during the module operation.


        | **returned**: always 
        | **type**: bool


   
      
   LtpaToken2
        The value of Lightweight Third Party Access (LTPA) token, which supports strong encryption.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "yDS7uJxqrd3h8v5WXq9pf1yPtztQ4JzroZN3XQKF26ZicXgHc7mdzgycMCudvhxM+JWpC9TzhM4SEHRe/Vb3dC......"



   
      
   jwtToken
        The value of JSON Web token, which supports strong encryption.


        | **returned**: on success 
        | **type**: str

        **sample**: ::

                  "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiQmVhcmVyIiwic3ViIjoiem9zbWZhZ....."



   
      
   zmf_host
        Hostname of the z/OSMF server.


        | **returned**: on success 
        | **type**: str


   
      
   zmf_port
        Port number of the z/OSMF server.


        | **returned**: on success 
        | **type**: int



