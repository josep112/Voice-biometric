import dill
import pyaudio
import wave
import pywt
import numpy as np
import os
from os import system
import soundfile as sf

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 2

 
audio = pyaudio.PyAudio()
os.system('clear')

re = True
x = 0


while(re):
    WAVE_OUTPUT_FILENAME ="temp.wav"

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("recording...")
    frames = []
     
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
     
    # stop Recording
    stream.stop_stream()
    stream.close()
     
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print("finished recording")

    system('python demo_file.py')

    x = x + 1
    if(input("Repeat? y/n ") == "n"):
        re = False

audio.terminate()

