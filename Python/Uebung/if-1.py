x = int(input("Please enter an integer: "))
#Please enter an integer: 42
if x < 0:
      x = 0
      print('Negative changed to zero')
elif x == 0:
      print('Zero')
elif x == 1:
      print('Single')
elif x == 5:
      print('fuenf setzen' )
# usw bis else folgt
else:
      print('More')

# Es macht wenig Sinn, wenn nur eine Eingabe erfolgt
#und dann endlos Zahlen eingegeben werden. Kein Abbruch.

#Man koennte einen  Sprungbefehl einbauen, der wieder zu Line 1 springt