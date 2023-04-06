import GUI
from ChatGPT_Assistant import ChatGPTAssistant as chatGPT

if __name__=='__main__':
    API_input = input("Input your API key: ")

    assistant = chatGPT(API_input)
    assistant.auth()
    assistant.chat()