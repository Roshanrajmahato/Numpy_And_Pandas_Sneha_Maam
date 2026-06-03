""" Read the specific line from a file"""

try:
    with open("info.txt","r") as fh:
        num=int(input("Enter the line number to read :"))
        if fh.readable():
            res=fh.readlines()
            try:
                print(res[num-1])
            except IndexError:
                print("No Spe")
except IndexError:
    print("There is no given specified line number")