#import openai
#openai.api_key = "Your API key"

from openai import OpenAI
client = OpenAI(api_key="your API key"
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__=="__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit","bye","quit"]:
            break
        response = chat_with_gpt(user_input)

        print("ChatGPT:", response)
