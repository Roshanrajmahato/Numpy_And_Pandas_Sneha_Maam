"""
Syntex:

try:
Doughtful Code Or Risky Code 

except:




"""

print("Program Started ")
try:
    x=10
    y=0
    print(x//y)
except ZeroDivisionError:
    print("Denometor cannot be zero")

except TypeError:
    print("Denomerator Cannot be Sting")

print("Program Ended")