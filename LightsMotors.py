# BACKEND LIGHTS AND MOTOR CONTROL

import RPi.GPIO as GPIO

def lightsConfig(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps):
    
    GPIO.setmode(GPIO.BCM) #set pins number on Rpi
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

redLights = 29
rightFrontDir = 31
leftFrontDir = 33
rightBackDir = 35
leftBackDir = 37
frontLights = 40 
foglamps = 38

lightsConfig(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps)
    
IDLEnoche(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps)