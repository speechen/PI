# Die Längen einiger Zeichenketten ermitteln:
a = ['Katze', 'Fenster', 'rauswerfen']
#for x in a:
#    print(x, len(x))
for x in a[:]: # benutze eine Kopie der gesamten Liste
#    if len(x) > 7: a.insert(0, x) # funktioniert nicht damit
     print(x, len(x))