
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

notes = input("Enter Meeting Notes: ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.2,
    max_tokens=500,
    messages=[
        {
            "role": "system",
            "content": """
You are a Meeting Notes Assistant.
Extract action items from meeting notes.

Think step by step internally, but do not show your reasoning.
Use this example to follow the output format.

Example:
Input: Rahul will submit the report by Friday.

Output:
Who: Rahul
What: Submit the report
Deadline: Friday

Rules:
- Do not guess missing information.
- Use Not specified if the owner or deadline is missing.
- Include a 2-line meeting summary.
- List all action items clearly.
"""
        },
        {
            "role": "user",
            "content": notes
        }
    ]
)

print(response.choices[0].message.content)
