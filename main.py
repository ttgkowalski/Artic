import speech_recognition as sr
import os
import sys
from modules import *




def switcher(command):
    if command == "say hello":
        sayHello()
    elif command == "open my home":
        openHome()

    elif command == "open my documents":
        openDocuments()

    elif command == "open my images":
        openImages()

    elif command == "open my downloads":
        openDownloads()
    
    elif command == "open the browser":
        openBrowser()


#Funcao responsavel por limpar o console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuario que esta pronto para ouvir
        print("Say something: ")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio,language='en-US')
            print("Your last command: " + frase)
            if frase == "goodbye":
                cls()
                print("goodbye!")
                exit()
            else:
                switcher(frase)
                
        except sr.UnknownValueError:
            print("Não entendi")
        finally:
            pass
        
        


while True:
    ouvir_microfone()


