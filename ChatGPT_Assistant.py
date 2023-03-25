import openai
import pyttsx3
import speech_recognition as sr

def gpt_speak(content):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(content)
    engine.runAndWait()

def gpt_listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        audio = recognizer.listen(mic)
    try:
        message = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        message = ""
    return message.lower() # type: ignore

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip() # type: ignore
    return message

def chat():
    print("Welcome to ChatGPT Assistant! Speak or type below:")
    gpt_speak("Welcome to ChatGPT Assistant! Speak or type below:")
    while True:
        print("You: ", end="")
        user_input = gpt_listen()
        print(user_input)
        if user_input in ["exit", "quit", "goodbye", "ok bye"]:
            print("ChatGPT Assistant: Goodbye!")
            break
        prompt = f"You: {user_input}\nChatGPT Assistant:"
        response = generate_text(prompt)
        print("ChatGPT Assistant:", response)
        gpt_speak(response)


if __name__ == '__main__':
    API_input = input("Enter your OpenAI API key: ")
    while True:
        if API_input.startswith("sk-"):
            openai.api_key = API_input
            break
        else:
            print("Invalid API key. Please enter a valid key.")
            API_input = input("Enter your OpenAI API key: ")
    chat()
    