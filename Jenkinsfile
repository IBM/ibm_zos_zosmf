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
		echo 'Jobapi BVT test24'
		dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks") {
		    sh "sed -i '' 17,18d /Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks/hosts"
		    sh "sed -i '' 5,6d /Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks/hosts"
                    sh "sed -i '' 's/zosmf1.ibm.com/pev211.pok.ibm.com/g' ~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks/hosts"
                    sh '/usr/local/bin/ansible-playbook ~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks/sample_role_job_complete.yml'
		}
            }
        }
    }
}
