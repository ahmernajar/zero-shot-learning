import time
import numpy as np
import cv2
import mss
from PIL import Image
def abc():
  with mss.mss() as sct:
    monitor = {'top': 52, 'left': 76, 'width': 700 , 'height': 1000}

    last_time = time.time()

    img = np.array(sct.grab(monitor))
    #print("in_mss")

    return img
