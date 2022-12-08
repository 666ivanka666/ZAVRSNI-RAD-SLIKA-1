import requests
import json

from datetime_utils import formatted_date, formatted_time


""" url = "https://weatherdbi.herokuapp.com/data/weather/zagreb"

response = requests.get(url)
data = json.loads(response.text) """

# zagreb_forecast = WeatherForecast("zagreb")

class WeatherForecast:
    def __init__(self, city):
        self.url = f"https://weatherdbi.herokuapp.com/data/weather/{city}"
        self.data = None
        self.send_request()
    
    def send_request(self):
        response = requests.get(self.url)

        self.data = json.loads(response.text)

    def get_formatted_weather_data(self):
        return {
            "location": self.data["region"],
            "current_temperature": self.data["currentConditions"]["temp"]["c"],
            "humidity": self.data["currentConditions"]["humidity"],
            "description": self.data["currentConditions"]["comment"],
            "last_refresh": f"{formatted_date()} {formatted_time()}"
        }
