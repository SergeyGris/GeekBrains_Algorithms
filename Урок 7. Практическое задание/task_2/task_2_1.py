"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

import math
from random import randint
from timeit import timeit


# Сортировка Шелла
def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return array


orig_list = [randint(-100, 100) for _ in range(9)]
print(orig_list)
rez = shellSort(orig_list)
print(rez)
print(f' Медиана: {rez[4]}')

# замеры 10
orig_list = [randint(-100, 100) for _ in range(9)]
print(
    timeit(
        "shellSort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "shellSort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "shellSort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.0058729
0.12840100000000002
2.1127818
"""


# Сортировка кучей

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


orig_list = [randint(-100, 100) for _ in range(9)]
print(orig_list)
rez = heapSort(orig_list)
print(rez)
print(f' Медиана: {rez[4]}')

orig_list = [randint(-100, 100) for _ in range(10)]
# замеры 10
print(
    timeit(
        "heapSort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit(
        "heapSort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit(
        "heapSort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
0.014110899999999926
0.22097140000000026
3.9141354999999995
"""
