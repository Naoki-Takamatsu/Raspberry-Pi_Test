# coding: utf-8

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

while True:
#	print GPIO.input(SENSOR)
	GPIO.output(LED, GPIO.LOW)

	if( GPIO.input(SENSOR) == GPIO.HIGH ) and ( intaval + INTAVAL_TIME < time.time() ):
		intaval = time.time()
#		print "!! Detection !!"
		GPIO.output(LED, GPIO.HIGH)

	time.sleep(SLEEP_TIME)
