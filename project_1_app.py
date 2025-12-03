import requests

# ---------- CONFIG ----------
API_KEY = "41bb05477f1a835c0e6a390e4088d2d3" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name: str):
    """
    Fetch current weather for a given city using OpenWeatherMap API.
    Returns a dict with main info or None if error.
    """
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  
        data = response.json()

      
        if data.get("cod") != 200:
            print("❌ City not found. Please check the name.")
            return None

        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        wind = data.get("wind", {})

        result = {
            "city": data.get("name", city_name),
            "temperature": main.get("temp"),
            "humidity": main.get("humidity"),
            "pressure": main.get("pressure"),
            "description": weather_desc.title(),
            "wind_speed": wind.get("speed"),
        }
        return result

    except requests.exceptions.RequestException as e:
        print("⚠️ Network error while fetching weather data:")
        print(e)
        return None


def print_weather(info: dict):
    """Nicely print the weather info."""
    print("\n----- Weather Report -----")
    print(f"City        : {info['city']}")
    print(f"Temperature : {info['temperature']} °C")
    print(f"Humidity    : {info['humidity']} %")
    print(f"Pressure    : {info['pressure']} hPa")
    print(f"Wind Speed  : {info['wind_speed']} m/s")
    print(f"Condition   : {info['description']}")
    print("--------------------------\n")


def main():
    print("=== Basic Weather App (Python) ===")
    print("Type 'exit' to quit.\n")

    while True:
        city = input("Enter city name: ").strip()
        if city.lower() in ("exit", "quit"):
            print("Goodbye! 👋")
            break

        if not city:
            print("Please enter a valid city name.\n")
            continue

        info = get_weather(city)
        if info:
            print_weather(info)


if __name__ == "__main__":
    main()

