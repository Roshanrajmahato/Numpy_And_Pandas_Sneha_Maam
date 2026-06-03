""" Progrom to count of vowel in a text file """

try:
    with open("info.txt","r") as fh:
        if fh.readable():
            cnt=0
            for i in fh.read():
                if i in "aieouA" :
                    cnt+=1
            print(f"Total no of Vowel")
                    

except FileNotFoundError as fe:
    print(fe)