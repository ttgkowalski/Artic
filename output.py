from ibm_conf import MySynthesizeCallback
from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import SynthesizeCallback
import pyaudio
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# --------------  IBMTTS Conf -------------- #
authenticator = IAMAuthenticator('eDo2r9KpxVU1vKV5-xZqVmQpcM9TqFlU1hlbgyiFupm_')
service = TextToSpeechV1(authenticator=authenticator)
service.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/f41e3431-1e96-4758-8c64-d6998adacd54')
# --------------  /IBMTTS Conf -------------- #
test_callback = MySynthesizeCallback()

def output_speech(texto):
    test_callback = MySynthesizeCallback()
    service.synthesize_using_websocket(texto,
                                    test_callback,
                                    accept='audio/wav',
                                    voice="pt-BR_IsabelaV3Voice"
                                    )