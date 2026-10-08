pipeline {
    agent any
	parameters {
		choice choices: ['dev', 'test', 'prod'], name: 'UMGEBUNG'
	}
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
	stage('Lint') {
		steps {
			echo 'Prüfe Codequalität...'
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
        sstage('Deploy') {
    when {
        expression { params.UMGEBUNG == 'prod' }
    }
    steps {
        echo 'Deploye...'
    }
}uccess {
            archiveArtifacts artifacts: 'version.txt'
        }
        failure {
            echo 'Build fehlgeschlagen!'
        }
    }
}
