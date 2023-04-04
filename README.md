# **ChatGPT Assistant**

## **A simple Python program enables you to talk to GPT. Just enter your API key and chat with it.**

---
Well, this is a program that allows you to interact and chat with chatGPT using your voice and hear its response to your requests. In previous versions, I coded it sequentially in a single file, and now I have made some changes by dividing it into a directory tree and converting the ChatGPT_Assistant program into a class for easier reuse in OOP-style coding projects

### ChatGPTAssistant class has the following methods

- **init(self, api_key)**: a method that initializes the ChatGPTAssistant class and performs the initialization of the class's initial attributes.
speak(self, content): a method that reads the content passed in using speech.
- **listen(self)**: a method that listens to sound from the microphone, converts it to text, and returns that text in lowercase.
- **generate_text(self, prompt)**: a method that generates text based on the input prompt using the OpenAI API and returns that text.
- **chat(self)**: a method that interacts with the user, listens to and processes user requests, generates text responses, and reads that text using speech.
- **check_API_key(self)**: a method that checks the validity of the API key.
- **auth(self)**: a method that authenticates the API key by requesting the user to enter a new key when the current key is invalid.

**To understand more about how I verify the accuracy of the API key that the user inputs or how I retrieve information from the model, etc., you can access and read the following documents:**

- Completions: <https://platform.openai.com/docs/api-reference/completions>
- Models: <https://platform.openai.com/docs/api-reference/models>
- Chat: <https://platform.openai.com/docs/api-reference/chat>

---

### Install dependencies using pip

    pip install openai
    pip install speechrecognition 
    pip install pyttsx3 
    pip install PyAudio

### How to use this dumb_ass Python program

1. Download and run the file named "Main.py"
2. Enter your API key
3. Talk to GPT

### How to get your API key?

To get an API key for OpenAI, you will need to create an account on the OpenAI website (<https://openai.com/>) and follow these steps:

1. Log in to your OpenAI account.
2. Go to the API keys page.
3. Click on the "Create new API key" button.
4. Enter a name for your API key (optional).
5. Choose the permissions you want to grant to the API key.
6. Click on the "Create API key" button.
7. Copy the generated API key to use in your code.

Note: OpenAI requires you to have a paid subscription to use some of their language models. If you want to use one of these models, you will need to subscribe and provide payment information before you can generate an API key.
