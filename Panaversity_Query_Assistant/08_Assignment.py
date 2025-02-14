import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the document
loader = PyPDFLoader("Panaversity_Query_Assistant/document.pdf")
doc = loader.load()

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key="AIzaSyAkcbY4zaoZ5ftLEkRVoWEjmWgdx9Kxcmo")

# Streamlit app
st.title("📚 Panaversity Query Assistant")
st.write(
    "🔍 **Unleash the power of your document!**\n\n"
    "- Type your question below to extract precise insights directly from the PDF. \n"
    "- Our smart assistant will analyze the document and provide you with detailed, accurate answers. \n"
    "- If your query isn't covered by the document, you'll receive a polite notification. Enjoy exploring! \n"
)

user_input = st.text_input("Your question:")
st.button("Get Answer") 

if user_input:
    prompt = f"""
    You have to response the user {user_input} according to the provided document
    document {doc}

    if the user query don't match with the document, then response
    """
  
    response = llm.invoke(prompt)
    st.write(response.content)  # Output: The response from the LLM
  