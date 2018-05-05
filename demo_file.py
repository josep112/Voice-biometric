import dill
import pyaudio
import wave
import pywt
import numpy as np
import os
from os import system
import soundfile as sf

print ("Loading pnn-model.dill....")
# Load PNN
with open('pnn-model.dill', 'rb') as f:
    pnn = dill.load(f)

def wavedec(audio, mode='haar', level=5):

    # read audio wav
    data, samplerate = sf.read(audio)  

     #cetak ukuran array data
    print(str(data.shape))

    #cetak samplerate
    print(str(samplerate))

     #ambil data pada kolom 1  
    #x=data[:,0]
    x=data
    #ca: koef aproximasi, cd:koef.detail, haar:filter)
    c = pywt.wavedec(x, mode, level=level)

    # for x in range(len(ca)):
    #     print(str(ca[x]))    
    #fd = ca.flatten()

    # np.float32(ca)
    # print('FD ADALAH: ' + str(len(c[0])))
    print(c[0])

    return c[0]

print ("Wavelet Temp.wav...")

wavelet = wavedec("temp.wav")

wavelet = np.expand_dims(wavelet, axis=0) #chek dokumentasi ato stack overflow

print ("Check data...")
res = pnn.predict(wavelet) #hasil prediksi kelas pnn dari wavelet (dalam bentuk array, isi arraynya 0 dan 1)
prob = pnn.predict_proba(wavelet) #hasil prediksi di luar kelas (data yg tidak terdaftar) (dalam bentuk array isi array 0 dan isi)
print ("RESULT : \n")
if np.argmax(prob) < 0: #probabilitas nilai arraynya apa isi arraynya di bawah 1
    print('Unknown')
    system('python test_fail_indicator.py')
else:
    print('INI ADALAH SUARA SI: ', res)
    system('python test_success_indicator.py') 

