"""  
Regular
> it is a inbuilt module present in python
> This Module help us to search for the given pattern , is present in the given location or not 
syntex:
import re
var=re.search(Par1,Par2)
Par1:- Pattern To Search
Par2:- Location to Search

search() method:-
> search method accept patten to search 1st , location to search as 2nd parameter
> if the pattern is found in given location it return the span details or its retun none
> Pattern can find anyway in given location , either at begging or at middle or at last

sapn() Method:-
> This method return the start and end index of given pattern ,from where to where it is present
 in given location
> res.span()

"""

import re

data=" I am not the danger , i am the danger , now say my name "

res=re.search("he",data) # search() the pattern

if res!=None:
    print("Match Found",res.span()) # span() gives index of pattern

else:
    print("Match not found")