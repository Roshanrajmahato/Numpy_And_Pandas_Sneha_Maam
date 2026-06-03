try:
    with open("mydata.txt","w") as fh:
        if fh.writable():
            fh.write("This is a write mode of operation")
            fh.write("This Is second line")
except FileNotFoundError as fe:
    print(fe)