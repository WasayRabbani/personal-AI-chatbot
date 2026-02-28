# Part 1: Loading Dependencies and making connection

from google import genai
import os
from dotenv import load_dotenv
from google.genai import types


# types: the instruction form we send to gemini like what is system instruction, what is temperature and what is response format.

load_dotenv()
client=genai.Client()


# Part 2: Making Chat session

chat=client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig
    (
        system_instruction="""
        So you are a person who is strict, doesnot joke a lot and is not emotional, says what is correct and doesnot give any false hopes.
        If user types in roman urdu, you type in roman urdu, if in english you type back in english. Your Name is MindWired. You are fluent In Artificial Intelligence.
        """
    )
) 
 
#  Part 3: Making loop that makes chatbot alive

print('MindWired. Your own Chatbot')
while True:
        user_input=input('You: ')
        if user_input.lower()=='quit':
            break
        response=chat.send_message(user_input)
        print(response.text)
       
