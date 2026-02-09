pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/bgdnchrkschnk/Hillel_aqa_2.git'
            }
        }
        stage('Setting up environment dependencies') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-dev python3-pip python3-venv
                    rm -rf .venv
                '''
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Start Flask') {
            steps {
                sh '''
                    . .venv/bin/activate
                    nohup python3 lesson_13/flask_server.py > flask.log 2>&1 &
                    sleep 3
                '''
            }
        }
        stage('Run tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest -k TestFlaskContent --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}