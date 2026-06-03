try:
    fh=open("info.txt",'r')
    if fh.readable():
        print(fh.read(5)) # It will read 5 character from 0 position
    
        print(fh.read()) # It will read all the charecter from current cursor position

except FileNotFoundError as fe:
    print(fe)