import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error: GROQ_API_KEY environment variable not set")


client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role  ="user"
prompt= "sugesst any name for my food company "

#SYSTEM
message_system ={
    "role": "system",
    "content": "You are a brand manager and you have to suggest a name for a food company. The name should be in one word"
}

message ={
    "role": role,
    "content": prompt
}

messages = [message_system, message]
#temperature by default is 0 means safe play

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1
)
#print (response)
print("######################################")



answer = response.choices[0].message.content
print(answer)