import dill
import pyaudio
import wave
import pywt
import numpy as np
import os
import soundfile as sf
import matplotlib.pyplot as plt
# from sklearn.svm import SVC
from sklearn import svm



print ("Loading svm-model.dill....")
# Load PNN
with open('svm-model.dill', 'rb') as f:
    classifier = dill.load(f)

def wavedec(audio, mode='haar', level=5):

    # read audio wav
    data, samplerate = sf.read(audio)  

     #cetak ukuran array data
    print(str(data.shape))

    #cetak samplerate
    print(str(samplerate))


    #pre emphasis 
    # A pre-emphasis filter is useful in several ways: 
    # (1) balance the frequency spectrum since high frequencies usually have smaller magnitudes compared to lower frequencies
    # (2) avoid numerical problems during the Fourier transform operation 
    # (3) may also improve the Signal-to-Noise Ratio (SNR)

    # pre_emphasis = 0.95
    # emphasized_signal = np.append(data[0], data[1:] - pre_emphasis * data[:-1])

     #ambil data pada kolom 1  
    #x=data[:,0]
    # x = emphasized_signal

    x = data

    #ca: koef aproximasi, cd:koef.detail, haar:filter)
    c = pywt.wavedec(x, mode, level=level)


    print(c[0])


    print ("Plot Data\n")
	#plot original data
    plt.figure(1)
    plt.title('Original Signal Wave')
    plt.plot(data)

    # plt.figure(2)
    # plt.title('emphasized_signal')
    # plt.plot(emphasized_signal) 

	#plot wavelet data
    plt.figure(3)
    plt.title('wavelet Signal Wave')
    plt.plot(c[0])

   
    plt.show()

    return c[0]


wavelet = wavedec("temp.wav")


wavelet = np.expand_dims(wavelet, axis=0)

res = (classifier.predict(wavelet))
prob = (classifier.predict_proba(wavelet)[0])
prob_total = sum(prob)*100
prob_per_class_dictionary = dict(zip(classifier.classes_, prob))
winner = np.argmax(prob)

print ("probabilitas : \n", prob)
print ("probabilitas per class: \n", prob_per_class_dictionary)
print ("Predicted class : \n", res)

print (np.argmax(prob))


print ("RESULT : \n")
if prob[winner] > 0.55 : #probabilitas nilai arraynya apa isi arraynya di bawah 1
    print ('INI ADALAH SUARA SI: ', res)
    
    #system('python test_fail_indicator.py')
else:
    print ('Unknown')
    #system('python test_success_indicator.py') 








# # gets a list of ['most_probable_class', 'second_most_probable_class', ..., 'least_class']
# results_ordered_by_probability = map(lambda x: x[0], sorted(zip(classifier.classes_, prob), key=lambda x: x[1], reverse=True))
# print (results_ordered_by_probability)




#print ("Classes : ",classifier.best_estimator_.classes)

# print ("RESULT : \n")
# if np.argmax(prob) > 0.8 : #probabilitas nilai arraynya apa isi arraynya di bawah 1
#     print('INI ADALAH SUARA SI: ', res)
    
#     #system('python test_fail_indicator.py')
# else:
#     print('Unknown')
#     #system('python test_success_indicator.py') 




