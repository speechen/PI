Zum Alarmanlagen Projekt
Anschlüsse
Anschlüsse Safe Projekt

Anschlüsse Raspberry Pi	Anschlüsse Module
Box	
GPIO 5	1. Kupferklebeband
GND	2. Kupferklebeband
Buzzer	
GPIO 18	langes Bein Buzzer
GND	kurzes Bein Buzzer
Keypad
GPIO 6	1
GPIO 13	2
GPIO 19	1
GPIO 26	1
GPIO 12	1
GPIO 16	1
GPIO 20	1
GPIO 21	1
Display	
GPIO 24	1 - RST
GPIO 8 /SPI CE0	2 - CE
GPIO 23	3 - DC
GPIO 10 / SPI MOSI	4 - Din
GPIO 11 / SPI CLK	5 - CLK
3,3V	6 - VCC
3,3V	7 - BL
GND	8 - GND
Das Programm
Für das Display müssen wir erst noch weitere Schriftarten (Fonts) herunterladen.

Bash
$ git clone https://github.com/coding-world/fonts
display.py

Bash
$ import Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

spiSettings = SPI.SpiDev(0, 0, max_speed_hz=4000000)
d = LCD.PCD8544(23, 24, spi=spiSettings)

d.begin(contrast=60)
d.clear()
d.display()
font = ImageFont.truetype("/home/pi/fonts/Unique.ttf", 13)

def anzeige(text1, text2, text3):
    image = Image.new("1",(LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,84,48),outline=255,fill=255)
    d.clear()
    d.display()
    draw.text((25,1), text1, font=font)
    draw.text((1,13), text2, font=font)
    draw.text((1,30), text3, font=font)
    d.image(image)
    d.display()
keypad.py

Bash
$ import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

matrix = [["1","2","3", "A"],
    ["4","5","6", "B"],
    ["7","8","9", "C"],
    ["*", "0", "#", "D"]]

spalte = [12, 16, 20, 21]
zeile = [6,13,19,26]

for j in range(4):
  gpio.setup(spalte[j], gpio.OUT)
  gpio.output(spalte[j], 1)
  gpio.setup(zeile[j],gpio.IN,
       pull_up_down=gpio.PUD_UP)

def keypad():
  while True:
      for j in range(4):
          gpio.output(spalte[j], 0)
          for i in range(4):
              if gpio.input(zeile[i]) == 0:
                  benutzerEingabe = matrix[i][j]
                  while gpio.input(zeile[i]) == 0:
                      pass
                  return benutzerEingabe
          gpio.output(spalte[j], 1)
  return False
alarm.py

Bash
$ import RPi.GPIO as gpio
from keypad import keypad
from display import anzeige
import time

# Pins
buzzer = 18
kontakt = 5

gpio.setmode(gpio.BCM)
gpio.setup(buzzer, gpio.OUT)
gpio.setup(kontakt, gpio.IN,pull_up_down=gpio.PUD_UP)

# Alarm
def offen(channel):
    global einbruch
    if(offenErlaubt == False): #unerlaubt geöffnet
        einbruch = True
        gpio.output(buzzer, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(buzzer, gpio.LOW)
        time.sleep(0.5)

gpio.add_event_detect(kontakt, gpio.RISING, callback=offen)

eingabe = ""
offenErlaubt = False
einbruch = False
pin = "123A"

while True:
    uhrzeit = time.strftime("%H:%M")
    if(offenErlaubt == True):
        if(einbruch == True):
            text1 = "Einbruch"
        else:
            text1 = uhrzeit

        anzeige(text1, "Offen", "schliessen *")
    else:
        anzeige(uhrzeit, "Verschlossen", "Pin eingeben")

    keypadEingabe = keypad()
    if(keypadEingabe == "#"):
        eingabe = ""
    elif(keypadEingabe == "*"):
        offenErlaubt = False
        einbruch = False
        eingabe = ""
    else:
        eingabe += keypadEingabe
    if(eingabe == pin):
        offenErlaubt = True
Erklärungen für das Keypad gibt es hier.

Erklärungen für das Display gibt es hier.

Kurz erklärt
Wir wollen nochmal kurz auf das Programm eingehen. Das Hauptprogramm ist alarm.py . Dieses bindet als Bibliothek die anderen beiden Programme ein. Die kümmern sich dann um das Display und das Keypad und sind den Programmen, die wir vorher benutzt haben, ziemlich ähnlich.

Grundsätzlich gibt es in diesem Programm folgende wichtige Variablen:

eingabe	Speichert die Eingaben des Keypads ab
offenErlaubt	Diese wird auf True gestellt, wenn der richtige Pin eingegeben wurde
einbruch	Wenn die Box geöffnet wird, ohne dass der richtige Pin eingegeben wurde, wird diese auf True gesetzt
pin	Speichert den Pin, der für das Freischalten eingegeben werden muss
Dir sollte das Meiste schon bekannt sein, aber in Zeile 24 gibt es eine Neuerung. Mit gpio.add_event_detect(kontakt, gpio.RISING, callback=offen) binden wir eine Funktion (offen) an ein bestimmtes Ereignis an den GPIO Pin Kontakt. Heißt für uns, wenn kein Strom mehr auf diesem Pin fließt, wird die Funktion offen aufgerufen. Diese haben wir vorher schon definiert. Wenn offenErlaubt False ist, handelt es sich um einen Einbruch. Wenn das der Fall ist, läuft der Buzzer und die Variable einbruch * wird auf True gestellt.

Das Ganze läuft unabhängig von der While-Schleife, die in Zeile 31 anfängt. Dort werden in Zeile 32 bis 41 die richtigen Werte auf dem Display angezeigt. Diese sind abhängig davon, ob die Box offen ist und ob es einen Einbruch gegeben hat. Das regeln wir über die verschiedenen Bedingungen.

In Zeile 43 bis 53 wird die Pineingabe verwaltet. Zunächst gibt es dabei drei verschiedene Szenarien. Wenn eine # (Raute) eingegeben wird, wird die Variable eingabe wieder zurückgesetzt. So können falsche Pineingaben korrigiert werden. Wenn ein (Stern) eingegeben wird, wird die Box wieder gesperrt, indem offenErlaubt wieder auf False gesetzt wird. So kann die Box nach dem Öffnen wieder gesichert werden. Beim letzten Fall wurde eine Zahl oder Buchstabe eingegeben und diese wird zur eingabe * hinzugefügt.

In Zeile 52 wird dann geprüft, ob die Benutzereingabe gleich dem Pin ist. Wenn das der Fall ist wird offenErlaubt auf True gesetzt und die Schleife fängt von vorne an.

Das Prinzip ist recht simpel, aber dadurch, dass es soo viele Möglichkeiten gibt, schleichen sich auch schnell Fehler ein. Deswegen kontrolliere am besten alles nochmal, wenn etwas nicht funktioniert. Wenn du das Problem anders gelöst hast, kannst du dir unsere Lösung auf jeden Fall als Inspiration ansehen!
