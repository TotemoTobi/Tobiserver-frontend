pipeline {
agent { label 'ubuntu' }
    {
        docker { image 'python:3.13.1-alpine3.21' }
    }
    stages {
        stage('build') {
            steps {
                sh 'pip install requests'
                sh 'python IPpinger.py'
            }
        }
    }
}
