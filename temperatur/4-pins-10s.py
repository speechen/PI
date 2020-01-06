# LED Test Script
# schaltet 4 Pins für 10 Sekunden an

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.HIGH)
GPIO.output(4, GPIO.HIGH)
GPIO.output(17, GPIO.HIGH)

time.sleep(10)

GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(17, GPIO.LOW)

GPIO.cleanup()