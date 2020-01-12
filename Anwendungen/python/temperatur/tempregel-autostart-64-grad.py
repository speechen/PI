#!/usr/bin/env python3.3
# Raspberry Pi Lüftersteuerung
# Fertiges Programm, geschrieben in Python3
# heute Strippen loeten um Pins rueberzuziehen

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)



GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)




while 1:
 tempData = "/sys/class/thermal/thermal_zone0/temp"
 dateilesen = open(tempData, "r")
 temperatur = dateilesen.readline(2)
 dateilesen.close()
 print("Deine CPU hat " + temperatur + " Grad")

 kalt = 40
 warm = 43
 heiss = 44

 temperatur = int(temperatur)



 if temperatur > warm:
     print ("LUEFTER Aus")
     GPIO.output(14, GPIO.LOW)
     GPIO.output(15, GPIO.LOW)
 if temperatur > heiss:
     print ("SCHNELL Lüfter!")

     GPIO.output(14, GPIO.HIGH)
     GPIO.output(15, GPIO.HIGH)
 time.sleep(2)

GPIO.cleanup(all)
#GPIO.cleanup(2,3,4,17,22,27)