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
                sh 'git clone git@github.ibm.com:lqibj/zmf-ansible.git'
                sh 'ansible-galaxy collection build'
                sh '/usr/local/bin/ansible-galaxy collection install ibm-ibm_zos_zosmf-1.0.0.tar.gz -p tests/workflow/collections'
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
                echo 'Hello, Test1'
                echo 'run playbook'
                sh 'cd tests/workflow'
                sh 'ansible-playbook test_module_check.yml'
            }
        }
    }
}
