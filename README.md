#Transformer-Based Chatbot

This project contains a Python-based chatbot using two Hugging Face models:
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- `microsoft/DialoGPT-small`

It supports contextual conversation using transformer models and a basic in-memory chat history (via `ChatMemory` class).

---

1. Setup instructions

Install python if its not already installed .
Install Required Libraries
Open Command Prompt and run:
"pip install transformers torch"

Create a folder named chatbot_project and inside it, create 3 files name model_loader.py, chat_memory.py , interface.py.

Write the code for the 3 files and run the interface file.


2.How to run

you can run like this,
    Open terminal in the chatbot_project folder and run:
        "python interface.py"
or 
    Directly clicking the run button in the VS code Top right side.

3.Sample interaction example

🤖 Chatbot ready. Type '/exit' to quit.

You: what is the capital of france
Bot: The capital of France is Paris.

You: what is the capital of germany
Bot: Germany's capital city is Berlin, located in the state of Brandenburg.

You: who is the founder of python
Bot: The founder of Python is Guido van Rossum, who developed the language in the mid-1990s as a programming language for the web. Python is a high-level, interpreted, object-oriented, and dynamic programming language that is used for web development, data analysis, and machine learning.

You: /exit
Exiting chatbot. Goodbye!