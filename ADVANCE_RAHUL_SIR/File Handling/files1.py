try:
    fh=open("info.txt",'r')
    print(fh)

except FileNotFoundError as fe:
    print(fe)