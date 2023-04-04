pipeline{
    agent any
    environment{
        DOCKER_IMAGE_NAME = 'tejachittamuri/gitopscicd'
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
            steps{
                script{
                echo "triggering updatemanifestjob"
                build job: 'update_k8manifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
                }
        }
        }
    }
}

