
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

role = input("Enter job role: ")
level = input("Enter difficulty (Easy/Medium/Hard): ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.5,
    max_tokens=800,
    messages=[
        {
            "role": "system",
            "content": """
You are a professional Technical Interviewer.

Generate 5 interview questions for the given job role
and difficulty level.

Think through the role and difficulty before creating
questions, but do not show internal reasoning.

Use this format:
1. Question:
   Ideal Answer Points:

Separate questions into:
- Technical Questions
- Behavioral Questions

Keep the questions clear and useful.
"""
        },
        {
            "role": "user",
            "content": f"""
Job Role: {role}
Difficulty Level: {level}

Generate 5 interview questions with ideal answer points.
"""
        }
    ]
)

print("\n--- INTERVIEW QUESTIONS ---\n")
print(response.choices[0].message.content)
