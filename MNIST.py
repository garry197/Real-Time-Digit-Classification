import cv2
import numpy as np
import sound_module
from sound_module import sound
import matplotlib.pyplot as plt
import keras
from keras.models import load_model
import image_preprocessing_module
from image_preprocessing_module import image_process
import input_module
from input_module import inp
inp()

img =cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='Greys')
img=image_process(img)


model=load_model('model1.h5')
out=model.predict(img)
f=np.argmax(out)
sound(f)

