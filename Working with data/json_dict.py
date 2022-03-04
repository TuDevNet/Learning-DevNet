import json

with open("d:\Cyber Security\Programming\Python program\Working with data\json_sample.json") as data:
    json_data = data.read()
    
json_dict = json.loads(json_data)
print(json_dict)