"""Реализовать функцию my_func(),которая принимает три
    позиционных аргумента,и возвращает сумму наибольших двух аргументов."""


def my_func(x, y, z):
    return max(x + y, y + z, x + z)
"""
    Функция возвращает сумму наибольших двух аргументов
    :param x: str
    :param y: str
    :param z: int

"""


print(my_func(10000, 20000, 30))
print(my_func(100, 20000, 30))
print(my_func(100, 20, 3000))
print(my_func(1, 20000, 300))
