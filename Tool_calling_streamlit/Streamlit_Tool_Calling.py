from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",api_key = "AIzaSyAkcbY4zaoZ5ftLEkRVoWEjmWgdx9Kxcmo")

st.title("Conversational AI Assistant 🧠")
user_input = st.text_input("Ask AI")
button = st.button("Generate Response")

# Custom CSS to change button color on hover
st.markdown("""
    <style>
        .stButton > button:hover {
            background-color: green;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

if user_input:
    response = llm.invoke(user_input)
    st.write(response.content)  # prints the response from the model
