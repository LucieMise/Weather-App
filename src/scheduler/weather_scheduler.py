from apscheduler.schedulers.background import BackgroundScheduler
from src.config.cities import CITIES
from src.api_client.weather_client import get_weather
from src.services.weather_service import save_weather


def collect_weather():

    print("Running weather collection job...")

    for city in CITIES:

        data = get_weather(city)

        save_weather(data)

        print("Saved:", city)


def start_scheduler():

    scheduler = BackgroundScheduler()

    scheduler.add_job(
        collect_weather,
        "interval",
        minutes=1
    )

    scheduler.start()

    print("Scheduler started...")