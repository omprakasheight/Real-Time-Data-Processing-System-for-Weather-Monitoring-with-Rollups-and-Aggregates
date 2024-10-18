import os
import time
import requests
from dotenv import load_dotenv

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 300  # 5 minutes
API_KEY = "6027866698d0c4a0e2b6a0f4218ae673"

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def convert_kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def process_weather_data(data):
    temp_celsius = convert_kelvin_to_celsius(data['main']['temp'])
    feels_like_celsius = convert_kelvin_to_celsius(data['main']['feels_like'])
    main_condition = data['weather'][0]['main']
    timestamp = data['dt']
    return temp_celsius, feels_like_celsius, main_condition, timestamp

def main():
    while True:
        for city in CITIES:
            weather_data = get_weather_data(city)
            if weather_data:
                temp, feels_like, condition, timestamp = process_weather_data(weather_data)
                print(f"City: {city}, Temp: {temp}°C, Feels Like: {feels_like}°C, Condition: {condition}")
                # Implement storage or further processing here
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()

