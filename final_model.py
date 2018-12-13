# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:37:06 2018

@author: Garry
"""
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0


'''import matplotlib.pyplot as plt
image_index = 7777 # You may select anything up to 60,000
print(y_train[image_index]) # The label is 8
plt.imshow(x_train[image_index], cmap='Greys')
'''

x_train = x_train.reshape(x_train.shape[0], 28, 28,1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

import keras
import theano
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

model = Sequential()
model.add(Conv2D(32,(3,3),input_shape=(28,28,1),padding='same',activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=512,activation='relu'))
model.add(Dropout(0.4))
model.add(Dense(units=10,activation='softmax'))
model.compile(optimizer= 'rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x=x_train,y=y_train,epochs=20,batch_size=50,verbose=1)  


test_score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', test_score[0])
print('Test accuracy:', test_score[1])




model.save('model1.h5')

