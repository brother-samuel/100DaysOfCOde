import requests
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BEARER = os.environ.get("BEARER")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("Tell me what kind of exercise you did: ")

parameters = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 95,
    "height_cm": 193,
    "age": 41,
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
response.raise_for_status()
exercise_data = response.json()

today = dt.datetime.now()

sheety_endpoint = os.environ.get("SHEET_ENDPOINT")
sheety_headers = {
    'Authorization': f"Bearer {BEARER}"
}
for exercise in exercise_data["exercises"]:
    sheet_input = {
        "workout" : {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }


upload = requests.post(url=sheety_endpoint, json=sheet_input, headers=sheety_headers)
print(upload.text)