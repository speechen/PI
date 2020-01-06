Temp

import Nokia_LCD as LCD
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
font = ImageFont.truetype("/home/pi/fonts/BBrick.ttf", 18)
fontSmall = ImageFont.truetype("/home/pi/fonts/BBrick.ttf", 8)

def anzeige(text1, text2, text3):
    image = Image.new("1",(LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,84,48),outline=255,fill=255)
    d.clear()
    d.display()
    draw.text((15,1), text1, font=fontSmall)
    draw.text((10,10), text2, font=font)
    draw.text((20,30), text3, font=font)
    d.image(image)
    d.display()
uhr    
    from display import anzeige
from ds18b20 import grad_lesen
import time

while True:
    text1 = time.strftime("%d.%m.%Y")
    text2 = time.strftime("%H:%M")
    text3 = str(grad_lesen())+"°c"
    anzeige(text1, text2, text3)
    time.sleep(1)
    
    
Projekt: Temperatur Anzeige
In den letzten Lektionen haben wir schon viel gelernt. Deswegen geht es jetzt erstmal an ein richtiges kleines Projekt. Unser Ziel ist es, mit dem Display und dem Temperatursensor eine eigene kleine Uhr zu bauen, die uns die Uhrzeit, das Datum und die Temperatur anzeigt.

Der Raspberry Pi hat keine eigene Uhr, sondern besorgt sich die aktuelle Zeit über das Internet. Deswegen kann es sein, dass du erst noch die richtige Zeitzone einstellen musst. Das geht mit sudo raspi-config und dann unter 5 Internationalisation Options -> I2 Change Timezone. Dort dann einfach Europa und dann Berlin auswählen.

Da wir dieses Mal viel mit Schriften arbeiten, wollen wir nicht wieder die Standardschriftart benutzten. Du kannst auch deine eigenen Schriftarten benutzen. Wir haben dir hier aber mal eine kleine Sammlung zusammengestellt, die du mit diesem Befehl herunterladen kannst. Für das Programm gleich ist es wichtig, dass du diesen Befehl im Home-Verzeichnis ausführst.

Bash
$ git clone https://github.com/coding-world/fonts
Nokia 5110 Display mit DS18B20 Raspberry Pi


Anschlüsse am Raspberry Pi	Anschlüsse am Display
GPIO 24	1 - RST
GPIO 8 /SPI CE0	2 - CE
GPIO 23	3 - DC
GPIO 10 / SPI MOSI	4 - Din
GPIO 11 / SPI CLK	5 - CLK
3,3V	6 - VCC
3,3V	7 - BL
GND	8 - GND
3,3V	VCC DS18B20
GPIO4	Data DS18B20 + 4,7kΩ zu VCC
GND	GND DS18B20
Du musst das Display und den DS18B20 so anschließen, wie wir es in den vorherigen Kapiteln gezeigt haben.

Damit die Programme übersichtlicher sind, haben wir diese aufgeteilt. Deswegen ändere hier am Besten nicht die Dateinamen!
    
    
    
Bevor du das Programm uhr.py ausführst, musst du noch die im Temperatursensor erstellten Programme in der Datei ds18b20.py speichern und am Ende die While-Schleife entfernen. Die erstellten Funktionen benutzen wir gleich weiter.

Wenn du damit fertig bist, kannst du jetzt mit sudo python3 uhr.py das Programm starten und auf dem Display sollten jetzt die wichtigen Informationen ausgegeben werden.

Schritt für Schritt Für das gesamte Programm brauchen wir drei Dateien. In display.py wird die gesamte Kommunikation mit dem Display geregelt. Dafür gibt es dort die Funktion anzeige(), der drei Parameter für verschiedene Texte übergeben werden können. Die zweite Datei ist ds18b20.py. Diese macht nichts anderes als die Werte des Temperatursensors auszulesen und diese in Gradzahlen umzuarbeiten. Ganz konkret gibt es dafür die Funktion grad_lesen(). Diese unterscheidet sich fast gar nicht von dem Programm, welches wir vorher benutzt haben. Die dritte Datei heißt uhr.py und erstellt die Uhrzeiten, ruft die Temperatur ab und übergibt alles dem Display. Natürlich könnten wir alles in eine große Datei schreiben, doch diese wird dann unübersichtlich und vor allem müssten wir alles neu schreiben, wenn wir zum Beispiel für ein anderes Programm auch das Display benutzen wollen.

Kommen wir zuerst zur display Funktion. Diese unterscheidet sich nicht groß von der bisherigen Nutzung des Display, außer dass wir jetzt neue Schriftarten benutzen. Dafür haben wir in Zeile 15 folgende Zeile: font = ImageFont.truetype("/home/pi/fonts/BBrick.ttf", 18). Mit der Funktion .truetype() können wir andere Schriftarten als die Standardmäßigen benutzen. Dafür müssen wir als ersten Parameter nur den Pfad zur Schriftart angeben und können dann mit dem zweiten Parameter die Schriftgröße verändern. Deswegen haben wir auch extra neue Schriftarten heruntergeladen. Da wir zweimal einen großen Text und nur einmal einen kleinen Text haben wollen, haben wir auch gleich zwei Variablen mit verschieden großen Schriften erstellt. Die andere große Veränderung ist nur, dass wir eine neue Funktion erstellt haben, der drei Texte als Parameter übergeben werden können, welche dann auf dem Display dargestellt werden.

Das heißt: Bis jetzt war alles simpel, doch in uhr.py gibt es ein paar Neuerungen, die wir vorher noch nicht hatten. Wieder werden in den Zeilen 1 - 4 die benötigten Bibliotheken eingebunden. In Zeile 1 und 2 sollten dir die Bibliotheken und Funktionen bekannt vorkommen, denn diese haben wir gerade erst erstellt. Wenn die Bibliothek nicht im System installiert ist, wie beispielsweise time, dann sucht das Programm die Dateien im selben Ordner. Das heißt, in Zeile 1 sucht es dann die Datei display.py und bindet dann dort die Funktion anzeige() ein. Das .py und die () Klammern müssen dabei nicht angegeben werden.

Wie gesagt wollen wir eine Uhr bauen. Doch dazu brauchen wir noch die aktuelle Uhrzeit. Dafür gibt es Hilfe in der time Bibliothek. Damit die Uhr nicht hängen bleibt, gibt es in Zeile 5 eine While-Schleife, die solange läuft, wie das Programm nicht beendet wird. Da Uhrzeit und Datum in der ganzen Welt unterschiedlich dargestellt wird, gibt es mit time.strftime() eine Möglichkeit, eine Struktur in die Darstellung zu bringen. Im ersten Paramter wird übergeben, welche Daten dargestellt werden sollen. Dafür gibt es die %-Zeichen. %d steht zum Beispiel für den Tag im Monat. In Zeile 8 wird dann am Ende noch das Zeichen für Grad hinzugefügt. In Zeile 9 wird die anzeige() Funktion aufgerufen und die notwendigen Parameter werden übergeben. In Zeile 10 wird dann eine kleine Pause eingefügt. Du kannst diese Pausenzeit auch variieren, weil sich Uhrzeit und Temperatur so schnell nicht verändern.



Format	Bedeutung
%d	Tag im Monat 01 - 31
%m	Monat 01 - 12
%Y	Jahr (vierstellig)
%H	Stunde von 00 - 23
%M	Minute
%S	Sekunde
%u	Wochentag 1 = Montag bis 7 = Sonntag
%U	Nummer der Woche
Jetzt haben wir eine Uhr, aber das coole an den meisten Uhren ist, dass diese nicht über das Terminal gestartet werden müssen. Damit die Uhr immer beim Starten des Pis auch startet, können wir einfach einen Cronjob einrichten. Mit einem Cronjob können wir Programme zu bestimmen Uhrzeiten ausführen.

Bash
$ crontab -e
Wenn du zum ersten Mal ein Crontab konfigurierst, musst du erst einen Editor auswählen. Bei uns ist das Nano, also einfach eine 1 eintippen und Enter drücken.

@reboot sudo python3 /home/pi/uhr.py
Diesen Text musst du ganz am Ende der Datei hinzufügen. Mit @reboot sagst du, dass das Programm beim Starten des Pis gestartet werden soll. Ab da an läuft das Programm immer weiter, was bedeutet, sobald sich der Pi startet, es also eine Stromverbindung gibt, startet sich unsere Uhr.
