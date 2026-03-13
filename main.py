# from src.database.db import engine
# from src.database.models import Base
# from fastapi import FastAPI 
# from src.services.weather_service import save_weather
# from src.api.weather_client import get_weather
# from multiple_cities_weather import multiple_cities_weather, router as multiple_cities



# app = FastAPI()

# app.include_router(multiple_cities)

# @app.get("/")
# def home():
#     return {"message": "Welcome to the Weather API"}


# @app.get("/weather/{city}")
# def weather(city: str):
#     weather_data = get_weather(city)
#     return weather_data

# @app.get("/weather/multiple")
# def multiple_city_weather(cities: str):
#     weather_data = multiple_cities_weather(cities)
#     return weather_data


from fastapi import FastAPI
from src.api.routes import router
from src.database.db import engine
from src.database.models import Base

app = FastAPI(title="Weather AI API")

Base.metadata.create_all(bind=engine)

app.include_router(router)