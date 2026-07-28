import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error: GROQ_API_KEY environment variable not set")


client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

JD="""
We are hiring a backend engineer to join our team. The ideal candidate will have experience with Python, Django, and RESTful APIs. Responsibilities include developing and maintaining backend services, collaborating with frontend developers, and ensuring the scalability and performance of our applications.
Requirements:
- Proficiency in Python and Django framework
- Experience with RESTful API design and implementation
- strong understanding of database systems (SQL and NoSQL)
- docker and containerization experience
- AWS or cloud platform experience
- 2+ years of backend development experience
"""
RESUME="""
Name: John Doe
Email: john.doe@example.com
Experience: 3 years as a Software developer
Skills: Python, Django, RESTful APIs, SQL, Docker, AWS
Projects: Developed and maintained several web applications using Django, implemented RESTful APIs, and deployed applications on AWS using Docker containers.
"""
def ask_llm(system_prompt, user_prompt):
    sys_msg={
        "role": "system",
        "content": system_prompt
    }
    user_msg={
        "role": "user",
        "content": user_prompt
}
    messages=[sys_msg, user_msg]
    response =client.chat.completions.create(
        model=model,
        messages=messages,
    )
    answer = response.choices[0].message.content
    return answer


def step1_res_extract(RESUME):
    print("STEP 1")
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the candidates resume provided.
    Only return the skills no other information. Do not invent any skillsby yourself.
    Output Format:
    Skills should be separated by commas. Just return comma separated skills do not return any other filler information
    """
    user_prompt=f"""
    Extract the skills from this resume
    {RESUME}
    """
    return ask_llm(system_prompt, user_prompt)

def step2_JD_extract(JD):
    print("step2")
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the Job description  provided.
    Only return the skills no other information. Do not invent any skills by yourself.
    Output Format:
    Skills should be separated by commas. Just return comma separated skills do not return any other filler information
    """
    user_prompt=f"""
    Extract the skills from this JD
    {JD}
    """
    return ask_llm(system_prompt, user_prompt)

def step3_match(candidate,jd):
    print("step3")
    system_prompt="""
    You are a professional HR assistant. compare the skills of candidate and the skills required in the JD and produce a final score between
    1 and 100. also produce a short verdict whther the candidate is a good fit for the role.
    """
    user_prompt=f"""
    Compare and matc h the skills
    JD:
    {jd}
    Candidate:
    {candidate}
    """
    return ask_llm(system_prompt, user_prompt)

candidate=step1_res_extract(RESUME)
print(candidate)
sleep(2)
jd=step2_JD_extract(JD)
print(jd)
sleep(2)
score=step3_match(candidate,jd)
print(score)
