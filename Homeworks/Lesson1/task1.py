""" 1.Поработайте с переменными, создайте несколько, выведите на экран,
    запросите у пользователя несколько чисел и строк
    и сохраните в переменные, выведите на экран"""
var_int = 1
var_float = 3.1416
var_str = 'To be or not to be'
var_boolean = False
print(var_int,type(var_int))
print(var_float,type(var_float))
print(var_str,type(var_str))
print(var_boolean,type(var_boolean))
n_int=2
n_str=3
while n_int !=0 or n_str!=0:
    request = f'Введите {n_int} числа и {n_str} строки :'
    user_answer = input(request)
    if user_answer.isdigit():
        a=user_answer
        print ('Вы ввели целое число',a)
        n_int -= 1
        if n_int<0 :
            n_int +=1
            print ('Числа ввели . Хватит. Пора строки')
    else:
        b = user_answer
        print ('Вы ввели строку',b)
        n_str -= 1
        if n_str < 0:
            n_str += 1
            print('Строки ввели . Хватит. Пора числа')