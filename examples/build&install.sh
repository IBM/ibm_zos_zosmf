#!/bin/bash

cd ..

rm -rf ibm-ibm_zos_zosmf*.tar.gz tests/collections/ansible_collections/ibm | true

ansible-galaxy collection build -f

ansible-galaxy collection install ibm-ibm_zos_zosmf-1.0.0.tar.gz -p tests/collections -f
