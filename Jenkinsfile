pipeline {
    agent none
    
    stages {
        stage('Build') {
            agent {
               node {
                   label 'zmf-ansible-configuration'
                   /* customWorkspace "workspace/${env.BRANCH_NAME}" */
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
		dir("/Users/strangepear2019/ansible_20200609") {
                        sh "pwd"
			sh "rm -rf *"	
			sh 'git clone -b dev git@github.com:IBM/ibm_zos_zosmf.git'
		}
		dir("/Users/strangepear2019/ansible_20200609/ibm_zos_zosmf") {   
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
                   /* customWorkspace "workspace/${env.BRANCH_NAME}" */
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
			sh '/usr/local/bin/ansible-playbook job_complete_test1.yml'
			sh '/usr/local/bin/ansible-playbook sample_role_job_complete.yml'
		}
		echo 'Workflow BVT'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD/playbooks") {
			sh '/usr/local/bin/ansible-playbook sample_role_workflow_complete.yml'
		}
		echo 'CICD test successfully!'
            }
        }
    }
}
