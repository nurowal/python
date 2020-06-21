"""
Реализовать функцию, принимающую несколько параметров,описывающих данные пользователя:имя, фамилия, год рождения, город проживания,
 email, телефон.Функция должна принимать параметры как именованные аргументы.Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(first_name: str,
              surname: str,
              year_birth: int,
              city: str,
              e_mail: str,
              phone: int
              ):
    """
    Функция отображает данные о пользователе на экране
    :param name: str
    :param surname: str
    :param year_birth: int
    :param city: str
    :param e_mail: str
    :param phone: int
    :return: str
    """
    return f'{first_name}\n{surname}\n{year_birth} года рождения,\n' \
           f'проживает в городе {city}.\nE-mail : {e_mail}. Телефон +7{phone} '


print(user_data('Василий', 'Ковалев', 1982, 'Челябинск', 'koval82 @ gmail.com', 9966256974))
