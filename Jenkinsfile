pipeline {
agent { label 'ubuntu' }
    stages {
        stage('build') {
            steps {
                sh 'python3 IPpinger.py'
            }
        }
    }
}
