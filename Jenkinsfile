pipeline{
    agent any
    environment{
        DOCKER_IMAGE_NAME = 'ultimate-cicd:latest'
        DOCKER_REGISTRY_CREDENTIALS_ID = 'dockerlogin'
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_REGISTRY_CREDENTIALS_ID) {
                        def dockerImage = docker.build(DOCKER_IMAGE_NAME)
                        dockerImage.push("${env.BUILD_NUMBER}")
                    }
                }
            }
        }
        stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
    }
}

