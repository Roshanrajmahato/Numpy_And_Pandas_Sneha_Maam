"""   
Program to check the given email id is valid or not 


"""

import re

email="Rahul@gamil.com"
res=re.search(r'[a-zA-Z]+@[a-zA-Z]+\.com',email)


email="Rahulraj4532@pyspiders.com"
res=re.search(r'[a-zA-Z0-9]+@[a-zA-Z]+\.com|edu',email)


email="Rahul_Raj3456@tata_nexarc.com"
res=re.search(r'[a-zA-Z0-9_]+@[a-zA-Z_]+\.com|edu|in',email)



if res!=None:
    print("Valid")

else:
    print("Not Valid")