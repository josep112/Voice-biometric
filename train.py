import sys 
from create_dataset import wavelet_data
import pywt #untuk wavelet (inklut normalisasi)

import dill #import untuk nimpen hasil pnn
from sklearn.preprocessing import LabelEncoder #label jdi integer
#from sklearn.model_selection import train_test_split #untuk bagi data untuk training n test

import numpy as np


# from sklearn.svm import SVC

from sklearn import svm

#from mlxtend.plotting import plot_decision_regions
# import matplotlib.pyplot as plt
# from mlxtend.plotting import plot_decision_regions
# from mlxtend.classifier import EnsembleVoteClassifier
# import itertools
# from sklearn.linear_model import LogisticRegression
# import matplotlib.gridspec as gridspec


# from sklearn.metrics import classification_report

#from neupy.algorithms import PNN

import time



start_time = time.time()


def train(path="data"):
    audio_data, audio_label = wavelet_data(path)

    X = np.float32(audio_data) 
    print('shape X:', str(X.shape)) #untuk nampilin array x

    Y = audio_label
    print('shape Y: ', str(len(Y))) #untuk nampilin array y

    # Encode class target ke integer
    # encoder = LabelEncoder()
    # encoder.fit(img_label)
    # Y = encoder.transform(img_label)
    # print('shape Y:', str(Y.shape))


#dibawah ini untuk proses pengujian secara otomatis, dari folder data train di ambil 0.2 dari data tersebut secara random untuk jadi data uji
#    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0) #untuk spilt data latih n uji, ukuran test_size chek dokumentasi
#    print('X_train shape: ', X_train.shape) #nampilin array train yg sudh di spit 
#    print('X_test shape', X_test.shape) # nampili array uji yg sudh di split
    C = 1.0 
    classifier = svm.SVC(kernel='linear',C=C, class_weight='balanced',probability=True)
    # classifier = svm.SVC(probability=True)
    classifier.fit(X, Y)
    with open('svm-model.dill', 'wb') as f: #hasil sebuah file model dngn nama pnn-mdel.dill
        dill.dump(classifier, f)

    # clf1 = classifier.fit(X, Y)

    # # Plotting Decision Regions

    # gs = gridspec.GridSpec(2, 2)
    # fig = plt.figure(figsize=(10, 8))

    # labels = ['SVM linear']

    # for clf, lab, grd in zip([clf1],
    #                          labels,
    #                          itertools.product([0, 1],
    #                          repeat=2)):
    #     # clf.fit(X, y)
    #     ax = plt.subplot(gs[grd[0], grd[1]])
    #     fig = plot_decision_regions(X=X, y=Y,
    #                                 clf=clf, legend=2)
    #     plt.title(lab)

    # plt.show()



    # # get the separating hyperplane
    # w = classifier.coef_[0]
    # a = -w[0] / w[1]
    # xx = np.linspace(-5, 5)
    # yy = a * xx - (classifier.intercept_[0]) / w[1]

    # # plot the parallels to the separating hyperplane that pass through the
    # # support vectors
    # b = classifier.support_vectors_[0]
    # yy_down = a * xx + (b[1] - a * b[0])
    # b = classifier.support_vectors_[-1]
    # yy_up = a * xx + (b[1] - a * b[0])

    # # plot the line, the points, and the nearest vectors to the plane
    # plt.plot(xx, yy, 'k-')
    # plt.plot(xx, yy_down, 'k--')
    # plt.plot(xx, yy_up, 'k--')

    # plt.scatter(classifier.support_vectors_[:, 0], classifier.support_vectors_[:, 1],s=80, facecolors='none')
    # plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)

    # plt.axis('tight')
    # plt.show()

  
if __name__ == '__main__':
    train()
