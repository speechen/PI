# funktioniert nicht!!!!
# durch einfuegen von print wird f100 ausgegeben.


def fib2(n): # gibt die Fibonacci-Folge bis  n zurück

     """Return a list containing the Fibonacci series up to n.""" # Drei Anfuerungszeiechen?? Tun nichts? Stimmt!!!
     result = list()
     a, b = 0, 1
     while a < n:
         result.append(a)    # siehe unten
         a, b = b, a + b
     return result

f100 = fib2(100)    # ruf es auf
print(f100)                # gib nun auch das Ergebnis aus

"""Beispiel 7.7. Verwendung der return-Anweisung (funk_return.py)

                
#!/usr/bin/python

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

print maximum(2, 3)
                
                

Ausgabe
                
$ python funk_return.py
3
                
                
So funktioniert es
Die Funktion maximum gibt als Wert das Maximum ihrer Parameter zurück.
In diesem Fall sind dies Zahlen, die der Funktion als Argumente übergeben werden.
In der Funktion wird eine einfache if..else-Anweisung benutzt, um den größeren Wert zu finden,
und dieser Wert wird dann mit return zurückgegeben.

Beachten Sie, dass eine return-Anweisung ohne Wert gleichbedeutend ist mit return None.
None ist ein besonderer Datentyp in Python, der einfach für Nichts steht.
Man benutzt ihn zum Beispiel, um anzuzeigen, dass eine Variable keinen speziellen Wert hat,
wenn sie den Wert None besitzt.

Jede Funktion hat am Ende implizit die Anweisung return None, wenn Sie nicht stattdessen
Ihre eigene return-Anweisung geschrieben haben. Sie können das ausprobieren, indem Sie
print eineFunktion() ausführen, wobei eineFunktion eine Funktion ohne return-Anweisung sein soll, etwa:

"""
"""Die Anweisung result.append(a) ruft eine Methode des Listenobjektes in result auf.
Eine Methode ist eine Funktion, die zu einem Objekt ‘gehört’ und wird mittels Punktnotation (obj.methodname) dargestellt.
Dabei ist obj irgendein Objekt (es kann auch ein Ausdruck sein) und methodname der Name einer Methode, die vom Typ des Objektes definiert wird.
Unterschiedliche Typen definieren verschiedene Methoden. Methoden verschiedener Typen können denselben Namen haben ohne doppeldeutig zu sein.
(Es ist auch möglich, eigene Objekttypen zu erstellen, indem man Klassen benutzt, siehe Klassen.)
Die Methode append(), die im Beispiel gezeigt wird, ist für Listenobjekte definiert. Sie hängt ein neues Element an das Ende der Liste an.
Im Beispiel ist es äquivalent zu result = result + [a], aber effizienter."""