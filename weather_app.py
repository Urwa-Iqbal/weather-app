import tkinter as tk
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import pytz
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        # Get coordinates and timezone
        geolocator = Nominatim(user_agent="weatherApp")
        location = geolocator.geocode(city)
        if not location:
            raise ValueError("City not found.")

        tz_finder = TimezoneFinder()
        timezone = tz_finder.timezone_at(lat=location.latitude, lng=location.longitude)
        if not timezone:
            raise ValueError("Timezone not found.")

        tz = pytz.timezone(timezone)
        local_time = datetime.now(tz).strftime("%I:%M %p")

        # Get weather data
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            raise ValueError(data.get("message", "API Error"))

        temp = int(data["main"]["temp"] - 273.15)
        condition = data["weather"][0]["main"]
        description = data["weather"][0]["description"].capitalize()
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        # Update labels
        city_label.config(text=city.title())
        time_label.config(text=f"Local Time: {local_time}")
        temperature_label.config(text=f"{temp}°C")
        condition_label.config(text=f"{condition} - {description}")
        wind_label.config(text=f"Wind: {wind} m/s")
        humidity_label.config(text=f"Humidity: {humidity}%")
        pressure_label.config(text=f"Pressure: {pressure} hPa")

    except Exception as e:
        messagebox.showerror("Weather Error", f"Error: {e}")

# ----------------- GUI -----------------
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#e0f7fa")

# Title
title = tk.Label(root, text="🌤️ Weather App", font=("Arial", 20, "bold"), bg="#e0f7fa", fg="#006064")
title.pack(pady=10)

# City input
city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)
city_entry.focus()

get_button = tk.Button(root, text="Get Weather", font=("Arial", 12), bg="#00acc1", fg="white", command=get_weather)
get_button.pack(pady=5)

# Output display
city_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#e0f7fa")
city_label.pack(pady=5)

time_label = tk.Label(root, text="", font=("Arial", 12), bg="#e0f7fa")
time_label.pack()

temperature_label = tk.Label(root, text="", font=("Arial", 30, "bold"), bg="#e0f7fa", fg="#d84315")
temperature_label.pack(pady=5)

condition_label = tk.Label(root, text="", font=("Arial", 14), bg="#e0f7fa")
condition_label.pack(pady=5)

wind_label = tk.Label(root, text="", font=("Arial", 12), bg="#e0f7fa")
wind_label.pack()

humidity_label = tk.Label(root, text="", font=("Arial", 12), bg="#e0f7fa")
humidity_label.pack()

pressure_label = tk.Label(root, text="", font=("Arial", 12), bg="#e0f7fa")
pressure_label.pack()

root.mainloop()
