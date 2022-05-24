# BACKEND LIGHTS AND MOTOR CONTROL

import RPi.GPIO as GPIO
import time

def lightsConfig(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps):
    
    GPIO.setwarnings(False)
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

def dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight):
    if (daynight):
        IDLEdia(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps)
    else:
        IDLEnoche(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps)

def intermitentes(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight)
    
    GPIO.output(rightFrontDir, GPIO.HIGH)
    GPIO.output(leftFrontDir, GPIO.HIGH)
    GPIO.output(rightBackDir, GPIO.HIGH)
    GPIO.output(leftBackDir, GPIO.HIGH)
    time.sleep(500)
    
    GPIO.output(rightFrontDir, GPIO.LOW)
    GPIO.output(leftFrontDir, GPIO.LOW)
    GPIO.output(rightBackDir, GPIO.LOW)
    GPIO.output(leftBackDir, GPIO.LOW)
    time.sleep(500)

def rightDir(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
             leftBackDir, frontLights, foglamps, daynight):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
               leftBackDir, frontLights, foglamps, daynight)
    
    GPIO.output(rightFrontDir, GPIO.HIGH)
    GPIO.output(rightBackDir, GPIO.HIGH)
    time.sleep(500)
    
    GPIO.output(rightFrontDir, GPIO.LOW)
    GPIO.output(rightBackDir, GPIO.LOW)
    time.sleep(500)
    
def leftDir(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight)
    
    GPIO.output(leftFrontDir, GPIO.HIGH)
    GPIO.output(leftBackDir, GPIO.HIGH)
    time.sleep(500)
    
    GPIO.output(leftFrontDir, GPIO.LOW)
    GPIO.output(leftBackDir, GPIO.LOW)
    time.sleep(500)

def reverse(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight)
    
    GPIO.output(redLights, GPIO.HIGH)
    GPIO.output(rightBackDir, GPIO.HIGH)
    GPIO.output(leftBackDir, GPIO.HIGH)
    
def stopMovement(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight)
    
    GPIO.output(redLights, GPIO.HIGH)

def fogLights(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight):
    
    dayORnight(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps, daynight)
    
    GPIO.output(foglamps, GPIO.HIGH)

redLights = 29
rightFrontDir = 31
leftFrontDir = 33
rightBackDir = 35
leftBackDir = 37
frontLights = 40 
foglamps = 38
daynight = True

lightsConfig(redLights, rightFrontDir, leftFrontDir, rightBackDir, \
                 leftBackDir, frontLights, foglamps)
GPIO.output(frontLights, GPIO.HIGH)
