import speech_recognition as sr
import os
import sys
import time
import timeit
from config import ANS
from src import *
from src import denoise as dn
from src import noiseProfiler as npf
import soundfile

class Speech2Text:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        #self.recognizer.dynamic_energy_threshold = True
        #self.recognizer.non_speaking_duration
        #self.recognizer.pause_threshold = 0.7 #seconds
        self.micro = sr.Microphone(sample_rate=44000)
        print("Microfone iniciado com sucesso")


    def denoisy(self, sound):
        denoiser = dn.Denoiser()
        data, sampleRate = soundfile.read(sound)
        noiseProfile = npf.NoiseProfiler(data)
        dataNoise = noiseProfile.getNoiseDataPredicted()
        dataDenoised = denoiser.denoise(Xin=data, Nin=dataNoise)
        return dataDenoised
    
    def listen_mic(self):       
        
        with self.micro as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Microfone aberto e escutando")
            audio = self.recognizer.listen(source, timeout=5) #timeout(sec) tempo que microfone ficara aberto até a primeira frase ser dita
            with open("44k.wav", "wb") as f:
                f.write(audio.get_wav_data())
                self.denoised = self.denoisy(sound = "44k.wav")
            #return self.audio2text(audio)
            return self.denoised

    def audio2text(self, audio):      
            try:
                frase = self.recognizer.recognize_google(audio,language='pt-BR')              
                # if frase == "cancelar":
                #     print("Sem problemas, até mais")
                #     exit()
                # else:
                print(frase)
                return frase.lower()

            except sr.UnknownValueError:
                frase = "Não entendi"
                print(frase)
                return frase.lower()
            
    def somalista(self, numeros):
        soma = 0
        for i in numeros:
            soma = soma + i
        return soma

    def word_to_num(self, input_word):
        num_splited = str(input_word).lower().split(' ')
        print(num_splited)
        filter_e = list(filter(lambda a: a != 'e', num_splited))
        print(filter_e)
        array_store_num = []
        for i in filter_e:
            str_num = str(i)
            int_num = ANS[str_num]
            array_store_num.append(int_num)
        
        total = self.somalista(array_store_num)        
        return total

            
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from time import time, ctime
        
class Text2Speech:

    def __init__(self, api_key, api_url):
        authenticator = IAMAuthenticator(api_key)
        self.text_to_speech = TextToSpeechV1(authenticator=authenticator)
        self.text_to_speech.set_service_url(api_url)
        self.voice = 'pt-BR_IsabelaV3Voice'
        self.accept = 'audio/wav'

    def text2record_audio(self, text, name_file = '{}.wav'.format(ctime(time())).replace(" ","").replace(":", ''), path="./db_audio/"):
        with open(path + name_file, 'wb') as audio_file:
            audio_file.write(
                self.text_to_speech.synthesize(
                    text,
                    voice=self.voice,
                    accept=self.accept        
                ).get_result().content)

    def create_db_from_dic(self, dic):        
        for i in dic.keys():
            a.text2record_audio(dic[i], i+'.mp3')


if __name__ == "__main__":    
    from config import API_KEY, API_URL, JORNADA
    # criar banco de audios
    a = Text2Speech(API_KEY,API_URL)
    a.create_db_from_dic(JORNADA)