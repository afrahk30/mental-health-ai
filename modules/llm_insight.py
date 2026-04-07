#OPTION A
def generate_insight(text, sentiment, emotion):
    return f"It seems like you're experiencing {emotion.lower()} feelings. Your overall sentiment appears {sentiment.lower()}. Take a moment to reflect and be kind to yourself."

#OPTION B
# import os
# from openai import OpenAI

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_insight(text, sentiment, emotion):
#     prompt = f"""
#     User text: {text}
#     Sentiment: {sentiment}
#     Emotion: {emotion}

#     Generate a short, empathetic, human-like reflection.
#     No advice. No diagnosis.
#     """

#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return response.choices[0].message.content