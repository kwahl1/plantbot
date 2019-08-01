#!/usr/bin/python
import sys
import os
#from twython import Twython
#import Adafruit_DHT
import time
#import RPi.GPIO as GPIO


os.system("fswebcam -D 2 -S 20 -F 10 -d/dev/video0 -r640x480 --no-banner test.jpg")
os.system("mirage test.jpg")
