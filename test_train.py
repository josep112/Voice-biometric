import sys
from create_dataset import wavelet_data
import pywt

import dill
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import numpy as np
from neupy.algorithms import PNN

import time

#path ="data"

start_time = time.time()

def train(path="data"):
    audio_data, audio_label = wavelet_data(path)

    X = np.float32(audio_data) 
    print('shape X:', str(X.shape))

    Y = audio_label
    print('shape Y: ', str(len(Y)))

    # Encode class target ke integer
    # encoder = LabelEncoder()
    # encoder.fit(img_label)
    # Y = encoder.transform(img_label)
    # print('shape Y:', str(Y.shape))

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2) #untuk spilt data latih n uji
    print('X_train shape: ', X_train.shape)
    print('X_test shape', X_test.shape)

    pnn = PNN(std=2, verbose=False)
    pnn.train(X_train, Y_train)

    with open('pnn-model.dill', 'wb') as f:
        dill.dump(pnn, f)

    result = pnn.predict(X_test)

    n_predicted_correctly = np.sum(result == Y_test)
    n_test_samples = X_test.shape[0]

    print("Guessed {} out of {}".format(n_predicted_correctly, n_test_samples))
    print("Processiing time : %s seconds" % (time.time() - start_time))

if __name__ == '__main__':
    train()
