
"""
[] 
It is used to look for any individual charecter in a given range 

[a-z] :- It will look for any lower case characters between lower case "a" to lower case "z"

[A-Z] :- It will look for any lower case characters between lower case "A" to lower case "Z"

[0-9] :- It will look for any  between integer 0 "0" to integer 9 "9"

Wildcard Charecter (.)
.
dot will bw consider as wildcard charecter in python re module,it can look for any charecter eigther 
lowercase,uppercase,numeric and special charecter , except new line charecter(/n)

"""

import re

data="Kno\nwledge"

res=re.search('Kno.',data) # Match Not Found  . is except new line charecter(/n)

if res!= None:
    print("Match Found ")

else:
    print("Match Not Found ")
    