"""
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(var_str: str):
    var_str = "{0}{1}".format(var_str[:1].upper(), var_str[1:])
    return var_str

def user_temp(var_str: str):
    return ' '.join(list(map(int_func, var_str.split(' '))))

print(user_temp("hsdgg jsdkjsdjkjas asldihjkb oqwejmnsm, ksldlk"))