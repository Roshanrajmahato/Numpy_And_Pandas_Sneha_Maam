import pickle

data={"name": "roshan", "age": 16, "degree": "Btech", "skill": "Everything", "extra_skill": ["fliarting", "dancing", "singing"]}


print(type(data))

# pickling the data (serializtion->sending or saving)
pickled_data=pickle.dumps(data)
print(type(pickled_data))
print(pickled_data)



# un-pickling the data (desialization-> retriving) 
unpicked_data=pickle.loads(pickled_data)
print(type(unpicked_data))
print(unpicked_data)

