from dotenv import load_dotenv
import os
from google import genai

# Load .env file
load_dotenv()



# Create client with API key
client = genai.Client()

# Use stable model name
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello Gemini!"
)

print(response.text)