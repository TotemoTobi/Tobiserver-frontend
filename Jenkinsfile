pipeline {
agent { label 'ubuntu' }
    stages {
        stage('build') {
            steps {
                sh 'pip install requests'
                sh 'python IPpinger.py'
            }
        }
    }
}
