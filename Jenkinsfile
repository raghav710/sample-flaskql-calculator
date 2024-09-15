pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/raghav710/sample-flaskql-calculator'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'pip install Flask pytest'
            }
        }
        stage('Build and Test') {
            steps {
                bat 'python -m pytest'
            }
        }
    }
}