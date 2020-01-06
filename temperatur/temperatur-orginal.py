#!/usr/bin/env python3.3
# Raspberry Pi Lüftersteuerung
# Fertiges Programm, geschrieben in Python3
# heute Strippen loeten um Pins rueberzuziehen

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)

# set up a list of the channels your program has used
#channels_used = [2,4,3,17,22,27]
# clean up everything except channel 6
#channels_used.remove(6)   # remove channel 6 from the list
#for channel in channels_used:
#     GPIO.cleanup(channel)

while 1:
 tempData = "/sys/class/thermal/thermal_zone0/temp"
 dateilesen = open(tempData, "r")
 temperatur = dateilesen.readline(2)
 dateilesen.close()
 print("Deine CPU hat " + temperatur + " Grad")

 normal = 45
 warm = 47
 heiss = 49

 temperatur = int(temperatur)

 if temperatur == normal:
    print ("Die CPU ist Normal, die grüne LED geht aus.")
     GPIO.output(3, GPIO.LOW)
     GPIO.output(2, GPIO.LOW)



 if temperatur >= normal:
     print ("Die CPU ist Normal, die grüne LED geht an.")
     GPIO.output(3, GPIO.HIGH)
     GPIO.output(2, GPIO.LOW)

 if temperatur > warm:
     print ("Die CPU ist Warm, die Gelbe LED geht auch an")
     GPIO.output(3, GPIO.HIGH)
     GPIO.output(2, GPIO.HIGH)
     GPIO.output(22, GPIO.HIGH)
     GPIO.output(27, GPIO.HIGH)
     GPIO.output(4, GPIO.LOW)
     GPIO.output(17, GPIO.LOW)
 if temperatur > heiss:
     print ("Die CPU ist wärmer als warm! Die Rote LED geht an und wir schalten den Lüfter ein !")
     GPIO.output(3, GPIO.HIGH)
     GPIO.output(2, GPIO.HIGH)
     GPIO.output(4, GPIO.HIGH)
     GPIO.output(17, GPIO.HIGH)
 time.sleep(2)

GPIO.cleanup(all)
#GPIO.cleanup(2,3,4,17,22,27)