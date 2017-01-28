# coding: utf-8

import datetime

import picamera
import time

import RPi.GPIO as GPIO
import time

SLEEP_TIME = 1
INTAVAL_TIME = 1

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

SENSOR = 5
GPIO.setup(SENSOR, GPIO.IN)

LED = 6
GPIO.setup(LED, GPIO.OUT) 

intaval = time.time() - INTAVAL_TIME

camera = picamera.PiCamera()

while True:
	if( GPIO.input(SENSOR) == GPIO.HIGH ) and ( intaval + INTAVAL_TIME < time.time() ):
		intaval = time.time()

		GPIO.output(LED, GPIO.HIGH)

		camera.led = True
		camera.start_preview()
		time.sleep(1)

		NowTime = datetime.datetime.now()
		camera.capture(NowTime.strftime("%Y%m%d_%H:%M:%S") + '.jpg')

		camera.stop_preview()
		camera.led = False

		GPIO.output(LED, GPIO.LOW)

	time.sleep(SLEEP_TIME)
