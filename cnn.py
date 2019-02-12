#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.layers import Dense ,BatchNormalization,Dropout,LSTM
from keras.layers.wrappers import TimeDistributed
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.optimizers import Adam
from keras.models import load_model
from models import lstm

#importing the dataset
import numpy as np
x = np.load('frame-1.npy', encoding = 'latin1')

# For labels
Y = [i[1] for i in x]
Y = np.array(Y)

# For frames
data = np.array([i[0] for i in x])
#data = data.reshape(5339,100,100,1)
data = data / 255.0

#Spliting it into traing ant testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, Y, test_size =                           0.25, random_state = 0)

cnn = Sequential()

cnn.add(Convolution2D(128, 3, 3, input_shape = (100,100,1), activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (2, 2)))
#cnn.add(Dropout0(0.4))


cnn.add(Convolution2D(64, 3, 3, activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (2, 2)))
#cnn.add(Dropout(0.4))

cnn.add(Convolution2D(32, 3, 3, activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (2, 2)))

cnn.add(Convolution2D(16, 3, 3, activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (2, 2)))

#cnn.add(Convolution2D(16, 3, 3, activation = 'relu'))
#cnn.add(MaxPooling2D(pool_size = (2, 2)))
#classifier.add(BatchNormalization())

cnn.add(Flatten())
cnn.add(Dense(output_dim = 128, activation = 'relu'))
cnn.add(Dense(output_dim = 256, activation = 'relu'))

cnn.add(Dense(output_dim = 7, activation = 'softmax'))

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=30)
#you can add batch_size also


model.save('your file name.h5')
