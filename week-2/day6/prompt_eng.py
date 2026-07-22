import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error: GROQ_API_KEY environment variable not set")

client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"


def llm_ans(prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content


prompt = """
#ROLE
You are a support assistant at a mobile/laptop company.

#TASK
Classify EACH customer complaint separately.

#CATEGORIES
- Billing
- Technical
- Return

#OUTPUT FORMAT
Return the answer as:

1. <Category>
2. <Category>
3. <Category>

If a complaint does not belong to any category, return OTHER.

#CUSTOMER COMPLAINTS

1. I am not happy with my mobile phone. It is not working properly and I want a refund.

2. My laptop doesn't turn on and I need help fixing it.

3. I was charged twice for my order.

4. I want to exchange my phone because I received the wrong color.
"""

print(llm_ans(prompt))