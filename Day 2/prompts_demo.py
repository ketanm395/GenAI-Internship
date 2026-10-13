import os
from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv()

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {"role": "system", "content": "you are a helpful AI tutor Explain everything in simplest language you are personal ai assistance. hepl me learn solve problems and complete tasks step by step."},
        {"role":"user","content":"give me three useful skills i can learn as a begginer in ai"}
    ],
)

print(response.choices[0].message.content)