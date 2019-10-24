import schedule
import time
from requests.exceptions import HTTPError
import db.connection
import weather.yandexWeather

weekWeather = []
date = []


def job():
    print("I'm working...")
    try:
        db = connection.connect()
        week_forecast = yandexWeather.read_week_forecast()
        db.execute(
            connection.executiv(str(week_forecast.date), str(week_forecast.day_forecasts[0].temperature),
                                               str(week_forecast.day_forecasts[1].temperature),
                                               str(week_forecast.day_forecasts[2].temperature),
                                               str(week_forecast.day_forecasts[3].temperature),
                                               str(week_forecast.day_forecasts[4].temperature),
                                               str(week_forecast.day_forecasts[5].temperature),
                                               str(week_forecast.day_forecasts[6].temperature)))
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    # except Exception as err:
    #     print(f'Other error occurred: {err.__traceback__.}')


def run():
    schedule.every().day.at("22:22").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
