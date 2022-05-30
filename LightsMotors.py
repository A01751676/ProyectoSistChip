# BACKEND LIGHTS AND MOTOR CONTROL

import RPi.GPIO as GPIO
import time

## -------------------------------- LIGHTS -----------------------------------

def lightsConfig(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin):
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD) #set pins number on Rpi
    GPIO.setup(autoLightsPin, GPIO.IN)
    
    GPIO.setup(redLights, GPIO.OUT)
    
    GPIO.setup(rightFrontDir, GPIO.OUT)
    GPIO.setup(leftFrontDir, GPIO.OUT)
    GPIO.setup(rightBackDir, GPIO.OUT)
    GPIO.setup(leftBackDir, GPIO.OUT)
    
    GPIO.setup(frontLights, GPIO.OUT)
    GPIO.setup(foglamps, GPIO.OUT)
    

def IDLEnoche(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps):
    
    GPIO.output(redLights, GPIO.LOW)
    GPIO.output(rightFrontDir, GPIO.LOW)
    GPIO.output(leftFrontDir, GPIO.LOW)
    GPIO.output(rightBackDir, GPIO.LOW)
    GPIO.output(leftBackDir, GPIO.LOW)
    GPIO.output(frontLights, GPIO.HIGH)
    GPIO.output(foglamps, GPIO.LOW)
    
def IDLEdia(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps):
    
    GPIO.output(redLights, GPIO.LOW)
    GPIO.output(rightFrontDir, GPIO.LOW)
    GPIO.output(leftFrontDir, GPIO.LOW)
    GPIO.output(rightBackDir, GPIO.LOW)
    GPIO.output(leftBackDir, GPIO.LOW)
    GPIO.output(frontLights, GPIO.LOW)
    GPIO.output(foglamps, GPIO.LOW)

def dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin):
    
    daynight = GPIO.input(autoLightsPin)
    print(daynight)
    if (daynight == 0):
        IDLEdia(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps)
    else:
        IDLEnoche(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps)

def intermitentes(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin)
    
    GPIO.output(rightFrontDir, GPIO.HIGH)
    GPIO.output(leftFrontDir, GPIO.HIGH)
    GPIO.output(rightBackDir, GPIO.HIGH)
    GPIO.output(leftBackDir, GPIO.HIGH)
    time.sleep(0.5)
    
    GPIO.output(rightFrontDir, GPIO.LOW)
    GPIO.output(leftFrontDir, GPIO.LOW)
    GPIO.output(rightBackDir, GPIO.LOW)
    GPIO.output(leftBackDir, GPIO.LOW)
    time.sleep(0.5)

def rightDir(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
             leftBackDir, frontLights, foglamps, autoLightsPin):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
               leftBackDir, frontLights, foglamps, autoLightsPin)
    
    GPIO.output(rightFrontDir, GPIO.HIGH)
    GPIO.output(rightBackDir, GPIO.HIGH)
    time.sleep(0.5)
    
    GPIO.output(rightFrontDir, GPIO.LOW)
    GPIO.output(rightBackDir, GPIO.LOW)
    time.sleep(0.5)
    
def leftDir(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin)
    
    GPIO.output(leftFrontDir, GPIO.HIGH)
    GPIO.output(leftBackDir, GPIO.HIGH)
    time.sleep(0.5)
    
    GPIO.output(leftFrontDir, GPIO.LOW)
    GPIO.output(leftBackDir, GPIO.LOW)
    time.sleep(0.5)

def reverse(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin)
    
    GPIO.output(redLights, GPIO.HIGH)
    GPIO.output(rightBackDir, GPIO.HIGH)
    GPIO.output(leftBackDir, GPIO.HIGH)
    
def stopMovement(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin)
    
    GPIO.output(redLights, GPIO.HIGH)

def fogLights(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin)
    
    GPIO.output(foglamps, GPIO.HIGH)

## -------------------------------- MOTORS -----------------------------------
def moveForward():
    pass

def turnRight():
    pass

def turnLeft():
    pass

def stopMovement():
    pass

def moveBack():
    pass

redLights = 29
rightFrontDir = 31
leftFrontDir = 33
rightBackDir = 35
leftBackDir = 37
frontLights = 40 
foglamps = 38
autoLightsPin = 36

lightsConfig(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin)

leftDir(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, autoLightsPin)
