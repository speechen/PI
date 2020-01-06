Raspberry Pi: Interrupt-Verarbeitung mit Python
Allgemeines
Was ist ein Interrupt? In diesem Fall ist es eine Unterbrechung des normalen Programmablaufs durch ein
äußeres Ereignis, beispielsweise der Pegelwechsel an einem GPIO-Port, ausgelöst durch eine Taste.
Das normale Programm wird unterbrochen und eine sogenannte Interrupt-Serviceroutine (manchmal auch "Callback" genannt)
ausgeführt. Danach läuft das Programm ganz normal weitr als sein nichts geschehen. Es ist auso eine Methode,
auf ein Ereignis zu warten, ohne ständig überprüfen zu müssen, ob es schon eingetreten ist.

Viele einfache Programme lesen in einer Endlosschleife den Wert eines Eingabesignals aus und reagieren,
sobald sich dessen Wert verändert. Bei einer einzelnen Signalquelle mag das gerade noch angehen.
Jedoch lastet eine solche Schleife ("Busy Waitig") die CPU stark aus und bremst damit alle anderen
Vorgänge auf dem Raspberry. Eine Verbesserung wäre ein Wartezyklus in der Schleife, der mit der
Funktion time.sleep() zwischen den Abfragen realisiert werden kann. Das schafft zwar "Luft" für
andere Aktionen, bedeutet aber auch, dass immer auch eine gewisse Zeit vergeht, bevor das Programm
eine Veränderung des Eingabewerts mitbekommt. Eie derartige Programmierung läuft unter dem Oberbegriff "Polling".

Mit Interrupts gibt es eine wesentlich effektivere Methode, um direkt auf Signalveränderungen zu reagieren.
Solche Interrupts sind vor allem dann ideal, wenn es darum geht, Veränderungen an verschiedenen Pins des GPIO zu registrieren.
Beim Polling kann unter Umständen schon mal ein Ereignis im wahrsten Sinn des Wortes "verschlafen" werden.

Viele Programm erledigen keine Aufräumarbeiten wenn sie mit Strg-C unterbrochen werden.
Da die Pin- und Interrupt-Einstellungen auch nach dem Programmende erhalten bleiben, kann es vorkommen,
dass die benutzten Pins bei einer anderen Anwendung anschließend nicht funktioniert.
Man sollte also beim Unterbrechen des Programms die Funktion GPIO.cleanup() auszuführen.
Der Keyboard-Interrupt läßt sich nutzen, um das Programm ordnungsgemäß zu beenden, wie folgendes Beispiel zeigt:

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

try:
  while True:
    GPIO.output(18,1)
    time.sleep(0.5)
    GPIO.output(18,0)
    time.sleep(0.5)


Stupid Python Tricks: The KeyboardInterrupt Exception
February 17, 2003 | Fredrik Lundh

If you try to stop a CPython program using Control-C, the interpreter throws a KeyboardInterrupt exception.

Unfortunately, this is an ordinary exception, and is, like all other exceptions, caught by a “catch-all” try-except statement.

try:
    # do something
except:
    # you'll end up here if something goes wrong,
    # or if the user presses control-c
For example, if your program contains code like the following, your users may find that pressing Control-C is a great way to mess up their database, but a really lousy way to stop the program:

for record in database:
    try:
        process(record)
        if changed:
            update(record)
    except:
        # report error and proceed
To solve the exception problem, add a separate except-clause that catches the KeyboardInterrupt exception, and raises it again:

for record in database:
    try:
        process(record)
        if changed:
            update(record)
    except KeyboardInterrupt:
        raise
    except:
        # report error and proceed
or, even better:

for record in database:
    try:
        process(record)
        if changed:
            update(record)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        # report error and proceed
By looking for SystemExit as well, calling sys.exit() in the processing or update code will actually stop the program.

Note that if the update process isn’t an atomic operation in itself, it’s also a good idea to use database transactions, and roll back when something goes wrong:

for record in database:
    begin()
    try:
        process(record)
        if changed:
            update(record)
    except (KeyboardInterrupt, SystemExit):
        rollback()
        raise
    except:
        rollback()
        # report error and proceed
    else:
        commit()


Ende Einfuegung


except KeyboardInterrupt:
  GPIO.cleanup()
  print "Bye"
Die Interrupt-Methoden
Die Methode GPIO.add_event_detect() installiert einen Interrupt und die zugehörige Callback-Funktion für einen bestimmten Eingangspin des GPIO.
Mittels GPIO.event_detected() kann das Ereignis später abgefragt werden. Vorteil: Das Ereignis kann nicht "verloren gehen":
   ...
channel = 18  # GPIO-Pin
   ...
GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel

do_something()
if GPIO.event_detected(channel):
    print('Button pressed')
   ...
Das ist aber noch keine richtige Interrupt-Verarbeitung, es fehlt noch die Callback-Funktion. Diese wird durch eine Flanke am entsprechenden GPIO-Pin ausgelöst. Für die Angabe der Flanke gibt es drei Möglichkeiten:
GPIO.add_event_detect(channel, GPIO.RISING, ...) für das Erkennen einer steigenden Flanke (0 → 1)
GPIO.add_event_detect(channel, GPIO.Falling, ...) für das Erkennen einer fallendenden Flanke (1 → 0)
GPIO.add_event_detect(channel, GPIO.BOTH, ...) für das Erkennen einer steigenden oder fallenden Flanke (0 → 1, 1 → 0)
Im letzten Fall muss dann innerhalb der Callback-Funktion der entsprechende Port ausgelesen werden, um festzustellen, ob der Auslöser eine steigende Flanke (Port-Wert "1") oder eine fallende war (Port-Wert "0").
Die vollständige Syntax der Methode lautet:

GPIO.add_event_detect(channel, GPIO.BOTH, callback=<Name der Callback-Funktion>)
Die Callback-Funktion wird wie eine ganz normale Funktion definiert, z. B.:
def my_callback(channel):
    print('This is a edge event callback function!')
      ...
Zu beachten ist, dass die Callback-Funktion mit den anderen Programmteilen nur über globale Variablen kommunizieren kann. Diese Variablen müssen im Hauptprogramm definiert und in der Callback-Funktion als global deklariert werden.
Die Definition einer Callback-Funktion kann auch mit zwei getrennten Methoden, der oben angeführten GPIO.add_event_detect() und GPIO.add_event_callback() erreicht werden. Angewendet wird dies meist nur dann, wenn man mehr als eine Callback-Funktion hat:

GPIO.add_event_detect(channel, GPIO.RISING)
GPIO.add_event_callback(channel, antwort_1)
GPIO.add_event_callback(channel, antwort_2)
Die beiden Funktionen werden nacheinander ausgeführt.
Gelegentlich kann man feststellen, dass die Callback-Funktion mehr als einmal für jedes Ereignis aufgerufen wird. Dies kann die Folge eines "prellenden" Tasters sein. Es gibt zwei Möglichkeiten, mit Schalterprellen umzugehen:

einen Kondensator von ca. 100 nF über den Schalter legen. Zusammen mit dem Pullup-Widerstand bildet das einen Filter für das kurzzeitige Prellen des Tasters.
Software Entprellung: die Software ignoriert nach der ersten erkannten Flanke für kurze Zeit weitete Flanken.
Natürlich hilft auch eine Kombination aus beidem. Auch ist gelegentlich ein externer Pullup-Widerstand sinnvoll. Im Python-GPIO-Modul kann auch ein interner Pullup- oder Pulldown-Widerstand eingeschaltet werden:
# Pulldown-Widerstand (gegen Masse)
GPIO.setup(XX, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
                  oder
# Pullup-Widerstand (gegen + 3,3 V)
GPIO.setup(XX, GPIO.IN, pull_up_down = GPIO.PUD_UP)
Die internen Widerstände sind aber recht hochohmig (40 bis 50 kΩ). Bei Störungen im Umfeld kann deren Wert zu hoch sein, um diese auszufiltern. Lässt man den Widerstand weg oder ist sein Wert zu hoch, genügt es, einen Draht am entsprechenden Pin anzuschließen und dessen anderes Ende frei in der Luft hängen zu lassen. Dann kann es durchaus sein, dass der Eingang bereits Signale empfängt (Elektrosmog ist inzwischen überall). Mit einem externen Widerstand kann man auf 10 kΩ bis 1 kΩ heruntergehen und so die Störsicherheit verbessern.
Um das Entprellen per Software zu erledigen, fügen Sie den bouncetime-Parameter dem Aufruf von GPIO.add_event_detect() hinzu, wobei die Zeit in Millisekunden angegeben wird. Die Methode hat demnach zwei obligatorische und zwei optionale Parameter. Zum Beispiel lautet der Aufruf für 300 ms Entprellzeit:

GPIO.add_event_detect(channel, GPIO.BOTH, callback=antwort, bouncetime=300)
Da auch nach einem Programmende die GPIO-Funktionen noch aktiv sein können, sollte man im Programm immer aufräumen. Manchmal will man aber nur eine Interrupt-Definiton löschen, nicht aber alles andere. In solchen Situationen kann dann die Methode GPIO.remove_event_detect() verwendet werden.

GPIO.remove_event_detect(channel)
Beispiele und Anwendungen
Das erste Beispiel zählt Tastendrücke (der Taster mit Pullup-Widerstand schliesst gegen GND-Pegel) auf Interrupt-Basis. Als Eingang dient GPIO 18 mit aktiviertem Pullup-Widerstand. Die globale Variable "Counter" wird in der Callback-Funktion verändert, um die Tastendrücke zu zählen. Der Zusatz bouncetime = 250 legt die Totzeit für das Tastenprellen fest. Dies ist nur wichtig, wenn Taster als Interruptquelle dienen. Um zu zeigen, dass das Programm auch läuft, wird ein Zähler namens "Tic" im Sekundentakt hochgezählt. Die Tastendrücke werden per Interrupt registriert.

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Zaehler-Variable, global
Counter = 0
Tic = 0

# Pinreferenz waehlen
GPIO.setmode(GPIO.BCM)

# GPIO 18 (Pin 12) als Input definieren und Pullup-Widerstand aktivieren
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Callback-Funktion
def Interrupt(channel):
  global Counter
  # Counter um eins erhoehen und ausgeben
  Counter = Counter + 1
  print "Counter " + str(Counter)

# Interrupt-Event hinzufuegen, steigende Flanke
GPIO.add_event_detect(18, GPIO.RISING, callback = Interrupt, bouncetime = 250)

# Endlosschleife, bis Strg-C gedrueckt wird
try:
  while True:
    # nix Sinnvolles tun
    Tic = Tic + 1
    print "Tic %d" % Tic
    time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
  print "\nBye"
Ein Programmlauf siht dann z. B. folgendermaßen aus:
Tic 1
Tic 2
Tic 3
Tic 4
Tic 5
Tic 6
Counter 1
Tic 7
Counter 2
Tic 8
Counter 3
Counter 4
Counter 5
Tic 9
Counter 6
Tic 10
^C
Bye


Es lassen sich durchaus mehrere Signalquellen mit Interrupts verbinden. Für jede Signalquelle muss dann eine Callback-Funktion definiert und der Interrupt aktiviert werden. Das folgende Beispiel hat zwei Taster an den GPIO-Ports 17 (Pin 11) und 18 (Pin 12). Die Taster haben wieder den Pullup-Widerstand aktiviert und schliessen gegen GND-Pegel.

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# GPIO-Ports
Counter_17 = 0
Counter_18 = 0

# Zaehlvariable
Tic = 0

# GPIO initialisieren
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) # Pin 11
GPIO.setup(18, GPIO.IN) # Pin 12

# internen Pullup-Widerstand aktivieren.
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Callback fuer GPIO 17
def isr17(channel):
    global Counter_17
    Counter_17 = Counter_17 + 1
    print "Counter_17: %d" % Counter_17

# Callback fuer GPIO 18
def isr18(channel):
    global Counter_18
    Counter_18 = Counter_18 + 1
    print "Counter_18: %d" % Counter_18

# Interrupts aktivieren
GPIO.add_event_detect(17, GPIO.FALLING, callback = isr17, bouncetime = 200)
GPIO.add_event_detect(18, GPIO.FALLING, callback = isr18, bouncetime = 200)

# Endlosschleife wie oben
try:
  while True:
    # nix Sinnvolles tun
    Tic = Tic + 1
    print "Tic %d" % Tic
    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()
  print "\nBye"
Wenn man das Programm startet kann man beide Interrupts verfolgen. Es funktioniert auch, wenn man beide GPIOs gemeinsam an einen Taster anschließt. Es geht also auf keinen Fall etwas verloren. Unten ein typischer Programmlauf:
Tic 1
Tic 2
Tic 3
Tic 4
Tic 5
Tic 6
Counter_17:1
Tic 7
Counter_17:2
Tic 8
Tic 9
Counter_18:1
Tic 10
Counter_18:2
Counter_18:3
Counter_18:4
Counter_18:5
Tic 11
Tic 12
Tic 13
^C
Bye
Die dritte Möglichkeit bei der Interrupt-Verarbeitung ermöglicht es, auf beide Flanken zu reagieren. Mit dem Befehl GPIO.add_event_detect(17, GPIO.BOTH, callback=measure) wird die Funktion measure() als Interrupt-Serviceroutine für steigende und fallende Flanke (GPIO.BOTH) eingetragen. Innerhalb der Funktion measure() wird dann der Port abgefragt. Hat er den Wert "1", war eine steigende Flanke Auslöser und die globale Variable start speichert die aktuelle Zeit. Im anderen Fall war die fallende Flanke der Auslöser und es wird die aktuelle Zeit in stopp gespeichert. Danach wird die Zeitdifferenz berechnet und ausgegeben. Der Taster hat wieder den Pullup-Widerstand aktiviert und schließt gegen GND-Pegel. Alles andere ist wie gehabt.

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
Nach dem Start ermittelt das Programm, wie lange der Taster gedrückt wurde, wobei Zeiten kleiner 200 ms (bouncetime) nicht vorkommen können. Will man genauere Werte, muss die Entprellung der Taste hardwaremäßig erfolgen.
Tic 1
Tic 2
Tic 3
delta = 0.03
Tic 4
delta = 1.52
Tic 5
Tic 6
Tic 7
Tic 8
Tic 9
delta = 0.37
Tic 10
Tic 11
delta = 2.53
delta = 0.26
Tic 12
Tic 13
Tic 14
Tic 15
^C
Bye!
Timeouts
Es gibt manchmal den Fall, dass ein am GPIO angeschlossenes Device nicht reagiert oder dass bei einer seriellen Verbindung die Gegenseite plötzlich nicht mehr reagiert. Das bearbeitende Programm bleibt dann "hängen". Das wäre nicht weiter schlimm, wenn der Prozess möglicherweise nicht ständig die Hardware abfragen und so Rechenzeit aufnehmen würde. Wird er dann noch per crontab in regelmäßigen Zeitabständen gestartet, kommt hinzu, dass ja jedesmal ein neuer, ebenfalls hängender Prozess hinzukommt. Langsam aber sicher würde der RasPi immer träger arbeiten und irgendwann geht dann gar nichts mehr.

Also muss dafür gesorgt werden, dass so ein Programm nach einer gewissen Zeit abgbrochen wird. Dies kann relativ einfach nach folgendem Schema erreicht werden. Im Python-Programm wird ein Timer gestartet und nach fünf Minuten das Programm zwangsweise abgebrochen. Dazu wird einerseits die entsprechende Bibliothek mittels import signal eingebunden und andererseits bei den Funktionen ein Signalhandler hinzugefügt, der das Programm beendet:

# Signalhandler fuer den Timeout
def to_handler(signum, frame):
  print "Timeout!"
  exit(1)
Am Anfang des Hauptprogramms wird der Signalhandler mit dem Timer verknüpft und der Timeout beispielsweise auf 10 s eingestellt:
# signal function handler registrieren
signal.signal(signal.SIGALRM, to_handler)
# timeout definieren
signal.alarm(10)
Das war es dann auch schon. Ist das Programm nach weniger als 10 Sekunden fertig, endet es ganz normal. Bleibt es "hängen", wird es nach fünf Minuten zwangsweise beendet.
Man kann das System noch dahingehnd erweitern, dass der Signalhandler das Programm nicht einfach beendet, sondern eine Exception wirft, damit sich noch Aufräumarbeiten erledigen lassen. Dazu wird der kritische Teil in try - except eingebunden. Das folgende Beispiel zeigt diese Erweitereung. Damit sich während der Wartezeit etwas tut, wird im Sekundenrhythmus "tick" ausgegeben:

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