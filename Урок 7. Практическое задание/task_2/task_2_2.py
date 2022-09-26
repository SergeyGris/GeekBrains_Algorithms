"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit

orig_list = [randint(-100, 100) for _ in range(9)]


def median(array):
    array_sum = sum(array)
    while len(array) > 1:
        min_el = min(array)
        max_el = max(array)
        array_sum -= max_el
        array_sum -= min_el
        array.pop(array.index(min_el))
        array.pop(array.index(max_el))
    return array[0]


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
0.006281400000000006
0.1363145
10.751290099999999
"""
