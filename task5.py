"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
    должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
    и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
    Но если вместо числа вводится специальный символ, выполнение программы завершается.
    Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
    чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_sum(*args):
    result = 0
    exit_flag = False
    for item in args:
        try:
            result += float(item)
        except ValueError as e:
            if item == 'q':
                exit_flag = not exit_flag
                break
    return result, exit_flag


user_sum = 0
user_exit = False
while not user_exit:
    user_input = input('введите числа через пробел\n').split(' ')
    print(user_input)
    result_summ, user_exit = my_sum(*user_input)
    user_sum += result_summ
    print(f'сумма: {user_sum}')
