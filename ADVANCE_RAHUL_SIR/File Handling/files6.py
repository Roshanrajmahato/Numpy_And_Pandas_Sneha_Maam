try:
    with open("info.txt","r") as fh:
        if fh.readline():
            print(fh.readline())# reads only first 

            print(fh.readlines())
 
except FileNotFoundError as fe:
    print(fe)