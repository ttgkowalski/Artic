from config import API_KEY, API_URL
from recogntion_system import Speech2Text, Text2Speech
import time

def main():    
    speech2text = Speech2Text()
    text2speech = Text2Speech(API_KEY, API_URL)

    
    speech2text.listen_mic()
    
    text = speech2text.audio2text()
    print("Comando por voz: %s"%text)

    speech2text.retun_values()
    #text2speech.text2record_audio(text, 'db_audio/teste.wav')



    

if __name__ == "__main__":
    main()
