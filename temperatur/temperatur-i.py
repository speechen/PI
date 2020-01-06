import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

try:
 while True:
     GPIO.output(2,1)
     time.sleep(0.5)
     GPIO.output(2,0)
     time.sleep(0.5)

#channel = 2  # GPIO-Pin
     GPIO.add_event_detect(2, GPIO.RISING)
#if   GPIO.event_detected(2):
     print('Button pressed')

     GPIO.add_event_detect(channel, GPIO.RISING, ...) #für das Erkennen einer steigenden Flanke (0 → 1)
     GPIO.add_event_detect(channel, GPIO.Falling, ...) #für das Erkennen einer fallendenden Flanke (1 → 0)
     GPIO.add_event_detect(channel, GPIO.BOTH, ...) #für das Erkennen einer steigenden oder fallenden Flanke (0 → 1, 1 → 0)



#if GPIO.event_detected(2):
     print('Button pressed')

#def my_callback(channel):
#    print('This is a edge event callback function!')

GPIO.add_event_detect(2, GPIO.RISING)
GPIO.add_event_callback(2, antwort_1)
GPIO.add_event_callback(2, antwort_2)

GPIO.setup(XX, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(XX, GPIO.IN, pull_up_down = GPIO.PUD_UP)

import signal
import time

# Signalhandler fuer den timeout
def handler(signum, frame):
  print "Timeout!"
  raise Exception("end of time")

# signal function handler registrieren
signal.signal(signal.SIGALRM, handler)
# timeout definieren
signal.alarm(10)

# Hauptprogramm
try:
  while 1:        # eigentlich eine Endlosschleife
    print "tick"
    time.sleep(1)

except Exception, exc:
  print exc