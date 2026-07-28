# knowledge_base.py
"""
============================================================
  knowledge_base.py — Q&A Data for DecoBot
  DecodeLabs AI Internship | Project 1 | Batch 2026
============================================================

This file contains all the predefined questions and answers
for the DecoBot chatbot.

Each entry in QA_PAIRS is a dictionary with:
  - "keywords" : list of words/phrases that trigger this response
  - "response" : the chatbot's reply text
  - "topic"    : category label (shown in the help menu)

How matching works (in chatbot.py):
  The chatbot loops through each entry and checks if any
  keyword is present inside the user's typed message.
  No regex is used — just simple Python 'in' operator.
============================================================
"""

# ──────────────────────────────────────────────────────────────
#  QA_PAIRS — The full knowledge base (24 Q&A entries)
#  Add more entries here to expand the chatbot's knowledge.
# ──────────────────────────────────────────────────────────────

QA_PAIRS = [

    # ── 1. GREETINGS ──────────────────────────────────────────
    {
        "keywords": ["hello", "hi", "hey", "salam", "greetings", "howdy", "hola"],
        "response": (
            "Hey there! Welcome to DecoBot!\n"
            "I am your AI learning assistant, built for the DecodeLabs Internship.\n"
            "Type 'help' to see the list of topics I can talk about."
        ),
        "topic": "Greetings"
    },

    # ── 2. HOW ARE YOU ────────────────────────────────────────
    {
        "keywords": ["how are you", "how r u", "how do you do", "kaisa hai", "kya haal"],
        "response": (
            "I am doing great, thanks for asking!\n"
            "I am an AI chatbot, so I am always ready to help you learn.\n"
            "What would you like to know today?"
        ),
        "topic": "General"
    },

    # ── 3. WHAT IS AI ─────────────────────────────────────────
    {
        "keywords": ["what is ai", "define ai", "explain ai", "artificial intelligence", "tell me about ai"],
        "response": (
            "Artificial Intelligence (AI) is the ability of a computer or machine\n"
            "to perform tasks that normally require human intelligence.\n"
            "\n"
            "Examples of AI in everyday life:\n"
            "  - Voice assistants like Siri and Alexa\n"
            "  - Netflix and YouTube recommendations\n"
            "  - Google Search results\n"
            "  - Spam filters in Gmail\n"
            "  - Face unlock on your smartphone"
        ),
        "topic": "Artificial Intelligence"
    },

    # ── 4. TYPES OF AI ────────────────────────────────────────
    {
        "keywords": ["types of ai", "kinds of ai", "narrow ai", "general ai", "super ai", "categories of ai"],
        "response": (
            "There are 3 main types of Artificial Intelligence:\n"
            "\n"
            "  1. Narrow AI (Weak AI)\n"
            "     -> Designed for ONE specific task.\n"
            "     -> Example: Chess programs, face recognition.\n"
            "\n"
            "  2. General AI (AGI)\n"
            "     -> Can do ANY intellectual task a human can do.\n"
            "     -> Example: Still a theoretical concept!\n"
            "\n"
            "  3. Super AI\n"
            "     -> Surpasses human intelligence in every area.\n"
            "     -> Example: Only exists in science fiction for now."
        ),
        "topic": "Artificial Intelligence"
    },

    # ── 5. MACHINE LEARNING ───────────────────────────────────
    {
        "keywords": ["machine learning", "what is ml", "ml kya hai", "tell me about ml", "learn from data"],
        "response": (
            "Machine Learning (ML) is a branch of AI where machines\n"
            "learn from data without being explicitly programmed.\n"
            "\n"
            "Instead of writing rules manually, you give the machine\n"
            "lots of examples and it figures out the patterns itself!\n"
            "\n"
            "Real-world examples:\n"
            "  - Email spam detection\n"
            "  - Credit card fraud detection\n"
            "  - Movie recommendations on Netflix\n"
            "  - House price prediction"
        ),
        "topic": "Machine Learning"
    },

    # ── 6. SUPERVISED LEARNING ────────────────────────────────
    {
        "keywords": ["supervised learning", "what is supervised", "labeled data", "supervised"],
        "response": (
            "Supervised Learning is a type of Machine Learning where\n"
            "the model is trained on LABELED data (data with known answers).\n"
            "\n"
            "Think of it like a student learning with an answer key:\n"
            "  - Input  : Email text\n"
            "  - Label  : Spam OR Not Spam\n"
            "  - Goal   : Predict labels for new, unseen emails\n"
            "\n"
            "Common algorithms:\n"
            "  Linear Regression, Decision Trees, SVM, Random Forest"
        ),
        "topic": "Machine Learning"
    },

    # ── 7. UNSUPERVISED LEARNING ──────────────────────────────
    {
        "keywords": ["unsupervised learning", "unsupervised", "clustering", "unlabeled data"],
        "response": (
            "Unsupervised Learning works with UNLABELED data.\n"
            "The model finds hidden patterns and groups on its own!\n"
            "\n"
            "Real-world examples:\n"
            "  - Customer segmentation (grouping shoppers by behavior)\n"
            "  - Anomaly detection (spotting unusual bank transactions)\n"
            "  - Document clustering (grouping similar news articles)\n"
            "\n"
            "Common algorithms:\n"
            "  K-Means Clustering, PCA, DBSCAN, Autoencoders"
        ),
        "topic": "Machine Learning"
    },

    # ── 8. DEEP LEARNING ──────────────────────────────────────
    {
        "keywords": ["deep learning", "what is dl", "dl kya hai", "tell me about deep learning"],
        "response": (
            "Deep Learning is a subset of Machine Learning that uses\n"
            "Neural Networks with many layers — that is why it is called 'deep'.\n"
            "\n"
            "It is inspired by the structure of the human brain!\n"
            "\n"
            "Deep Learning is used in:\n"
            "  - Image recognition (Google Photos, Face ID)\n"
            "  - Speech recognition (Alexa, Google Assistant)\n"
            "  - ChatGPT and Large Language Models (LLMs)\n"
            "  - Self-driving cars"
        ),
        "topic": "Deep Learning"
    },

    # ── 9. NEURAL NETWORKS ────────────────────────────────────
    {
        "keywords": ["neural network", "what is neural", "neurons", "hidden layer", "perceptron"],
        "response": (
            "A Neural Network is a computer system inspired by the human brain.\n"
            "It is made up of layers of connected 'neurons' (small processing units).\n"
            "\n"
            "Structure of a Neural Network:\n"
            "  - Input Layer  -> receives the raw data\n"
            "  - Hidden Layers -> finds patterns in the data\n"
            "  - Output Layer -> produces the final prediction\n"
            "\n"
            "The more hidden layers there are, the 'deeper' the network becomes!"
        ),
        "topic": "Deep Learning"
    },

    # ── 10. NLP ───────────────────────────────────────────────
    {
        "keywords": ["nlp", "natural language processing", "natural language", "text processing", "language model"],
        "response": (
            "NLP stands for Natural Language Processing.\n"
            "It is the ability of computers to understand and process human language.\n"
            "\n"
            "NLP is used in:\n"
            "  - Chatbots and virtual assistants (like me!)\n"
            "  - Google Translate\n"
            "  - Sentiment Analysis (positive or negative reviews)\n"
            "  - Auto-correct on your phone keyboard\n"
            "  - ChatGPT and other AI writing tools"
        ),
        "topic": "Artificial Intelligence"
    },

    # ── 11. COMPUTER VISION ───────────────────────────────────
    {
        "keywords": ["computer vision", "image recognition", "object detection", "image processing"],
        "response": (
            "Computer Vision is a field of AI that trains computers\n"
            "to understand and interpret images and videos.\n"
            "\n"
            "Applications of Computer Vision:\n"
            "  - Face unlock on smartphones\n"
            "  - Medical image analysis (cancer detection)\n"
            "  - Self-driving car cameras\n"
            "  - Quality control in manufacturing\n"
            "  - Augmented Reality (AR) filters on Instagram"
        ),
        "topic": "Artificial Intelligence"
    },

    # ── 12. PYTHON FOR AI ─────────────────────────────────────
    {
        "keywords": ["python", "why python", "python for ai", "python kya hai", "python language"],
        "response": (
            "Python is the most popular programming language for AI and ML!\n"
            "\n"
            "Why is Python so popular for AI?\n"
            "  - Simple and beginner-friendly syntax\n"
            "  - Huge collection of AI and data science libraries\n"
            "  - Strong community and online support\n"
            "  - Used by Google, OpenAI, Meta, and NASA!\n"
            "\n"
            "Top Python AI Libraries:\n"
            "  - NumPy, Pandas  -> data processing\n"
            "  - scikit-learn   -> classical machine learning\n"
            "  - TensorFlow, PyTorch -> deep learning\n"
            "  - Matplotlib, Seaborn -> data visualization"
        ),
        "topic": "Python"
    },

    # ── 13. AI LIBRARIES ──────────────────────────────────────
    {
        "keywords": ["tensorflow", "pytorch", "scikit-learn", "scikit", "keras", "numpy", "pandas", "libraries", "library"],
        "response": (
            "Here are the most popular Python AI and ML libraries:\n"
            "\n"
            "  Data Processing:\n"
            "  - NumPy     -> fast numerical computation and arrays\n"
            "  - Pandas    -> data manipulation and analysis\n"
            "\n"
            "  Visualization:\n"
            "  - Matplotlib -> basic charts and graphs\n"
            "  - Seaborn   -> beautiful statistical plots\n"
            "\n"
            "  Machine Learning:\n"
            "  - scikit-learn -> classical ML algorithms\n"
            "\n"
            "  Deep Learning:\n"
            "  - TensorFlow -> deep learning framework by Google\n"
            "  - PyTorch    -> deep learning framework by Meta\n"
            "  - Keras      -> simple deep learning API on top of TensorFlow"
        ),
        "topic": "Python"
    },

    # ── 14. WHAT IS A CHATBOT ─────────────────────────────────
    {
        "keywords": ["what is chatbot", "chatbot kya hai", "chat bot", "what is a chatbot"],
        "response": (
            "A chatbot is a computer program designed to have a conversation with humans.\n"
            "\n"
            "Types of chatbots:\n"
            "  1. Rule-Based   -> follows fixed if-else rules (that is what I am!)\n"
            "  2. AI-Based     -> uses Machine Learning to understand context\n"
            "  3. Hybrid       -> a combination of both approaches\n"
            "\n"
            "Chatbots are widely used in:\n"
            "  - Customer service and support\n"
            "  - Healthcare information\n"
            "  - E-commerce shopping assistance\n"
            "  - Educational platforms"
        ),
        "topic": "Artificial Intelligence"
    },

    # ── 15. RULE-BASED CHATBOT ────────────────────────────────
    {
        "keywords": ["rule based", "rule-based", "how do you work", "how does this chatbot work", "if else"],
        "response": (
            "I am a Rule-Based Chatbot, and here is exactly how I work:\n"
            "\n"
            "  Step 1: You type a message.\n"
            "  Step 2: I convert your message to lowercase.\n"
            "  Step 3: I loop through a list of known keywords.\n"
            "  Step 4: If a keyword is found in your message, I return\n"
            "          the matching response using if-elif-else logic.\n"
            "  Step 5: If nothing matches, I give a polite fallback reply.\n"
            "\n"
            "I do not learn or improve on my own.\n"
            "My rules are pre-programmed — that is what makes me 'rule-based'!"
        ),
        "topic": "Artificial Intelligence"
    },

    # ── 16. DECODELABS ────────────────────────────────────────
    {
        "keywords": ["decodelabs", "decode labs", "about decodelabs", "what is decodelabs"],
        "response": (
            "DecodeLabs is a tech training platform for students and developers!\n"
            "\n"
            "  Location : Greater Lucknow, India\n"
            "  Phone    : +91 89330 06408\n"
            "  Email    : decodelabs.tech@gmail.com\n"
            "  Website  : www.decodelabs.tech\n"
            "\n"
            "DecodeLabs provides hands-on internship training through\n"
            "real-world projects — just like the one you are using right now!"
        ),
        "topic": "DecodeLabs"
    },

    # ── 17. ABOUT THIS PROJECT ────────────────────────────────
    {
        "keywords": ["this project", "about project", "project 1", "internship project", "what is this"],
        "response": (
            "This is Project 1 of the DecodeLabs AI Internship — Batch 2026!\n"
            "\n"
            "  Project Name : Rule-Based AI Chatbot\n"
            "  Language     : Python (Standard Library only)\n"
            "  Concepts     : Control Flow, Functions, String Matching\n"
            "  Files        : chatbot.py, knowledge_base.py\n"
            "\n"
            "Goal: Build a chatbot using if-elif-else logic that handles\n"
            "greetings, AI topics, and general conversation — without\n"
            "using any Machine Learning or external libraries."
        ),
        "topic": "DecodeLabs"
    },

    # ── 18. WHO ARE YOU / NAME ────────────────────────────────
    {
        "keywords": ["who are you", "your name", "what are you", "introduce yourself", "tumhara naam"],
        "response": (
            "I am DecoBot — a Rule-Based AI Chatbot!\n"
            "\n"
            "Built with Python as part of the DecodeLabs AI Internship (Batch 2026).\n"
            "I can answer questions about AI, Machine Learning, Python, and more.\n"
            "\n"
            "I was built to demonstrate that you can create an intelligent-\n"
            "looking chatbot using only basic Python — no fancy libraries needed!\n"
            "\n"
            "Type 'help' to see the full list of topics I know about."
        ),
        "topic": "General"
    },

    # ── 19. THANKS ────────────────────────────────────────────
    {
        "keywords": ["thank you", "thanks", "thank", "shukriya", "thx", "ty"],
        "response": (
            "You're welcome! Happy to help!\n"
            "If you have more questions, feel free to ask anytime."
        ),
        "topic": "General"
    },

    # ── 20. JOKE ──────────────────────────────────────────────
    {
        "keywords": ["joke", "funny", "make me laugh", "tell me a joke", "humor"],
        "response": (
            "Here is a classic programmer joke for you:\n"
            "\n"
            "Why do programmers prefer dark mode?\n"
            "  --> Because light attracts bugs!\n"
            "\n"
            "Hope that made you smile!"
        ),
        "topic": "General"
    },

    # ── 21. MOTIVATION / QUOTE ────────────────────────────────
    {
        "keywords": ["motivate me", "motivation", "quote", "inspire me", "encourage", "i am tired", "struggling"],
        "response": (
            "Here is a quote to keep you going:\n"
            "\n"
            "  'The best way to predict the future is to invent it.'\n"
            "   -- Alan Kay\n"
            "\n"
            "You are learning AI from scratch. That takes courage.\n"
            "Keep coding, keep building. You are doing great!"
        ),
        "topic": "General"
    },

    # ── 22. AI vs ML ──────────────────────────────────────────
    {
        "keywords": ["difference between ai and ml", "ai vs ml", "ml vs ai", "ai and ml", "ai or ml"],
        "response": (
            "Great question! Here is the difference:\n"
            "\n"
            "  AI (Artificial Intelligence):\n"
            "  -> The broader concept of machines mimicking human intelligence.\n"
            "  -> AI is the big umbrella.\n"
            "\n"
            "  ML (Machine Learning):\n"
            "  -> A SUBSET of AI where machines learn from data.\n"
            "  -> ML is one branch under the AI umbrella.\n"
            "\n"
            "Simple analogy:\n"
            "  AI is the pizza.\n"
            "  ML is just one slice of that pizza!\n"
            "  (Deep Learning is an even smaller slice.)"
        ),
        "topic": "Artificial Intelligence"
    },

    # ── 23. DATA SCIENCE ──────────────────────────────────────
    {
        "keywords": ["data science", "what is data science", "data scientist", "data analysis"],
        "response": (
            "Data Science is the field of extracting knowledge and\n"
            "useful insights from large amounts of data.\n"
            "\n"
            "A Data Scientist typically:\n"
            "  - Collects and cleans raw data\n"
            "  - Analyzes patterns and trends\n"
            "  - Builds predictive models using ML\n"
            "  - Presents findings using charts and dashboards\n"
            "\n"
            "Tools used: Python, R, SQL, Tableau, Jupyter Notebooks"
        ),
        "topic": "Artificial Intelligence"
    },

    # ── 24. CAREER IN AI ──────────────────────────────────────
    {
        "keywords": ["career in ai", "job in ai", "ai jobs", "ai career", "become ai engineer", "how to learn ai"],
        "response": (
            "Great ambition! Here is a simple roadmap to a career in AI:\n"
            "\n"
            "  Step 1: Learn Python basics\n"
            "  Step 2: Study Math (Linear Algebra, Statistics, Calculus)\n"
            "  Step 3: Learn NumPy and Pandas for data handling\n"
            "  Step 4: Study Machine Learning with scikit-learn\n"
            "  Step 5: Learn Deep Learning with TensorFlow or PyTorch\n"
            "  Step 6: Build projects (like this one!) for your portfolio\n"
            "  Step 7: Apply for internships and jobs!\n"
            "\n"
            "You are already on Step 1 by being here at DecodeLabs!"
        ),
        "topic": "Artificial Intelligence"
    },

]
