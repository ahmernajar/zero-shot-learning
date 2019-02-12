# zero-shot-learning


Zero shot learning consists in training a machine/agent with little training data and then test it on a  similar or random environment

This is the implementation of our Research Paper https://drive.google.com/open?id=1JhLX2T0H02QnOCxdoYatNhghbIbakmKI

In this respository i have used three methods to solve the zero shot learning problem on UAV
 I do this project on Parrot-BeBop-2 Drone

# REQUIRMENTS


##Prerequisites##

1. Ubuntu 16.04

2. ROS Kinetic

```
http://wiki.ros.org/kinetic/Installation/Ubuntu
Visit this site and follow all the instructions (all the instructions)
```

3. OpenCV

4. TensorFlow GPU (For Training)

```
Follow instructions on
https://www.tensorflow.org/install/install_linux
```

5. TensorFlow CPU (For Testing)

```
Follow instructions on
https://www.tensorflow.org/install/install_linux
```


6. Python 2.7 / 3.5

7. CV Bridge (to interface between OpenCV and Python)

```
sudo apt-get install ros-kinetic-cv-bridge
```

8. Configuring Drone with Laptop

```
sudo apt-get install build-essential python-rosdep python-catkin-tools


# Create and initialize the workspace

mkdir -p ~/bebop_ws/src && cd ~/bebop_ws
catkin init
git clone https://github.com/AutonomyLab/bebop_autonomy.git src/bebop_autonomy

# Update rosdep database and install dependencies (including parrot_arsdk)

rosdep update
rosdep install --from-paths src -i

# Build the workspace

catkin build

#Copy the teleop_key-master in folder PreRequisites to ~/bebop_ws/src

catkin build

```

9. Dependencies

```

Xlib
mss
numpy
pandas
future
pyautogui

sudo pip install xlib

#Similarly other dependencies

```

10. Folder Contents
```

There are three folders--> datacollection, training and testing
These folders contain the resp. scripts for each task.

```

11. Script Changes
```

Some Scipts have to be changed according to your laptop state and configuration:

1. mss_capture.py: 
    change the dimensions according to the postion & dimensions of the strem window.

2. automation.py:
    a. change the paths and names according to your machine & choice.
    b. Mouse commands in this scripts also need to be changed according to the positions of windows.
*** REFER TO VIDEO[automationInAction.mp4] FOR MORE DETAILS***

```


There are three models which you can use namely cnn,lrcn,lstm
Also contains a python file modles.py in which all the models are define
you can use any of them but i have tested the model on above mentioned models


# Data Collection
In Data-Collection file there is a file namely automate.py which automatically runs all the required files 
for data-collection, conecting to the bebop etc

As the bebop collects the data in .npy in 5D
and to use it in LSTM first apply the Randon Transform to frame and the use lstm it work fine then



