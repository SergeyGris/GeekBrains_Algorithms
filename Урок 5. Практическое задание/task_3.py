"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
from timeit import timeit

lst = [x for x in range(10 ** 5)]
deque_1 = deque([x for x in range(10 ** 5)])

# append

# def append_list(some_list, n=1000):
#     for i in range(n):
#         some_list.append(i)
#     return some_list


# def append_deque(some_deque, n=1000):
#     for i in range(n):
#         some_deque.append(i)
#     return some_deque
#
#
# print(
#     timeit(
#         f'append_list(lst)',
#         globals=globals(),
#         number=10000))
#
# print(
#     timeit(
#         f'append_deque(deque_1)',
#         globals=globals(),
#         number=10000))
'''
append:
list 1.1112798
deque 0.6797142
'''

# pop
# def pop_list(some_list, n=10):
#     for i in range(n):
#         some_list.pop()
#     return some_list
#
#
# def pop_deque(some_deque, n=10):
#     for i in range(n):
#         some_deque.pop()
#     return some_deque
'''
pop:
list 0.009425099999999992
deque 0.016024499999999997
'''
#
# print(
#     timeit(
#         f'pop_list(lst)',
#         globals=globals(),
#         number=10000))
#
# print(
#     timeit(
#         f'pop_deque(deque_1)',
#         globals=globals(),
#         number=10000))

# popleft
# def popleft_list(some_list, n=10):
#     for i in range(n):
#         some_list.pop(0)
#     return some_list
#
#
# def popleft_deque(some_deque, n=10):
#     for i in range(n):
#         some_deque.pop()
#     return some_deque
#
#
# print(
#     timeit(
#         f'popleft_list(lst)',
#         globals=globals(),
#         number=10000))
#
# print(
#     timeit(
#         f'popleft_deque(deque_1)',
#         globals=globals(),
#         number=10000))

'''
popleft:
list 13.470078899999999
deque 0.011532100000000156
'''

# # Extend
#
# def extend_list(some_list):
#     second_list = [x for x in range(100)]
#     some_list.extend(second_list)
#
#
#
# def extend_deque(some_deque):
#     second_list=[x for x in range(100)]
#     some_deque.extend(second_list)
#
#
# print(
#     timeit(
#         f'extend_list(lst)',
#         globals=globals(),
#         number=10000))
#
# print(
#     timeit(
#         f'extend_deque(deque_1)',
#         globals=globals(),
#         number=10000))

'''
extend:
list 0.1230992
deque 0.05403150000000004
'''

# Extendleft

def extendleft_list(some_list):
    second_list = [x for x in range(100)]
    second_list.extend(some_list)


def extendleft_deque(some_deque):
    second_list=[x for x in range(100)]
    some_deque.extendleft(second_list)


print(
    timeit(
        f'extendleft_list(lst)',
        globals=globals(),
        number=10000))

print(
    timeit(
        f'extendleft_deque(deque_1)',
        globals=globals(),
        number=10000))

'''
extendleft:
list 3.2436902
deque 0.045644999999999936
'''

# find value

def find_list(some_list, n=10**3):
    some_list[n]


def find_deque(some_deque, n=10**3):
    some_deque[n]


print(
    timeit(
        f'find_list(lst)',
        globals=globals(),
        number=10000))

print(
    timeit(
        f'find_deque(deque_1)',
        globals=globals(),
        number=10000))
'''
Поиск элемента:
list 0.0010122999999992999
deque 0.0016346000000000416
'''