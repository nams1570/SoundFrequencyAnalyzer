#For Karim
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt

#Taking input from microphone
#Same program as before
fs = 44100 #sampling frquency 
duration = 5
channels = 1
print("Recording for {} seconds".format(duration))
audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=channels)

sd.wait()
audio = np.squeeze(audio_data)
print(audio_data)

wavfile.write("test.wav", fs, audio)

fourier = np.fft.fft(audio_data)
print(fourier)