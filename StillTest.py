# coding: utf-8

import picamera
import time
 
camera = picamera.PiCamera()

camera.led = True
camera.start_preview()
time.sleep(3)

camera.capture('test.jpg')

camera.stop_preview()
camera.led = False

camera.close()
