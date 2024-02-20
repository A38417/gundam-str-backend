import random
import time

import requests
import json


data = []
url = "http://127.0.0.1:8000/api/product/"


headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3OTQyNzg5LCJpYXQiOjE3MDUzNTA3ODksImp0aSI6IjBiYzE5MjUzNDNjYjQ2MGZiNmU2MTNkZDdlNGY4ZjVmIiwidXNlcl9pZCI6MX0.CVFEfXFSgWTuK9uL0fcG5ozoO41EkzbexlkikBF_zCg'
}


with open("data.json", "r+", encoding='UTF-8') as jsonFile:
    data = json.load(jsonFile)

for item in data:
    payload = json.dumps({
      "name": item['name'],
      "img": item['img'],
      "price": item['price'],
      "description": item['description'],
      "quantity": random.randint(1, 50),
      "type": item['type']
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    time.sleep(0.3)
