#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    
    @author: ahmernajar
    """

'''
    Trainig of bebop
    Here we will use LRCN for the the traing (LRCN-Long Term Recurrent Convolutional
    Neural Network) As our problem is sequence problem so it is best to use LRCN.LRCN is nothing but
    addition of two Neural Networks namely CNN and LSTM (improved version of RNN)
    '''

#importing the libraries
from keras.layers.convolutional import Convolution2D
from keras.layers.wrappers import TimeDistributed
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.layers.wrappers import TimeDistributed
from keras.layers import Dense ,BatchNormalization,Dropout
from keras.models import Sequential
from keras.layers import Convolution2D , LSTM
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.optimizers import Adam


import numpy as np
x = np.load('frame-1.npy', encoding = 'latin1')


Y = [i[1] for i in x]
Y = np.array(Y)

data = np.array([i[0] for i in x])
data = data.reshape(1116,100,100)
coloumns = 100


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, Y, test_size = 0.3, random_state = 0)

model = Sequential()

model.add(LSTM(128,input_shape = (100,100),return_sequences = True,activation = 'relu'))

model.add(LSTM(128, activation = 'relu'))

model.add(Dense(128,activation = 'relu'))
model.add(Dense(256,activation = 'relu'))

model.add(Dense(7, activation = 'softmax'))

model.compile(optimizer = 'Adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)
# you can also add btach size 

model.save('your_name_file.h5')
