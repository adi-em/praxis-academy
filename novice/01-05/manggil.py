import json

buka = open("01-05/database.json")

data = json.dumps(buka.read())

print(data)