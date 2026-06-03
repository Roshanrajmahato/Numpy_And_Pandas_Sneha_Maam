"""    
Program to check multiple pattern:-



"""


import re

data=" I am not the danger , i am the danger , now say my name "

patterns=['danger','am','name','rahul']

for pat in patterns:
    print("Searching for Pattern ",pat)
    res=re.search(pat,data)
    if res!=None:
        print("Match Found at ",res.span())
    else:
        print("Match Not Found")