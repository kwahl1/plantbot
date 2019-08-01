#!/usr/bin/python
import sys
import os
from twython import Twython
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import tokens

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT) # soil sensor
GPIO.setup(17,GPIO.IN)  # soil sensor

GPIO.output(27,GPIO.HIGH)
time.sleep(1)

soil_state = 'Dry' if GPIO.input(17) else 'Wet'

GPIO.output(27,GPIO.LOW)

# do twice
humidity, temperature = Adafruit_DHT.read_retry(11, 4)
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

os.system("fswebcam -D 2 -S 20 -F 10 -d/dev/video0 -r640x480 --no-banner plant.jpg")

caption = 'Temperature: {0:0.1f} C \nHumidity: {1:0.1f} %'.format(temperature, humidity)
caption = caption + '\nSoil: ' + soil_state

api = Twython(tokens.CONSUMER_KEY,tokens.CONSUMER_SECRET,tokens.ACCESS_KEY,tokens.ACCESS_SECRET)
photo = open('plant.jpg','rb')
image_ids = api.upload_media(media=photo)
api.update_status(status=caption, media_ids=image_ids['media_id'])


print 'Tweeted: \n' + caption
