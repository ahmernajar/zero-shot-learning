import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d,avg_pool_2d, conv_3d, max_pool_3d, avg_pool_3d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.merge_ops import merge
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Lambda,Conv2D,LSTM, MaxPooling2D
from keras.layers.convolutional import Convolution2D
from keras.layers.wrappers import TimeDistributed
from keras.regularizers import l2
from keras.optimizers import Adam
from keras.models import load_model
from keras.layers.normalization import BatchNormalization


def cnn2():
    classifier = Sequential()

    classifier.add(Convolution2D(32, 3, 3, input_shape = (100, 55, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))

    classifier.add(Convolution2D(64, 3, 3, activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))

    classifier.add(Convolution2D(128, 3, 3, activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))

    classifier.add(Flatten())

    classifier.add(Dense(units = 512, activation = 'relu'))

    classifier.add(Dense(units = 7, activation = 'softmax'))

    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    
    return classifier



def cnn():
    model = Sequential()

    model.add(Convolution2D(32, 3, 3, input_shape = (100, 55, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Convolution2D(64, 3, 3, activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Convolution2D(128, 5, 5, activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Convolution2D(256, 3, 3, activation = 'relu'))

    model.add(Flatten())
    model.add(Dense(output_dim = 512, activation = 'relu'))
    #model.add(Dropout(0.4))

    model.add(Dense(output_dim = 7, activation = 'softmax'))
    #model.add(Dropout(0.4))

    model.compile(optimizer = 'Adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

    return model

def lstm():
	model = Sequential()

#cnn.add(Convolution2D(128, 3, 3, input_shape = (100,100,1), activation = 'relu'))
#cnn.add(MaxPooling2D(pool_size = (2, 2)))
#cnn.add(Dropout0(0.4))

#cnn.add(TimeDistributed(Convolution2D(32, 3, 3, input_shape = (100, 100, 1), 
                                        #activation = 'relu')))



#cnn.add(Convolution2D(64, 3, 3, activation = 'relu'))
#cnn.add(MaxPooling2D(pool_size = (2, 2)))
#cnn.add(Dropout(0.4))

#cnn.add(Convolution2D(32, 3, 3, activation = 'relu'))
#cnn.add(MaxPooling2D(pool_size = (2, 2)))

#cnn.add(Convolution2D(16, 3, 3, activation = 'relu'))
#cnn.add(MaxPooling2D(pool_size = (2, 2)))

#cnn.add(Convolution2D(16, 3, 3, activation = 'relu'))
#cnn.add(MaxPooling2D(pool_size = (2, 2)))

#cnn.add(Flatten())
#cnn.add(Dense(output_dim = 128, activation = 'relu'))
#classifier.add(Dropout(0.4))

#cnn.add(Dense(output_dim = 7, activation = 'softmax'))
#classifier.add(Dropout(0.4))

	model.add(LSTM(128,input_shape = (100,100),return_sequences = True,activation = 'relu'))
#cnn.add(Dropout(0.2))

	model.add(LSTM(128, activation = 'relu'))
#cnn.add(Dropout(0.2))
#cnn.add(LSTM(512, activation = 'relu'))

#cnn.add(LSTM(128, activation = 'relu'))

	model.add(Dense(128,activation = 'relu'))
	model.add(Dense(256,activation = 'relu'))
#cnn.add(Dense(512,activation = 'relu'))
#cnn.add(Dense(32,activation = 'relu'))
#cnn.add(Dropout(0.2))

	model.add(Dense(7, activation = 'softmax'))

	model.compile(optimizer = 'Adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
	
	return model

def lrcn1(width, height, frame_count, lr, output = 7, model_name = 'lrcn1.model'):
    T = 1

    model = Sequential()
	
	#network = input_data(shape=[None, width, height,3, 1], name='input')
	#model.add(TimeDistributed(Lambda(lambda x: x/127.5-1.0), input_shape=(T, row, col, ch)))
	
    model.add(TimeDistributed(Lambda(lambda x: x/127.5-1.0), input_shape = (None, width, height, 1)))

    model.add(TimeDistributed(Conv2D(24,(5, 5),strides=(2, 2),activation='relu')))
    model.add(TimeDistributed(Conv2D(36, (5, 5),strides=(2, 2),activation='relu')))
    model.add(TimeDistributed(Conv2D(48, (5, 5),strides=(2, 2),activation='relu')))

    model.add(TimeDistributed(Conv2D(64, (3, 3), activation='relu')))
    model.add(TimeDistributed(Conv2D(64, (3, 3), activation='relu')))

    model.add((Dropout(0.25)))
    model.add(TimeDistributed(Flatten()))

    model.add(TimeDistributed(Dense(100, activation='relu')))
    model.add(TimeDistributed(Dense(50, activation='relu')))
    model.add(TimeDistributed(Dense(10, activation='relu')))
	
    model.add(LSTM(return_sequences=True, units=1))
    model.add(Dense(output))

    model.compile(optimizer=Adam(lr = lr), loss='mse', metrics=['accuracy'])

    return model

def lrcn2(width, height, frame_count, lr, output = 7, model_name = 'lrcn2'):
    #def nin_model(img):
        model = Sequential()
        model.add(TimeDistributed(Lambda(lambda x: x/127.5-1.0), input_shape = (None,width, height, 3)))
        model.add(TimeDistributed(Conv2D(96, (11,11), strides =  (4,4), padding = 'same', activation = 'elu')))
        model.add(TimeDistributed(MaxPooling2D(pool_size=(3, 3), strides=2, padding='valid', data_format=None)))
        model.add(TimeDistributed(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros', moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None, beta_constraint=None, gamma_constraint=None)))
        model.add(TimeDistributed(Conv2D(256, (5,5), strides = (1,1), padding = 'same', activation = 'elu')))
        model.add(TimeDistributed(MaxPooling2D(pool_size=(3, 3), strides=2, padding='valid', data_format=None)))
        model.add(TimeDistributed(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros', moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None, beta_constraint=None, gamma_constraint=None)))
        model.add(TimeDistributed(Conv2D(384, (3,3), strides = (1,1), padding = 'same', activation = 'elu')))
        model.add(TimeDistributed(Conv2D(384, (3,3), strides = (1,1), padding = 'same', activation = 'elu')))
        model.add(TimeDistributed(Conv2D(256, (3,3), strides = (1,1), padding = 'same', activation = 'elu')))
        #model.add(TimeDistributed(MaxPooling2D(pool_size=(3, 3), strides=2, padding='valid', data_format=None)))
        model.add(TimeDistributed(Conv2D(256, (3,3), strides = (1,1), padding = 'same', activation = 'elu')))
        #model.add(TimeDistributed(MaxPooling2D(pool_size=(3, 3), strides=2, padding='valid', data_format=None)))
        model.add(TimeDistributed(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True, beta_initializer='zeros', gamma_initializer='ones', moving_mean_initializer='zeros', moving_variance_initializer='ones', beta_regularizer=None, gamma_regularizer=None, beta_constraint=None, gamma_constraint=None)))
        model.add(TimeDistributed(Conv2D(384, (3,3), strides = (1,1), padding = 'same', activation = 'elu')))
        model.add(TimeDistributed(Conv2D(384, (3,3), strides = (1,1), padding = 'same', activation = 'elu')))
        model.add(TimeDistributed(Conv2D(256, (3,3), strides = (1,1), padding = 'same', activation = 'elu')))
        model.add(TimeDistributed(Flatten()))
        model.add(TimeDistributed(Dense(4096, activation='tanh')))
        model.add(TimeDistributed(Dropout(0.25)))
        model.add(TimeDistributed(Dense(4096, activation='tanh')))
        model.add(TimeDistributed(Dropout(0.25)))
        #model.add(TimeDistributed(Dense(4096, activation='tanh')))
        #model.add(TimeDistributed(Dropout(0.25)))
        #model.add(TimeDistributed(Dense(4096, activation='tanh')))
        #model.add(TimeDistributed(Dropout(0.25)))
        model.add(TimeDistributed(Dense(output, activation='softmax')))

        model.compile(optimizer='adadelta',loss = 'mean_squared_error', metrics = ['accuracy'])

        return model

    #input_img = input_data(shape = (width,height,1))
    #NiN = Model(input_img, nin_model(input_img))
    #NiN.compile(optimizer='adadelta',loss = 'mean_absolute_percentage_error')
    #x_train,y_train,x_test,y_test = preprocess()
    #NiN.fit(x_train,y_train,
            #epochs=10,
            #batch_size=30,
            #shuffle=True)

    #return NiN


#def lrcn2(width, height, frame_count, lr, output = 7, model_name = 'lrcn2')
	
	#model = Sequential()
	
	#model.add(TimeDistributed(Conv2D()
def resnext(width, height, frame_count, lr, output=9, model_name = 'sentnet_color.model'):
    net = input_data(shape=[None, width, height, 3], name='input')
    net = tflearn.conv_2d(net, 16, 3, regularizer='L2', weight_decay=0.0001)
    net = tflearn.layers.conv.resnext_block(net, n, 16, 32)
    net = tflearn.resnext_block(net, 1, 32, 32, downsample=True)
    net = tflearn.resnext_block(net, n-1, 32, 32)
    net = tflearn.resnext_block(net, 1, 64, 32, downsample=True)
    net = tflearn.resnext_block(net, n-1, 64, 32)
    net = tflearn.batch_normalization(net)
    net = tflearn.activation(net, 'relu')
    net = tflearn.global_avg_pool(net)
    # Regression
    net = tflearn.fully_connected(net, output, activation='softmax')
    opt = tflearn.Momentum(0.1, lr_decay=0.1, decay_step=32000, staircase=True)
    net = tflearn.regression(net, optimizer=opt,
                             loss='categorical_crossentropy')

    model = tflearn.DNN(net,
                        max_checkpoints=0, tensorboard_verbose=0, tensorboard_dir='log')

    return model


def sentnet_color_2d(width, height, frame_count, lr, output=9, model_name = 'sentnet_color.model'):
    network = input_data(shape=[None, width, height, 3], name='input')
    network = conv_2d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 256, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 256, 3, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = conv_2d(network, 256, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 256, 3, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, output, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, max_checkpoints=0, tensorboard_verbose=0, tensorboard_dir='log')

    return model



def inception_v3(width, height, frame_count, lr, output=7, model_name = 'default.model'):
    network = input_data(shape=[None, width, height,1], name='input')
    conv1_7_7 = conv_2d(network, 64, 7, strides=2, activation='relu', name = 'conv1_7_7_s2')
    pool1_3_3 = max_pool_2d(conv1_7_7, 3,strides=2)
    pool1_3_3 = local_response_normalization(pool1_3_3)
    conv2_3_3_reduce = conv_2d(pool1_3_3, 64,1, activation='relu',name = 'conv2_3_3_reduce')
    conv2_3_3 = conv_2d(conv2_3_3_reduce, 192,3, activation='relu', name='conv2_3_3')
    conv2_3_3 = local_response_normalization(conv2_3_3)
    pool2_3_3 = max_pool_2d(conv2_3_3, kernel_size=3, strides=2, name='pool2_3_3_s2')
    inception_3a_1_1 = conv_2d(pool2_3_3, 64, 1, activation='relu', name='inception_3a_1_1')
    inception_3a_3_3_reduce = conv_2d(pool2_3_3, 96,1, activation='relu', name='inception_3a_3_3_reduce')
    inception_3a_3_3 = conv_2d(inception_3a_3_3_reduce, 128,filter_size=3,  activation='relu', name = 'inception_3a_3_3')
    inception_3a_5_5_reduce = conv_2d(pool2_3_3,16, filter_size=1,activation='relu', name ='inception_3a_5_5_reduce' )
    inception_3a_5_5 = conv_2d(inception_3a_5_5_reduce, 32, filter_size=5, activation='relu', name= 'inception_3a_5_5')
    inception_3a_pool = max_pool_2d(pool2_3_3, kernel_size=3, strides=1, )
    inception_3a_pool_1_1 = conv_2d(inception_3a_pool, 32, filter_size=1, activation='relu', name='inception_3a_pool_1_1')

    # merge the inception_3a__
    inception_3a_output = merge([inception_3a_1_1, inception_3a_3_3, inception_3a_5_5, inception_3a_pool_1_1], mode='concat', axis=3)
    inception_3b_1_1 = conv_2d(inception_3a_output, 128,filter_size=1,activation='relu', name= 'inception_3b_1_1' )
    inception_3b_3_3_reduce = conv_2d(inception_3a_output, 128, filter_size=1, activation='relu', name='inception_3b_3_3_reduce')
    inception_3b_3_3 = conv_2d(inception_3b_3_3_reduce, 192, filter_size=3,  activation='relu',name='inception_3b_3_3')
    inception_3b_5_5_reduce = conv_2d(inception_3a_output, 32, filter_size=1, activation='relu', name = 'inception_3b_5_5_reduce')
    inception_3b_5_5 = conv_2d(inception_3b_5_5_reduce, 96, filter_size=5,  name = 'inception_3b_5_5')
    inception_3b_pool = max_pool_2d(inception_3a_output, kernel_size=3, strides=1,  name='inception_3b_pool')
    inception_3b_pool_1_1 = conv_2d(inception_3b_pool, 64, filter_size=1,activation='relu', name='inception_3b_pool_1_1')

    #merge the inception_3b_*
    inception_3b_output = merge([inception_3b_1_1, inception_3b_3_3, inception_3b_5_5, inception_3b_pool_1_1], mode='concat',axis=3,name='inception_3b_output')

    pool3_3_3 = max_pool_2d(inception_3b_output, kernel_size=3, strides=2, name='pool3_3_3')
    inception_4a_1_1 = conv_2d(pool3_3_3, 192, filter_size=1, activation='relu', name='inception_4a_1_1')
    inception_4a_3_3_reduce = conv_2d(pool3_3_3, 96, filter_size=1, activation='relu', name='inception_4a_3_3_reduce')
    inception_4a_3_3 = conv_2d(inception_4a_3_3_reduce, 208, filter_size=3,  activation='relu', name='inception_4a_3_3')
    inception_4a_5_5_reduce = conv_2d(pool3_3_3, 16, filter_size=1, activation='relu', name='inception_4a_5_5_reduce')
    inception_4a_5_5 = conv_2d(inception_4a_5_5_reduce, 48, filter_size=5,  activation='relu', name='inception_4a_5_5')
    inception_4a_pool = max_pool_2d(pool3_3_3, kernel_size=3, strides=1,  name='inception_4a_pool')
    inception_4a_pool_1_1 = conv_2d(inception_4a_pool, 64, filter_size=1, activation='relu', name='inception_4a_pool_1_1')

    inception_4a_output = merge([inception_4a_1_1, inception_4a_3_3, inception_4a_5_5, inception_4a_pool_1_1], mode='concat', axis=3, name='inception_4a_output')


    inception_4b_1_1 = conv_2d(inception_4a_output, 160, filter_size=1, activation='relu', name='inception_4a_1_1')
    inception_4b_3_3_reduce = conv_2d(inception_4a_output, 112, filter_size=1, activation='relu', name='inception_4b_3_3_reduce')
    inception_4b_3_3 = conv_2d(inception_4b_3_3_reduce, 224, filter_size=3, activation='relu', name='inception_4b_3_3')
    inception_4b_5_5_reduce = conv_2d(inception_4a_output, 24, filter_size=1, activation='relu', name='inception_4b_5_5_reduce')
    inception_4b_5_5 = conv_2d(inception_4b_5_5_reduce, 64, filter_size=5,  activation='relu', name='inception_4b_5_5')

    inception_4b_pool = max_pool_2d(inception_4a_output, kernel_size=3, strides=1,  name='inception_4b_pool')
    inception_4b_pool_1_1 = conv_2d(inception_4b_pool, 64, filter_size=1, activation='relu', name='inception_4b_pool_1_1')

    inception_4b_output = merge([inception_4b_1_1, inception_4b_3_3, inception_4b_5_5, inception_4b_pool_1_1], mode='concat', axis=3, name='inception_4b_output')


    inception_4c_1_1 = conv_2d(inception_4b_output, 128, filter_size=1, activation='relu',name='inception_4c_1_1')
    inception_4c_3_3_reduce = conv_2d(inception_4b_output, 128, filter_size=1, activation='relu', name='inception_4c_3_3_reduce')
    inception_4c_3_3 = conv_2d(inception_4c_3_3_reduce, 256,  filter_size=3, activation='relu', name='inception_4c_3_3')
    inception_4c_5_5_reduce = conv_2d(inception_4b_output, 24, filter_size=1, activation='relu', name='inception_4c_5_5_reduce')
    inception_4c_5_5 = conv_2d(inception_4c_5_5_reduce, 64,  filter_size=5, activation='relu', name='inception_4c_5_5')

    inception_4c_pool = max_pool_2d(inception_4b_output, kernel_size=3, strides=1)
    inception_4c_pool_1_1 = conv_2d(inception_4c_pool, 64, filter_size=1, activation='relu', name='inception_4c_pool_1_1')

    inception_4c_output = merge([inception_4c_1_1, inception_4c_3_3, inception_4c_5_5, inception_4c_pool_1_1], mode='concat', axis=3,name='inception_4c_output')

    inception_4d_1_1 = conv_2d(inception_4c_output, 112, filter_size=1, activation='relu', name='inception_4d_1_1')
    inception_4d_3_3_reduce = conv_2d(inception_4c_output, 144, filter_size=1, activation='relu', name='inception_4d_3_3_reduce')
    inception_4d_3_3 = conv_2d(inception_4d_3_3_reduce, 288, filter_size=3, activation='relu', name='inception_4d_3_3')
    inception_4d_5_5_reduce = conv_2d(inception_4c_output, 32, filter_size=1, activation='relu', name='inception_4d_5_5_reduce')
    inception_4d_5_5 = conv_2d(inception_4d_5_5_reduce, 64, filter_size=5,  activation='relu', name='inception_4d_5_5')
    inception_4d_pool = max_pool_2d(inception_4c_output, kernel_size=3, strides=1,  name='inception_4d_pool')
    inception_4d_pool_1_1 = conv_2d(inception_4d_pool, 64, filter_size=1, activation='relu', name='inception_4d_pool_1_1')

    inception_4d_output = merge([inception_4d_1_1, inception_4d_3_3, inception_4d_5_5, inception_4d_pool_1_1], mode='concat', axis=3, name='inception_4d_output')

    inception_4e_1_1 = conv_2d(inception_4d_output, 256, filter_size=1, activation='relu', name='inception_4e_1_1')
    inception_4e_3_3_reduce = conv_2d(inception_4d_output, 160, filter_size=1, activation='relu', name='inception_4e_3_3_reduce')
    inception_4e_3_3 = conv_2d(inception_4e_3_3_reduce, 320, filter_size=3, activation='relu', name='inception_4e_3_3')
    inception_4e_5_5_reduce = conv_2d(inception_4d_output, 32, filter_size=1, activation='relu', name='inception_4e_5_5_reduce')
    inception_4e_5_5 = conv_2d(inception_4e_5_5_reduce, 128,  filter_size=5, activation='relu', name='inception_4e_5_5')
    inception_4e_pool = max_pool_2d(inception_4d_output, kernel_size=3, strides=1,  name='inception_4e_pool')
    inception_4e_pool_1_1 = conv_2d(inception_4e_pool, 128, filter_size=1, activation='relu', name='inception_4e_pool_1_1')


    inception_4e_output = merge([inception_4e_1_1, inception_4e_3_3, inception_4e_5_5,inception_4e_pool_1_1],axis=3, mode='concat')

    pool4_3_3 = max_pool_2d(inception_4e_output, kernel_size=3, strides=2, name='pool_3_3')


    inception_5a_1_1 = conv_2d(pool4_3_3, 256, filter_size=1, activation='relu', name='inception_5a_1_1')
    inception_5a_3_3_reduce = conv_2d(pool4_3_3, 160, filter_size=1, activation='relu', name='inception_5a_3_3_reduce')
    inception_5a_3_3 = conv_2d(inception_5a_3_3_reduce, 320, filter_size=3, activation='relu', name='inception_5a_3_3')
    inception_5a_5_5_reduce = conv_2d(pool4_3_3, 32, filter_size=1, activation='relu', name='inception_5a_5_5_reduce')
    inception_5a_5_5 = conv_2d(inception_5a_5_5_reduce, 128, filter_size=5,  activation='relu', name='inception_5a_5_5')
    inception_5a_pool = max_pool_2d(pool4_3_3, kernel_size=3, strides=1,  name='inception_5a_pool')
    inception_5a_pool_1_1 = conv_2d(inception_5a_pool, 128, filter_size=1,activation='relu', name='inception_5a_pool_1_1')

    inception_5a_output = merge([inception_5a_1_1, inception_5a_3_3, inception_5a_5_5, inception_5a_pool_1_1], axis=3,mode='concat')


    inception_5b_1_1 = conv_2d(inception_5a_output, 384, filter_size=1,activation='relu', name='inception_5b_1_1')
    inception_5b_3_3_reduce = conv_2d(inception_5a_output, 192, filter_size=1, activation='relu', name='inception_5b_3_3_reduce')
    inception_5b_3_3 = conv_2d(inception_5b_3_3_reduce, 384,  filter_size=3,activation='relu', name='inception_5b_3_3')
    inception_5b_5_5_reduce = conv_2d(inception_5a_output, 48, filter_size=1, activation='relu', name='inception_5b_5_5_reduce')
    inception_5b_5_5 = conv_2d(inception_5b_5_5_reduce,128, filter_size=5,  activation='relu', name='inception_5b_5_5' )
    inception_5b_pool = max_pool_2d(inception_5a_output, kernel_size=3, strides=1,  name='inception_5b_pool')
    inception_5b_pool_1_1 = conv_2d(inception_5b_pool, 128, filter_size=1, activation='relu', name='inception_5b_pool_1_1')
    inception_5b_output = merge([inception_5b_1_1, inception_5b_3_3, inception_5b_5_5, inception_5b_pool_1_1], axis=3, mode='concat')

    pool5_7_7 = avg_pool_2d(inception_5b_output, kernel_size=7, strides=1)
    pool5_7_7 = dropout(pool5_7_7, 0.4)


    loss = fully_connected(pool5_7_7, output,activation='softmax')



    network = regression(loss, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network,
                        max_checkpoints=0, tensorboard_verbose=0,tensorboard_dir='log')


    return model



def inception_v3_3d(width, height, frame_count, lr, output=9, model_name = 'sentnet_color.model'):
    network = input_data(shape=[None, width, height,3, 1], name='input')
    conv1_7_7 = conv_3d(network, 64, 7, strides=2, activation='relu', name = 'conv1_7_7_s2')
    pool1_3_3 = max_pool_3d(conv1_7_7, 3,strides=2)
    #pool1_3_3 = local_response_normalization(pool1_3_3)
    conv2_3_3_reduce = conv_3d(pool1_3_3, 64,1, activation='relu',name = 'conv2_3_3_reduce')
    conv2_3_3 = conv_3d(conv2_3_3_reduce, 192,3, activation='relu', name='conv2_3_3')
    #conv2_3_3 = local_response_normalization(conv2_3_3)
    pool2_3_3 = max_pool_3d(conv2_3_3, kernel_size=3, strides=2, name='pool2_3_3_s2')
    inception_3a_1_1 = conv_3d(pool2_3_3, 64, 1, activation='relu', name='inception_3a_1_1')
    inception_3a_3_3_reduce = conv_3d(pool2_3_3, 96,1, activation='relu', name='inception_3a_3_3_reduce')
    inception_3a_3_3 = conv_3d(inception_3a_3_3_reduce, 128,filter_size=3,  activation='relu', name = 'inception_3a_3_3')
    inception_3a_5_5_reduce = conv_3d(pool2_3_3,16, filter_size=1,activation='relu', name ='inception_3a_5_5_reduce' )
    inception_3a_5_5 = conv_3d(inception_3a_5_5_reduce, 32, filter_size=5, activation='relu', name= 'inception_3a_5_5')
    inception_3a_pool = max_pool_3d(pool2_3_3, kernel_size=3, strides=1, )
    inception_3a_pool_1_1 = conv_3d(inception_3a_pool, 32, filter_size=1, activation='relu', name='inception_3a_pool_1_1')

    # merge the inception_3a__
    inception_3a_output = merge([inception_3a_1_1, inception_3a_3_3, inception_3a_5_5, inception_3a_pool_1_1], mode='concat', axis=4)

    inception_3b_1_1 = conv_3d(inception_3a_output, 128,filter_size=1,activation='relu', name= 'inception_3b_1_1' )
    inception_3b_3_3_reduce = conv_3d(inception_3a_output, 128, filter_size=1, activation='relu', name='inception_3b_3_3_reduce')
    inception_3b_3_3 = conv_3d(inception_3b_3_3_reduce, 192, filter_size=3,  activation='relu',name='inception_3b_3_3')
    inception_3b_5_5_reduce = conv_3d(inception_3a_output, 32, filter_size=1, activation='relu', name = 'inception_3b_5_5_reduce')
    inception_3b_5_5 = conv_3d(inception_3b_5_5_reduce, 96, filter_size=5,  name = 'inception_3b_5_5')
    inception_3b_pool = max_pool_3d(inception_3a_output, kernel_size=3, strides=1,  name='inception_3b_pool')
    inception_3b_pool_1_1 = conv_3d(inception_3b_pool, 64, filter_size=1,activation='relu', name='inception_3b_pool_1_1')

    #merge the inception_3b_*
    inception_3b_output = merge([inception_3b_1_1, inception_3b_3_3, inception_3b_5_5, inception_3b_pool_1_1], mode='concat',axis=4,name='inception_3b_output')

    pool3_3_3 = max_pool_3d(inception_3b_output, kernel_size=3, strides=2, name='pool3_3_3')
    inception_4a_1_1 = conv_3d(pool3_3_3, 192, filter_size=1, activation='relu', name='inception_4a_1_1')
    inception_4a_3_3_reduce = conv_3d(pool3_3_3, 96, filter_size=1, activation='relu', name='inception_4a_3_3_reduce')
    inception_4a_3_3 = conv_3d(inception_4a_3_3_reduce, 208, filter_size=3,  activation='relu', name='inception_4a_3_3')
    inception_4a_5_5_reduce = conv_3d(pool3_3_3, 16, filter_size=1, activation='relu', name='inception_4a_5_5_reduce')
    inception_4a_5_5 = conv_3d(inception_4a_5_5_reduce, 48, filter_size=5,  activation='relu', name='inception_4a_5_5')
    inception_4a_pool = max_pool_3d(pool3_3_3, kernel_size=3, strides=1,  name='inception_4a_pool')
    inception_4a_pool_1_1 = conv_3d(inception_4a_pool, 64, filter_size=1, activation='relu', name='inception_4a_pool_1_1')

    inception_4a_output = merge([inception_4a_1_1, inception_4a_3_3, inception_4a_5_5, inception_4a_pool_1_1], mode='concat', axis=4, name='inception_4a_output')


    inception_4b_1_1 = conv_3d(inception_4a_output, 160, filter_size=1, activation='relu', name='inception_4a_1_1')
    inception_4b_3_3_reduce = conv_3d(inception_4a_output, 112, filter_size=1, activation='relu', name='inception_4b_3_3_reduce')
    inception_4b_3_3 = conv_3d(inception_4b_3_3_reduce, 224, filter_size=3, activation='relu', name='inception_4b_3_3')
    inception_4b_5_5_reduce = conv_3d(inception_4a_output, 24, filter_size=1, activation='relu', name='inception_4b_5_5_reduce')
    inception_4b_5_5 = conv_3d(inception_4b_5_5_reduce, 64, filter_size=5,  activation='relu', name='inception_4b_5_5')

    inception_4b_pool = max_pool_3d(inception_4a_output, kernel_size=3, strides=1,  name='inception_4b_pool')
    inception_4b_pool_1_1 = conv_3d(inception_4b_pool, 64, filter_size=1, activation='relu', name='inception_4b_pool_1_1')

    inception_4b_output = merge([inception_4b_1_1, inception_4b_3_3, inception_4b_5_5, inception_4b_pool_1_1], mode='concat', axis=4, name='inception_4b_output')


    inception_4c_1_1 = conv_3d(inception_4b_output, 128, filter_size=1, activation='relu',name='inception_4c_1_1')
    inception_4c_3_3_reduce = conv_3d(inception_4b_output, 128, filter_size=1, activation='relu', name='inception_4c_3_3_reduce')
    inception_4c_3_3 = conv_3d(inception_4c_3_3_reduce, 256,  filter_size=3, activation='relu', name='inception_4c_3_3')
    inception_4c_5_5_reduce = conv_3d(inception_4b_output, 24, filter_size=1, activation='relu', name='inception_4c_5_5_reduce')
    inception_4c_5_5 = conv_3d(inception_4c_5_5_reduce, 64,  filter_size=5, activation='relu', name='inception_4c_5_5')

    inception_4c_pool = max_pool_3d(inception_4b_output, kernel_size=3, strides=1)
    inception_4c_pool_1_1 = conv_3d(inception_4c_pool, 64, filter_size=1, activation='relu', name='inception_4c_pool_1_1')

    inception_4c_output = merge([inception_4c_1_1, inception_4c_3_3, inception_4c_5_5, inception_4c_pool_1_1], mode='concat', axis=4,name='inception_4c_output')

    inception_4d_1_1 = conv_3d(inception_4c_output, 112, filter_size=1, activation='relu', name='inception_4d_1_1')
    inception_4d_3_3_reduce = conv_3d(inception_4c_output, 144, filter_size=1, activation='relu', name='inception_4d_3_3_reduce')
    inception_4d_3_3 = conv_3d(inception_4d_3_3_reduce, 288, filter_size=3, activation='relu', name='inception_4d_3_3')
    inception_4d_5_5_reduce = conv_3d(inception_4c_output, 32, filter_size=1, activation='relu', name='inception_4d_5_5_reduce')
    inception_4d_5_5 = conv_3d(inception_4d_5_5_reduce, 64, filter_size=5,  activation='relu', name='inception_4d_5_5')
    inception_4d_pool = max_pool_3d(inception_4c_output, kernel_size=3, strides=1,  name='inception_4d_pool')
    inception_4d_pool_1_1 = conv_3d(inception_4d_pool, 64, filter_size=1, activation='relu', name='inception_4d_pool_1_1')

    inception_4d_output = merge([inception_4d_1_1, inception_4d_3_3, inception_4d_5_5, inception_4d_pool_1_1], mode='concat', axis=4, name='inception_4d_output')

    inception_4e_1_1 = conv_3d(inception_4d_output, 256, filter_size=1, activation='relu', name='inception_4e_1_1')
    inception_4e_3_3_reduce = conv_3d(inception_4d_output, 160, filter_size=1, activation='relu', name='inception_4e_3_3_reduce')
    inception_4e_3_3 = conv_3d(inception_4e_3_3_reduce, 320, filter_size=3, activation='relu', name='inception_4e_3_3')
    inception_4e_5_5_reduce = conv_3d(inception_4d_output, 32, filter_size=1, activation='relu', name='inception_4e_5_5_reduce')
    inception_4e_5_5 = conv_3d(inception_4e_5_5_reduce, 128,  filter_size=5, activation='relu', name='inception_4e_5_5')
    inception_4e_pool = max_pool_3d(inception_4d_output, kernel_size=3, strides=1,  name='inception_4e_pool')
    inception_4e_pool_1_1 = conv_3d(inception_4e_pool, 128, filter_size=1, activation='relu', name='inception_4e_pool_1_1')


    inception_4e_output = merge([inception_4e_1_1, inception_4e_3_3, inception_4e_5_5,inception_4e_pool_1_1],axis=4, mode='concat')

    pool4_3_3 = max_pool_3d(inception_4e_output, kernel_size=3, strides=2, name='pool_3_3')


    inception_5a_1_1 = conv_3d(pool4_3_3, 256, filter_size=1, activation='relu', name='inception_5a_1_1')
    inception_5a_3_3_reduce = conv_3d(pool4_3_3, 160, filter_size=1, activation='relu', name='inception_5a_3_3_reduce')
    inception_5a_3_3 = conv_3d(inception_5a_3_3_reduce, 320, filter_size=3, activation='relu', name='inception_5a_3_3')
    inception_5a_5_5_reduce = conv_3d(pool4_3_3, 32, filter_size=1, activation='relu', name='inception_5a_5_5_reduce')
    inception_5a_5_5 = conv_3d(inception_5a_5_5_reduce, 128, filter_size=5,  activation='relu', name='inception_5a_5_5')
    inception_5a_pool = max_pool_3d(pool4_3_3, kernel_size=3, strides=1,  name='inception_5a_pool')
    inception_5a_pool_1_1 = conv_3d(inception_5a_pool, 128, filter_size=1,activation='relu', name='inception_5a_pool_1_1')

    inception_5a_output = merge([inception_5a_1_1, inception_5a_3_3, inception_5a_5_5, inception_5a_pool_1_1], axis=4,mode='concat')


    inception_5b_1_1 = conv_3d(inception_5a_output, 384, filter_size=1,activation='relu', name='inception_5b_1_1')
    inception_5b_3_3_reduce = conv_3d(inception_5a_output, 192, filter_size=1, activation='relu', name='inception_5b_3_3_reduce')
    inception_5b_3_3 = conv_3d(inception_5b_3_3_reduce, 384,  filter_size=3,activation='relu', name='inception_5b_3_3')
    inception_5b_5_5_reduce = conv_3d(inception_5a_output, 48, filter_size=1, activation='relu', name='inception_5b_5_5_reduce')
    inception_5b_5_5 = conv_3d(inception_5b_5_5_reduce,128, filter_size=5,  activation='relu', name='inception_5b_5_5' )
    inception_5b_pool = max_pool_3d(inception_5a_output, kernel_size=3, strides=1,  name='inception_5b_pool')
    inception_5b_pool_1_1 = conv_3d(inception_5b_pool, 128, filter_size=1, activation='relu', name='inception_5b_pool_1_1')
    inception_5b_output = merge([inception_5b_1_1, inception_5b_3_3, inception_5b_5_5, inception_5b_pool_1_1], axis=4, mode='concat')

    pool5_7_7 = avg_pool_3d(inception_5b_output, kernel_size=7, strides=1)
    pool5_7_7 = dropout(pool5_7_7, 0.4)


    loss = fully_connected(pool5_7_7, output,activation='softmax')



    network = regression(loss, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path=model_name,
                        max_checkpoints=1, tensorboard_verbose=0,tensorboard_dir='log')


    return model






def sentnet_LSTM_gray(width, height, frame_count, lr, output=9):
    network = input_data(shape=[None, width, height], name='input')
    #network = tflearn.input_data(shape=[None, 28, 28], name='input')
    network = tflearn.lstm(network, 128, return_seq=True)
    network = tflearn.lstm(network, 128)
    network = tflearn.fully_connected(network, 9, activation='softmax')
    network = tflearn.regression(network, optimizer='adam',
    loss='categorical_crossentropy', name="output1")

    model = tflearn.DNN(network, checkpoint_path='model_lstm',
                        max_checkpoints=1, tensorboard_verbose=0, tensorboard_dir='log')

    return model





def sentnet_color(width, height, frame_count, lr, output=9, model_name = 'sentnet_color.model'):
    network = input_data(shape=[None, width, height,3, 1], name='input')
    network = conv_3d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 256, 5, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 256, 3, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    network = conv_3d(network, 256, 5, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 256, 3, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, output, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path=model_name,
                        max_checkpoints=1, tensorboard_verbose=0, tensorboard_dir='log')

    return model




def sentnet_frames(width, height, frame_count, lr, output=9):
    network = input_data(shape=[None, width, height,frame_count, 1], name='input')
    network = conv_3d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 256, 5, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 256, 3, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    network = conv_3d(network, 256, 5, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 256, 3, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, output, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                        max_checkpoints=1, tensorboard_verbose=0, tensorboard_dir='log')

    return model



def sentnet2(width, height, frame_count, lr, output=9):
    network = input_data(shape=[None, width, height, frame_count, 1], name='input')
    network = conv_3d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 256, 5, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 256, 3, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                        max_checkpoints=1, tensorboard_verbose=0, tensorboard_dir='log')

    return model


def sentnet(width, height, frame_count, lr, output=9):
    network = input_data(shape=[None, width, height, frame_count, 1], name='input')
    network = conv_3d(network, 96, 11, strides=4, activation='relu')
    network = avg_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 256, 5, activation='relu')
    network = avg_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 256, 3, activation='relu')
    network = max_pool_3d(network, 3, strides=2)
    network = conv_3d(network, 256, 5, activation='relu')
    network = avg_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 384, 3, activation='relu')
    network = conv_3d(network, 256, 3, activation='relu')
    network = avg_pool_3d(network, 3, strides=2)
    #network = local_response_normalization(network)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, output, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                        max_checkpoints=1, tensorboard_verbose=0, tensorboard_dir='log')

    return model



def alexnet2(width, height, frame_count, lr, output=3, model_name = 'alexnet2'):

    model = Sequential()
    #network = input_data(shape=[None, width, height, 1], name='input')
    model.add(TimeDistributed(Lambda(lambda x: x/127.5-1.0), input_shape = (None, width, height, 1)))
    #network = conv_2d(network, 96, 11, strides=4, activation='relu')
    model.add(TimeDistributed(Conv2D(96, (11,11), padding = 'same',strides = (4,4), activation = 'relu')))
    #network = max_pool_2d(network, 3, strides=2)
    model.add(TimeDistributed(MaxPooling2D(pool_size = (3,3), padding = 'same',strides = 2)))

    #network = local_response_normalization(network)
    model.add(TimeDistributed(BatchNormalization()))

    #network = conv_2d(network, 256, 5, activation='relu')
    model.add(TimeDistributed(Conv2D(256, (5,5), padding = 'same', activation = 'relu')))
    #network = max_pool_2d(network, 3, strides=2)
    model.add(TimeDistributed(MaxPooling2D(pool_size = (3,3), padding = 'same', strides = 2)))

    #(?) network = local_response_normalization(network)
    model.add(TimeDistributed(BatchNormalization()))

    #network = conv_2d(network, 384, 3, activation='relu')
    model.add(TimeDistributed(Conv2D(384, (3,3), padding = 'same', activation = 'relu')))
    #network = conv_2d(network, 384, 3, activation='relu')
    model.add(TimeDistributed(Conv2D(384, (3,3), padding = 'same', activation = 'relu')))
    #network = conv_2d(network, 256, 3, activation='relu')
    model.add(TimeDistributed(Conv2D(256, (3,3), padding = 'same', activation = 'relu')))
    #network = max_pool_2d(network, 3, strides=2)
    model.add(TimeDistributed(MaxPooling2D(pool_size = (3,3), padding = 'same', strides = 2)))
    #network = conv_2d(network, 256, 5, activation='relu')
    model.add(TimeDistributed(Conv2D(256, (5,5), padding = 'same', activation = 'relu')))
    #network = max_pool_2d(network, 3, strides=2)
    model.add(TimeDistributed(MaxPooling2D(pool_size = (3,3), padding = 'same', strides = 2)))

    #(?) network = local_response_normalization(network)
    model.add(TimeDistributed(BatchNormalization()))

    #network = conv_2d(network, 384, 3, activation='relu')
    model.add(TimeDistributed(Conv2D(384, (3,3), padding = 'same', activation = 'relu')))
    #network = conv_2d(network, 384, 3, activation='relu')
    model.add(TimeDistributed(Conv2D(384, (3,3), padding = 'same', activation = 'relu')))
    #network = conv_2d(network, 256, 3, activation='relu')
    model.add(TimeDistributed(Conv2D(256, (3,3), padding = 'same', activation = 'relu')))
    #network = max_pool_2d(network, 3, strides=2)
    model.add(TimeDistributed(MaxPooling2D(pool_size = (3,3), padding = 'same', strides = 2)))

    #(?) network = local_response_normalization(network)
    model.add(TimeDistributed(BatchNormalization()))

    model.add(TimeDistributed(Flatten()))
    
    #network = fully_connected(network, 4096, activation='tanh')
    model.add(TimeDistributed(Dense(4096, activation = 'tanh')))
    #network = dropout(network, 0.5)
    model.add(TimeDistributed(Dropout(0.5)))
    #network = fully_connected(network, 4096, activation='tanh')
    model.add(TimeDistributed(Dense(4096, activation = 'tanh')))
    #network = dropout(network, 0.5)
    model.add(TimeDistributed(Dropout(0.5)))
    #network = fully_connected(network, 4096, activation='tanh')
    model.add(TimeDistributed(Dense(4096, activation = 'tanh')))
    #network = dropout(network, 0.5)
    model.add(TimeDistributed(Dropout(0.5)))
    #network = fully_connected(network, 4096, activation='tanh')
    model.add(TimeDistributed(Dense(4096, activation = 'tanh')))
    #network = dropout(network, 0.5)
    model.add(TimeDistributed(Dropout(0.5)))
    #network = fully_connected(network, output, activation='softmax')
    model.add(TimeDistributed(Dense(output, activation = 'softmax')))

    model.add(LSTM(return_sequences=True, units=1))
    model.add(Dense(output, activation='linear'))

    #network = regression(network, optimizer='momentum',loss='categorical_crossentropy',learning_rate=lr, name='targets')
    model.compile(optimizer = Adam(lr = lr), loss = 'categorical_crossentropy', metrics = ['accuracy'])
    #model = tflearn.DNN(network, checkpoint_path='model_alexnet',max_checkpoints=1, tensorboard_verbose=0, tensorboard_dir='log')

    return model





def sentnet_v0(width, height, frame_count, lr, output=9):
    network = input_data(shape=[None, width, height, frame_count, 1], name='input')
    network = conv_3d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_3d(network, 3, strides=2)

    #network = local_response_normalization(network)

    network = conv_3d(network, 256, 5, activation='relu')
    network = max_pool_3d(network, 3, strides=2)

    #network = local_response_normalization(network)

    network = conv_3d(network, 384, 3, 3, activation='relu')
    network = conv_3d(network, 384, 3, 3, activation='relu')
    network = conv_3d(network, 256, 3, 3, activation='relu')

    network = max_pool_3d(network, 3, strides=2)

    #network = local_response_normalization(network)

    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, output, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                        max_checkpoints=1, tensorboard_verbose=0, tensorboard_dir='log')

    return model



def alexnet(width, height, lr, output=3):
    network = input_data(shape=[None, width, height, 1], name='input')
    network = conv_2d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 256, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 256, 3, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, output, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                        max_checkpoints=1, tensorboard_verbose=0, tensorboard_dir='log')

    return model


