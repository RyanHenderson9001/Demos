import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('The people in space are currently')
for person in json['people']:
    print(person['name'])