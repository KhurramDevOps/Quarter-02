import streamlit as st
import requests
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

# Set your API keys
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")  # Replace with your actual OpenWeatherMap API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Replace with your actual Gemini API key

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

# System Prompt
SYSTEM_PROMPT = """You are a helpful weather assistant that provides accurate, up-to-date weather forecasts and insights. You should:
- Provide current weather conditions based on the user's location or specified city.
- Include details such as temperature, humidity, wind speed, and the chance of precipitation.
- Offer a brief summary of the weather outlook for the day.
- Suggest appropriate attire or precautions based on the forecast (e.g., 'Carry an umbrella' or 'Wear sunscreen').
- Use a friendly, conversational tone, and adapt your responses to the user's needs (e.g., vacation planning, outdoor activities, or driving conditions).
- Be concise but informative, delivering the key weather information quickly.
- Use both Fahrenheit and Celsius if not specified, but default to the user’s preference if they mention it.
- If a user asks about topics that are not weather-related, respond with a message such as: 'I'm sorry, but I can only provide weather information. Please ask me about the weather.' Always maintain a friendly, concise, and informative tone in your responses.
"""

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
            full_prompt = f"{SYSTEM_PROMPT}\n\nUser Input: {user_input}\n\nWeather Details:\n{weather_data}"
            response = llm.invoke(full_prompt)
            
            st.subheader("📡 Weather Forecast:")
            st.write(response)
    else:
        st.error("❌ Please enter a valid City or Country name.")





