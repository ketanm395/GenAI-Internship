
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

topic = input("Enter Poem Topic: ")
poem_type = input("Enter Poem Type (Rhyming, Haiku, Free Verse): ")
mood = input("Enter Poem Mood (Happy, Sad, Romantic): ")
length = input("Enter Poem Length (Short, Medium, Long): ")
language = input("Enter Poem Language: ")

response = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.9,
    max_tokens=700,
    messages=[
        {
            "role": "system",
            "content": """
            You are an experienced AI Poem Writer.
            Your task is to generate an original poem based on
            the user's inputs.

            Follow these rules:
            - Use the provided topic, poem type, mood, length,
              and language.
            - Use creative and meaningful words.
            - Keep the poem relevant to the user's topic.
            - Use proper line breaks and stanzas.
            - Do not add unrelated explanations.
            - Return only the poem and its title.
            """
        },
        {
            "role": "user",
            "content": f"""
            Write a poem about {topic}.
            Poem Type: {poem_type}
            Mood: {mood}
            Length: {length}
            Language: {language}
            """
        },
    ]
)

print(response.choices[0].message.content)
