pipeline {
    options {
        ansiColor('xterm')
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
                    sh 'pip isntall -r requirements.txt'
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