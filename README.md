# Rule-Based AI Chatbot 🤖

> **DecodeLabs AI Internship — Project 1 | Batch 2026**

A simple yet functional rule-based AI chatbot built with **pure Python** — no external libraries, no machine learning, just clean control flow and logic.

This project demonstrates that you can build an intelligent-looking conversational interface using only **if-elif-else statements**, **keyword matching**, and **Python's standard library**.

---

## 📌 Project Overview

| Field         | Details                              |
|---------------|--------------------------------------|
| Project Name  | Rule-Based AI Chatbot (DecoBot)      |
| Internship    | DecodeLabs AI Internship — Batch 2026|
| Language      | Python 3.x                           |
| Libraries     | Standard Library only (no pip needed)|
| Difficulty    | Beginner                             |
| Concepts Used | Control Flow, Functions, String Matching |

---

## ✨ Features

- 🙋 **Personalized Greeting** — Asks for your name and greets you by it
- 🕐 **Time-Based Welcome** — Good Morning / Afternoon / Evening / Night
- 📚 **24 Predefined Q&A Topics** — AI, ML, Deep Learning, Python, and more
- ❓ **Help Command** — Lists all available topics and commands
- 📅 **Date Command** — Displays today's date
- ⏰ **Time Command** — Displays the current time
- 🔄 **Continuous Loop** — Runs until user types `bye`, `exit`, or `quit`
- 🤷 **Unknown Input Handling** — Polite and random fallback responses
- 🧩 **Modular Code** — Organized into clear functions with comments
- 📂 **Separated Data** — Q&A data is in `knowledge_base.py`, logic in `chatbot.py`

---

## 📁 Project Structure

```
Project-1-Rule-Based-AI-Chatbot/
│
├── chatbot.py          ← Main chatbot logic (run this file)
├── knowledge_base.py   ← All Q&A data (keywords + responses)
├── README.md           ← Project documentation (this file)
├── requirements.txt    ← No external libraries required
└── screenshots/        ← Sample screenshots of the chatbot
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher installed on your system
- No additional packages needed

### Installation

1. **Clone or download the project:**
   ```bash
   git clone https://github.com/yourusername/Project-1-Rule-Based-AI-Chatbot.git
   cd Project-1-Rule-Based-AI-Chatbot
   ```

2. **Run the chatbot:**
   ```bash
   python chatbot.py
   ```

That's it! No `pip install` needed.

---

## 💬 Sample Output

```
=======================================================
         DecoBot — Rule-Based AI Chatbot
    DecodeLabs AI Internship | Batch 2026
=======================================================

  Before we begin, I'd love to know your name.
  What is your name? >> Abdul

  Good Afternoon, Abdul! I am DecoBot, your AI learning assistant.
  Type 'help' to see all topics  |  Type 'bye' to exit.

-------------------------------------------------------

  Abdul >> what is machine learning

  DecoBot >>
             Machine Learning (ML) is a branch of AI where machines
             learn from data without being explicitly programmed.
             ...

-------------------------------------------------------

  Abdul >> tell me a joke

  DecoBot >>
             Here is a classic programmer joke for you:

             Why do programmers prefer dark mode?
               --> Because light attracts bugs!

-------------------------------------------------------

  Abdul >> bye

  DecoBot >> Goodbye, Abdul! It was great chatting with you.
             Keep learning and keep building. See you next time!

=======================================================
        Thanks for using DecoBot | DecodeLabs
=======================================================
```

---

## 📸 Screenshots

> Screenshots will be added here after running the chatbot.
> Save them in the `screenshots/` folder.

| Screenshot | Description |
|------------|-------------|
| `screenshots/welcome.png` | Welcome screen with name input |
| `screenshots/help_menu.png` | Help menu showing all topics |
| `screenshots/ai_response.png` | Sample AI question response |
| `screenshots/exit.png` | Exit screen |

---

## 🧠 Topics the Chatbot Covers

| Category | Topics |
|----------|--------|
| Artificial Intelligence | What is AI, Types of AI, NLP, Computer Vision, Data Science, AI vs ML, Career in AI |
| Machine Learning | What is ML, Supervised Learning, Unsupervised Learning |
| Deep Learning | Deep Learning, Neural Networks |
| Python | Python for AI, AI Libraries (TensorFlow, PyTorch, etc.) |
| Chatbots | What is a chatbot, Rule-based chatbot, How it works |
| DecodeLabs | About DecodeLabs, About this project |
| General | Greetings, How are you, Jokes, Motivation, Thanks |

---

## 🛠️ How It Works

The chatbot follows a simple rule-based approach:

```
User types a message
       ↓
Convert to lowercase
       ↓
Check special commands first (help, date, time, bye)
       ↓
Loop through QA_PAIRS in knowledge_base.py
       ↓
Check if any keyword is present in the message (using 'in' operator)
       ↓
If found → return matching response
If not found → return a polite fallback message
```

No machine learning. No regex. Just clean Python logic!

---

## 📋 Available Commands

| Command | Description |
|---------|-------------|
| `help` | Shows all available topics and commands |
| `date` | Displays today's date |
| `time` | Displays the current time |
| `bye` / `exit` / `quit` | Exits the chatbot |

---

## 🧩 How to Extend the Chatbot

To add a new topic, simply open `knowledge_base.py` and add a new entry to the `QA_PAIRS` list:

```python
{
    "keywords": ["your keyword", "another keyword"],
    "response": (
        "Your response goes here.\n"
        "You can use multiple lines!"
    ),
    "topic": "Your Topic Category"
},
```

No changes needed in `chatbot.py` — it automatically picks up new entries!

---

## 💡 Skills Demonstrated

- ✅ Python control flow (`if-elif-else`)
- ✅ String manipulation (`.lower()`, `.strip()`, `in` operator)
- ✅ Functions and modular code organization
- ✅ Loops (`while True`, `for` loop)
- ✅ Lists and dictionaries
- ✅ Python standard library (`datetime`, `random`)
- ✅ File organization and imports
- ✅ Clean code with comments and docstrings

---

## 👨‍💻 Author

**ABDUL SAMI UTHWAL**
- DecodeLabs AI Internship — Batch 2026
- 📧 abdulsamiuthwal@gmail.com
- 🔗 [GitHub Profile](https://github.com/abdulsamiuthwal-eng)

---

## 🏢 About DecodeLabs

DecodeLabs is a tech training platform that provides hands-on AI internship programs to students and developers.

- 📍 Greater Lucknow, India
- 📞 +91 89330 06408
- ✉️ decodelabs.tech@gmail.com
- 🌐 [www.decodelabs.tech](https://www.decodelabs.tech)

---

## 📄 License

This project is created for educational purposes as part of the DecodeLabs AI Internship program.
Feel free to use and modify it for your own learning.

---

*"The best way to learn AI is to build something with it — even if it is just if-elif-else."*
