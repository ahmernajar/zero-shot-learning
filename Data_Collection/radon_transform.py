
from __future__ import print_function, division
import os
import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread,imsave
from skimage import data_dir
from skimage.transform import radon, rescale
from skimage.transform import iradon
import cv2

i = 1
inc = 1
while True:
	file_name = 'frame-{}.npy'.format(i)

	if os.path.isfile(file_name):
		print('File no: ',i)
		print('\nsve_no:',inc)
		train_data = np.load(file_name)
		count = 0
		new_data = []
		x = len(train_data)
		for data in train_data: 
			image = data[0]
			image = cv2.resize(image,(100,100))
			keys = data[1]
			image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
			#image = rescale(image, scale=0.4, mode='reflect', multichannel=False)
			theta = np.linspace(0., 180., max(image.shape), endpoint=False)
			sinogram = radon(image, theta=theta, circle=False)
			reconstruction_fbp = iradon(sinogram, theta=theta, circle=False)
			#print (reconstruction_fbp)
			im = np.array(reconstruction_fbp,dtype=np.int8)
			new_data.append([image, im, keys])
			count = count + 1
			remaining = x - count
			print(remaining)
		#save_file_name = 'data-{}.npy'.format(starting_value)
		save_file_name = 'data-{}.npy'.format(inc)
		np.save(save_file_name,new_data)
		inc +=1
		i+=1



	else:
		print('Ho Gaya Khatam')
		break
