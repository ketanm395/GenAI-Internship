
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

product = input("Enter Product Name: ")
features = input("Enter 3-4 Product Features: ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.9,
    max_tokens=700,
    messages=[
        {
            "role": "system",
            "content": (
                "You are a creative marketing copywriter. "
                "Write attractive and persuasive product descriptions "
                "using the product name and features provided. "
                "Generate 3 different descriptions for A/B testing. "
                "Each variation must include a short tagline "
                "and a product description. "
                "Use catchy language but do not invent product features. "
                "Use this template:\n"
                "Variation 1:\nTagline:\nDescription:\n"
                "Variation 2:\nTagline:\nDescription:\n"
                "Variation 3:\nTagline:\nDescription:"
            )
        },
        {
            "role": "user",
            "content": (
                f"Product Name: {product}\n"
                f"Product Features: {features}"
            )
        }
    ]
)

print("\nProduct Descriptions:\n")
print(response.choices[0].message.content)
