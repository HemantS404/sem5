import json

data = None

with open('8.json', 'r') as f:
    data = json.load(f)
print(data)

for i in data['users']:
    if i['id'] == 2:
        print(i)

data['users'].append({'id':4, "name":"Sahil", 'age':20})
with open('8.json', 'w') as f:
    json.dump(data, f)
print(data)

for i in data['users']:
    if i['id'] == 4:
        i['age'] = 26
with open('8.json', 'w') as f:
    json.dump(data, f)
print(data)

data['users'] = [user for user in data['users'] if user['id'] != 4]
with open('8.json', 'w') as f:
    json.dump(data, f)
print(data)