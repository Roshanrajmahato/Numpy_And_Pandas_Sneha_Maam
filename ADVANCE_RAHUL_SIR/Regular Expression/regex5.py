"""
{int}
It is used to check the specified charecter is exactly present for 
specified number of occurance of not.

re.search("but{2}er",data) :- "t" should be present only 2 times

import  re

data="colourful butterflies"
res=re.search("but{2}er",data)
# it will look for charecter that is exactly present for 2 occurance or not
# re.search("but{2}er",data) :- "t" should be present only 2 times
if res!=None:
    print("Match Found")

else:
    print("Not found")


"""

"""  
? 
It will look for specified charecter is present or not 
or 
it will check the previous charecter is present for 0 or 1 occurance only

"""

import  re

data="colorful butterflies"
res=re.search("colou?r",data)
# it will look for prevoius charecter(u) that is exactly present for 0 or 1 times 
# re.search("colou?r",data) :- "u" should be present only 0 or 1 times

if res!=None:
    print("Match Found")

else:
    print("Not found")