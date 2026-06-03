try:
    fh=open("info.txt",'r')
    if fh.readable():
        position=fh.tell()

        print(position) # It current cursor position 0
    
        print(fh.read(7)) # from 0 position it read to 7 charector

        fh.seek(12) # it helps to move the cursor from position 7 to 12 

        print(fh.read()) # It will read all the charecter from current 12 position

except FileNotFoundError as fe:
    print(fe)
  