# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 23:34:24 2018

@author: Garry
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
def image_process(img):
  img= cv2.bitwise_not(img)
  import skimage .transform
  img=skimage.transform.resize(img,(28,28))
  #plt.imshow(img, cmap='Greys')
  img=img.reshape(1,28,28,1)
  img = img.astype('float32')
  img /= 255
  return img