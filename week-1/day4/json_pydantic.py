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

#structure it

from pydantic import BaseModel
class Ticket (BaseModel):
    name: str
    device: str
    issue: str
    address: str
    phone_number: str
    email: str
schema =Ticket.model_json_schema()

response_format ={
    "type": "json_object"
}

system_prompt = f"""
Extract the personal information from the ticket strictly based on this schema and give the output in json format.
{schema}
"""

message_system ={
    "role": "system",
    "content": system_prompt
}

text ="My name is Priyanshi.I have an iphone which is not working properly. My address is 123, ABC street, Lucknow. My phone number is 1234567890. I want to get it repaired. Can you help me with that?.My email address is priyanshi@example.com"
prompt = f"""
This is a Customer Ticket.Please extract the following information from the this.
{text}
"""

#message mein role and content ko define karna hai. Role user hai aur content mein prompt hai.

message ={
    "role": role,
    "content": prompt
}

messages = [message_system, message]
response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)

answer = response.choices[0].message.content
print(answer)

#isko pdhte kese hain

import json
raw_json =(answer)
data_file =json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.device)
print(ticket.issue)
print(ticket.address)
print(ticket.phone_number)
print(ticket.email)