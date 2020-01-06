total_sum = 0
a = int(input())
while a != 0:
     total_sum += a
     if total_sum >= 21:
         print('Total sum is', total_sum)
         break
     a = int(input())
else:
     print('Total sum is less than 21 and is equal to', total_sum, '.')