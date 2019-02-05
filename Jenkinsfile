pipeline {
    agent { dockerfile true }

    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'pytest tests/test_basic_assert.py'
            }
        }
    }
}