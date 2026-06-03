AKIAUOB6V533PJWDFQ7T

V6gBgRleNvnLMYar6X3rflFpa0uTZuMkedm9z17I

ami-07a00cf47dbbc844c
<!--
====== How To Build Iris Project ===========
=========== In EC2 Instances ===============
-->
To Root User
To run command as administrator (root) → sudo 
To interactive login shell   → -i 
<!-- sudo -i -->

To Update system software list
<!-- sudo apt update -y -->


# Install Docker and Docker-compose Inside The EC2
To Install Docker in ubantu entance
<!-- sudo apt install docker.io  -->

To Install Docker Compose in ubantu entance
<!-- sudo apt install docker-compose  -->

To Check The version of docker
<!-- docker --version -->

To Check The version of Docker Compose
<!-- docker-compose --version -->


# Install Git inside the ubuntu EC2 Enstance
To Install Git  in ubantu enstance
<!-- sudo apt install git -->

To Check The version of git
<!-- git --version -->

Set your username in github:
<!--  git config --global user.name "Your Name"  -->
<!--  git config --global user.name "Roshanrajmahato"  -->

Set your email address in github:
<!--  git config --global user.email "your.email@example.com"  -->
<!--  git config --global user.email "roshanrajmahato9204@gmail.com"  -->

To Make Sure Git is Connect
<!--  git config --list  -->

Then Clone the Repository
<!--  git clone https://github.com/Roshanrajmahato/Iris-ML-Project.git  -->

Navigate into the cloned project directory first in ubuntu instance:
<!-- cd Iris-ML-Project   -->

Verify and Check docker-compose file exists:
<!-- ls -la  -->

# To Build images and Run it inside a container Through Docker Compose
To Building Docker image and container through docker compose
1. <!--  docker-compose up -d  (Detach Mode in the Background) -->
1. <!--  docker-compose up  (In the Terminal)  -->
2. <!--  docker-compose down -->

To get the logs of the images 
<!-- docker logs images_name -->
<!-- docker logs iris-frontend -->
<!-- docker logs iris-backend -->

To Start The Container
<!-- docker start 0f60af6450fa -->
<!-- docker start 86521e998f0f -->

Verify Image Was Created
<!-- docker images -->

Run the Docker Container # Port Mapping
<!-- docker run -d -p 8080:80 my-nginx-image -->

To see the container :-
<!-- docker ps -a --> -a :- all the Hidding container( Show all Stopped + running Both Container)

To see Only running the container :-
<!-- docker ps --> Show Only the running container

# How Access It WWW
To Get PUBLIC IP of EC2:-
<!-- curl ifconfig.me --> 
PUBLIC-IP 
OPEN IN BROWSER
<!-- http://<PUBLIC-IP>:3000 -->  for frontend
<!-- http://15.207.116.144:3000 --> like that
<!-- http://*:3000 --> 

<!-- http://<PUBLIC-IP>:5000 --> for backend
<!-- http://13.201.194.147:5000  -->
<!-- http://*:5000 --> 

After Any Changes in code for re-building image and re-container :-

1. <!-- docker compose build --no-cache  --> # Rebuild the image
2. <!-- docker compose up -d  -->
3. <!-- docker compose down  -->

# Files
To Open any File
<!-- cat file_name -->
<!-- cat * -->

To Open and Make Changes in a file
<!-- nano file_name  -->
<!-- nano * -->
<!-- nano docker-compose.yml  -->
Edit it And Then Save It
<!-- CTRL + O  Then Press ENTER -->
To EXIT nano
<!-- CTRL + X -->
Verify the changes in the docker-compose.yml file
<!-- cat docker-compose.yml -->

# For Rebuild the image and Rerun the Container,After The Any Changes in files 
<!--  1. docker-compose build --no-cache       -->
<!--  2. docker-compose up -d   -->
<!--  3. docker-compose down -->

To get the logs of the images 
<!-- docker logs images_name -->
<!-- docker logs iris-frontend -->
<!-- docker logs iris-backend -->

# How Access It WWW
To Get PUBLIC IP of EC2:-
<!-- curl ifconfig.me --> 
PUBLIC-IP 
OPEN IN BROWSER
<!-- http://<PUBLIC-IP>:3000 -->  for frontend
<!-- http://*:3000 --> 

<!-- http://<PUBLIC-IP>:5000 --> for backend
<!-- http://*:5000 --> 


After Any Changes in code for re-building image and re-container :-

1. docker compose up
2. docker compose build --no-cache     # Rebuild the image
3. docker compose down


Devops      Devops      Devops       Devops     Devops
       Devops      Devops      Devops      Devops
Devops      Devops      Devops       Devops     Devops


------------------  Linex  Command -----------------
Print Working Directory
Shows the current directory path you're in
<!-- pwd  -->







-----------------------------------------------------



Docker -------------------------------
---------Start -----------------------
--------------------From -------------
------------------------------Here ---

To see the docker images in my system :-
<!-- docker images -->

To see the container :-
<!-- docker ps -a --> -a :- all the Hidding container( Show all Stopped + running Both Container)

To see Only running the container :-
<!-- docker ps --> Show Only the running container



To pull the images
Container Status :- Only Existed Not Running 
<!-- docker pull hello-world -->
<!-- docker pull ubuntu -->
<!-- docker pull ubuntu:22.04 --> :22.04 :- tag name

To pull the images And running From dockerhub
To run an images from dockerhub:-
Container Status :- Only Existed + Running
<!-- docker run image_names -->
<!-- docker run image_id -->
<!-- docker run hello-world -->
<!-- docker run ubantu -->
<!-- docker run ubantu:22.04 --> :22.04 :- tag name

To Move The images inside the Container Afterthat STATUS is Exist <-- docker ps -a --> 
<!--  docker run -it image_name -->
<!--  docker run -it ubuntu -->
<!--  exit -->

Now images is inside the Container ,Then Start the Container
<!-- docker start container_name -->
<!-- docker start b27931fff65d -->


To Move Inside The Container Or To Go Inside the Container
<!-- docker attach   -->
<!-- docker exec -it container_Name bash -->
Then Get Out From Container 
Ctrl + C or Ctrl+p or Ctrl+q 

To rename the container names:
<!-- docker run --name container_Name  -->
<!-- docker run --name roshan  -->
<!-- docker run --name ubantu  -->


For images of the container Continous Running
<!-- docker run --name  container_name -itd image_name --> -itd :- means interect teminal contious running 
<!-- docker run --name  container_name -itd image_name -->


To Start The Container
<!-- docker start container_name  -->
<!-- docker start container_id -->

To Stop the container 
<!-- docker stop container_name  -->
<!-- docker stop container_id  -->

To delete The Image
<!-- docker rmi images_name -->
<!-- docker rmi images_id -->

To delete The container
<!-- docker rm container_name -->
<!-- docker rm container_id -->


Login DockerHub First 




