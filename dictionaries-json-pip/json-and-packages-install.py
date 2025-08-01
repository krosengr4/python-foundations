# pip is used to install packages from the Python Package index
# To install the requests package, run 'pip3 requests' in the terminal
import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

print('\nThe people currently in space are:')
for person in json['people']:
    print(person['name']);

print('');