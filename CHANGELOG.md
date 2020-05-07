# Changelog
All notable changes to this project will be documented in this file.

## [v1.0.3](https://github.com/IBM/ibm_zos_zosmf/releases/tag/v1.0.3) - 2020-05-10
### Fixed
- changed role names: `zmf_cpm_provision_software_service`, `zmf_cpm_manage_software_instance`, `zmf_cpm_remove_software_instance`

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
- add roles: `complete_workflow`, `zmf_cpm_provision_software_service`, `zmf_cpm_manage_software_instance`, `zmf_cpm_remove_software_instance`
