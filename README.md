# MindWired — AI Chatbot with Memory

A command-line chatbot built with Google Gemini API.  
Remembers full conversation history, supports Urdu & English, and tracks token usage.

---

## What This Project Does

- Maintains conversation memory throughout the session
- Custom AI personality via system instructions
- Replies in Urdu or English based on user input
- Tracks tokens used per message and total session tokens
- Commands: `history` | `tokens` | `quit`

---

## Tech Stack

- Python
- Google Gemini API (`gemini-2.5-flash`)
- `google-genai` SDK
- `python-dotenv`

---

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/WasayRabbani/LLM-Basics-Stage-1.git
cd llm-basics
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Create `.env` file**
```
GEMINI_API_KEY=your_api_key_here
```
Get your free API key from: https://aistudio.google.com

**4. Run the chatbot**
```bash
python chatbot.py
```

---

## What I Learned

- How LLMs are stateless — memory must be managed manually
- How `chat.send_message()` sends full conversation history every time
- How system instructions control AI personality and behavior
- How to track token usage for cost estimation
- How to structure a Python project with `.env` for secure API key storage

---

## Project Status

Work in Progress — Stage 1 of Gen AI Roadmap

---

## Author

**Wasay Rabbani**  
Learning Gen AI Development | Building in Public
