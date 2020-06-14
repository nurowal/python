"""4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
   Для решения используйте цикл while и арифметические операции."""
integer_number = int(input('Введите целое положительное число n:'))
s=1
k=integer_number
l=integer_number
max=0
while k//10 != 0:
  s+=1
  k=k//10
for i in range (1,s+1):
  m=l%(10)
  l=l//(10)
  if m>max:
     max=m
  if max == 9:
     max=9
     break
print('Наибольшая цифра в числе :', max)