# IBM z/OS Management Facility Collection

This collection has been slated for deprecation and will no longer be updated or supported.

Components related to Workflows and Cloud Provisioning and Management have been migrated to the new ibm_zosmf collection in [Galaxy](https://galaxy.ansible.com/ibm/ibm_zosmf) and [Ansible Hub](https://cloud.redhat.com/ansible/automation-hub/repo/published/ibm/ibm_zosmf). If you would like to see specific new functionality added to this collection please reach out to travis.biro@ibm.com and zhuxiaoz@cn.ibm.com.

For solutions involving z/OS job, data set, USS file and command operations IBM recommends that clients use the [ibm_zos_core](https://galaxy.ansible.com/ibm/ibm_zos_core) collection.


**IBM z/OS Management Facility (z/OSMF) Collection**, referred as **ibm_zos_zosmf**, consists of modules and roles that you can use with z/OS.

**IBM z/OSMF collection** intends to allow Ansible to drive z/OS operations via z/OSMF RESTful services, such as z/OS jobs REST services, z/OS console REST services, z/OS data set and file REST services etc.


## Features

**IBM z/OSMF collection** includes [modules](https://github.com/IBM/ibm_zos_zosmf/tree/master/plugins/modules/), [roles](https://github.com/IBM/ibm_zos_zosmf/tree/master/roles/), [sample playbooks](https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/) and `ansible-doc` to automate tasks on z/OS.

For guides and reference, see [Docs Site](https://ibm.github.io/ibm_zos_zosmf/index.html).

For a quick approach to set up z/OSMF dependencies for z/OSMF collection **ibm_zos_zosmf**, please refer to [here](https://github.com/IBM/ibm_zos_zosmf/tree/master/docs/zmf_sample_conf/README.md).

Check out the sample Ansible playbooks for automating 3 different z/OS use case [here](https://github.com/IBM/ibm_zos_zosmf/tree/master/playbooks/use_cases/).

If you want to use z/OSMF Workflow or CP&M functions, please use [ibm_zosmf](https://github.com/IBM/ibm_zosmf) collection.

## Copyright
© Copyright IBM Corporation 2020


## License
Some portions of the collection are licensed under [GNU General Public License, Version 3.0](https://opensource.org/licenses/GPL-3.0), and other portions of the collection are licensed under [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0). See individual files for applicable licenses.


## Author Information
**IBM z/OSMF collection** is maintained by the IBM z/OSMF development team. For more information about z/OSMF， see [IBM z/OSMF One Stop Hub](https://ibm.github.io/zOSMF/).