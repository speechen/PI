#4.7.2. Schlüsselwortargumente ( keine Ahnung wies tut)
#Funktionen können auch mit Schlüsselwortargumenten in der Form   Schlüsselwort=Wert   aufgerufen werden. Zum Beispiel die folgende Funktion:
"""keyword argument
Argumente, denen ein variable_name= im Aufruf vorausgeht. Der Variablenname bestimmt den lokalen Namen der Funktion,
dem der Wert zugewiesen wird. ** wird benutzt um ein Dictionary von Schlüsselwort-Argumenten zu übergeben
oder zu akzeptieren. Siehe argument."""
"""
argument
Ein Wert, der einer Funktion oder Methode übergeben wird und einer benannten lokalen Variable im Funktionsrumpf zugewiesen
wird. Eine Funktion oder Methode kann sowohl Positions-, als auch Schlüsselwort-Argumente in ihrer Definition haben.
Positions- und Schlüsselwort-Argumente können von variabler Länge sein: * akzeptiert (falls in der Funktionsdefinition)
oder übergibt (im Funktionsaufruf) mehrere Positionsargumente in einer Liste, während ** dasselbe für
Schlüsselwort-Argumente in einem Dictionary leistet.

Jeder Ausdruck kann innerhalb der Argumentliste benutzt werden und der ausgewertete Wert wird an die lokale Variable
übergeben."""


def parrot(voltage='völlig steif',action='fliegen',type='norwegische Blauling'):
     print("-- Der Vogel würde selbst dann nicht",action, end=' ')
     print("selbst wenn Sie ihm ",voltage, "Volt durch den Schnabel jagen täten")
     print("-- Ganz erstaunlicher Vogel, der", type, "! Wunderhübsche Federn!")
     print("-- Er is",state, "!")

#mindestens ein Argument (voltage) akzeptiert drei optionale Argumente (state, action und type) und kann mit allen folgenden Varianten aufgerufen werden:

#parrot(4000)
#parrot(action = 'VOOOOOM', voltage = 1000000)
#parrot('Viertausend', state = 'an den Gänseblümchen riechen')
#parrot('eine Million', 'keine Spur leben', 'springen')
#die folgenden Aufrufe wären allerdings alle ungültig:

#parrot()                     # das benötigte Argument fehlt
#parrot(voltage=5.0, 'tot')   # auf ein Schlüsselwortargument folgt ein normales
#parrot(110, voltage=220)     # doppelter Wert für ein Argument
#parrot(actor='John Cleese')  # unbekanntes Schlüsselwort


#Bei einem Funktionsaufruf müssen Schlüsselwortargumente nach positionsabhängigen Argumenten kommen.
#Alle übergebenen Schlüsselwortargumente müssen jeweils auf eines der Argumente passen, die die Funktion akzeptiert
#(beispielsweise ist actor kein gültiges Argument für die parrot Funktion), wobei ihre Reihenfolge aber unwichtig ist.
#Das gilt auch für nicht-optionale Argumente (beispielsweise ist parrot(voltage=1000) auch gültig).
#Kein Argument darf mehr als einen Wert zugewiesen bekommen. Ein Beispiel, das wegen dieser Einschränkung scheitert:

""" Anfang Text
def function(a):
     pass

function(0, a=0)
Traceback (most recent call last):
 File "<stdin>", line 1, in ?
TypeError: function() got multiple values for keyword argument 'a'
Ist ein Parameter der Form **name in der Definition enthalten, bekommt dieser ein Dictionary (siehe Mapping Types),
das alle Schlüsselwortargumente enthält, bis auf die, die in der Definition vorkommen.
Dies kann mit einem Parameter der Form *name, der im nächsten Unterabschnitt beschrieben wird,
kombiniert werden. Dieser bekommt ein Tupel, das alle positionsabhängigen Argumente enthält,
die über die Anzahl der definierten hinausgehe. (*name muss aber vor **name kommen.)
Wenn wir zum Beispiel eine Funktion wie diese definieren:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Haben sie", kind, "?")
    print("-- Tut mir leid,", kind, "ist leider gerade aus.")
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])
könnte sie so aufgerufen werden:

cheeseshop("Limburger", "Der ist sehr flüssig, mein Herr.",
          "Der ist wirklich sehr, SEHR flüssig, mein Herr.",
          shopkeeper="Michael Palin",
          client="John Cleese",
          sketch="Cheese Shop Sketch")
und natürlich würde sie folgendes ausgeben:

-- Haben sie Limburger ?
-- Tut mir leid, Limburger ist leider gerade aus.
Der ist sehr flüssig, mein Herr.
Der ist wirklich sehr, SEHR flüssig, mein Herr.
----------------------------------------
client : John Cleese
shopkeeper : Michael Palin
sketch : Cheese Shop Sketch
Man beachte, dass die Liste der Schlüsselwortargumente erzeugt wird, indem das Ergebnis der Methode keys() sortiert wird,
bevor dessen Inhalt ausgegeben wird. Tut man das nicht, ist die Reihenfolge der Ausgabe undefiniert.

Ende Text
"""