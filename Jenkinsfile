pipeline {
    agent none
    
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
		sh '/usr/local/bin/ansible --version' 
                sh 'git clone -b dev git@github.com:IBM/ibm_zos_zosmf.git' 
                sh '/usr/local/bin/ansible-galaxy collection build'
	        sh '/usr/local/bin/ansible-galaxy collection install ibm-ibm_zos_zosmf-2.0.1.tar.gz'
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
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks/host_vars") {
			sh "touch p00.yml"
			sh 'echo " zmf_user: \"debug26\"" >> p00.yml'
			sh 'echo " zmf_password: \"upup2016\"" >> p00.yml'
			sh "touch p03.yml"
			sh 'echo " zmf_user: \"debug27\"" >> p03.yml'
			sh 'echo " zmf_password: \"upup2016\"" >> p03.yml'
		}
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks") {
		    sh "sed -i '' 17,18d hosts"
		    sh "sed -i '' 5,6d hosts"
                    sh 'sed -i "" "14a\\"$'\n'"P00 zmf_host=pkstp00.pok.stglabs.ibm.com zmf_port=1035
			" hosts'
		    sh 'sed -i "" "15a\\"$'\n'"P03 zmf_host=pkstp03.pok.stglabs.ibm.com zmf_port=1035
			" hosts'
		    sh 'sed -i "" "4a\\"$'\n'"P00 zmf_host=pkstp00.pok.stglabs.ibm.com zmf_port=1035
			" hosts'
		    sh 'sed -i "" "5a\\"$'\n'"P03 zmf_host=pkstp03.pok.stglabs.ibm.com zmf_port=1035
			" hosts'
                    sh '/usr/local/bin/ansible-playbook ~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks/sample_role_job_complete.yml'
		}
		echo 'Jobapi BVT test27'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD") {
			sh '/usr/local/bin/ansible-playbook sample_role_job_complete.yml'
		}
		echo 'Workflow BVT test27'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/tests/CICD") {
			sh '/usr/local/bin/ansible-playbook sample_role_workflow_complete.yml'
		}
            }
        }
    }
}
