==================================================
*Maven Installation*
==================================================

🟣 STEP 1 – Install Maven in Server

Run in Jenkins EC2:

```bash

sudo apt update
sudo apt install maven -y
mvn -version

```

🟣 STEP 2 – Install Maven Plugin in Jenkins
Open Jenkins

Manage Jenkins
→ Plugins
    → Available Plugin
        → Search:
            👉 Maven Integration Plugin
            👉 Warnings Plugin
            👉 JUnit Plugin

Install them.

🟣 STEP 3 – Configure Maven Tool

Manage Jenkins
→ Tools
→ Maven Installations
→ Add Maven

Name:
👉 my-maven

Version:
👉 3.9.9 (auto install)

SAVE


==================================================
🔴 Clone the Repository
==================================================

Name:
github-webhook-job

Select → Freestyle Project

STEP 3 – Configure Git Repository

Open Job → Configure

Source Code Management → Git

Repository URL:

https://github.com/your-username/your-repo.git


Branch:

*/main

STEP 4 – Enable GitHub Trigger

Scroll to:

Build Triggers

✅ Check this option:

👉 GitHub hook trigger for GITScm polling

STEP 5 – Add Build Step

Build → Add Build Step → Execute Shell

echo "Webhook Triggered Build"
date


Save the job.

STEP 6 – Configure GitHub Webhook

Go to your GitHub Repository:

👉 Settings → Webhooks → Add Webhook

Payload URL:
http://YOUR_JENKINS_IP:8080/github-webhook/


Example:

http://15.206.68.181:8080/github-webhook/

Content type:
application/json


🔴 JOB 1 – CLONE JOB
==================================================
Purpose

Download code from GitHub to Jenkins workspace.

Steps

New Item
→ Name: clone
→ Freestyle → OK

SCM → Git

Repository URL:

https://github.com/Become-DevOps/DevOpsClassCodes.git


Save → Build Now

What happens internally?

Code stored in:

/var/lib/jenkins/workspace/clone


Nothing compiled yet – ONLY DOWNLOAD.


==================================================
🔴 JOB 2 – COMPILE JOB
==================================================
Purpose

Convert source code to byte code.

Create Job

New Item → compile → Freestyle

SCM → Git
(same repo URL)

Build Step

Invoke top level Maven targets

Maven Version:
👉 my-maven

Goals:

compile


Save → Build Now

🔎 Internal Process

Maven does:

src/main/java → .class files


Created inside:

target/classes

❌ If compile fails?

Reasons:

Syntax error

pom.xml issue

dependency not found

Console output shows exact line.


==================================================
🔴 JOB 3 – CODE REVIEW (PMD)
==================================================
Purpose

Check code quality:

bad coding

unused variables

naming standards

Create Job

New Item → code-review

SCM → Git

Build Step:

Invoke Maven

Goals:

pmd:pmd


Build Now

Output

File created:

workspace/target/pmd.xml


But xml is hard to read.

Convert to Report

Install Plugin:
👉 Warnings Plugin

Post Build Action

Record compiler warning

Tool: PMD
Pattern:

**/pmd.xml


Save → Build

Now you see:

👉 Trend Report
👉 Graph
👉 Issues

==================================================
🔴 JOB 4 – TEST JOB
==================================================
Purpose

Run unit test cases.

Create Job

New Item → test

SCM → Git

Build Step:

Invoke Maven

Goals:

test

If We Build THen ,What happens?

Maven runs:
src/test/java

Reports in:
target/surefire-reports/

Show Report in Jenkins

Install Plugin:
👉 JUnit

Post Build

Publish JUnit result

Path:

target/surefire-reports/*.xml


Save → Build

Now you see:

👉 Test pass/fail
👉 How many cases

==================================================
🔴 JOB 5 – PACKAGE JOB
==================================================
Purpose

Create WAR file for deployment.

Create Job

New Item → package

SCM → Git

Build Step:

Invoke Maven

Goals:

package

Output

Inside workspace:

target/app.war


This is final application.