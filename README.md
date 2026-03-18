# 🤖 AI Chatbot with Conversation History

A personal AI chatbot built with Python and Google Gemini that remembers your conversation across sessions using a local JSON file.

---

## 📌 Features

- 💬 Chat with Gemini AI in your terminal
- 🧠 Conversation history saved locally and loaded on every session
- 📜 View full chat history anytime with `H`
- 🔢 Track token usage with `T`
- 🔒 Secure API key management using `.env` file

---

## 🛠️ Tech Stack

- Python
- [Google GenAI SDK](https://pypi.org/project/google-genai/) (`google-genai`)
- `python-dotenv`
- JSON (for local history storage)

---

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**2. Install dependencies**
```bash
pip install google-genai python-dotenv
```

**3. Create a `.env` file in the root directory**
```
GEMINI_API_KEY=your_api_key_here
```

> Get your free API key from [Google AI Studio](https://aistudio.google.com/)

**4. Run the chatbot**
```bash
python chatbot.py
```

---

## 💻 Usage

Once running, you'll see:

```
---------------------------------------------
Welcome to Chatbot
Press Q to quit
H for history
T for token
---------------------------------------------
You: 
```

| Command | Action |
|--------|--------|
| Any text | Send a message to the AI |
| `H` | View full conversation history |
| `T` | Check token usage |
| `Q` | Quit the chatbot |

---

## 📁 Project Structure

```
├── chatbot.py        # Main chatbot script
├── history.json      # Auto-generated conversation history
├── .env              # Your API key (never share or upload)
├── .gitignore        # Excludes .env and history.json
└── README.md         # Project documentation
```

---

## 🔐 Important

- **Never share your API key** with anyone
- **Never upload your `.env` file** to GitHub
- Add `.env` and `history.json` to your `.gitignore`

```
# .gitignore
.env
history.json
```

---


## 📄 License

This project is open source and available under the [MIT License](LICENSE).