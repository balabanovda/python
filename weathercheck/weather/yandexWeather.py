import requests
import os
from dataclasses import dataclass

url = 'https://api.weather.yandex.ru/v1/forecast?lat=55.75396&lon=37.620393&extra=true'


def read_week_forecast():
    return __json_to_forecasts(__read_json())


def __read_json():
    response = requests.get(
        url, headers={'X-Yandex-API-Key': os.environ['X-YANDEX-API-KEY']})
    return response.json()


def __json_to_forecasts(json):
    day_forecasts = list(map(__json_to_forecast, json['forecasts']))
    return WeekForecast(day_forecasts[0].date, day_forecasts)


def __json_to_forecast(json):
    print(json)
    temperature = json['parts']['day']['temp_avg']
    date = json['date']
    return Forecast(date, temperature)


@dataclass
class Forecast:
    date: str
    temperature: str


@dataclass
class WeekForecast:
    date: str
    day_forecasts: str
