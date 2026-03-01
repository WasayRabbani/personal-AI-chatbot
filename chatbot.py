from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

load_dotenv() # loading api key into file

client=genai.Client() # Makes a client with gemini, so gemini knows this is a client which i will provide service


# This makes a chat which can have multiple messages. Also client makes it remember which person it is chatting to. Here connection made and gemini knows how to behave

chat=client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        system_instruction='You will reply me with one word only. So we use very less tokens'
    )
)

# Making Chatbot

print('-'*45)
print('Basic Level Chatbot')
print('-'*45)

while True:
    user_input=input('You: ').strip() # takes user input using input function

    if not user_input: # So if nothing written, it doesnot do anything.
        continue
    
    # Quit option Chatbot
    
    if user_input.lower()=='quit':
        print('Quitting...')
        break
    
    # Seeing how many tokens used
    
    
    

    



