def remoteWorkspace = ''

pipeline {
	agent none
	
	options {
		// Skip checking out code from source control by default in the agent directive
		skipDefaultCheckout()
		// Disallow concurrent executions of the Pipeline
		disableConcurrentBuilds()
		// only keep 15 builds to prevent disk usage from growing out of control
		buildDiscarder(
			logRotator(
				daysToKeepStr: '15',
				numToKeepStr: '15',
			)
		)
   
	}
	
	stages {
		stage('Build') {
			agent {
				node {
					label 'zmf-ansible-configuration'
					customWorkspace "workspace/${env.BRANCH_NAME}"
				}
			}
	steps {
		echo 'Hello, build'
		sh "pwd"
		sh '/usr/local/bin/ansible --version'
		dir("/Users/strangepear2019/.ansible") {
			sh "pwd"
			sh "rm -rf *"
		}	
		
		checkout scm
		
		script {
			remoteWorkspace = env.WORKSPACE
			
			echo "Remote workspace is ${remoteWorkspace}"
			
			dir("${remoteWorkspace}") {
				if (fileExists('ibm-ibm_zos_zosmf-2.5.0.tar.gz')) {
					echo "ibm-ibm_zos_zosmf-2.5.0.tar.gz existed"
					sh 'rm ibm-ibm_zos_zosmf-2.5.0.tar.gz'
					sh '/usr/local/bin/ansible-galaxy collection build'
				} else {
					sh '/usr/local/bin/ansible-galaxy collection build'
				}
				sh "pwd"
				sh '/usr/local/bin/ansible-galaxy collection install ibm-ibm_zos_zosmf-2.5.0.tar.gz'
			}
		}
            }
        }

        stage('Test') {
            agent {
               node {
                   label 'zmf-ansible-configuration'
                   customWorkspace "workspace/${env.BRANCH_NAME}"
                    }
	    }

            steps {
		echo 'sanity test'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf") {
                     sh "pwd"
	             sh '/usr/local/bin/ansible-test sanity'
	             sh '/usr/local/bin/ansible-lint roles/zmf_job_query'
	             sh '/usr/local/bin/ansible-lint roles/zmf_job_complete'
	             sh '/usr/local/bin/ansible-lint roles/zmf_workflow_complete'
	             sh '/usr/local/bin/ansible-lint roles/zmf_cpm_manage_software_instance'
		     sh '/usr/local/bin/ansible-lint roles/zmf_cpm_provision_software_service'
		     sh '/usr/local/bin/ansible-lint roles/zmf_cpm_remove_software_instance'
                }
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks/host_vars") {
			sh "cp -p /Users/strangepear2019/ansible-tmp/p00.yml /Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks/host_vars/p00.yml"
			sh "cp -p /Users/strangepear2019/ansible-tmp/hosts /Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks/hosts"
		}
		echo 'Jobapi BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook job_complete_CICDtest1.yml'
			sh '/usr/local/bin/ansible-playbook job_complete_CICDtest2.yml'
		}
		echo 'Workflow BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook workflow_complete_CICDtest1.yml'
		}
		echo 'Console BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook console_CICDtest1.yml'
			sh '/usr/local/bin/ansible-playbook console_CICDtest2.yml'
		}
		echo 'DatasetAPI Fetch BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook FVT-Dataset-Fetch-CICD1.yml'
		}
		echo 'FileAPI Fetch BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook FVT-FIle-Fetch-CICD1.yml'
		}
		echo 'DatasetAPI Copy BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook FVT-Dataset-Copy-CICD1.yml'
		}
		echo 'Dataset Create/Rename/Delete/Remote Copy BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook CICDtest_dataset_copy_remote_PDS2PDS.yml'
			sh '/usr/local/bin/ansible-playbook CICDtest_dataset_create_mem.yml'
			sh '/usr/local/bin/ansible-playbook CICDtest_dataset_rename.yml'
			sh '/usr/local/bin/ansible-playbook CICDtest_dataset_delete.yml'
		}
		echo 'FileAPI Create/Rename/changemode/Delete BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook CICDtest_file_create_dir.yml'
			sh '/usr/local/bin/ansible-playbook CICDtest_file_create_file.yml'
			sh '/usr/local/bin/ansible-playbook CICDTest_file_rename_file.yml'
			sh '/usr/local/bin/ansible-playbook CICDtest_file_changemode_dir.yml'
			sh '/usr/local/bin/ansible-playbook CICDtest_file_delete_dir.yml'
		}
		echo 'CICD test successfully!'
            }
        }
    }
}
