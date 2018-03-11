from keras.models import load_model
import cv2
import numpy as np
from keras import backend as K
K.set_image_dim_ordering('th')
import numpy
from PIL import Image

img = cv2.imread('/home/pritesh/Desktop/COM/lib/data/Prediction/c.jpeg')
new_width  = 250
new_height = 250
img = cv2.resize(img,(250,250))
a = numpy.asarray(img)
#a = a.reshape(4,250,250,4)
model = load_model('first_try.h5')
model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#img = np.reshape(a,[1,3,250,250])
classes = model.predict_classes(a)
print(classes)