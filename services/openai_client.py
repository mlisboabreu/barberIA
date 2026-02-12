from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('key'))


def chamarAgente(question):
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.7,
        messages=[{
            "role":"user", "content": question
        }]
        )
    
    return resposta.choices[0].message.content


print(chamarAgente("you are intro of my software, say hello"))
    