# Bisher keine Ahnung warum die Ausgabe so erfolgt.
# hatte nicht bedacht, dass man auf die Ausgabe mit ja oder nein antworten muss.

def ask_ok(prompt, retries=4, complaint='Bitte Ja oder Nein!'):
   while True:
       ok = input(prompt)
       if ok in ('j', 'J', 'ja', 'Ja'): return True
       if ok in ('n', 'N', 'ne', 'Ne', 'Nein'): return False
       retries = retries - 1
       if retries < 0:
           raise IOError('Benutzer abgelehnt!')
       print(complaint)

ask_ok("Willst du wirklich aufhören?")

ask_ok("Willst du die Datei überschreiben?", 2)

ask_ok("Willst du die Datei überschreiben?", 2, "Komm schon, nur Ja oder Nein")


# Anfang der Erlaueterungen, ev. code nach oben uebernehmen.
"""Das Beispiel führt auch noch das Schlüsselwort in ein. Dieses überprüft ob ein gegebener Wert in einer Sequenz gegeben ist.

Die Standardwerte werden zum Zeitpunkt der Funktionsdefinition im definierenden Gültigkeitsbereich ausgewertet, so dass:

i = 5

def f(arg=i):
   print(arg)

i = 6
f()
5 ausgeben wird.

Wichtige Warnung: Der Standardwert wird nur einmal ausgewertet. Das macht einen Unterschied, wenn der Standardwert veränderbares Objekt,
wie beispielsweise eine Liste, ein Dictionary oder Instanzen der meisten Klassen, ist.
Zum Beispiel häuft die folgende Funktion alle Argumente an, die ihr in aufeinanderfolgenden Aufrufen übergeben wurden:

def f(a, L=[]):
   L.append(a)
   return L

print(f(1))
print(f(2))
print(f(3))
Und sie gibt folgendes aus:

[1]
[1, 2]
[1, 2, 3]
Wenn man nicht will, dass der Standardwert von aufeinanderfolgenden Aufrufen gemeinsam benutzt wird,
kann man die Funktion folgendermaßen umschreiben:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

Ende Text"""
# Achtung:
"""Wichtige Warnung: Der Standardwert wird nur einmal ausgewertet. Das macht einen Unterschied, wenn der Standardwert veränderbares Objekt, wie beispielsweise eine Liste, ein Dictionary oder Instanzen der meisten Klassen, ist. Zum Beispiel häuft die folgende Funktion alle Argumente an, die ihr in aufeinanderfolgenden Aufrufen übergeben wurden:

def f(a, L=[]):
   L.append(a)
   return L

print(f(1))
print(f(2))
print(f(3))
Und sie gibt folgendes aus:

[1]
[1, 2]
[1, 2, 3]
Wenn man nicht will, dass der Standardwert von aufeinanderfolgenden Aufrufen gemeinsam benutzt wird, kann man die Funktion folgendermaßen umschreiben:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
Ende"""