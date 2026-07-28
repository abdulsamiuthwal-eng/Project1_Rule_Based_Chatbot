# chatbot.py
"""
============================================================
  DecoBot - Rule-Based AI Chatbot
  DecodeLabs AI Internship | Project 1 | Batch 2026
============================================================

Description:
  A simple rule-based chatbot built using Python.
  It uses if-elif-else logic and keyword matching
  to respond to user inputs about AI, ML, Python,
  DecodeLabs, and general conversation topics.

Tech Used:
  - Python (Standard Library only)
  - Modules: datetime, time, random

Files:
  - chatbot.py       : main logic and chatbot loop
  - knowledge_base.py: all Q&A data (keywords + responses)

How to Run:
  python chatbot.py
============================================================
"""

# ── Standard library imports (no external libraries needed) ──
import time
import random
from datetime import datetime

# ── Import our Q&A knowledge base ────────────────────────────
from knowledge_base import QA_PAIRS


# ============================================================
#  SECTION 1: DISPLAY / UI FUNCTIONS
#  These functions handle what the user sees on screen.
# ============================================================

def print_separator():
    """Prints a simple line to separate chat sections."""
    print("-" * 55)


def print_header():
    """
    Prints the welcome banner when the chatbot starts.
    This is the first thing the user sees.
    """
    print()
    print("=" * 55)
    print("         DecoBot — Rule-Based AI Chatbot")
    print("    DecodeLabs AI Internship | Batch 2026")
    print("=" * 55)
    print()


def print_help():
    """
    Displays all available commands and conversation topics.
    Triggered when the user types 'help'.
    """
    print()
    print_separator()
    print("  HELP MENU — Here is what I can talk about:")
    print_separator()
    print()

    print("  [ Artificial Intelligence ]")
    print("    -> 'what is ai'")
    print("    -> 'types of ai'")
    print("    -> 'ai vs ml'")
    print("    -> 'nlp' or 'natural language processing'")
    print("    -> 'computer vision'")
    print("    -> 'data science'")
    print("    -> 'career in ai'")
    print()

    print("  [ Machine Learning ]")
    print("    -> 'machine learning'")
    print("    -> 'supervised learning'")
    print("    -> 'unsupervised learning'")
    print()

    print("  [ Deep Learning ]")
    print("    -> 'deep learning'")
    print("    -> 'neural network'")
    print()

    print("  [ Python & Libraries ]")
    print("    -> 'python'")
    print("    -> 'tensorflow' / 'pytorch' / 'libraries'")
    print()

    print("  [ Chatbot Topics ]")
    print("    -> 'what is a chatbot'")
    print("    -> 'rule-based chatbot'")
    print("    -> 'how do you work'")
    print()

    print("  [ DecodeLabs ]")
    print("    -> 'decodelabs'")
    print("    -> 'about project'")
    print()

    print("  [ General ]")
    print("    -> 'hello' / 'hi'")
    print("    -> 'how are you'")
    print("    -> 'who are you'")
    print("    -> 'tell me a joke'")
    print("    -> 'motivate me'")
    print("    -> 'thanks'")
    print()

    print("  [ Commands ]")
    print("    -> 'date'   — shows today's date")
    print("    -> 'time'   — shows the current time")
    print("    -> 'help'   — shows this help menu")
    print("    -> 'bye' / 'exit' / 'quit' — exit the chatbot")
    print()
    print_separator()
    print()


# ============================================================
#  SECTION 2: HELPER / UTILITY FUNCTIONS
#  Small functions that support the main chatbot logic.
# ============================================================

def get_time_greeting():
    """
    Returns a greeting based on the current time of day.

    Morning   : 5 AM  to 12 PM
    Afternoon : 12 PM to 5 PM
    Evening   : 5 PM  to 9 PM
    Night     : 9 PM  onwards
    """
    hour = datetime.now().hour   # get current hour (0-23)

    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"


def get_current_date():
    """
    Returns today's date in a human-readable format.
    Example output: "Today is: Friday, July 25, 2026"
    """
    today = datetime.now()
    return "Today is: " + today.strftime("%A, %B %d, %Y")


def get_current_time():
    """
    Returns the current time in 12-hour format.
    Example output: "Current time: 01:30 PM"
    """
    now = datetime.now()
    return "Current time: " + now.strftime("%I:%M %p")


def get_response(user_input):
    """
    Searches the QA_PAIRS knowledge base for a matching response.

    How it works:
      1. Convert user input to lowercase (case-insensitive match).
      2. Loop through each Q&A entry in QA_PAIRS.
      3. For each entry, check if any keyword is present in the input.
      4. If a match is found, return that response.
      5. If no match is found, return None.

    Note: This uses Python's 'in' operator — NOT regex.
    The matching is simple, readable, and beginner-friendly.

    Parameters:
      user_input (str): The message typed by the user.

    Returns:
      str  : The matching response text, OR
      None : If no keyword matched the user input.
    """

    # Convert to lowercase so matching is not case-sensitive
    # Example: "Hello" and "HELLO" and "hello" all work the same
    user_input_lower = user_input.lower().strip()

    # Loop through every Q&A entry in the knowledge base
    for qa in QA_PAIRS:

        # Check each keyword in this Q&A entry
        for keyword in qa["keywords"]:

            # Check if the keyword appears anywhere in the user's message
            if keyword in user_input_lower:
                return qa["response"]   # Found a match! Return the response.

    # No keyword matched — return None to signal no match found
    return None


def get_fallback_response(name):
    """
    Returns a polite message when the chatbot does not understand
    what the user typed.

    Uses random.choice() to pick from a list of fallback messages
    so the bot does not always give the same 'I don't know' reply.

    Parameters:
      name (str): The user's name (for personalized response).

    Returns:
      str: A friendly fallback message.
    """
    fallback_options = [
        f"Hmm, I am not sure about that, {name}. Try typing 'help' to see what I know!",
        f"I did not quite understand that, {name}. Can you rephrase it?",
        f"That is outside my knowledge for now, {name}. Ask me about AI or Machine Learning!",
        f"I am still learning, {name}! Try asking about AI, Python, or DecodeLabs.",
        f"I don't have an answer for that yet, {name}. Type 'help' to see available topics.",
    ]

    # Randomly pick one fallback to avoid repetition
    return random.choice(fallback_options)


# ============================================================
#  SECTION 3: MAIN CHATBOT FUNCTION
#  This is the core function that runs the entire chatbot.
# ============================================================

def run_chatbot():
    """
    Main function that starts and runs the DecoBot chatbot.

    Flow:
      1. Print welcome banner
      2. Ask the user for their name
      3. Greet the user personally with a time-based greeting
      4. Enter the main conversation loop
      5. Keep running until the user types 'bye', 'exit', or 'quit'
    """

    # ── Step 1: Show the welcome banner ──────────────────────
    print_header()

    # ── Step 2: Ask for the user's name ──────────────────────
    print("  Before we begin, I'd love to know your name.")
    name = input("  What is your name? >> ").strip()

    # Use a default name if the user just presses Enter
    if not name:
        name = "Friend"

    # ── Step 3: Greet the user personally ────────────────────
    time_greeting = get_time_greeting()   # Morning / Afternoon / Evening / Night

    print()
    print(f"  {time_greeting}, {name}! I am DecoBot, your AI learning assistant.")
    print(f"  Type 'help' to see all topics  |  Type 'bye' to exit.")
    print()
    print_separator()
    print()

    # ── Step 4: Main conversation loop ───────────────────────
    # This loop keeps running until the user types an exit command.

    while True:

        # Get user input from the keyboard
        user_input = input(f"  {name} >> ").strip()

        # ── Handle empty input ────────────────────────────────
        if not user_input:
            print()
            print("  DecoBot >> Please type something! Type 'help' if you are stuck.")
            print()
            continue   # Go back to the top of the loop

        print()   # Blank line for readability

        # ── Check for EXIT commands ───────────────────────────
        # If the user wants to leave, print a goodbye and stop the loop.
        if user_input.lower() in ["bye", "exit", "quit"]:
            print(f"  DecoBot >> Goodbye, {name}! It was great chatting with you.")
            print(f"             Keep learning and keep building. See you next time!")
            print()
            print("=" * 55)
            print("        Thanks for using DecoBot | DecodeLabs")
            print("=" * 55)
            print()
            break   # Exit the while loop — chatbot stops here

        # ── Check for HELP command ────────────────────────────
        elif user_input.lower() == "help":
            print_help()

        # ── Check for DATE command ────────────────────────────
        elif user_input.lower() in ["date", "today", "what is today", "what is the date", "current date"]:
            print(f"  DecoBot >> {get_current_date()}")
            print()

        # ── Check for TIME command ────────────────────────────
        elif user_input.lower() in ["time", "what time", "what is the time", "current time"]:
            print(f"  DecoBot >> {get_current_time()}")
            print()

        # ── Search the KNOWLEDGE BASE ─────────────────────────
        # If none of the special commands matched, look in QA_PAIRS.
        else:
            response = get_response(user_input)

            if response:
                # A keyword match was found — display the response
                print("  DecoBot >>")
                for line in response.split("\n"):
                    print(f"             {line}")
                print()

            else:
                # No match found — show a polite fallback message
                print(f"  DecoBot >> {get_fallback_response(name)}")
                print()

        # Print a separator after every reply for clean formatting
        print_separator()
        print()


# ============================================================
#  ENTRY POINT
#  Python runs this block when you execute: python chatbot.py
# ============================================================

if __name__ == "__main__":
    run_chatbot()
