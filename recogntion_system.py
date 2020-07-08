import src.speech_recognition as sr
import os
import time
from timeit import default_timer as timer
import pyaudio
import wave
from io import BytesIO
from config import ANS
import denoiser as dn
import numpy as np

class Speech2Text:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.resultados = []
        #self.recognizer.dynamic_energy_threshold = True
        #self.recognizer.non_speaking_duration
        #self.recognizer.pause_threshold = 0.7 #seconds
        start = timer()
        self.micro = sr.Microphone(sample_rate=44000)
        end = timer()
        self.resultados.append(end - start)
        self.instanciar_mic = end - start
        print("Microfone iniciado com sucesso")
    
    def listen_mic(self):
        with self.micro as source:
            print('Ajustando para ambiente')
            start = timer()
            self.recognizer.adjust_for_ambient_noise(source)
            end = timer()
            self.resultados.append(end - start)
            self.ajustar_env = end - start
            print("Escutando...")
            audio = self.recognizer.listen(source)
            self.wav_data = audio.get_wav_data()
            start = timer()
            self.denoised, self.sampleRate = dn.denoise_audio(audio_data=BytesIO(self.wav_data))
            end = timer()
            self.resultados.append(end - start)
            self.denoise_time = end - start
        
    def retun_values(self):
        print("Instanciar microfone: {}".format(self.instanciar_mic))
        print("Ajustar ao ambiente: {}".format(self.ajustar_env))
        print("Remover ruído: {}".format(self.denoise_time))
        print("Reconhecer: {}\n".format(self.reconhecer))
        total = self.somalista(self.resultados)
        print("Total: {}".format(total))
        

    def audio2text(self):
        start = timer()
        with sr.AudioFile("swap/out_tmp_user.wav") as source:
            audio = self.recognizer.record(source)
            end = timer()
            self.resultados.append(end - start)
            self.reconhecer = end - start
            return self.recognizer.recognize_google(sr.AudioData(np.int16(self.denoised/np.max(np.abs(self.denoised)) * 32767).tobytes(), self.sampleRate, 2), language = 'pt-BR').lower()

        try:
            return self.recognizer.recognize_google(audio, language = 'pt-BR').lower()
        except LookupError:
            print("Could not understand audio")
        
        
                    
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

    def text2record_audio(self, text, name_file = '{}.wav'.format(ctime(time())).replace(" ","").replace(":", ''), path=""):
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
