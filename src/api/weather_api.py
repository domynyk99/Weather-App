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
        self.total_days = 14


        print("WeatherAPI class has been initialized.")

    def get_weather(self, location: str):
        date_1 = datetime.now().strftime('%Y-%m-%d')
        date_2 = (datetime.now() + timedelta(days=self.total_days)).strftime('%Y-%m-%d')
        api_url = f"{self.base_url}{location}/{date_1}/{date_2}?key={self.api_key}"\
            f"&unitGroup={self.unit_group}"
    
        response = requests.get(api_url)

        if response.status_code != 200:
            raise Exception(f"Request ERROR: {response.status_code}")

        data = response.json()

        self._write_to_json(data)

        # if u want to see what the extracted weather data looks like uncomment next line
        # self._write_to_json2(self._extract_weather_data(data))

        self.notify_observers(self._extract_weather_data(data))

    def _write_to_json(self, data: dict):
        try:
            with open('src/data/response.json', 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"ERROR: While trying to save the api GET request!\n{e}")

    def _write_to_json2(self, data: dict):
        try:
            with open('src/data/data_response.json', 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"ERROR: While trying to save the api GET request!\n{e}")

    def _extract_weather_data(self, data: dict) -> dict:
        forecast_days = []
        for i in range(self.total_days):
            forecast_hours = []
            for j in range(24):
                hour = {
                    'time': data['days'][i]['hours'][j]['datetime'],
                    'temp': data['days'][i]['hours'][j]['temp'],
                    'conditions': data['days'][i]['hours'][j]['conditions'],
                    'icon': data['days'][i]['hours'][j]['icon'] 
                }
                forecast_hours.append(hour)
            day = {
                'datetime': data['days'][i]['datetime'],
                'temp_max': data['days'][i]['tempmax'],
                'temp_min': data['days'][i]['tempmin'],
                'temp_now': data['days'][i]['temp'],
                'conditions': data['days'][i]['conditions'],
                'description': data['days'][i]['description'],
                'icon': data['days'][i]['icon'],
                'hours': forecast_hours
            }
            forecast_days.append(day)
        
        return {
            'unit_group': self.unit_group, 
            'location': data['address'],
            'forecast_days': forecast_days
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