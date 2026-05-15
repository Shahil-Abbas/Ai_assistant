import requests
import os
from dotenv import load_dotenv 
load_dotenv() 
key = os.getenv("API_KEY") 
API_KEY = key


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    temp = data["main"]["temp"]

    description = data["weather"][0]["description"]

    return f"Temperature is {temp} degree celsius with {description}"