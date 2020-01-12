veraenderung im branch inter

neu hinzu


#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime

# Variablen initialisieren
Tic = 0    # Zaehler
stopp = 0  # Zeitpunkt steigende Flanke
start = 0  # Zeitpunkt fallende Flanke
delta = 0  # Zeitdifferenz zwischen start und stopp

# GPIO initialisieren
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) # Pin 11

# internen Pullup-Widerstand aktivieren.
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Callback-Funktion fuer beide Flanken
def measure(channel):
  global start
  global stopp
  global delta
  if GPIO.input(17) == 0:       # fallende Flanke, Startzeit speichern
    start = time.time()
  else:                         # steigende Flanke, Endezeit speichern
    stopp = time.time()
    delta = stopp - start       # Zeitdifferenz berechnen
    print("delta = %1.2f" % delta)

# Interrupt fuer beide Flanken aktivieren
GPIO.add_event_detect(17, GPIO.BOTH, callback=measure, bouncetime=200)

try:
  while True:
    # nix Sinnvolles tun
    Tic = Tic + 1
    print "Tic %d" % Tic
    time.sleep(1)

# reset GPIO settings if user pressed Ctrl+C
except KeyboardInterrupt:
  GPIO.cleanup()
  print("\nBye!")

  def to_handler(signum, frame):
  print "Timeout!"
  exit(1)
