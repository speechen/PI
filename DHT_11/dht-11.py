import time, locale
import Python_DHT
import RPi.GPIO as GPIO

sensor = Python_DHT.DHT11
pin = 22

i = 1
temperatur = 40
while temperatur < 120:
     feuchtigkeit, temperatur = Python_DHT.read_retry(sensor, pin)
     r=str(time.strftime("%d.%m.%Y"))
     s=str(time.strftime("%H:%M:%S"))
     print ( " es wird im Abstand von 15 min gemessen " )
     time.sleep(900)
     print(r+"  "+"   Temperatur = " + str(temperatur)+" C ,     Feuchtigkeit = " + str( feuchtigkeit)+" %",)
     f_out = open('/media/pi/Scandisk/PI/DHT_11/excel.cvs', 'a')
     t = str ( temperatur)
     f = str ( feuchtigkeit)
     u = str (i)
     v = '  temperatur'
     w = '  feuchtigkeit'
     g = '  feinstaub 2.5 '
     h = '  feinstaub 10 '
     k = str(10)
     l = str(2.5)
     c = " \n "
     d = "\t  "

     wri = (u+d+r+d+s+d+v+d+t+d+w+d+f+d+g+d+h+d+k+d+l+c)
     f_out.write(wri)
     i = i + 1
     f_out.close()