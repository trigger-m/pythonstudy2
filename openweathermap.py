# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
import requests
import json

city_name = "Moscow"
API_KEY = "90dfe6368da40d53b334d7cd070fc84c"
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

url = api.format(city = city_name, key = API_KEY)
print(url)
response = requests.get(url)
data = response.json()
jsonText = json.dumps(data, indent=4)
print(jsonText)

# jsonからのデータの取り出し　json parser
print("Temperature in Tokyo is: {}".format(data["main"]["temp"]))
print("Main in Tokyo is: {}".format(json.dumps(data["main"],indent=4)))

temp_location = data["main"]["temp"] + 30
print(temp_location)