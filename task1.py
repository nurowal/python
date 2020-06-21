"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def my_division(var_int1: float,
                var_int2: float):
    """
        делит а на b
        :param var_int1:
        :param var_int2:
        :return: float
        """
    try:
        return var_int1 / var_int2
    except ZeroDivisionError as e:
        print("На ноль делить нельзя")


print(my_division(0, 10))
print(my_division(100, 2000))
print(my_division(100, 0))
