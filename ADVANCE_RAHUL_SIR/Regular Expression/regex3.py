"""   
search for first occurences
findall for duplicate element

findall:~
> It is used to find the given pattern is present in the given location or not 
> This method looks for the given pattern for all the duplicate occurance and collect everything
and store in the form of list
> if the pattern is not found ,it return empty list

syntex:- 
re.findall(par1,par2)


"""

import re

data="dont trouble the trouble ,if you trouble the trouble, trouble troubles you , i am not in trouble"

res=re.findall('trouble',data)

print(res)