# Access The EC2 Instance From Terminal

1.Go Terminal to the folder where the key exists
<!-- Devops-Private-Key.pem -->
2. Remove ALL inherited permissions
<!-- icacls "Devops-Private-Key.pem" /inheritance:r -->

3. Remove access for ALL common users/groups
<!--                                                         
icacls "Devops-Private-Key.pem" /remove "Authenticated Users"
icacls "Devops-Private-Key.pem" /remove "BUILTIN\Users"
icacls "Devops-Private-Key.pem" /remove "BUILTIN\Administrators"
icacls "Devops-Private-Key.pem" /remove "NT AUTHORITY\SYSTEM"
icacls "Devops-Private-Key.pem" /remove "Everyone"

Copy & Paste

icacls "*" /remove "Authenticated Users"
icacls "*" /remove "BUILTIN\Users"
icacls "*" /remove "BUILTIN\Administrators"
icacls "*" /remove "NT AUTHORITY\SYSTEM"
icacls "*" /remove "Everyone"

-->

5. Give permission ONLY to YOU (read-only)
<!-- icacls "Devops-Private-Key.pem" /grant:r "%USERNAME%:R"  -->

<!-- icacls "*" /grant:r "%USERNAME%:R"  -->


6. For VERIFICATION only (most important step)
<!-- icacls "Devops-Private-Key.pem"  -->
<!-- icacls "*"  -->


✅ Correct output should look like:
Devops-Private-Key.pem YOUR-LAPTOP-NAME\Roshan Raj Mahato:(R)

7. EC2 Instance -> Connect -> Instance Id -> Copy and Paste Example

CONNECT EC2 Instance And Then Open  SSH client.
Copy and Paste
Example:-
<!-- ssh -i "Devops-Private-Key.pem" ubuntu@ec2-13-203-217-86.ap-south-1.compute.amazonaws.com  -->