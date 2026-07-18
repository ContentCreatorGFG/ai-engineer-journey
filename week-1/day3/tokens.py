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
#3 PROMPTS
prompt1="Hii!"
prompt2="Explain time travel in detail"
prompt3="Write a poem about the moon in 1000 words"

prompts =[prompt1, prompt2, prompt3]
for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=5000
    )

    usage = response.usage

    print(f"Prompt: {prompt} --> your tokens: {usage.prompt_tokens}, completion tokens: {usage.completion_tokens}, total tokens: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")


# prompt= "DO you know about the latest trends in AI and machine learning? If yes, please explain in detail"

# #SYSTEM
# message_system ={
#     "role": "system",
#     "content": "You are a brand manager and you have to suggest a name for a food company. The name should be in one word"
# }

# message ={
#     "role": role,
#     "content": prompt
# }

# messages = [message_system, message]
# #temperature by default is 0 means safe play

# response = client.chat.completions.create(
#     model=model,
#     messages=messages,
#     temperature=1
# )
# #print (response)
# print("######################################")



# answer = response.choices[0].message.content
# print(answer)