"""4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
   Для решения используйте цикл while и арифметические операции."""
str_number = input('Введите целое положительное число n:')
if str_number.isdigit():
    str_digit = '9'
    k = int(str_digit)
    while str_number.find(str_digit) == -1:
        k -= 1
        str_digit = str(k)
    print('Самая большая цифра в числе ', k)
else : print('Ошибочный ввод')