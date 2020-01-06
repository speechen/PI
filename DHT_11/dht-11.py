import time, locale
import Python_DHT
locale.setlocale(locale.LC_ALL, '')
sensor = Python_DHT.DHT11
pin = 22

i = 1
temperatur = 40
while temperatur < 120:
     feuchtigkeit, temperatur = Python_DHT.read_retry(sensor, pin)
     #Zeitstempel erzeugen
     now = time.localtime()
     print("Datum:",now.tm_mday,".",now.tm_mon,".",now.tm_year,"  Zeit:",now.tm_hour,":", now.tm_min,":", now.tm_sec)
     print ( " es wird gemessen " )
     time.sleep(60)
     print("Temperatur = " + str(temperatur)+" C ,    Feuchtigkeit = " + str( feuchtigkeit)+" %",)
     f_in = open('/media/pi/Scandisk/PI/DHT_11/text.txt')
     f_out = open('/media/pi/Scandisk/PI/DHT_11/text.txt', 'a')
     # aus now werden die folgenden Variablen ausgewertet und als str gespeichert in tag mon usw.
     tag = str(now.tm_mday)
     mon = str(now.tm_mon)
     ya  = str(now.tm_year)
     st  = str(now.tm_hour)
     mi  = str(now.tm_min)
     se  = str(now.tm_sec)
     # in zeit und dat werden formatiert Zeit und Datum gespeichert.
     zeit= ("  Zeit: " + st +":"+mi+":"+se)
     dat = ("  Datum: "+tag + "."+ mon + "."+ ya )
     # erzeugen von str
     s = str ( temperatur)
     t = str ( feuchtigkeit)
     u = str (i)
     v = '  temperatur = '
     w = '  feuchtigkeit = '
     # Zeielenvorschub
     c = " \n "
     #Variablen schreiben in Datei
     f_out.write(c)
     f_out.write(u)
     f_out.write(dat)
     f_out.write(zeit)
     f_out.write(v)
     f_out.write(s)
     f_out.write(w)
     f_out.write(t)

     i = i + 1

     f_in.close()
     f_out.close()