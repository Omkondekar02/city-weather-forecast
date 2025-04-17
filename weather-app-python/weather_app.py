import requests
import tkinter as tk
from tkinter import messagebox

# Function to get weather data
def get_weather(city):
    api_key = "f3a0bbb5ef7dba3e0879463b71b1bb06"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == 200:
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].capitalize(),
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather
        else:
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")
        return None

# Function to display weather data
def display_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    weather = get_weather(city)

    if weather:
        result_label.config(text=f"City: {weather['city']}\n"
                                f"Temperature: {weather['temperature']}°C\n"
                                f"Description: {weather['description']}\n"
                                f"Humidity: {weather['humidity']}%\n"
                                f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        result_label.config(text="No weather data available for the given city.")

# GUI setup
root = tk.Tk()
root.title("Weather App")

# Input field for city
tk.Label(root, text="Enter City:").grid(row=0, column=0, padx=10, pady=10)
city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to fetch weather
tk.Button(root, text="Get Weather", command=display_weather).grid(row=1, column=0, columnspan=2, pady=10)

# Label to display results
result_label = tk.Label(root, text="", justify=tk.LEFT, font=("Arial", 12))
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

