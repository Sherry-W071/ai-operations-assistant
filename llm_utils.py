from openai import OpenAI
from config import OPENAI_API_KEY

client =  OpenAI(api_key=OPENAI_API_KEY)

def simple_chat(question: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content