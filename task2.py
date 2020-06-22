"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from typing import List, Any, Union

lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# a = [int(i) for i in lst]
# for i in range(1, len(lst)):
#    if a[i] > a[i - 1]:
#        print(a[i])


mask = list(map(lambda x, y: x < y, lst, lst[1:]))
res1 = list(map(lambda x, y: x*y, lst[1:], mask))
res = [itm for itm in res1 if itm!=0]
print(res)
# res = [itm for itm in lst for c in tmp if tmp < 0]
# print([itm for itm in lst if itm < next(lst)])
