import re
phone="+1-(123)-456-7891"

"""   
Note:- 
+ \+?
1 \d{1,3} :- It will check for numeric value for 1 digit or 3 digit only
-
(
123
)
-
456
-
7891 \d{1,4} numeric 

"""
res=re.search(r"\+?\d{1,3}[-\&]?\(?\d{1,3}\)?[-\&]?\d{1,3}[-\&]?\d{1,4}",phone)
if res!=None:
    print("Valid")

else:
    print("Not valid")

"""    

[-\s]? :- It will check for - or white space for 0 or 1 occurance

\+?  :- It will check character plus is present for 0 or 1 ocuurance only

\d{1,3} :- It will check for numeric value for 1 digit or 3 digit only


"""




