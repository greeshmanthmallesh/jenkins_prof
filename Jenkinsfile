@Library('jenkins_prof') _
pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/greeshmanthmallesh/jenkins_prof.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t django-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d --build'
            }
        }
    }
}
