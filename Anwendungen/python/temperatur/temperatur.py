#!/usr/bin/env python3.3
# Raspberry Pi Lüftersteuerung
# Fertiges Programm, geschrieben in Python3
# heute Strippen loeten um Pins rueberzuziehen

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setmode(BOARD)
# Festlegung der Pins als Ausgang 3,3 V ( BCM ) gibt auch BOARD

# hat fuer Temperatur keine Bedeutung, soll nur als Beispiel gelten,
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
# alle auf OUT setzen

GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
# erstmal alle auf LOW setzen

frequenz = 10

while 1:
 tempData = "/sys/class/thermal/thermal_zone0/temp"
# dort findet man die CPU-Temperaur
 dateilesen = open(tempData, "r")
# jetzt wird die Datei mit der Temperatur lesend  (r) geoeffnet
 temperatur = dateilesen.readline(2)
# jetzt werden die ersten zwei Stellen der fuenstelligen Teperaturangabe ausgelsen. 53213 ( 53,213 Grad )
 dateilesen.close()




 now    = 6000
 normal = 47
 warm   = 48
 heiss  = 49

 frequenz = int(frequenz)
# umwandeln des String Temperatur in einen Integer, damit mit = < > ausgewertet werden kann.
 if frequenz == now:
# bei 600 MHz wird mit 4 Stellen 6000 ausgegeben
     print ("Die Frequenz betraegt 600 MHz")
     #GPIO.output(3, GPIO.LOW)
     #GPIO.output(2, GPIO.LOW)
     GPIO.output(22, GPIO.HIGH)
     GPIO.output(27, GPIO.LOW)

 frequenz = int(frequenz)
# umwandeln des String Temperatur in einen Integer, damit mit = < > ausgewertet werden kann.
 if frequenz < now:
     print ("Die Frequenz betraegt 1500 MHz")
     #GPIO.output(3, GPIO.LOW)
     #GPIO.output(2, GPIO.LOW)
     GPIO.output(22, GPIO.LOW)
     GPIO.output(27, GPIO.HIGH)

 temperatur = float(temperatur)
# umwandeln des String Temperatur in einen Integer, damit mit = < > ausgewertet werden kann.
 if temperatur < normal:
     print ("Die CPU ist Kalt, die grüne LED geht aus.")
     GPIO.output(3, GPIO.LOW)
     GPIO.output(2, GPIO.LOW)
     #GPIO.output(22, GPIO.LOW)
     #GPIO.output(27, GPIO.LOW)
 temperatur = float(temperatur)
# umwandeln des String Temperatur in einen Integer, damit mit = < > ausgewertet werden kann.


 if temperatur == normal:
     print ("Die CPU ist Normal, die grüne LED geht an.")
     GPIO.output(3, GPIO.HIGH)
     GPIO.output(2, GPIO.LOW)
# Ist die Temperatur nicht gleich oder kleiner wird der naechste Befehl ausgefuehrt.
# Ist die Temperatur aber dann auf oder ueber warm wird der Befehl ausgefuehrt

 if temperatur >= warm:
     print ("Die CPU ist Warm, die Gelbe LED geht auch an")
     GPIO.output(3, GPIO.HIGH)
     GPIO.output(2, GPIO.HIGH)
     #GPIO.output(22, GPIO.HIGH)
     #GPIO.output(27, GPIO.HIGH)
     GPIO.output(4, GPIO.LOW)
     GPIO.output(17, GPIO.LOW)
 if temperatur >= heiss:
     print ("Die CPU ist wärmer als warm! Die Rote LED geht an und wir schalten den Lüfter ein !")
     GPIO.output(3, GPIO.HIGH)
     GPIO.output(2, GPIO.HIGH)
     GPIO.output(4, GPIO.HIGH)
     GPIO.output(17, GPIO.HIGH)

# GPIO.cleanup(all)
# wird hier eingefuegt, dann gibt time.sleep() einen Fehler aus ????
# STOP
 time.sleep(3)


GPIO.cleanup(all)

#frame.clear( ) #Diese Methode löscht alle Verweise auf lokale Variablen, die im Frame enthalten sind.

# all geht auch
#GPIO.cleanup(2,3,4,17,22,27)
# (2,3 usw geht auch
# GPIO.cleanup() dann lassen sich die GPIO nicht auf LOW setzen

# http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_GPIO_int.html Interrupsmethode!!!