# Changelog
All notable changes to this project will be documented in this file.

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
