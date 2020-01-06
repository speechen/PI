def fib(n):    # die Fibonacci-Folge bis n ausgeben
     """Print the Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a,b = b, a+b
     print()
# fuer end kann man mit Leerzeichen den Abstand regeln oder einen String dazu setzen, end='  ' 2 Leerzeichen dazwischen
# Jetzt rufen wir die Funktion auf, die wir gerade definiert haben:
fib(2000)
# oder danach noch
fib(3000) # addieren geht nicht    + fib(4000)

# Man kann die Funktion immer wieder aufrufen.

# fib wird an f uebergeben.
#   <function fib at 10042ed0> was das soll ist unklar. So in Tutorial
f = fib
f(100)