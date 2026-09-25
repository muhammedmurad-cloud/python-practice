data = [
    {
        "name": "Ali",
        "age": 19,
        "city": "Baku"
    },
    {
        "name": "Murad",
        "age": 17,
        "city": "Ganja"
    },
    {
        "name": "Leyla",
        "age": 20,
        "city": "Baku"
    }
]

file_name = "users.json"
import json
with open(file_name,"w") as file:
    json.dump(data,file,indent=4)
with open(file_name,"r") as file:
    data = json.load(file)
city = input("Enter the city:")    
for user in data:
        if user["city"] == city:
             print(user)