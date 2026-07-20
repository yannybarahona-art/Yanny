import json  
#! JSON FILES           
with open("source/example.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)
    print(data.get("name"))
    print(data.get("lastname"))
