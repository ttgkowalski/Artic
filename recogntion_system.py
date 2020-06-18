import speech_recognition as sr
import os
import time
import timeit
import pyaudio
import wave
from config import ANS
from playsound import playsound

class Speech2Text:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        #self.recognizer.dynamic_energy_threshold = True
        #self.recognizer.non_speaking_duration
        #self.recognizer.pause_threshold = 0.7 #seconds
        #self.micro = sr.Microphone(sample_rate=44000)
        #print("Microfone iniciado com sucesso")
    
    def listen_mic(self):
        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 2
        fs = 44100  # Record at 44100 samples per second
        seconds = 7
        filename = "swap/in_tmp_user.wav"

        p = pyaudio.PyAudio()  # Create an interface to PortAudio
        
        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        print('Recording')
        playsound("db_audio/ui-check.wav")
        
        # Store data in chunks for 3 seconds
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream 
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()
        print("Finalizando gravação...")

        # Save the recorded data as a WAV file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        os.system("python3 denoiser.py -i swap/in_tmp_user.wav -o swap/out_tmp_user.wav")

    def audio2text(self):
        with sr.AudioFile("swap/out_tmp_user.wav") as source:
            audio = self.recognizer.record(source)

        try:
            success = self.recognizer.recognize_google(audio, language = 'pt-BR')
        except LookupError:
            print("Could not understand audio")
        
        return self.recognizer.recognize_google(audio, language = 'pt-BR').lower()
                    
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
