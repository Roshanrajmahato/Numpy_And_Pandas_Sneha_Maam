"""   

Meta Characters:`

\A
It will look for the given pattern is present only at the begginning of given location or not 
Syntax:-
\ACharacters

\Z
It will look for the given pattern is present only at the end of the given location 
Syntax:-
\ZCharacters 


"""

import re

def mult_char_find (test_message,test_pattern):
    for pat in test_pattern:
        print("searching for pattern ->",pat)
        print(re.findall(pat,test_message))

data="Freinds in need is a freiend indeed "

res=re.search('\AFrie',data)
# it will look for the pattern Frie is present at beginning of given location

res=re.search('indeed\Z',data)
# it will look for the pattern indeed is present at end of given location
