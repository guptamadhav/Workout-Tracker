import requests
import datetime
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
body = {
    "query": input("Tell me which exercise you did")
}
response = requests.post(url=exercise_endpoint, json=body, headers=headers)
data = response.json()["exercises"]

for i in data:
    print(i["name"])
    print(i["duration_min"])
    print(i["nf_calories"])
date = datetime.datetime.now().strftime("%d/%m/%y")
time = datetime.datetime.now().strftime("%H:%M:%S")

sheety = os.environ.get("SHEETY")
headers_sheety = {"Authorization": os.environ.get("TOKEN")}
for i in data:
    body = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": i["name"],
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }
    add = requests.post(url=sheety,json=body, headers=headers_sheety)

