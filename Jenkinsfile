pipeline {
    options {
        timestamps()
    }

    agent {
        docker {
            image 'python:3.11-alpine'
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
        stage('Greetings') {
            steps {
                script {
                    sh 'python3 --version'
                }
            }
        }
        stage('Setup') {
            steps {
                script {
                    echo 'Setting up Python environment'
                    sh 'pip install -r requirements.txt --break-system-packages'
                }
            }
        }
        stage('Linting') {
            steps {
                script {
                    echo 'Running linting'
                    sh '''
                    pip install pylint --break-system-packages
                    export PATH=$HOME/.local/bin:$PATH
                    pylint --exit-zero stack.py
                    '''
                }
            }
        }
        stage('Testing') {
            steps  {
                script {
                    echo 'Running tests'
                    sh 'pytohn3 test.py'
                }
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