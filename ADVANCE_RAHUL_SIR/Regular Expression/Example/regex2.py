"""

Write a program To check given date is valid or not
YYYY-MM-DD
YYYY/MM/DD

DD/MM/YYYY

"""
import re 
date="98//2085"

res=re.search(r"(0[1-9]|1[0-9]|2[0-9]|[0-1][-/](0[1-9]|1[0-2][-/]\d{4})",date)

if res!=None:
    print("Valid")

else:
    print("In Valid ")


"""   
(0[1-9]|1[0-9]|2[0-9]|[0-1][-/](0[1-9]|1[0-2][-/]\d{4})

It will check for the valid date format as follow 
1. 0[1-9]:- In this first digit must be 0 , second can be anything from 1 to 9,
it will check date from 01 to 09
2. 1[0-9] :- In this first digit must be 1 and second can be anything from 0 to 9,
i will check date from 10 to 19
3. 2[0-9] :- In this first digit must be 2 and second can be anything from 0 to 9,
i will check date from 20 to 29
4. 3[0-1] :- In this first digit must be 3 and second can be 0 or 1,
i will check date from 30 to 31


"""