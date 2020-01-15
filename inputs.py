import speech_recognition as sr
import pyaudio
from modules import cls



def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Estou te escutando...")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio,language='pt-BR')
            cls()
            print("Your last command: " + frase)
            if frase == "cancelar":
                cls()
                print("Sem problemas, até mais")
                exit()
            else:
                print(frase)
                cls()
                return frase
                
        except sr.UnknownValueError:
            print("Não entendi")
        finally:
            pass
        
frase_returned = ouvir_microfone
