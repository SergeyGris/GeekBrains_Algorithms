"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(lst):
    return [lst.index(i) for i in lst if i % 2 == 0]


lst1 = [i for i in range(1000)]
print(
    timeit(
        'func_1(lst1[:])', globals=globals(), number=1000
    )
)

lst1 = [i for i in range(1000)]
print(
    timeit(
        'func_2(lst1[:])', globals=globals(), number=1000
    )
)

lst1 = [i for i in range(10000)]
print(
    timeit(
        'func_1(lst1[:])', globals=globals(), number=1000
    )
)

lst1 = [i for i in range(10000)]
print(
    timeit(
        'func_2(lst1[:])', globals=globals(), number=1000
    )
)

'''
Заполнение списка с помощью list comprehension происходит быстрее.
для сравнения прямое добавление: 
1000 элементов
0.13889569999999998

с  list comprehension:
0.07439049999999997

10000 элементов

1.5939658

с  list comprehension:
0.7813341

'''
