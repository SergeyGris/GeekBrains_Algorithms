"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

from random import randint
from timeit import timeit
from statistics import median

orig_list = [randint(-100, 100) for _ in range(9)]
print(orig_list)
print(median(orig_list))

orig_list = [randint(-100, 100) for _ in range(9)]
# замеры 10
print(
    timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(99)]

# замеры 100
print(
    timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(999)]

# замеры 1000
print(
    timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.001082600000000003
0.008265599999999998
0.07376839999999998
"""
