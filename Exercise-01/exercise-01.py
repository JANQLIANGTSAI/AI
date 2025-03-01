##
#  mt8168@gmail.com 
#  NOT FOR PRODUCTION USE
#  This is a simple script to test the OpenAI API
##
import os
import openai

from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.chat.completions.create(
    model="gpt-4",  # You can use other models like gpt-3.5-turbo
    messages=[
        {"role": "system", "content": "You are an AI assistant."},
        {"role": "user", "content": "Is OpenAI better than DeepSeek?"},
    ]
)

# Print the response
print(response.choices[0].message.content)