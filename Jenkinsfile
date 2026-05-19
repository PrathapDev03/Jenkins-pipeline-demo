pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Clone Code') {
            steps {
                echo 'Cloning Repository...'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv $VENV
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Stop Old App') {
            steps {
                sh '''
                pkill -f app.py || true
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                . $VENV/bin/activate
                nohup python3 app.py > output.log 2>&1 &
                '''
            }
        }

        stage('Verify Application') {
            steps {
                sh '''
                sleep 5
                ps aux | grep app.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Application Deployed Successfully!'
        }

        failure {
            echo 'Pipeline Failed!'
        }
    }
}