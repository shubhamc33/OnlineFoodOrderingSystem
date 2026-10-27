
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat 'py --version'
                bat 'py -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'py -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All automated tests passed!'
        }
        failure {
            echo 'FAILURE: Check the console output.'
        }
    }
}
