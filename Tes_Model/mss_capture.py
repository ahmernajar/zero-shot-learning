from __future__ import print_function, division
import time
import numpy as np
import cv2
import mss
from PIL import Image
###########################################
import os
#import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread,imsave
from skimage import data_dir
from skimage.transform import radon, rescale
from skimage.transform import iradon
#import cv2


def abc():
	with mss.mss() as sct:
		monitor = {'top': 52, 'left': 76 , 'width': 700, 'height': 1000}

		last_time = time.time()

		img = np.array(sct.grab(monitor))

		return img

def test():
	with mss.mss() as sct:

		monitor = {'top': 52, 'left': 76, 'width': 700, 'height': 1000}
		last_time = time.time()
		img = np.array(sct.grab(monitor))
		img = cv2.resize(img,(16500,100))
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		#img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
		#theta = np.linspace(0., 180., max(img.shape), endpoint=False)
		#sinogram = radon(img, theta=theta, circle=False)
		#reconstruction_fbp = iradon(sinogram, theta=theta, circle=False)
		#img = np.array(reconstruction_fbp,dtype=np.int8)

		return img
