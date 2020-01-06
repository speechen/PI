BMP mit Raspberry Pi und Python auslese
BMP mit Raspberry Pi und Python auslese Titelbild
Manche Sensoren sprechen einfach eine andere Sprache. So wie der BMP180, den du in den nächsten Einheiten kennen lernen wirst. Dieser kleine Sensor kommuniziert über das so genannte I2C. Und da dieses I2C nicht standardmäßig aktiviert ist, müssen wir das mal wieder selbst machen.

I2C haben wir am Anfang schon aktiviert, aber wir müssen den Pi noch ein wenig mehr konfigurieren, damit dieser auch wirklich weiß, wie wir mit ihm arbeiten wollen.

Deswegen müssen wir folgende Datei bearbeiten:

Bash
$ sudo nano /etc/modules
und dann musst du noch diese Zeilen hinzufügen:

i2c-bcm2708 
i2c-dev
und wie gewohnt mit strg + x, oder ctrl + x, speichern. Das sollte bei dir dann so aussehen:

102.png
Folgende Datei muss dann auch noch mit diesen beiden Werten ergänzt werden:

Bash
$ sudo nano /boot/config.txt
Scrolle dafür am besten ganz nach Unten (Pfeiltaste Unten/Oben):

dtparam=i2c1=on
dtparam=i2c_arm=on
Es kann sein, dass dtparam=i2c1=on schon bei dir steht. Dann ergänzt du nur die zweite Zeile.*
und wie immer mit str + x, oder ctrl + x, speichern. Bei dir sollte das, wenn du am Ende beiden Zeilen hinzugefügt hast, so aussehen:

103.png
Jetzt ist alles geschafft! Eine kleine Pause und dann werden wir uns darum kümmern, den Luftdrucksensor vernünftig auszulesen.

Du kennst das doch bestimmt, die dicke Luft während eines Mathetests. Dicke Luft während eines Mathetests ist sehr gefährlich, da sie dazu führen kann, dass die Fenster aufgehen. Und wenn Fenster unachtsam geöffnet werden, kann da ganz leicht jemand raus auf die Straße fallen. Deswegen setzen wir uns dafür ein, Mathetests zu verbieten. Dazu müssen wir die dicke Luft aber erst einmal nachweisen und das machen wir am besten einfach mit dem BMP180, der kann nämlich den Luftdruck messen.

104.png
Anschlüsse am Pi	Anschlüsse am BMP180
3,3V	3,3V am BMP
GPIO2 (SDA)	SDA BMP
GPIO3 (SCL)	SCL BMP
GND (Ground)	GND/td>
Leider kann es bei den BMP180 unterschiedlich sein, in welcher Reihenfolge die Pins sind. Wichtig ist dabei, dass du SDA vom BMP auch an den SDA Pin am Raspberry Pi anschließt. Selbiges gilt natürlich auch für die anderen Pins.

Als nächstes wirst du etwas fürs Leben lernen. Große Aufgaben setzen ein großes Wissen voraus. Aber das erfährst du erst in der nächsten Einheit.

Aus diesem Grund musst du jetzt erstmal ein paar wichtige Bibliotheken aus dem Internet laden:

Bash
$ sudo apt-get install libi2c-dev i2c-tools  libffi-dev
Wir haben zwar schon unseren Raspberry Pi in den vorherigen Einheiten so konfiguriert, dass er I2C spricht, aber wir brauchen noch ein paar mehr Programme.

Bash
$ sudo apt-get install python3-pip
Bei pip handelt es um einen sogenannten Paketmanager. Mit diesem können wir Bibliotheken für Python installieren, die noch nicht auf dem System vorhanden sind.

Bash
$ sudo pip-3.2 install cffi
Bash
$ sudo pip-3.2 install smbus-cffi
Das sind beide Pakete, die wir für eine ordentliche I2C-Kommunikation brauchen. Denn auch Python muss erst einmal ordentlich I2C sprechen lernen.

Bash
$ git clone https://github.com/coding-world/Python_BMP.git
Bash
$ cd Python_BMP
Bash
$ sudo python3 setup.py install
Und dann mit cd .. wieder aus dem Ordner.

Danach musst du den Pi einmal neu starten.

Bash
$ sudo reboot
Jetzt haben wir alles Wissen, das wir benötigen, installiert und können endlich das passende Programm schreiben.

Wenn ihr euch nicht ganz sicher seid, oder ihr gleich beim Ausführen des Programmes eine Fehlermeldung bekommt, könnt ihr mit diesem Terminalbefehl kontrollieren, ob alles richtig konfiguriert ist.

Bash
$ sudo i2cdetect -y 1
105.png
Mit diesem Befehl könnt ihr euch alle angeschlossenen I2C-Geräte anzeigen lassen. Wenn bei euch eine 77 Steht ist der BMP richtig angeschlossen und ist per I2C verbunden.

Für unser neues Programm brauchen wir aber erstmal eine neue Datei. Nano ist dabei mal wieder unser bester Freund.

Bash
$ nano bmp-test.py
Jetzt solltest du dich besser hinsetzen und festhalten, reine Vorsichtsmaßnahmen, damit du nicht vom Stuhl fällst. Denn ich präsentiere dir jetzt den Programmcode:

Python
import Python_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

print("Luftdruck:"+str(sensor.read_pressure()))
print("Höhe:"+str(sensor.read_altitude()))
Bash
$ sudo python3 bmp-test.py
So wenig Zeilen und doch eine so coole Sache. Den Funktionen sei Dank. Wenn alles richtig gelaufen ist, sollte dir beim Ausführen des Programms der Luftdruck angezeigt werden.

Jetzt bist du dran:

Schreibe ein Programm, das zehnmal hintereinander mit jeweils drei Sekunden Abstand den Luftdruck misst. Wenn du richtig richtig gut bist, könntest du nach mehrmaligem Messen einen Durchschnittswert ausrechnen und diesen ausgeben. Eine Beispiel-Lösung findest du dafür in der nächsten Einheit. *
Lösung Hier die Lösung für die Aufgabe:

Python
import Python_BMP.BMP085 as BMP085
import time

sensor = BMP085.BMP085()

messungen = 0
messwerte = 0

while messungen < 10:
        messwerte += sensor.read_pressure()
        messungen +=1
        time.sleep(3)
print('DurchschnittsLuftdruck: '+ str(messwerte/messungen))
[alert-info]Tipp: Eigene Notizen sind beste Notizen![/alert]

Hier eine kleine Zusammenfassung mit allem, was du gelernt haben solltest!.

Zuerst müssen wir I2C einrichten. Das ist einfach nur ein anderer Kommunikationskanal, den wir aber zuerst aktivieren müssen.
Bevor wir den BMP auch wirklich benutzen können, müssen wir eine zusätzliche Bibliothek installieren.
.read_pressure() ist die Funktion, mit der wir die Daten aus dem Sensor auslesen können.
Das Anschließen ist meistens komplizierter als der ganze Rest und wenn das geschafft ist, ist das Auslesen von den Sensorendaten recht einfach. Wir hatten jetzt viel Praxis, deswegen geht es nun weiter mit ein wenig mehr Python Theorie.
