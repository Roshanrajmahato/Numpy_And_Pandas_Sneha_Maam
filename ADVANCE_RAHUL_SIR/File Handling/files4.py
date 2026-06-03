try:
    fh=open("info.txt",'r')
    if fh.readable():
        print(fh.read(12)) # It will read 12 character from 0 position
    
except FileNotFoundError as fe:
    print(fe)

finally:
    if fh !=None:
        fh.close() # Close() Function 
        print("File Is Closed")

print(fh.read(5)) # error i/o operation on closed file