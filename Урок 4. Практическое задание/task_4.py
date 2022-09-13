"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())


def func_3(lst):
    dct = {i: lst.count(i) for i in set(lst)}
    max_num = lst[0]
    for i in set(lst):
        if dct[i] > dct[max_num]:
            max_num = dct[i]
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {dct[max_num]} раз(а)'


def func_4(array):
    num=max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'

print(func_3(array))

print(
    timeit.timeit(
        f'func_1()',
        globals=globals(),
        number=10000))

print(
    timeit.timeit(
        f'func_2()',
        globals=globals(),
        number=10000))

print(
    timeit.timeit(
        f'func_3(array)',
        globals=globals(),
        number=10000))
print(
    timeit.timeit(
        f'func_4(array)',
        globals=globals(),
        number=10000))

'''
Функция 1 с помощью counter
0.013025099999999998

функция 2 с помощью max
0.015637399999999996

Функция 3 с помощью словаря
0.019162699999999998

Конечно же, мой вариант самый долгий, т.к. на создане словаря используется
большее время

функция 4 с помощью max
0.010248999999999994

'''