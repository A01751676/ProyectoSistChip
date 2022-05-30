# -*- coding: utf-8 -*-
"""
Created on Tue May 24 11:59:48 2022
cap.release()
@author: apisl
"""

# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
import RPi.GPIO as GPIO

# Create an instance of TKinter Window or frame
win = Tk()

# Set the size of the window
win.geometry("800x420")

# Create a Label to capture the Video frames sized 800 x 420
label =Label(win)
label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 420)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

reverseStatusPin = 32
GPIO.setup(reverseStatusPin, GPIO.OUT)
# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   GPIO.output(reverseStatusPin, GPIO.HIGH)
   
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   
   linesPts = np.array([[0, 415], [90, 300], [710, 300], [800, 415]])
   linesPts = linesPts.reshape((-1, 1, 2))
   cv2image = cv2.polylines(cv2image, np.int32([linesPts]), True, (255, 0, 0), 2)
   
   linesPts = np.array([[90, 300], [180, 180], [620, 180], [710, 300]])
   linesPts = linesPts.reshape((-1, 1, 2))
   cv2image = cv2.polylines(cv2image, np.int32([linesPts]), True, (255, 255, 0), 2)
   
   linesPts = np.array([[180, 180], [270, 60], [530, 60], [620, 180]])
   linesPts = linesPts.reshape((-1, 1, 2))
   cv2image = cv2.polylines(cv2image, np.int32([linesPts]), True, (0, 255, 0), 2)
   
   
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

show_frames()
win.mainloop()