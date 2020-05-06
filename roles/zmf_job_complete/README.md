# Ansible role: zmf_workflow_complete
The collection [ibm_zos_zosmf](../../README.md) provides an [Ansible role](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html), which is referred to as `zmf_workflow_complete`. This role is used for completing a z/OS workflow, either forcibly or idempotently.


## Role variables
The available role variables are described as follows.

The following variables are defined by role. For the default values, see [defaults/main.yml](defaults/main.yml).

- *job_jcl_path:
- job_jcl_location:
  - **local**
  - data_set
- job_internal_reader_class
- job_internal_reader_recfm
  - F
  - v  
- job_internal_reader_lrecl
- job_interanl_reader_mode
  - TEXT
  - BINARY
  - RECORD
- job_user_correlator
- job_symbols
    `{k1: v1, k2: v2}`
- job_expect_rc
- job_expect_output
- job_expect_output_ddname
- job_expect_logic
  - AND
  - OR
- ~~job_expect~~
- `complete_check_times` - The maximum number of time that is used for periodic checks of the workflow status.
- `complete_check_delay` - The interval time between periodic checks of the workflow status.


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