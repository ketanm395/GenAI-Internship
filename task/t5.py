
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

topic = input("Enter Topic: ")
platform = input("Enter Platform (Twitter/LinkedIn/Instagram/All): ")
tone = input("Enter Tone (Professional/Friendly/Funny): ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.7,
    max_tokens=800,
    messages=[
        {
            "role": "system",
            "content": """
You are a professional Social Media Content Writer.

Create social media posts using the topic, platform, and tone.

Follow these examples:

Twitter:
Short and engaging post with a few hashtags.

LinkedIn:
Professional post with useful information and hashtags.

Instagram:
Creative caption with emojis and relevant hashtags.

Rules:
- Match the requested tone.
- Keep each post suitable for its platform.
- If the platform is All, generate posts for all 3 platforms.
- Include relevant hashtags.
- Avoid unnecessary words.
"""
        },
        {
            "role": "user",
            "content": f"""
Topic: {topic}
Platform: {platform}
Tone: {tone}

Generate the social media post using these details.
"""
        }
    ]
)

print("\n--- GENERATED POSTS ---\n")
print(response.choices[0].message.content)
