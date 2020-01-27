# Schreibe hier Deinen Code :-)
a , b = 0 , 1
while b<100:
    print('b = ' , b )
    a , b = b , a+b

while b<10000:
    print('b = ' , b , a )
    a , b = b , a+b

while b<100000000:
    print(b, end='  =  ' )
    a , b = b , a+b

x = int(input())

if x < 0:
    x = 0
    print('Negative changed to zero')
    print(x)
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    print(x)