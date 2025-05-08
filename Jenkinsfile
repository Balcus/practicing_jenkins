pipeline {
    options {
        timestamps()
    }

    agent {
        docker {
            image 'python:3.11'
            args '-u root:root -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp'
            reuseNode true
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
            steps {
                script {
                    sh 'pip install -r requirements.txt --break-system-packages'
                }
            }
        }
        stage('Linting') {
            steps {
                script {
                    sh '''
                    pip install pylint --break-system-packages
                    export PATH=$HOME/.local/bin:$PATH
                    pylint --exit-zero main.py
                    '''
                }
            }
        }
        stage('Run') {
            steps {
                script {
                    sh 'python3 main.py'
                }
            }
        }
        post {
            always {
                script {
                    sh 'echo Testing complete'
                }
            }
        }
    }
}