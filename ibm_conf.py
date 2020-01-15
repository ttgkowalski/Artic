import pyaudio
from ibm_watson.websocket import SynthesizeCallback

class Play(object):
    """
    Wrapper to play the audio in a blocking mode
    """
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 22050
        self.chunk = 1024
        self.pyaudio = None
        self.stream = None

    def start_streaming(self):
        self.pyaudio = pyaudio.PyAudio()
        self.stream = self._open_stream()
        self._start_stream()

    def _open_stream(self):
        stream = self.pyaudio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            output=True,
            frames_per_buffer=self.chunk,
            start=False
        )
        return stream

    def _start_stream(self):
        self.stream.start_stream()

    def write_stream(self, audio_stream):
        self.stream.write(audio_stream)

    def complete_playing(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()

class MySynthesizeCallback(SynthesizeCallback):
    def __init__(self):
        SynthesizeCallback.__init__(self)
        self.play = Play()

    def on_connected(self):
        print('Opening stream to play')
        self.play.start_streaming()

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_timing_information(self, timing_information):
        print(timing_information)

    def on_audio_stream(self, audio_stream):
        self.play.write_stream(audio_stream)

    def on_close(self):
        print('Completed synthesizing')
        self.play.complete_playing()