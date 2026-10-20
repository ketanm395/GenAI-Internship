
import os
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

reviews = []

n = int(input("How many reviews? "))

for i in range(n):
    review = input(f"Enter review {i + 1}: ")
    reviews.append(review)

positive = 0
negative = 0
neutral = 0

for review in reviews:
    response = client.chat.complete(
        model="mistral-small-latest",
        temperature=0.2,
        max_tokens=100,
        messages=[
            {
                "role": "system",
                "content": """
Classify the review as Positive, Negative, or Neutral.

Examples:
"Great product!" = Positive
"Very bad service." = Negative
"The product is okay." = Neutral

Return only the category.
"""
            },
            {"role": "user", "content": review}
        ]
    )

    sentiment = response.choices[0].message.content.strip()
    print(f"\nReview: {review}")
    print(f"Sentiment: {sentiment}")

    if "positive" in sentiment.lower():
        positive += 1
    elif "negative" in sentiment.lower():
        negative += 1
    else:
        neutral += 1

summary = client.chat.complete(
    model="mistral-small-latest",
    temperature=0.2,
    max_tokens=200,
    messages=[
        {
            "role": "system",
            "content": "Summarize what customers like and dislike in simple English."
        },
        {
            "role": "user",
            "content": "\n".join(reviews)
        }
    ]
)

print("\n--- CUSTOMER SUMMARY ---")
print(summary.choices[0].message.content)

print("\n--- SENTIMENT STATISTICS ---")
print("Positive reviews:", positive)
print("Negative reviews:", negative)
print("Neutral reviews:", neutral)
