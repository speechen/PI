for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
# Schleife wurde durchlaufen, ohne dass ein Faktor gefunden wurde
         print(n, 'is a prime number')