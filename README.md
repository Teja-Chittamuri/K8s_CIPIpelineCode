What it contains?
=======================

A complete CICD workflow floowed by Gitops pratices using Jenkins and Argo CD.

Tools Required
==========================

Git ===============> To store the Application Src code as well as Application K8s Manifest files.

Jenkins   =================>  To create Jobs to automate the CI and CD process.

Docker    ============ > To build the image and push it to Dockerhub

Kubernetes  ============> To deploy our application as pods using deployment manifests.

Argo CD   ===============> For Continuous Delivery Process

Jenkins Installation
====================
Follow jenkins official docs:https://www.jenkins.io/doc/book/installing/linux/
Once jenkins installtion is completed Install docker using 
 "sudo apt install docker.io -y ".
Once docker is installed add the jenkins user to docker group using " usermod -aG docker jenkins" also update docker.sock permissions using "chmod 666 /var/run/docker.sock".
Then switch to jenkins user using "su jenkins" and run docker cmds like docker images , docker ps to verify whether jenkins user is able to connect docker server or not.


Jenkins Plugins 
======================

1. Github Integration
2. Docker
3. Docker pipeline
4. Parameterized Trigger


Argo CD Installation
==============================

Install Minikube on your machine or if you have your K8s cluster ready deploy argocd on to your cluster.

steps To install Argo CD:
--------------------------
1. minikube start --driver=docker
2. kubectl create ns argocd
3. kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v2.5.8/manifests/install.yaml
4. kubectl get all -n argocd   // To verify the installation
5. kubectl port-forward svc/argocd-server -n argocd 8080:443   // port forwading once this is done you will be able to see your argocd running on "https://localhost:8080"
6. kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" ; echo   // run this cmd on your vs code terminal then you will get a key >> go to your browser and search for encode to decode then decide the key >> You're argocd password is ready.

Configure Argo CD
-------------------
1. Once Argo Cd is up and runnig.
   click on New APP >> Provide the name of your application  >> set the sync policy to "automatic"  >> Add the Github Repo url which argo cd will be keep on continuous Monitoring >> Add the cluster URL  >> click on create.

GitOps CICD Workflow
==============
1. Maintaining two seperate repos for your application code and k8s deployment manifests are considered as GitOps best practices.
2. Once developer push the changes to Git Repo repo then automatic build got triggered which we configured using Github webhooks calls Jenkins to start the CI process.

  Fetch code from SCM >> BUILD the code  >> Test the code  >> Perform SAST using Sonarqube  >> Build Docker Image  >> Push the Image to DockerHUB
  
3. Once the New image version had been pushed to the Dockerub then another job gets triggered which updated the deployment manifest file which is stored in another Git repo.
4. Since we have already configured argo cd on to our K8s Cluster, once the deployment manifest is updated then argocd will automatically sync the configuration that is provided in the manifest file and update the pods.

![image](https://user-images.githubusercontent.com/111578142/230021111-3f1596fc-d9fb-49dc-b5d1-b40f54494ec7.png)
![image](https://user-images.githubusercontent.com/111578142/230021209-783f6156-ca9f-4fbd-9623-b5c1d67fab33.png)

![image](https://user-images.githubusercontent.com/111578142/230019839-6cc093bf-6461-46f6-b85c-43fa5141dbfe.png)


Happy Learning 😊😊

