"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

simple_dict = {x: y for x, y in
               zip([x for x in range(10000)], [x for x in range(10000)])}
ordered_dict = OrderedDict(
    zip([x for x in range(10000)], [x for x in range(10000)]))


# item

# def items_simple_dict(dct):
#     return dct.items()
#
#
# def items_ordered_dict(dct):
#     return dct.items()
#
#
# print(
#     timeit(
#         f'items_simple_dict(simple_dict)',
#         globals=globals(),
#         number=10000))
#
# print(
#     timeit(
#         f'items_ordered_dict(ordered_dict)',
#         globals=globals(),
#         number=10000))
#
'''
item
simple_dict 0.001240100000000001
ordered_dict 0.002021999999999996
'''

# def get_simple_dict(dct):
#     return dct.get(500)
#
#
# def get_ordered_dict(dct):
#     return dct.get(500)
#
#
# print(
#     timeit(
#         f'get_simple_dict(simple_dict)',
#         globals=globals(),
#         number=10000))
#
# print(
#     timeit(
#         f'get_ordered_dict(ordered_dict)',
#         globals=globals(),
#         number=10000))
#
'''
get
simple_dict 0.0023929999999999993
ordered_dict 0.0021148
'''

# def update_simple_dict(dct):
#     return dct.update({x: y for x, y in
#                zip([x for x in range(100)], [x for x in range(100)])})
#
#
# def update_ordered_dict(dct):
#     return dct.update(zip([x for x in range(100)], [x for x in range(100)]))
#
#
# print(
#     timeit(
#         f'update_simple_dict(simple_dict)',
#         globals=globals(),
#         number=10000))
#
# print(
#     timeit(
#         f'update_ordered_dict(ordered_dict)',
#         globals=globals(),
#         number=10000))
#
'''
update
simple_dict 0.1125903
ordered_dict 0.11686299999999997
'''

# def pop_simple_dict(dct):
#     dct.pop(500)
#     return
#
#
# def pop_ordered_dict(dct):
#     return dct.pop(500)
#
#
# print(
#     timeit(
#         f'pop_simple_dict(simple_dict)',
#         globals=globals(),
#         number=1))
#
# print(
#     timeit(
#         f'pop_ordered_dict(ordered_dict)',
#         globals=globals(),
#         number=1))
#
'''
pop
simple_dict 1.799999999996249e-06
ordered_dict 2.5000000000025002e-06
'''

def popitem_simple_dict(dct):
    dct.popitem()
    return


def popitem_ordered_dict(dct):
    return dct.popitem()


print(
    timeit(
        f'popitem_simple_dict(simple_dict)',
        globals=globals(),
        number=10000))

print(
    timeit(
        f'popitem_ordered_dict(ordered_dict)',
        globals=globals(),
        number=10000))

'''
popitem
simple_dict 0.0014100000000000015
ordered_dict 0.0020000000000000018
'''

'''
На мой взгляд ordereddict работает чуть медленне, чем обычный словарь. 
Преимущество оказалось только в  поиске элемента
'''