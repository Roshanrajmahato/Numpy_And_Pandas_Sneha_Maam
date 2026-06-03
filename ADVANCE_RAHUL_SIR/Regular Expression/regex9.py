"""  
\b
It will look for the given pattern is present at beggning or end of each word in given location
syntax:

\bcharacters:
It will look for total of words  it start with the given pattern 

charactes\b:
it look for total no of words of given pattern which is present at the end of each word

"""
import re

def mult_char_find (test_message,test_pattern):
    for pat in test_pattern:
        print("searching for pattern ->",pat)
        print(re.findall(pat,test_message))
data=""


