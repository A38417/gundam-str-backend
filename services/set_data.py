import random
import time

import requests
import json


data = []
url = "http://127.0.0.1:8000/api/product/"


headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzExMTg4MjU1LCJpYXQiOjE3MDg1OTYyNTUsImp0aSI6ImExYjIyYjNhNTYyYTRjNWE4YzBmNmM1ZGJkNzI4ZDFiIiwidXNlcl9pZCI6MX0.yiCqeCTT_5JpnK4jFF8fqzUjpXi12JvS1DZg5wMppCk'
}


with open("data3.json", "r+", encoding='UTF-8') as jsonFile:
    data = json.load(jsonFile)

for item in data:
    payload = json.dumps({
      "name": item['name'],
      "img": item['img'],
      "price": item['price'],
      "description": item['description'],
      "quantity": random.randint(1, 100),
      "type": item['type']
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    time.sleep(0.3)
