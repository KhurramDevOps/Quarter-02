from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()

def llm():
    messages = [{"role":"user","content":"What is blue ringed octupus"}]
    llm = completion(model = os.getenv("MODEL"),api_key=os.getenv("GOOGLE_API_KEY"),messages=messages)
    return llm['choices'][0]['message']['content']
llm()