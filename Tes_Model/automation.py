# 1260 x 60

import pyautogui
import os
import time
#pyautogui.doubleClick(x=1260, y=60)

pyautogui.PAUSE = 0.7

#Step 1

pyautogui.hotkey('ctrl', 'alt', 't')

pyautogui.typewrite('roscore' )
pyautogui.hotkey('enter')

#Step 2

pyautogui.hotkey('ctrl', 'shift', 't')
pyautogui.typewrite('roslaunch bebop_driver bebop_node.launch' )
pyautogui.hotkey('enter')
time.sleep(5)
#Step 3

pyautogui.hotkey('ctrl', 'shift', 't')
pyautogui.typewrite('rosrun teleop_key teleop_key_pub' )
pyautogui.hotkey('enter')

#Step 4

pyautogui.hotkey('ctrl', 'shift', 't')
pyautogui.typewrite('rosrun teleop_key teleop_key_sub_bebop' )
pyautogui.hotkey('enter')
pyautogui.hotkey('alt', '3')



#Step 6

pyautogui.hotkey('ctrl', 'alt', 't')
pyautogui.typewrite('rosrun image_view image_view image:=/bebop/image_raw' )
pyautogui.hotkey('enter')
pyautogui.moveTo(952,37, duration=0.1)
pyautogui.dragTo(212,37, duration=0.3)


starting_value = 1

while True:
    file_name = 'odom_test_final{}.txt'.format(starting_value)

    if os.path.isfile(file_name):
        #print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        #print('File does not exist, starting fresh!',starting_value)
        #training_data = []
        opt = 'rostopic echo -p /bebop/odom > /home/sinchana-h/Desktop/baburaoRADON/odom_test_final{}.txt'.format(starting_value)
        pyautogui.hotkey('ctrl', 'alt', 't')
        pyautogui.typewrite(opt)
        pyautogui.hotkey('enter')
        break

while True:
    file_name = 'gps_test_final{}.txt'.format(starting_value)

    if os.path.isfile(file_name):
        #print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        #print('File does not exist, starting fresh!',starting_value)
        #training_data = []
        opt = 'rostopic echo -p /bebop/fix > /home/sinchana-h/Desktop/baburaoRADON/gps_test_final{}.txt'.format(starting_value)
        pyautogui.hotkey('ctrl', 'alt', 't')
        pyautogui.typewrite(opt)
        pyautogui.hotkey('enter')
        break


#Step 5

pyautogui.hotkey('ctrl', 'alt', 't')
pyautogui.typewrite('cd ~/Desktop/baburaoRADON')
pyautogui.hotkey('enter')
pyautogui.typewrite('python test_model.py' )        

#1144 x 454

#179 x 33n
