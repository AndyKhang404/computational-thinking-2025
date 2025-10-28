import json
json_str = '{"name": "Mai", "age": 25, "city": "Hanoi"}'
obj = json.loads(json_str)
print("Tên:", obj["name"])
print("Tuổi:", obj["age"])
print("Thành phố:", obj["city"])
print(json.dumps(obj))