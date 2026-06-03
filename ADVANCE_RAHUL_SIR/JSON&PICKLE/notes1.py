import json
data='{"one":100,"two":200,"three":300}'
print(type(data))



new_data=json.loads(data)
print(type(new_data))