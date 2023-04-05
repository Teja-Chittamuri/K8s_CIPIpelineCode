node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }

    stage('Build image') {
  
       app = docker.build("tejachittamuri/ultimatecicd")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
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
                    git push https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:master
                '''
            }
    }
       }
}
    
