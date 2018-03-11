from PIL import Image
import numpy as np
import os
import glob
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
K.set_image_dim_ordering('th')

batch_size = 20
input_shape=(3, 250, 250)
train_datagen = ImageDataGenerator()

train_generator = train_datagen.flow_from_directory('data/Training',target_size=(250, 250),batch_size=batch_size,class_mode='sparse')  
valid_generator = train_datagen.flow_from_directory('data/Validation',target_size=(250, 250),batch_size=batch_size,class_mode='sparse')  

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(3, 250, 250)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3), input_shape=(3, 250, 250)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(1000,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(5,activation='softmax'))

model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit_generator(train_generator,steps_per_epoch=100 // batch_size,epochs=5,validation_data=valid_generator,validation_steps=800 // batch_size)
model.save('first_try.h5') 
