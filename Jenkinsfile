pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Version 1.0" > version.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Teste...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploye...'
            }
        }
    }
    post {
        success {
            archiveArtifacts artifacts: 'version.txt'
        }
        failure {
            echo 'Build fehlgeschlagen!'
        }
    }
}
