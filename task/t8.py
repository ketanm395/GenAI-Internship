
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

candidate = input("Enter your key skills and experience: ")
job = input("Enter job description: ")
tone = input("Enter tone (confident/humble/enthusiastic): ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.5,
    max_tokens=600,
    messages=[
        {
            "role": "system",
            "content": """
You are a professional Career Coach.

Compare the candidate's skills with the job requirements
internally, then write a tailored cover letter.
Do not show internal reasoning.

Use a professional style and follow the requested tone.
Do not invent skills or experience.
Keep the letter simple and clear.
"""
        },
        {
            "role": "user",
            "content": f"""
Candidate's Skills and Experience:
{candidate}

Job Description:
{job}

Tone: {tone}

Write a professional cover letter.
"""
        }
    ]
)

print("\n--- COVER LETTER ---\n")
print(response.choices[0].message.content)
