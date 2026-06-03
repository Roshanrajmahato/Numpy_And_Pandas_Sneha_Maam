import json

data={
'name':"roshan",
'age':16,
'degree':"Btech",
'skill':"Everything",
"extra_skill":["fliarting","dancing","singing"]

}

try:
    with open("info.json","w") as fh :
        if fh.writable():
            json.dump(data,fh)#Take a value from "data" and dump into a "fh " file variale (info.json)
            print("Data Is Dump")



except FileNotFoundError as fe:
    print(fe)