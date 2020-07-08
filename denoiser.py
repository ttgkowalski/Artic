"""
Denoise a file (pass the filename as argument)
"""

import os
import argparse
import time
import soundfile
from src.wavelet_denoiser.denoise import Denoiser
from src.wavelet_denoiser.noiseProfiler import NoiseProfiler

def denoise_audio(audio_data):
    
    data, sampleRate = soundfile.read(audio_data)
    
    if len(data.shape) > 1:
        data = data.T[0]

    denoiser = Denoiser()    
    dataNoise = None
    noiseProfile = NoiseProfiler(data)
    dataNoise = noiseProfile.getNoiseDataPredicted()
    dataDenoised = denoiser.denoise(Xin=data, Nin=dataNoise)


    return dataDenoised, sampleRate

