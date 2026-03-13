from fastapi import APIRouter
from requests import session
from sqlalchemy.orm import Session 



from src.api_client.multiple_cities_weather_client import multiple_cities_weather
from src.api_client.weather_client import get_weather
from src.database.db import SessionLocal
from src.database.models import Weather

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Welcome to the Weather API"}

@router.get("/weather/{city}")
def weather(city: str):
    session: Session = SessionLocal()
    weather_data = get_weather(city)
    session.close() 
    return weather_data

@router.get("/weather/multiple")
def multiple_city_weather(cities: list):
    session: Session = SessionLocal()
    weather_data = multiple_cities_weather(cities)
    session.close()
    return weather_data



