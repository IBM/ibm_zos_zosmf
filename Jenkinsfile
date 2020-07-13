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
		}
		
		echo "Remote workspace is ${remoteWorkspace}"
		
		dir("${remoteWorkspace}") {   
			sh "pwd"
			sh '/usr/local/bin/ansible-galaxy collection build'
			sh "pwd"
			sh '/usr/local/bin/ansible-galaxy collection install ibm-ibm_zos_zosmf-2.0.1.tar.gz'
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
			sh "cp -p /Users/strangepear2019/ansible-tmp/p03.yml /Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks/host_vars/p03.yml"
			sh "ls -l"
		}
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
                    sh 'sed -i "" "s/SY1.*/P00 zmf_host=pkstp00.pok.stglabs.ibm.com zmf_port=1035/" hosts'
                    sh 'sed -i "" "s/SY2.*/P03 zmf_host=pkstp03.pok.stglabs.ibm.com zmf_port=1035/" hosts'
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
		echo 'console BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook console_CICDtest1.yml'
		}
		echo 'CICD test successfully!'
            }
        }
    }
}
