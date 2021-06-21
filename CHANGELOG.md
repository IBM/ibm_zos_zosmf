# Changelog
All notable changes to this project will be documented in this file.

## [v3.0.0](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v3.0.0) - 2021-06-20
### Removed
- remove module: `zmf_workflow`: use `ibm.ibm_zosmf.zmf_workflow` instead
- remove role: `zmf_cpm_provision_software_service`: use `ibm.ibm_zosmf.zmf_cpm_provision_software_service` instead
- remove role: `zmf_cpm_manage_software_instance`: use `ibm.ibm_zosmf.zmf_cpm_manage_software_instance` instead
- remove role: `zmf_cpm_remove_software_instance`: use `ibm.ibm_zosmf.zmf_cpm_remove_software_instance` instead

## [v2.5.0](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.5.0) - 2021-03-05
### Added
- add modules: `zmf_dataset`, `zmf_file`
- enhance for module: `zmf_dataset_copy`: support to copy file or data set from z/OS system
- enhance for role: `zmf_cpm_provision_software_service`: add input_vars parameter for CPM provision role, add zmf_body parameter for using playbook in full automation

## [v2.4.0](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.4.0) - 2020-12-30
### Added
- add modules: `zmf_dataset_copy`, `zmf_file_copy`
### Fixed
- fix for role `zmf_workflow_complete`: refine final_result
- fix for module `zmf_console_command`: console_cmdresponse_reg and console_broadcastmsg_reg should be bool type

## [v2.3.0](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.3.0) - 2020-12-18
### Added
- add modules: `zmf_dataset_fetch`, `zmf_file_fetch`

## [v2.2.1](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.2.1) - 2020-09-23
### Fixed
- fix for module `zmf_console_command`: conflict route params
- fix for module `zmf_console_command`: os issue when save output to local with python2.7
- fix for roles `zmf_job_complete`, `zmf_job_query`: overridden matched contents

## [v2.2.0](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.2.0) - 2020-08-21
### Added
- add modules: `zmf_authenticate`
- support to save job output on Ansible control node for roles: `zmf_job_complete`, `zmf_job_query`
- support to save command response on Ansible control node for module: `zmf_console_command`

## [v2.1.0](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.1.0) - 2020-07-14
### Added
- add modules: `zmf_console_command`

## [v2.0.1](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.0.1) - 2020-05-29
### Added
- support to search job output for roles: `zmf_job_complete`, `zmf_job_query`

## [v2.0.0](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v2.0.0) - 2020-05-21
### Added
- add roles: `zmf_job_complete`, `zmf_job_query`
- support a doc site for collection
### Refined
- refine and rename module `workflow` to `zmf_workflow`
- rename role `complete_workflow` to `zmf_workflow_complete`
- rename role `provision_software_service` to `zmf_cpm_provision_software_service`
- rename role `manage_software_instance` to `zmf_cpm_manage_software_instance`
- rename role `remove_software_instance` to `zmf_cpm_remove_software_instance`
### Fixed
- cleanup sanity test checks
- add tags

## [v1.0.3](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v1.0.3) - 2020-04-02
### Fixed
- cleanup ansible_lint checks
- cleanup sanity test checks

## [v1.0.2](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v1.0.2) - 2020-03-30
### Fixed
- cleanup ansible_lint checks
- fix bug for cmp roles: instance variable is not correctly parsed in the role

## [v1.0.1](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v1.0.1) - 2020-03-23
### Fixed
- cleanup ansible_lint checks
- fix README links on Galaxy webpage
- add tags

## [v1.0.0](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v1.0.0) - 2020-03-19
### Added
- initial `ibm_zos_zosmf` collection
- add modules: `workflow`
- add roles: `complete_workflow`, `provision_software_service`, `manage_software_instance`, `remove_software_instance`
