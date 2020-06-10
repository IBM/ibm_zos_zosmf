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
                /** sh 'git clone git@github.ibm.com:lqibj/zmf-ansible.git' */
                sh '/usr/local/bin/ansible-galaxy collection build'
                sh 'cd ~/.ansible/collections/ansible_collections/ibm/ibm_zos_zosmf/playbooks'
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
                echo 'Hello, Test5'
                echo 'run playbook'
		sh 'pwd'
                sh '/usr/local/bin/ansible-playbook sample_role_job_complete.yml'
            }
        }
    }
}
