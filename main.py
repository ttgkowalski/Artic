from config import API_KEY, API_URL
from recogntion_system import Speech2Text, Text2Speech

def main():    
    speech2text = Speech2Text()
    text2speech = Text2Speech(API_KEY, API_URL)

    text = speech2text.listen_mic()
    print("Comando por voz: %s"%text)

    text2speech.text2record_audio(text, 'teste.wav')



    

if __name__ == "__main__":
    main()
