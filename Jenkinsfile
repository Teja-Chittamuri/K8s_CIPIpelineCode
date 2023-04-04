
Pipeline{
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
       stage('Update Deployment File') {
        environment {
            GIT_REPO_NAME = "K8s_CDPIpelineCode"
            GIT_USER_NAME = "Teja-Chittamuri"
        }
        steps {
            withCredentials([string(credentialsId: 'githublogin', variable: 'GITHUB_TOKEN')]) {
                sh '''
                    git config user.email "tejschittamuri@gmail.com"
                    git config user.name "Teja Chittamuri"
                    BUILD_NUMBER=${BUILD_NUMBER}
                    sed -i "s/replaceImageTag/${BUILD_NUMBER}/g" deployment.yaml
                    git add .
                    git commit -m "Update deployment image to version ${BUILD_NUMBER}"
                    git push https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:main
                '''
            }
    }
       }
    }
}
    
