"""    
+
it will look for specified charecter for 1 or more Occurrance

*
It will look for specified charecter for 0 or more Occurrance 

"""

import re

def mult_char_find (test_message,test_pattern):
    for pat in test_pattern:
        print("searching for pattern ->",pat)
        print(re.findall(pat,test_message))


test_message="aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbb............bb............aaaaaaaaaaaaabbbb....aaaabbbbbaaaa"
test_pattern="a"
mult_char_find(test_message,test_pattern)

# test_pattern=['a+']
# it will look for char a for 1 or more occurance


# test_pattern=['a*']
# it will look for char a for 0 or more occurance




# test_pattern=['ab+']
# it will look for the combination of a and b, in that a should present for one occurance 
# and b can present for one and more

# test_pattern=['ab*']
# it will look for the combination of a and b, in that "a" should present for 0 occurance 
# and "b" can present for one and more




# test_pattern=['[ab]+']
# it will look for the combination of a and b, in that "a" should present for one and more occurance 
# and "b" can present for one and more

# test_pattern=['[ab]*']
# it will look for the combination of a and b, in that "a" should present for 0 and more occurance 
# and "b" can present for 0 and more