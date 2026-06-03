"""   
Program to connect external text file and read only the numeric data only fron regular expression


"""
import re
try:
    with open("read.txt","r") as fh:
        if fh.readable():
            print(re.findall(r'\d+',fh.read()))
except Exception as e:
    print(e)