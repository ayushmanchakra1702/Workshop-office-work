#import openai
#openai.api_key = "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"

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