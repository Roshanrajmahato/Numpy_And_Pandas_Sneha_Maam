"""  
Take file and read the word start with a and ends with e

"""
import re
try:
    with open("read.txt","r") as fh:
        if fh.readable():
            print(re.findall(r"\bA\w*e\b",fh.read(),re.IGNORECASE))
except Exception as e:
    print(e)

"""   
\bA :- start with A 
\w* :- except special chareter
e\b :- end with e
re.IGNORECASE :- wheither upercase or lowercase

"""