# BACKEND LIGHTS AND MOTOR CONTROL

import RPi.GPIO as GPIO
import time

## -------------------------------- MOTORES ----------------------------------
in1 = 24
in2 = 23
enA = 25
in3 = 24
in4 = 23
enB = 25

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
    
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(enA,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(enB,GPIO.OUT)
    
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    
    pA = GPIO.PWM(enA,1000)
    pA.start(25) 
    
    pB = GPIO.PWM(enA,1000)
    pB.start(25) 

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
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def turnRight():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def turnLeft():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    

def stopMovement():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    
def moveBack():
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
