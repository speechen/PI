"""4.3. Die Funktion range()
Wenn man wirklich über eine Zahlenfolge iterieren muss, bietet sich die eingebaute Funktion range() an,
die arithmetische Folgen erzeugt."""

for i in range(5):
     print(i)
     print()

"""Ergebniss:
0
1
2
3
4
Wird nur ein Argument angegeben, so beginnt der erzeugte Bereich bei Null und endet mit dem um 1 kleineren
Wert des angegebenen Arguments. range(10) erzeugt die Zahlen von 0 bis einschließlich 9.
Das entspricht den gültigen Indizes einer Sequenz mit zehn Elementen. Es ist ebenfalls möglich,
den Bereich mit einem anderen Wert als Null zu beginnen oder auch eine bestimmte Schrittweite (step) festzulegen —
sogar negative Schrittweiten sind möglich."""

for i in range(5,10):
     print(i)


for i in range(0, 10, 3):
     print(i)
     print()

# Ergebniss   0, 3, 6, 9

for i in range(-10, -100, -30):
     print(i)

#  -10, -40, -70
#Will man über die Indizes einer Sequenz iterieren( MATHEMATIK•EDV wiederholen, eine Iteration (2) vornehmen),
#kann man range() und len() wie folgt kombinieren:

a = ['Mary', 'hatte', 'ein', 'kleines', 'Lamm']
for i in range(len(a)):
     print(i, a[i])

"""Ergebniss:
0 Mary
1 hatte
2 ein
3 kleines
4 Lamm
Eleganter ist es jedoch, in solchen Fällen die Funktion enumerate() zu benutzen, siehe unter 5.6 Schleifentechnik  """