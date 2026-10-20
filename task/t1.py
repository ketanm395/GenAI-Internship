import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

complaint = input("Enter Customer Complaint: ")
tone = input("Enter Reply Tone (Professional, Friendly, Auto): ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.5,
    max_tokens=300,
    messages=[
        {
            "role": "system",
            "content": (
                "You are a professional customer support agent. "
                "First classify complaint severity as Low, Medium, or High "
                "and detect emotion as Angry or Neutral. "
                "If tone is Auto, choose a suitable tone based on emotion. "
                "Generate a short, polite reply using this template:\n"
                "Severity:\n"
                "Emotion:\n"
                "Reply:\n"
                "Do not invent refund promises or order details."
            )
        },
        {
            "role": "user",
            "content": (
                f"Customer Complaint: {complaint}\n"
                f"Reply Tone: {tone}"
            )
        }
    ]
)

print("\nCustomer Support Reply:\n")
print(response.choices[0].message.content)