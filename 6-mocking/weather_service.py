import api_client


def get_weather(city):
    """Get weather for a city"""
    data = api_client.fetch_weather_data(city)
    return data


def get_forecast(city, days=3):
    """Get forecast for a city"""
    return api_client.fetch_forecast(city, days)


def is_good_weather(conditions):
    """Check if weather conditions are good"""
    good_conditions = ["sunny", "partly cloudy"]
    return any(c in good_conditions for c in conditions)


def get_greeting_based_on_time():
    """Return greeting based on time of day"""
    hour = api_client.get_current_hour()
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
