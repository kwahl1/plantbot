#!/usr/bin/python
#import sys
#import os
#from twython import Twython
import Adafruit_DHT
import time
import RPi.GPIO as GPIO

humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)


