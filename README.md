# IBM z/OS Management Facility Ansible Collection
The IBM z/OS Management Facility Ansible collection, referred to as `ibm_zos_zosmf`, is an Ansible collection consisting of modules and roles to work with z/OS based on z/OS Management Facility (z/OSMF).


## Technical Overview
This project intends to allow Ansible to drive z/OS operation and configuration through manipulating z/OS resources and data based on z/OSMF RESTful services, e.g. z/OSMF workflow services, cloud provisioning services, z/OS jobs REST interface, z/OS data set and file REST interface, etc.

### Configure z/OS System and z/OSMF Server
The target z/OS systems should be configured as the target hosts (managed nodes) in playbook. It doesn’t matter whether z/OSMF server is installed on these z/OS systems, but there should be at least one z/OSMF server installed on any z/OS system in the same sysplex. 

The information of z/OSMF server should be configured in vars file, including the hostname, port number, and authentication info. Both username/password and client-certificate are supported for authenticating with z/OSMF server, and client-certificate will be used first if both of them are supplied.


## Contents
- [Manipulate z/OS Workflows](docs/README_workflow.md)
    - module - [workflow](docs/README_workflow.md#Modules)
    - role - [complete_workflow](docs/README_workflow.md#Roles)


## Installation
This collection is distributed via [Ansible Galaxy](https://galaxy.ansible.com/). You can use the [ansible-galaxy](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html) command to install the collection on your control node:

```
ansible-galaxy collection install ibm.ibm_zos_zosmf
```

By default, the collection is installed in `~/.ansible/collections`. The example output looks like:

```
Process install dependency map
Starting collection install process
Installing 'ibm.ibm_zos_zosmf:1.0.0' to '/Users/user/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf'
```

You can also use the `-p` option with [ansible-galaxy](https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html) command to specify the installation path:

```
ansible-galaxy collection install ibm.ibm_zos_zosmf -p /myAnsible/collections
```

### Local Build and Installation
For local build and installation, you can clone the Git repository, build the collection archive and install locally without Galaxy.

1.  Clone the Git repository:
    ```
    git clone git@github.com:ibm/ibm_zos_zosmf.git
    ```

2.  Run local build inside the collection:
    ```
    cd ibm_zos_zosmf
    ansible-galaxy collection build
    ```

    The example output looks like:
    ```
    Created collection for ibm.ibm_zos_zosmf at /Users/user/git/ibm/ibm_zos_zosmf/ibm-ibm_zos_zosmf-1.0.0.tar.gz
    ```

3.  Install the locally built collection:
    ```
    ansible-galaxy collection install ibm-ibm_zos_zosmf-1.0.0.tar.gz
    ```

    The example output looks like:
    ```
    Process install dependency map
    Starting collection install process
    Installing 'ibm.ibm_zos_zosmf:1.0.0' to '/Users/user/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf'
    ```


## Usage
Please refer to directory [examples](examples/README.md) for various example playbooks.


## Contributing
Please refer to [CONTRIBUTING.md](CONTRIBUTING.md).


## Copyright
© Copyright IBM Corporation 2020


## License
Some portions of this collection are licensed under [GNU General Public License, Version 3.0](https://opensource.org/licenses/GPL-3.0), and other portions of this collection are licensed under [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0). See individual files for applicable licenses.

## Author Information
This collection is maintained by the IBM z/OSMF development team. For more information about z/OSMF, visit the following website: https://ibm.github.io/zOSMF/