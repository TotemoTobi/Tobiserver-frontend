pipeline {
agent { label 'ubuntu' }
    stages {
        stage('build') {
            steps {
                sh 'python IPpinger.py'
            }
        }
    }
}
