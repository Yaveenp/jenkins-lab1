def call() {
    pipeline {
        agent any
        stages {
            stage('Run Second Job') {
                steps {
                    echo 'Hello from jenkins-lab1/jenkinsfile.groovy'
                }
            }
        }
    }
}
