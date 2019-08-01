#!/usr/bin/python
#import sys
#import os
#from twython import Twython
#import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(17,GPIO.IN)

GPIO.output(27,GPIO.HIGH)
time.sleep(3)


if not GPIO.input(17):
	print 'Soil: Wet'
else:
	print 'Soil: Dry'

time.sleep(1)
GPIO.output(27,GPIO.LOW)


time.sleep(1)


GPIO.output(27,GPIO.HIGH)
time.sleep(1)


if not GPIO.input(17):
        print 'Soil: Wet'
else:
        print 'Soil: Dry'

time.sleep(1)

GPIO.output(27,GPIO.LOW)

