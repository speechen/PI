#!/usr/bin/env python3.3
# Raspberry Pi Lüftersteuerung
# Fertiges Programm, geschrieben in Python3
# heute Strippen loeten um Pins rueberzuziehen

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)



GPIO.output(3, GPIO.LOW)
GPIO.output(2, GPIO.LOW)




while 1:
 tempData = "/sys/class/thermal/thermal_zone0/temp"
 dateilesen = open(tempData, "r")
 temperatur = dateilesen.readline(2)
 dateilesen.close()
 print("Deine CPU hat " + temperatur + " Grad")

 kalt = 40
 warm = 49
 heiss = 50

 temperatur = int(temperatur)


 if temperatur > warm:
     print ("LUEFTER Aus")
     GPIO.output(3, GPIO.LOW)
     GPIO.output(2, GPIO.HIGH)
 if temperatur > heiss:
     print ("SCHNELL Lüfter!")

     GPIO.output(3, GPIO.HIGH)
     GPIO.output(2, GPIO.LOW)
 time.sleep(2)

GPIO.cleanup(all)
#GPIO.cleanup(2,3,4,17,22,27)