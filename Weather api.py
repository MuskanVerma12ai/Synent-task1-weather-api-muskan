
import requests

API_KEY = "your api key"  # Replace with your OpenWeatherMap API key

# ==========================
# FUNCTIONS
# ==========================

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 401:
            print("\n❌ Invalid API Key.")
            return

        if response.status_code == 404:
            print("\n❌ City not found.")
            return

        response.raise_for_status()

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]

        temp_c = data["main"]["temp"]
        temp_f = celsius_to_fahrenheit(temp_c)

        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        print("\n" + "=" * 40)
        print("       CURRENT WEATHER REPORT")
        print("=" * 40)
        print(f"Location     : {city_name}, {country}")
        print(f"Temperature  : {temp_c:.1f} °C")
        print(f"Temperature  : {temp_f:.1f} °F")
        print(f"Humidity     : {humidity}%")
        print(f"Condition    : {weather_desc}")
        print(f"Wind Speed   : {wind_speed} m/s")
        print("=" * 40)

    except requests.exceptions.Timeout:
        print("\n❌ Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("\n❌ Network connection error.")

    except requests.exceptions.RequestException as e:
        print(f"\n❌ API Error: {e}")


# ==========================
# MAIN PROGRAM
# ==========================

def main():
    print("===== Weather App =====")

    city = input("Enter city name: ").strip()

    if not city:
        print("❌ City name cannot be empty.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()
