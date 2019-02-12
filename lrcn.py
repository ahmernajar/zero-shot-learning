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

#CNN
model = Sequential()

model.add(TimeDistributed(Convolution2D(32, 3, 3, input_shape = (100, 100, 1),
                                        activation = 'relu')))

model.add(TimeDistributed(MaxPooling2D( 2,2 )))

model.add(TimeDistributed(Convolution2D(32, 3, 3, activation = 'relu')))
model.add(TimeDistributed(MaxPooling2D( 2,2 )))

#model.add(TimeDistributed(Convolution2D(64, 5, 5, activation = 'relu')))
#model.add(TimeDistributed(MaxPooling2D( 2,2 )))
#model.add((Dropout(0.25)))

model.add(TimeDistributed(Flatten()))

model.add(Dense(output_dim = 256, activation = 'relu'))


#LSTM
model = Sequential()


model.add(LSTM(coloumns,return_sequences=True ,activation = 'sigmoid'))
model.add(Dense(coloumns))

#model.add(LSTM(coloumns,return_sequences=True,activation = 'sigmoid'))
#model.add(Dense(coloumns))

#model.add(LSTM(coloumns,return_sequences=True,activation = 'sigmoid'))
#model.add(Dense(coloumns))

#model.add(LSTM(coloumns,return_sequences=True,activation = 'sigmoid'))
#model.add(Dense(coloumns))

model.compile(loss='mean_absolute_error', optimizer='adam',metrics=['accuracy'])

model.fit(X_train,y_train, nb_epoch=20, batch_size=50, verbose=2,
          validation_data=(X_test,y_test))

model.save('your_name_file.h5')


