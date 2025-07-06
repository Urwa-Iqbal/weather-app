# 🌤️ Weather App (Tkinter GUI)

This is a Python GUI weather app built using Tkinter, OpenWeatherMap API, and GeoPy. It displays real-time weather details of any city including temperature, humidity, wind, description, and pressure.

---

## 📸 Features

- Get current weather by entering city name  
- Automatic timezone & local time detection  
- Built with pure Tkinter (no images or extra files)  
- Clean and responsive UI  

---

## 🛠️ Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
````

---

## 🔐 How to Get OpenWeatherMap API Key

1. Go to [OpenWeatherMap API](https://openweathermap.org/api)
2. Sign up or log in to your account
3. Navigate to the **API keys** section in your dashboard
4. Copy your API key or create a new one

---

## ⚙️ Setup Instructions

1. Clone the repo and navigate to the project folder:

   ```bash
   git clone https://github.com/Urwa-Iqbal/weather-app.git
   cd weather-app
   ```

2. Create a `.env` file in the root directory and add your API key:

   ```env
   API_KEY=your_api_key_here
   ```

3. Run the app:

   ```bash
   python weather_app.py
   ```

---

## 📝 Notes

* The `.env` file is included in `.gitignore` to keep your API key secure
* Make sure you have an active internet connection while using the app
