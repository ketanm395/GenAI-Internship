
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

email = input("Enter Email Message: ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.2,
    max_tokens=300,
    messages=[
        {
            "role": "system",
            "content": (
                "You are a professional email support assistant. "
                "Classify the email as Urgent, Billing, General, or Spam. "
                "First classify the email, then write a suitable reply. "
                "Use these examples:\n"
                "Email: My account is hacked! Category: Urgent\n"
                "Email: I was charged twice. Category: Billing\n"
                "Email: What are your working hours? Category: General\n"
                "Email: Win free money now, click this link! Category: Spam\n\n"
                "For Spam, do not reply to the sender. "
                "Keep replies short and professional. "
                "Do not invent facts.\n\n"
                "Output format:\n"
                "Category: [category]\n"
                "Reply: [reply]"
            )
        },
        {
            "role": "user",
            "content": f"Email Message: {email}"
        }
    ]
)

print("\nEmail Classification Result:\n")
print(response.choices[0].message.content)
