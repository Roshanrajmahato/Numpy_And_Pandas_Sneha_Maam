try:
    with open("new.txt","a") as fh:
          if fh.writable():
               fh.write("\n i am not in danger , I am the Danger , Now say my name")
               fh.write("And My Name is Danger Roshan")

except FileNotFoundError as fe:
    print(fe) 