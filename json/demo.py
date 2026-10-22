import os
import json
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.4,
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": """
            Analyze a car showroom customer review.
            Return JSON with:
            sentiment (positive, negative, neutral),
            rating_score (out of 5),
            summarize (short summary).
            """
        },
        {
            "role": "user",
            "content": "The cars are good, staff is friendly, but service is slow."
        }
    ]
)

raw = response.choices[0].message.content
print(raw)

try:
    data = json.loads(raw)
    print(data["sentiment"])
    print(data["rating_score"])
    print(data["summarize"])
except json.JSONDecodeError:
    print("Error while parsing JSON")