# Ansible role: zmf_workflow_complete
The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), which is referred to as `zmf_workflow_complete`. This role is used for completing a z/OS workflow, either forcibly or idempotently.


## Role variables
The available role variables are described as follows.

The following variables are defined by role. For the default values, see [defaults/main.yml](defaults/main.yml).

- job_jcl_src
- job_jcl_location
  - LOCAL(default)
  - DATASET
  - USS
- job_internal_reader_class
- job_internal_reader_recfm
- job_internal_reader_lrecl
- job_interanl_reader_mode
  - TEXT(default)
  - BINARY
  - RECORD
- job_user_correlator
- job_symbols
    dictionary
    ```json
    {
      "symbol1": "value1",
      "symbol2": "value2"
    }
    ```
- job_search_rc
    string/regex (default='CC 0000')
- job_search_output
    string/regex
- job_search_output_ddname
    array
    `["JESMSGLG","JESJCL"]`
- job_search_output_insensitive
  - True (default)
  - False
- job_search_output_maxreturnsize
    int (default=100)
- job_search_logic
  - AND (default)
  - OR
- `complete_check_times` - The maximum number of time that is used for periodic checks of the workflow status.
- `complete_check_delay` - The interval time between periodic checks of the workflow status.

## Copyright
© Copyright IBM Corporation 2020