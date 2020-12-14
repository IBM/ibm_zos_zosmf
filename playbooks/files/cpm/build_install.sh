#!/bin/bash -eux

# Copyright (c) IBM Corporation 2020

cd ../../..

rm -rf ibm-ibm_zos_zosmf-*.tar.gz || true

ansible-galaxy collection build -f

ansible-galaxy collection install ibm-ibm_zos_zosmf-*.tar.gz  -f
