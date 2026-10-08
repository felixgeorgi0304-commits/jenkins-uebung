pipeline {
    agent any
    parameters {
        choice choices: ['dev', 'test', 'prod'], name: 'UMGEBUNG'
    }
    stages {
        stage('Build') {
            steps {
                echo "Umgebung: ${params.UMGEBUNG}"
                sh 'echo "Version 1.0" > version.txt'
            }
        }
        stage('Lint') {
            steps {
                echo 'Prüfe Codequalität...'
            }
        }
        stage('Test') {
            steps {
                echo 'Teste...'
            }
        }
        stage('Deploy') {
            when {
                expression { params.UMGEBUNG == 'prod' }
            }
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
