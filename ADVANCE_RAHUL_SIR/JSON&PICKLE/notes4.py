import json

try:
    with open("info.json","r") as fh :
        if fh.readable():
            load_data=json.load(fh)#load the data from "fh ", file variale (for info.json file) in the load_data
            print(type(load_data))
            print(load_data)

except FileNotFoundError as fe:
    print(fe)