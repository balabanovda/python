import requests
import postgresql
import schedule
import time
from requests.exceptions import HTTPError

weekWeather = []
date = []
url = 'https://api.weather.yandex.ru/v1/forecast?lat=55.75396&lon=37.620393&extra=true'


def job():
    print("I'm working...")
    db = postgresql.open('pq://postgres:spartacus10@localhost:5433/db_value')

    try:
        response = requests.get(url, headers={'X-Yandex-API-Key': '6f3252fc-0fe9-4af8-9a52-fdff36dbcb17'})
        json_response = response.json()
        forecasts = 'forecasts'

        for forecast in json_response[forecasts]:
            weekWeather.append(forecast['parts']['day']['temp_avg'])
            date.append(forecast['date'])

        response.raise_for_status()
        db.execute("INSERT INTO weather (date, temperature1, temperature2, temperature3, temperature4, temperature5, temperature6, temperature7) VALUES ('" + date[0] + "', "+str(weekWeather[0])+","+str(weekWeather[1])+","+str(weekWeather[2])+","+str(weekWeather[3])+","+str(weekWeather[4])+","+str(weekWeather[5])+","+str(weekWeather[6])+")")

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


schedule.every().day.at("20:44").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
