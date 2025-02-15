import streamlit as st
from meta_ai_api import MetaAI

def main():
    # Set up page config
    st.set_page_config(page_title="Weather Information", page_icon="🌤️")
    
    # Add title
    st.title("🌍 Global Weather Information")
    
    # Initialize MetaAI
    llm = MetaAI()
    
    # Create input field
    user_input = st.text_input("Enter the country name:", placeholder="e.g., France")
    
    # Create button
    if st.button("Get Weather Info"):
        if user_input:
            # Show loading spinner
            with st.spinner("Fetching weather information..."):
                prompt = f"""You are custom gpt you have to tell about the weather of any country user asked 
                    user asked for {user_input}
                    you have to tell the weather of the country in the following format:
                    - Temperature: 20°C
                    - Weather: Sunny
                    - Wind: 10 km/h
                    - Humidity: 50%
                    - Precipitation: 0 mm
                    - Cloud cover: 50%
                    - Wind direction: North
                    - Wind speed: 10 km/h
                    - Visibility: 10 km
                    - Pressure: 1000 hPa
                    - Dew point: 10°C
                    - UV index: 10
                    - Sunrise: 06:00
                    - Sunset: 18:00
                    - Moon phase: Full moon
                    - Moon illumination: 100%

                    and if the user asked something else you have to tell that you are not able cable of that 
                """
                
                response = llm.prompt(prompt)
                # Display the response in a nice box
                st.markdown("### Weather Information")
                st.info(response["message"])
        else:
            st.warning("Please enter a country name!")

if __name__ == "__main__":
    main()





