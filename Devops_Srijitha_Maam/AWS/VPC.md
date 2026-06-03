🌐 What is a VPC in AWS?

A VPC (Virtual Private Cloud) in Amazon Web Services is your own private network inside the AWS cloud.
It allows you to:
Define your own IP address range
Create subnets (public & private)
Control routing
Attach Internet Gateway
Set security (Security Groups & NACL)

Think of it as your virtual data center inside AWS.

🏗️ Step-by-Step: VPC Creation in AWS

We will create:
1.VPC,2.Subnets (Public + Private),3.Internet Gateway,4.Route Table

Associate Public Subnet with Internet
🔹 STEP 1: Create VPC
1️⃣ Login to AWS Console

Go to:
👉 AWS Console → Search VPC

2️⃣ Click → “Create VPC”

Choose:

VPC only

Name: My-VPC

IPv4 CIDR Block: 10.0.0.0/16

Tenancy: Default

📌 What does 10.0.0.0/16 mean?

It allows 65,536 IP addresses

Large enough for multiple subnets

Click → Create VPC

✅ VPC Created

🔹 STEP 2: Create Subnets

Now we divide VPC into smaller networks.

🌍 Create Public Subnet

Go to Subnets

Click → Create Subnet

Select:

VPC: My-VPC

Name: Public-Subnet

Availability Zone: ap-south-1a (or your region)

CIDR: 10.0.1.0/24

Click → Create

📌 /24 means:

256 IP addresses

Good for web servers

🔒 Create Private Subnet

Repeat same steps:

Name: Private-Subnet

AZ: ap-south-1b

CIDR: 10.0.2.0/24

Click → Create

✅ Now you have 2 subnets.

🔹 STEP 3: Create Internet Gateway (IGW)

Public subnet needs internet.

Go to Internet Gateways

Click → Create

Name: My-IGW

Click Create

Now:

👉 Select IGW
👉 Click Attach to VPC
👉 Choose My-VPC

✅ Internet Gateway attached

🔹 STEP 4: Create Route Table for Public Subnet

Now we allow internet access.

Go to Route Tables

Click → Create

Name: Public-Route-Table

Select VPC → My-VPC

Click Create

Add Route to Internet

Select Route Table

Click → Edit Routes

Add Route:

Destination	Target
0.0.0.0/0	My-IGW

Click Save

📌 0.0.0.0/0 means:
→ Allow all internet traffic

Associate Route Table with Public Subnet

Go to Subnet Associations

Click → Edit

Select Public-Subnet

Save

✅ Now Public Subnet has internet access.

🔹 STEP 5: Private Subnet Setup

Private subnet:

Do NOT attach IGW

No route to 0.0.0.0/0

It stays private.

If you want internet for updates:
→ You create NAT Gateway (optional step)

📊 Final Architecture
                Internet
                   |
              Internet Gateway
                   |
            Public Route Table
                   |
         ------------------------
         |                      |
  Public Subnet         Private Subnet
  10.0.1.0/24           10.0.2.0/24

🔐 Security Layer

After this, when launching EC2:

Public subnet → Web Server

Private subnet → Database

Use:

Security Groups

NACL

🎯 Real Interview Explanation (Important)

If interviewer asks:

👉 How VPC works?

Answer:

VPC is a logically isolated network inside AWS.
We define CIDR range, create subnets across AZs, attach Internet Gateway for public access, configure route tables for traffic flow, and use security groups for access control.