import time, locale
locale.setlocale(locale.LC_ALL, '')

now = time.localtime()
print("Tag:", now.tm_mday)
print("Monat:", now.tm_mon)
print("Jahr:", now.tm_year)
print("Stunde:", now.tm_hour)
print("Minute:", now.tm_min)
print("Sekunde:", now.tm_sec)
print("Wochentag:", now.tm_wday)  # Montag = 0
print("Tag des Jahres:", now.tm_yday)
print("Sommerzeit:", now.tm_isdst)  # Sommerzeit: 1; Winterzeit: 0

print("Datum:",now.tm_mday,".",now.tm_mon,".",now.tm_year,"  Zeit:",now.tm_hour,":", now.tm_min,":", now.tm_sec)