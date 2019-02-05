pipeline {
    agent {
        docker { image 'python:3.7.2-alpine3.8' }
    }

    stages {
        stage("Install dependencies") {
            steps {
                echo 'Preparing environment..'
                pip install pytest
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                pytest tests/test_basic_assert.py
            }
        }
    }
}