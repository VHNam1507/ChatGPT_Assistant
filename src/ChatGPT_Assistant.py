import openai
import pyttsx3
import requests
import speech_recognition as sr

class ChatGPTAssistant:
    def __init__(self, api_key):
        self.api_key = api_key
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.recognizer = sr.Recognizer()

    def speak(self, content):
        self.engine.setProperty('voice', self.voices[1].id)
        self.engine.say(content)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as mic:
            self.recognizer.adjust_for_ambient_noise(mic)
            audio = self.recognizer.listen(mic)
        try:
            message = self.recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            message = ""
        return message.lower() # type: ignore

    def generate_text(self, prompt):
        openai.api_key = self.api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response.choices[0].text.strip() # type: ignore
        return message

    def chat(self):
        print("Welcome to ChatGPT Assistant! Speak or type below:")
        self.speak("Welcome to ChatGPT Assistant! Speak or type below:")
        while True:
            print("You: ", end="")
            user_input = self.listen()
            print(user_input)
            if user_input in ["exit", "quit", "goodbye", "ok bye"]:
                print("ChatGPT Assistant: Goodbye!")
                self.speak("Goodbye!")
                break
            prompt = f"You: {user_input}\nChatGPT Assistant:"
            response = self.generate_text(prompt)
            print("ChatGPT Assistant:", response)
            self.speak(response)

    def check_API_key(self):
        #Check API key is valid
        if len(self.api_key) != 64 and not self.api_key.startswith("sk-") and not self.api_key[3:].isalnum():
            print("Invalid API key. Please enter a valid key.")
            return False
        
        #check API key if it is enabled
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        url = "https://api.openai.com/v1/completions"
        data = {
            "model": "text-davinci-003",
            "prompt": "Say this is a test",
            "max_tokens": 7,
            "temperature": 0
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code != 200:
            print("Invalid API key. Please enter a valid key.")
            return False
        return True

    def auth(self):
        if self.check_API_key() == True:
            self.speak("API key verified.")
        else:
            new_API_input = input("Enter a valid API key please: ")
            self.api_key = new_API_input
            self.auth()
