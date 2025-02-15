import streamlit as st
import requests
from langchain_google_genai import GoogleGenerativeAI

# Set your API keys
WEATHER_API_KEY = "e472e9e4cfc93670c3cb249f26576ad9"  # Replace with your actual OpenWeatherMap API key
GEMINI_API_KEY = "AIzaSyAkcbY4zaoZ5ftLEkRVoWEjmWgdx9Kxcmo"  # Replace with your actual Gemini API key

# Initialize Google Generative AI
llm = GoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=GEMINI_API_KEY)

# Initialize the Weather API Function
def get_weather(city: str) -> str:
    """Fetch the current weather for a given location."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather = response.json()

        if "weather" in weather and "main" in weather:
            return (f"Weather in {weather['name']}, {weather['sys']['country']}: "
                    f"{weather['weather'][0]['description'].capitalize()}, "
                    f"{weather['main']['temp']}°C.")
        else:
            return "❌ Weather data not found. Please check the city name."
    except requests.exceptions.RequestException as e:
        return f"❌ Error fetching weather: {e}"

# Streamlit UI
st.title("🌤️ Weather Forecast Assistant")
st.markdown(
    """
    - **Enter a City or Country name below to receive the current weather forecast!**  
    - Whether you’re planning your day or a weekend getaway, get up-to-date weather details instantly.  
    🌍🏙️
    """
)

# User Input
user_input = st.text_input("City/Country Name", placeholder="e.g., New York, USA or Paris, France 🌆")

# Button Click Logic
if st.button("🔍 Get Weather"):
    if user_input:
        weather_data = get_weather(user_input)
        if "❌" in weather_data:
            st.error(weather_data)
        else:
            # Generate response using Gemini via LangChain
            prompt = f"Provide a detailed and friendly weather report based on the following data: {weather_data}"
            response = llm.invoke(prompt)
            
            st.subheader("📡 Weather Forecast:")
            st.write(response)
    else:
        st.error("❌ Please enter a valid City or Country name.")




