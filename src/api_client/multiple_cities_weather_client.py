
from src.api_client.weather_client import get_weather


def multiple_cities_weather(cities: str):
    city_list = cities.split(",")
    weather_data = []
    
    for city in city_list:
        city_weather = get_weather(city.strip())
        weather_data.append(city_weather)
    
    return {"weather_data": weather_data}