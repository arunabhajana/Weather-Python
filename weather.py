
"""
    The code is a Python program that uses the OpenWeatherMap API to fetch and display weather
    information for a given city.
    The code is returning a GUI application that allows the user to enter a city name and
    retrieve the current weather information for that city. The weather information includes the city
    name, country, local time, temperature in Celsius, and weather condition.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from datetime import datetime, timezone, timedelta
import requests

def get_weather():
    api_key = 'YOUR_API_KEY'
    city = entry.get()

    if not city:
        messagebox.showwarning("Warning", "Please enter a city.")
        return

    try:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        weather_data = response.json()

        city_name = weather_data['name']
        country = weather_data['sys']['country']
        local_time = get_local_time(weather_data['timezone'])
        temperature = weather_data['main']['temp'] - 273.15
        weather_condition = weather_data['weather'][0]['description']

        result_label.config(text=f"City: {city_name}\nCountry: {country}\nLocal Time: {local_time}\nTemperature: {temperature:.2f}°C\nWeather Condition: {weather_condition}")

    except Exception as e:
        result_label.config(text="Error fetching data")

def get_local_time(timezone_offset):
    current_utc_time = datetime.now(timezone.utc)
    local_time = current_utc_time + timedelta(seconds=timezone_offset)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")

icon_path = "weather.png"
root.iconphoto(True, tk.PhotoImage(file=icon_path))

entry = ttk.Entry(root, width=20, font=('Arial', 14), justify='center')
entry.grid(row=0, column=0, padx=10, pady=20, columnspan=2)

ttk.Button(root, text='Get Weather', command=get_weather).grid(row=0, column=2, padx=5, pady=20)

result_label = ttk.Label(root, text="", font=('Arial', 12), anchor='w')
result_label.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

root.mainloop()
