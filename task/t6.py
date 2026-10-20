
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

code = input("Enter your code: ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.2,
    max_tokens=500,
    messages=[
        {
            "role": "system",
            "content": """
You are a Senior Software Engineer.

Explain the code in simple English.
Explain what each part does step by step.
Generate comments and docstrings for the code.
Do not show internal reasoning.

Example:
Code: x = 10
Output:
Explanation: Stores 10 in x.
Commented Code:
x = 10  # Store the value 10
"""
        },
        {
            "role": "user",
            "content": f"Explain this code and add documentation:\n{code}"
        }
    ]
)

print(response.choices[0].message.content)
