import schedule
import time


def run_daily(at, job):
    schedule.every().day.at(at).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
