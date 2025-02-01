from litellm import completion

def llm():
    messages = [{"role":"user","content":"What is blue ringed octupus"}]
    llm = completion(model = "gemini/gemini-2.0-flash-exp",api_key="AIzaSyCoEfjVyPEyW8QIVwlHA4s8KJDbL0kBIBw",messages=messages)
    return llm['choices'][0]['message']['content']
llm()