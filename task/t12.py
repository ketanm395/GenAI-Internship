
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

topic = input("Enter topic: ")
level = input("Enter difficulty (Easy/Medium/Hard): ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.3,
    max_tokens=1000,
    messages=[
        {
            "role": "system",
            "content": """
You are a helpful Teacher.

Create 5 multiple-choice quiz questions
based on the given topic and difficulty.

Check that the questions and answers are correct.
Do not show internal reasoning.

Example format:
Q1. What is Python?
A. A programming language
B. A fruit
C. A car
D. A game

Answer: A
Explanation: Python is a programming language.

Follow this format for all 5 questions.
"""
        },
        {
            "role": "user",
            "content": f"Topic: {topic}\nDifficulty: {level}"
        }
    ]
)

print("\n--- YOUR QUIZ ---\n")
print(response.choices[0].message.content)
