import schedule
import time

from db import connection
from weather import yandex_weather

weekWeather = []
date = []


def job():
    print("I'm working...")
    try:
        cc = connection.connect()
        week_forecast = yandex_weather.read_week_forecast()
        cc.execute(
           connection.executiv(str(week_forecast.date), str(week_forecast.day_forecasts[0].temperature),
                                               str(week_forecast.day_forecasts[1].temperature),
                                               str(week_forecast.day_forecasts[2].temperature),
                                               str(week_forecast.day_forecasts[3].temperature),
                                               str(week_forecast.day_forecasts[4].temperature),
                                               str(week_forecast.day_forecasts[5].temperature),
                                               str(week_forecast.day_forecasts[6].temperature)))
    except Exception as err:
        print(f'Other error occurred: {err}')


def run():
    schedule.every().day.at("20:44").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
