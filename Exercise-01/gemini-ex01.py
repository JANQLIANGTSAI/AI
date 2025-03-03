##
#  mt8168@gmail.com 
#  NOT FOR PRODUCTION USE
#  This is a simple script to test the Gemini API
##
import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

print(os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Print the response
prompt = "Is Gemini AI better than DeepSeek?"
print ("\n\n\n Prompt: " + prompt)

# Initialize the model
models = genai.list_models()
for model in models:
    print(model.name)

model = genai.GenerativeModel("gemini-1.5-pro")

# Generate a response
response = model.generate_content(prompt)

# Print the response
print(response.text)
