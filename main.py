import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "178"
AGE = "28"
BEARER = "Bearer Sheety"

NUTX_ID = "your nutx_id"
NUTX_KEY = "your nutx key"

SHEETY_KEY ="sheety key"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_KEY}/workoutTracking/workouts"
question_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTX_ID,
    "x-app-key": NUTX_KEY,
}

parameters = {
    "query": question_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
finished_query = response.json()
exercises = finished_query["exercises"]

for exercise in exercises:
    headers_sheet = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": round(exercise["duration_min"]),
            "calories": round(exercise["nf_calories"]),
        }
    }
    header = {
        "Authorization": BEARER
    }


    update = requests.post(SHEETY_ENDPOINT, json=headers_sheet, headers=header)

    print(update.text)


