## Jankin Complete Installation Process
1. Installation of Java
As Jinkin is Developed in Java Development , So Jenkins requires Java to run, yet not all Linux distributions include Java by default 

```bash

sudo apt update
sudo apt install fontconfig openjdk-21-jre
java -version

```

2. Long Term Support release
A LTS (Long-Term Support) release is chosen every 12 weeks stable release for that time period. It can be installed from the debian-stable apt repository.

```bash

sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins

```

3. Then Access the Jinkin with its ports(8080) and the ip address of the EC2 Instances 
>runcmd
        > ``  http://<EC2_PUBLIC_IP>:8080   ``
        > ``  http://15.206.68.181:8080     ``
        > ``  http://*:8080   ``

4. Then You Get a Path There :- /var/lib/jenkins/secrets/initialAdminPassword
   And It Asking For PASSWORD 
   So For That 

5. Open EC2 Instance :-
 ` cat /var/lib/jenkins/secrets/initialAdminPassword  `
   Get a Password from Their

6. Now Again Access the Jinkin 
   And Paste it Where Asked For PASSWORD

7. Now Set Your  Username And Password

8. My Jankin Credancial :-
username:- roshanrajmahato
password:- 123456789

Login from that