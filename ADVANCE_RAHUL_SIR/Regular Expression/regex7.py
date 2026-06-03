"""    
Meta Charecter:`
It is charecter which has its own special meaning in python re module 
sytax:~
' \characters+ '

"""

import re

def mult_char_find (test_message,test_pattern):
    for pat in test_pattern:
        print("searching for pattern ->",pat)
        print(re.findall(pat,test_message))

test_message="sdfghjkkvbnm,,,,,,#$%^&**&^%$$######@!@#~!@#$%^ASDFGHJKCVBNDFGHJGHJXCVBNFGH"

# test_pattern=['[a-z]+']
# it will find all the group of all lower case cahrecters

# test_pattern=['[A-Z]+']
# it will find all the group of all upper case cahrecters

# test_pattern=['[0-1]+']
# it will find all the group of all numeric case cahrecters

# test_pattern=['\d+']
# it will find all the group of numeric case cahrecters

# test_pattern=['\D+']
# it will find all the group of charecter except numeric case cahrecters

# test_pattern=['\s+']
# it will find for all the white spaces

# test_pattern=['\S+']
# it will find all the non white spaces

# test_pattern=['\w+']
# it will find all the  of charecter, except special characters

# test_pattern=['\W+']
# it will find all the special charecter, except remaining characters


test_pattern=['[^$@#Ao45]+']
# ^ (caret) :- ^ is considered as a caret symbol, which ignores the specified character to it during runtime







mult_char_find(test_message,test_pattern)

