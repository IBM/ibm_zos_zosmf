#!/bin/bash

cd ../..

rm -rf ibm-ibm_zos_zosmf-1.0.0.tar.gz tests/cpm/collections/ansible_collections/ibm | true

ansible-galaxy collection build -f

ansible-galaxy collection install ibm-ibm_zos_zosmf-1.0.0.tar.gz -p tests/cpm/collections -f