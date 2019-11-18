import requests
import json
import os
import connection


class Weather:
    def __init__(self):
        with open("config.json") as config:
            f = json.load(config)
            self.APIKEY = f["key"]["openweatherapi"]
    
    def get_temperature(self, location="Kathmandu"):
        self.url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={self.APIKEY}'
        data = requests.get(self.url)
        li = dict(data.json())
        print(li)
        if connection.is_connected() and data.json()['cod'] != '404':
            return data.json()['main']['temp'] 
        else:
            return False


weather = Weather()


