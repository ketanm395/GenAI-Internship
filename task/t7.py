
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

text = input("Enter message: ")
language = input("Enter target language: ")
formality = input("Enter formality (formal/casual): ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.2,
    max_tokens=300,
    messages=[
        {
            "role": "system",
            "content": """
You are a professional translator.
Detect the original language.
Translate the message into the target language.
Follow the requested formality.

Example:
Message: Hello
Language: Hindi
Formality: Casual
Output: नमस्ते

Keep the translation simple.
"""
        },
        {
            "role": "user",
            "content": f"""
Message: {text}
Target Language: {language}
Formality: {formality}
"""
        }
    ]
)

print("\nTranslated Message:")
print(response.choices[0].message.content)
