import soundfile as sf #import audio wav
import scipy.io.wavfile
#import pywt #import wavelet

data, samplerate = sf.read('temp.wav')  # read audio wav
print(str(data.shape)) #cetak ukuran array data
print(str(samplerate)) #cetak samplerate
print(data)
#x=data[:,0] #ambil data pada kolom 1 
#ca,cd=pywt.dwt(x, 'haar')#ca: koef aproximasi, cd:koef.detail, haar:filter)
#print(ca)
rate, data = scipy.io.wavfile.read('temp.wav')
print(str(data.shape))
print(str(rate))
print(data)