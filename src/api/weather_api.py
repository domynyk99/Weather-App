from dotenv import dotenv_values
from datetime import datetime, timedelta
import requests
import json

class WeatherAPI:
    def __init__(self, base_url: str):
        self.observers = []
        
        self.secrets = dotenv_values('.env')
        self.api_key = self.secrets['API_KEY']

        self.base_url = base_url

        self.unit_group = 'metric' #default unit group setting


        print("WeatherAPI class has been initialized.")

    def get_weather(self, location: str):
        date_1 = datetime.now().strftime('%Y-%m-%d')
        date_2 = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
        api_url = f"{self.base_url}{location}/{date_1}/{date_2}?key={self.api_key}"\
            f"&unitGroup={self.unit_group}"
    
        response = requests.get(api_url)

        if response.status_code != 200:
            raise Exception(f"Request ERROR: {response.status_code}")

        data = response.json()

        with open('src/data/response.json', 'w') as f:
            json.dump(data, f, indent=4)

        self.notify_observers(self._extract_weather_data(data))

    def _extract_weather_data(self, data: dict) -> dict:
        return {
            'unit_group': self.unit_group, 
            'location': data['address'],
            'temp_max': data['days'][0]['tempmax'],
            'temp_min': data['days'][0]['tempmin'],
            'temp_now': data['days'][0]['temp'],
            'description_now': data['days'][0]['description']
        }

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, data: dict):
        for observer in self.observers:
            observer.update(data)

if __name__ == "__main__":
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
    weather_api = WeatherAPI(base_url)

    weather_api.get_weather("Mannheim,Germany")