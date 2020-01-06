import time, locale
locale.setlocale(locale.LC_ALL, '')


#new = time.localtime(timestamp)
now = time.localtime()
print(time.strftime( now)


tag = str(now.tm_mday)
mon = str(now.tm_mon)
ya  = str(now.tm_year)
st  = str(now.tm_hour)
mi  = str(now.tm_min)
se  = str(now.tm_sec)
zeit= ("  Zeit: " + st +":"+mi+":"+se)
dat = ("  Datum: "+tag + "."+ mon + "."+ ya )
print(zeit,dat)