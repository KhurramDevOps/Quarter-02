from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(model=os.getenv("MODEL"), api_key=os.getenv("DEEPSEEK_API_KEY"))\

user_input = st.text_input("ASK ME ANYTHING")
prompt = f"""You are an advanced AI translation model. Your task is to translate the given user input into 100 different languages and present the output strictly in table format.

Instructions:
Output only a structured table—no explanations, introductions, or additional text.
The table must have two columns:
Language (Full name of the language)
Translation (Accurate, natural translation of the input)
Do not include any preamble, summaries, or extra formatting outside the table.
User Input:
{user_input}"""




if user_input:
    response = model.invoke(prompt)
    st.write(response.content)

# response = model.invoke("Hello , who are you?")
# print(response.contents)