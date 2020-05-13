# Ansible role: zmf_workflow_complete
The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), which is referred to as `zmf_workflow_complete`. This role is used for completing a z/OS workflow, either forcibly or idempotently.


## Role variables
The available role variables are described as follows.

The following variables are defined by role. For the default values, see [defaults/main.yml](defaults/main.yml).

- **job_jcl_src**  
  Specifies the detail location of file or data set containing the JCL. This variable is mandatory. 
  - when `job_jcl_location` is set to `LOCAL`, this variable should be the absolute path of the JCL file on control node. For example, "/tmp/job1.jcl".
  - when `job_jcl_location` is set to `DATASET`, this variable should be the full name of the data set or the member. For example, "USER.TEST.JCLLIB" or "USER.TEST.JCLLIB(JCL1)".
  - when `job_jcl_location` is set to `USS`, this variable should be the absolute path of the JCL file in USS file system on managed z/OS node. For example, "/var/data/jcl/job1.jcl".

- **job_jcl_location**  
  An option to specify the location of the JCL to be submitted. Below values are supported, "LOCAL" is the default vlaue.
  - **LOCAL**  
    Specifies that the JCL residents in local, the role will try to load the JCL file from control node.
  - **DATASET**
    Specifies that the JCL is contained in a data set or s data set member on managed z/OS node. Note that the specified data set must be cataloged
  - **USS**
    Specifies that the JCL residents in USS file system on managed z/OS node.

- **job_internal_reader_class**  
  A single character that specifies the internal reader class; the default is 'A'. This value defines the default message class (MSGCLASS) for the job.

- **job_internal_reader_recfm**  
  A single character that specifies the internal reader record format: "F" or "V".  
  - When submitting a job from a data set, you can omit this header. Otherwise, this value must match the record format of the data set.
  - When not submitting a job from a data set, if you omit this header or specify a value other than "F" or "V", the default of "F" is used.

- **job_internal_reader_lrecl**  
  An integer value that specifies the internal reader logical record length (LRECL).  
  - When submitting a job from a data set, you can omit this header. Otherwise, this value must match the LRECL of the data set.
  - When not submitting a job from a data set, if you omit this header or specify a non-integer value, the default of 80 is used.

- **job_interanl_reader_mode**  
  A keyword that specifies the format of the input job. Below values are supported.
  - **RECORD**
    When submitting a job from a data set, you can ethier omit this variable or set it to "RECORD".
  - **TEXT**
    When not submitting a job from a data set, "TEXT" is default value.
  - **BINARY**
    When set this variable to "BINARY", `job_internal_reader_lrecl` must be omitted or set to "F".

- **job_user_correlator**  
  Specifies the user portion of the job correlator. In z/OS, a job correlator can be used to associate each job with a unique 64-character value. The correlator provides you with a means to query a job in the system and track it through execution.  
  A job correlator consists of a 31-byte system-defined portion and a colon character `:`, followed by a 32-byte user portion. This value is 1 – 32 characters in length, where the first character must be uppercase alphabetic (A-Z) or special ($, #, @). The remaining characters (up to 31) can be any combination of uppercase alphabetic, numeric (0-9), or special. Blank characters are not supported.

- **job_symbols**  
  This variable is a dictionary which specifies the name and value for JCL symbols.
  A symbol name is 1 – 8 characters, where the first character must be uppercase alphabetic (A-Z) or special ($, #, @). The remaining characters (up to 7) can be any combination of uppercase alphabetic, numeric (0-9), or special.
  A symbol value is limited to 255 characters. Multiple symbol names and values can be specified, up to a limit of 128.
  For example:
  ```json
  {
    "symbol1": "value1",
    "symbol2": "value2"
  }
  ```

- **job_search_rc**
  A string or a regular expression specifies the part of return code you expected to be matched. The default value is "CC 0000".
  - when `job_search_logic` is set to `AND`, the role will fail if the return code doesn't match the string or the regular expression.
  - when `job_search_logic` is set to `OR`, the role will continue to check the job output even the return code doesn't match the string or the regular expression.

- **job_search_output**
  A string or a regular expression specifies the part of job output you expected to be matched. Use `job_search_output_ddname` to specify the spool file list in which you want to do the match work.
  - when `job_search_logic` is set to `AND`, if the match of return code is failed, then the match of job output step will be bypassed, and the role will be failed.

- **job_search_output_ddname**
  An array specifies the list of spool files in which the match work will be done. This variable only take effects when `job_search_output` is set. 
  - If this variable is omitted, all spool files will be compared with `job_search_ouput`.
  - Or only spool files listed in this variable will be compared with `job_search_output`.
  An example of this variable:`["JESMSGLG","JESJCL"]`.

- **job_search_output_insensitive**
  Specifies whether the comparation of `job_search_output` is case insensitive. Default value is "True".
  - **True**
  - **False**

- **job_search_output_maxreturnsize**
  An integer specifies how many lines from the first matched line will be returned when `job_search_output` is matched in `job_search_output_ddname`. Default value is 100.

- **job_search_logic**
  Specifies the logic between the check of job return code and job output. This vairable only take effects when `job_search_ouput` is specified. Default option is "AND"
  - **AND**
    The role runs successfully only both return code and job output are matched with `job_search_rc` and `job_search_output`.  
    The role will fail when matching of `job_search_rc` fails and the remain matching step for `job_search_output` will be ignored.
  - **OR**
    Both matching step of `job_search_rc` and `job_search_ouput` will be run no matter whether the matching is successful. The role will fail only if both matching step of are `job_search_rc` and `job_search_ouput` failed.

- **complete_check_times** - The maximum number of time that is used for periodic checks of the job status.

- **complete_check_delay** - The interval time between periodic checks of the job status.


## Requirements
See the section [Requirements](../../docs/README_workflow.md#Requirements). 


## Dependencies
None


## Usage
For a sample playbook, see [sample_role_workflow_complete.yml](../../playbooks/sample_role_workflow_complete.yml) in the directory [playbooks](../../playbooks/README.md).


## Test
For a test playbook, see [test_role_workflow_complete.yml](../../tests/workflow/test_role_workflow_complete.yml) in the directory [tests/workflow](../../tests/workflow/README.md).


## Copyright
© Copyright IBM Corporation 2020.