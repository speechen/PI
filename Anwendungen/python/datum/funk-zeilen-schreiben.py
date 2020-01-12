import time,calendar,datetime
import Python_DHT
sensor = Python_DHT.DHT11
pin = 22

i = 1
temperatur = 40
while temperatur < 120:
     feuchtigkeit, temperatur = Python_DHT.read_retry(sensor, pin)
     print ( " es wird gemessen " )
     time.sleep(240)
     print("Temperatur = " + str(temperatur)+" C ,    Feuchtigkeit = " + str( feuchtigkeit)+" %",)

     f_in = open('/media/pi/Scandisk/PI/DHT_11/text.txt')
     f_out = open('/media/pi/Scandisk/PI/DHT_11/text.txt', 'a')
     s = str ( temperatur)
     t = str ( feuchtigkeit)
     u = str (i)
     v = '  temperatur = '
     w = '  feuchtigkeit = '
     c = " \n "
     f_out.write(c)
     f_out.write(u)
     f_out.write(v)
     f_out.write(s)
     f_out.write(w)
     f_out.write(t)

     i = i + 1
     f_in.close()
     f_out.close()