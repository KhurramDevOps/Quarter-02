import streamlit as st
from meta_ai_api import MetaAI

# Initialize the MetaAI instance
LLM = MetaAI()

# Define the system prompt for weather assistance
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


st.title("🌤️ Weather Forecast Assistant ")
st.markdown(
    """
    - **Enter a City or Country name below to receive the current weather forecast!**  \n
    - Whether you’re planning your day or a weekend getaway, get up-to-date weather details instantly.  
    🌍🏙️
    """
)

# User input for city/country name with an attractive placeholder
user_input = st.text_input("City/Country Name", placeholder="e.g., New York, USA or Paris, France 🌆")


if st.button("🔍 Get Weather"):
    if user_input:

        full_prompt = f"{SYSTEM_PROMPT}\n\nUser Input: {user_input}"

        response = LLM.prompt(full_prompt)
        

        st.subheader("📡 Weather Forecast:")
        st.write(response.get("message", "No response received."))
    else:
        st.error("❌ Please enter a valid City or Country name.")
