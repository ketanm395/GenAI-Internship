
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

text = input("Enter user text: ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.2,
    max_tokens=400,
    messages=[
        {
            "role": "system",
            "content": """
You are a Content Moderation Assistant.

Check the user text and choose:
- Safe
- Needs Review
- Violates Policy

Examples:
Text: Have a nice day!
Result: Safe
Reason: Friendly message.

Text: I will hurt you.
Result: Violates Policy
Reason: Threatening language.

Think carefully before deciding.
Do not show internal reasoning.

Also provide a safe rewritten version
if the text needs review or violates policy.

Output format:
Status:
Reason:
Safe Rewrite:
"""
        },
        {
            "role": "user",
            "content": text
        }
    ]
)

print("\n--- MODERATION RESULT ---\n")
print(response.choices[0].message.content)
