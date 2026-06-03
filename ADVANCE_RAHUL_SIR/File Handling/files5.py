try:

    with open("info.txt",'r') as fh:
        if fh.readable():
            print(fh.read(12)) # It will read 12 character from 0 position
    
except FileNotFoundError as fe:
    print(fe)



# print(fh.read(5)) # error i/o operation on closed file