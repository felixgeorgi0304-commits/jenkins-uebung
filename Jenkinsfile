pipeline {
    agent { label 'uebung' }
    options {
        timestamps()
    }
    triggers {
        pollSCM('H/2 * * * *')
    }
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install pytest'
            }
        }
        stage('Test') {
            steps {
                sh 'venv/bin/pytest --junitxml=reports/ergebnisse.xml'
            }
        }
    }
    post {
        always {
            junit testResults: 'reports/ergebnisse.xml', allowEmptyResults: true
        }
        success {
            archiveArtifacts artifacts: 'rechner.py'
        }
    }
}
