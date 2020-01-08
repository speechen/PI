     #Zeitstempel erzeugen
     #now = str(time.localtime("%d.%m.%Y %H:%M:%S"))
     #now=time.localtime()
     #print("Datum:",now.tm_mday,".",now.tm_mon,".",now.tm_year,"  Zeit:",now.tm_hour,":", now.tm_min,":", now.tm_sec)

     # aus now werden die folgenden Variablen ausgewertet und als str gespeichert in tag mon usw.

     # in zeit und dat werden formatiert Zeit und Datum gespeichert.
     #zeit= ("  Zeit: " + st +":"+mi+":"+se)
     #dat = ("  Datum: "+tag + "."+ mon + "."+ ya )
     # erzeugen von str

     tag = str(now.tm_mday)
     mon = str(now.tm_mon)
     ya  = str(now.tm_year)
     st  = str(now.tm_hour)
     mi  = str(now.tm_min)
     se  = str(now.tm_sec)