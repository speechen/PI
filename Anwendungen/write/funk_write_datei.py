import time, locale
locale.setlocale(locale.LC_ALL, '')

     r=str(time.strftime("%d.%m.%Y %H:%M:%S"))
     s = str ( temperatur)
     t = str ( feuchtigkeit)
     u = str (i)
     v = '  temperatur = '
     w = '  feuchtigkeit = '

     # Zeielenvorschub
     c = " \n "
     d = "\t  "
     #Variablen schreiben in Datei
     f_out.write(c)
     f_out.write(u)
     f_out.write(d)
     f_out.write(r)
     f_out.write(v)
     f_out.write(s)
     f_out.write(w)
     f_out.write(t)
     i = i + 1