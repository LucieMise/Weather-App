'''
This module provides functions for saving and retrieving weather data from the database.
'''

from sqlalchemy.orm import Session

from src.database.models import Weather
from src.database.db import SessionLocal


def save_weather(data):

    session: Session = SessionLocal()

    weather = Weather(
        city=data["city"],
        temperature=data["temperature"],
        humidity=data["humidity"],
       description=data["description"]
    )

    session.add(weather)

    session.commit()

    session.close()
