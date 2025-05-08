pipeline {
    options {
        timestamps()
    }

    agent any

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
                    sh 'ls -la'
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
    }
}