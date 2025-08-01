# Using weatherapi.com free api. Go to the website, create an account, select free version, and get your api key
# Use weatherapi.com to figure out the response body for your api key

import requests

city = input('\nEnter the city you want to see the weather of:\n').capitalize()

url = 'http://api.weatherapi.com/v1/current.json?key=9d60488783df4ead94065000250108&q=' + city + '&aqi=no'

response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')


print("\nToday's weather in", city,  "is", description, 'and', temp, 'degrees.\n');