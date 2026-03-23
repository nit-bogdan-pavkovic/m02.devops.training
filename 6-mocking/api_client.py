import requests
import random
from datetime import datetime


def fetch_weather_data(city):
    """Fetch weather data from external API (simulated)"""
    if not city:
        raise ValueError("City cannot be empty")

    if random.random() < 0.1:
        raise TimeoutError("API timeout")

    return {
        "city": city,
        "temp": random.randint(15, 30),
        "condition": random.choice(["sunny", "cloudy", "rainy"]),
        "humidity": random.randint(40, 80),
    }


def fetch_forecast(city, days=3):
    """Fetch weather forecast"""
    if not city:
        raise ValueError("City cannot be empty")

    forecast = []
    for i in range(days):
        forecast.append(
            {
                "day": i + 1,
                "temp": random.randint(15, 30),
                "condition": random.choice(["sunny", "cloudy", "rainy"]),
            }
        )
    return forecast


def get_current_hour():
    """Get current hour - useful for time-based testing"""
    return datetime.now().hour
