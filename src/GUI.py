import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import threading
import queue

import openai
import pyttsx3
import speech_recognition as sr

# Set up OpenAI API key
def auth(api_key):
    if api_key.startswith("sk-"):
        openai.api_key = api_key
        return True
    return False

class ChatGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ChatGPT Assistant")
        self.chat_history = tk.Text(self.root, state=tk.DISABLED)
        self.chat_history.pack(fill=tk.BOTH, expand=True)
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill=tk.X, padx=5, pady=5)
        self.input_box = tk.Entry(self.input_frame)
        self.input_box.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.input_box.bind("<Return>", self.send_message)
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)
        self.chat_queue = queue.Queue()
        self.chat_thread = threading.Thread(target=self.run_chatbot)
        self.chat_thread.start()
        
    def run_chatbot(self):
        while True:
            message = self.chat_queue.get()
            if message is None:
                break
            response = self.generate_text(message)
            self.chat_history.configure(state=tk.NORMAL)
            self.chat_history.insert(tk.END, "You: " + message + "\n")
            self.chat_history.insert(tk.END, "ChatGPT Assistant: " + response + "\n")
            self.chat_history.see(tk.END)
            self.chat_history.configure(state=tk.DISABLED)
            self.gpt_speak(response)
            
    def send_message(self, event=None):
        message = self.input_box.get()
        if message.strip():
            self.input_box.delete(0, tk.END)
            self.chat_queue.put(message.lower())
            
    def generate_text(self, prompt):
        response = openai.Completion.create(
            model='gpt-3.5-turbo',
            messages=prompt
        )
        message = response.choices[0].text.strip() # type: ignore
        return message
    
    def gpt_speak(self, content):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(content)
        engine.runAndWait()
        
    def start(self):
        api_key = simpledialog.askstring("OpenAI API Key", "Enter your OpenAI API key:")
        if not auth(api_key):
            messagebox.showerror("Error", "Invalid API key.")
            self.root.destroy()
            return
        self.root.deiconify()
        self.root.mainloop()
        self.chat_queue.put(None)
        self.chat_thread.join()
        
if __name__ == "__main__":
    chat_gui = ChatGUI()
    chat_gui.start()
