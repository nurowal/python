"""
Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.

"""


def int_func(var_str: str):
    var_str = "{0}{1}".format(var_str[:1].upper(), var_str[1:])
    return var_str


print(int_func('adfgfdhdshab'))
