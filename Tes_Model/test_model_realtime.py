from collections import deque, Counter
import numpy as np
from mss_capture import test
import cv2
import time
from models import our
from keras.models import load_model
import pyautogui
import pyxhook
import time

GAME_WIDTH = 580
GAME_HEIGHT = 280


WIDTH = 100
HEIGHT = 100
LR = 1e-4
EPOCHS = 5

key = 0

KeyList = [116]

def OnKeyPress(event):
    global key
    if event.Ascii in KeyList:
        key = event.Ascii

        

w = [1,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0]
a = [0,0,1,0,0,0,0]
d = [0,0,0,1,0,0,0]
c = [0,0,0,0,1,0,0]
z = [0,0,0,0,0,1,0]
nk =[0,0,0,0,0,0,1]


def straight():
    pyautogui.hotkey('w')
    

def reverse():
    pyautogui.hotkey('s')
    
def left():
    pyautogui.hotkey('a')
    
def right():
    pyautogui.hotkey('d')
    
def strafe_right():
    pyautogui.hotkey('c')
    
def strafe_left():
    pyautogui.hotkey('z')
    
def no_keys():
	a = 1





model = our()
MODEL_NAME = 'bebop_model.h5'

model = load_model(MODEL_NAME)

print('We have loaded a previous model!!!!')

def main():

    new_hook=pyxhook.HookManager()
    new_hook.KeyDown=OnKeyPress
    new_hook.HookKeyboard()
    new_hook.start()
    screen = test()
    global key
    paused =False
    while(True):        
        
        if not paused:
            screen = test()
            start_time = time.time()
            prediction = model.predict([screen.reshape(300,100,55,3)])[0]
            prediction = np.array(prediction)

            mode_choice = np.argmax(prediction)
            end_time = time.time()

            qwerty = end_time - start_time

            print(qwerty)

            if mode_choice == 0:
                straight()
                choice_picked = 'straight'
            elif mode_choice == 1:
                reverse()
                choice_picked = 'reverse'
            elif mode_choice == 2:
                left()
                choice_picked = 'left'
            elif mode_choice == 3:
                right()
                choice_picked = 'right'
            elif mode_choice == 4:
                strafe_right()
                choice_picked = 'strafe_right'
            elif mode_choice == 5:
                strafe_left()
                choice_picked = 'strafe_left'
            elif mode_choice == 6:
                no_keys()
                choice_picked = 'no_keys'

        # p pauses game and can get annoying.
        if key == 116:
            if paused:
                paused = False
                print('UnPaused')
                key = 0
                
            else:
                paused = True
                print('Paused')
                key = 0
                
                
                
        

main()       
