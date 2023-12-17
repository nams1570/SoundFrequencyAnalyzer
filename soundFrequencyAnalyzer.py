#For Karim
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt


def convertToFreqDomain(audio:np.ndarray)->np.ndarray:
    """Runs an fft on given audio data, returning freq domain output"""
    return np.fft.fft(audio,axis=0)

#Taking input from microphone
#Same program as before

print("Would you like to ready to record? Type any letter when you are ready and 'q' to quit")
userInput = input()

while userInput!= "q":
    fs = 44100  # sampling frequency
    duration = 5  # duration in seconds
    channels = 1

    print("Recording for {} seconds".format(duration))
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    audio = np.squeeze(audio_data)
    
    # Save the audio data to a WAV file
    wavfile.write("test.wav", fs, audio)
    print("Recording saved as test.wav")

    fourier = convertToFreqDomain(audio_data[:,0])

    # Plotting the data
    print("Thank you for your sound input! Here is the frequency analysis of your sound")
    print("Plotting...")
    frequencyDomain = np.fft.fftfreq(len(fourier), 1/fs)
    
    plt.plot(frequencyDomain, np.abs(fourier), color='green')  # Plot magnitude of the Fourier transform
    plt.title("Frequency Analysis")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.savefig("fourier.png")
    plt.show()
    print("Plot saved as fourier.png")

    print("Would you like to record again? Type any letter when you are ready and 'q' to quit")
    userInput = input()

print("Thank you for using the sound frequency analyzer! Goodbye!")
