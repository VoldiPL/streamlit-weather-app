import requests
from datetime import datetime

def fetch_weather(key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response = requests.get(url)

    # Odczytuje JSON i sprowadza do formy zbliżonej do dict
    data = response.json()

    weather = {
        "datetime": datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
        "temperature": data['main']['temp'],
        "perc_temp.": data['main']['feels_like'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed'],
        "city": data['name']
    }
    return weather