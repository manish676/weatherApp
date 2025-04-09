from django.shortcuts import render
import requests
import datetime

def index(request):
    API_KEY = open("API_KEY", "r").read().strip()
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&units=metric&appid={}"

    if request.method == "POST":
        city1 = request.POST.get("city1")
        city2 = request.POST.get("city2", None)

        weather_data1, daily_forecasts1 = fetch_weather_and_forecast(city1, API_KEY, current_weather_url, forecast_url)

        if city2:
            weather_data2, daily_forecasts2 = fetch_weather_and_forecast(city2, API_KEY, current_weather_url, forecast_url)
        else:
            weather_data2, daily_forecasts2 = None, None

        context = {
            "weather_data1": weather_data1,
            "daily_forecasts1": daily_forecasts1,
            "weather_data2": weather_data2,
            "daily_forecasts2": daily_forecasts2
        }

        return render(request, "index.html", context)
    else:
        return render(request, "index.html")


def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    try:
        # Get current weather
        response = requests.get(current_weather_url.format(city, api_key)).json()
        print("DEBUG current_weather_response:", response)

        lat = response['coord']['lat']
        lon = response['coord']['lon']

        # Get forecast
        forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()
        print("DEBUG forecast_response:", forecast_response)

        weather_data = {
            "city": city,
            "temperature": round(response['main']['temp'] - 273.15, 2),  # Still using manual conversion, optional
            "description": response['weather'][0]['description'],
            "icon": response['weather'][0]['icon']
        }

        daily_forecasts = []
        if 'daily' in forecast_response:
            for daily_data in forecast_response['daily'][:5]:
                daily_forecasts.append({
                    "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
                    "min_temp": daily_data['temp']['min'],
                    "max_temp": daily_data['temp']['max'],
                    "description": daily_data['weather'][0]['description'],
                    "icon": daily_data['weather'][0]['icon']
                })
        else:
            print("❌ 'daily' key not found in forecast response")
            daily_forecasts = []

        return weather_data, daily_forecasts

    except Exception as e:
        print(f"⚠️ Error fetching weather/forecast data for {city}: {e}")
        return None, None
