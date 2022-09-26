"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для четвертого скрипта
"""
from memory_profiler import profile
import sys

sys.setrecursionlimit(2000)


# до оптимизации
@profile
def odd_even_func(i, odd=0, even=0):
    if i // 10 < 1:
        even += 1
        return even, odd
    j = i % 10
    i = i // 10
    if j % 2 == 0:
        odd += 1
    else:
        even += 1
    return odd_even_func(i, odd, even)


num = 12315465123546546512315131517897879846546549879875346531321651897987 * 99
odd, even = odd_even_func(num)
print(f'Четных: {odd}, нечетных: {even}')

sys.setrecursionlimit(1000)


# После оптимизации
@profile
def odd_even_func2(i):
    even, odd = 0, 0

    while i // 10 >= 1:
        even += 1
        j = i % 10
        i = i // 10
        if j % 2 == 0:
            odd += 1
        else:
            even += 1
    return odd, even


num = 12315465123546546512315131517897879846546549879875346531321651897987 * 99
odd, even = odd_even_func2(num)
print(f'Четных: {odd}, нечетных: {even}')

'''
Наверно с помощью цикла более экономично по памяти. четсно говоря,
у меня не получилось увидить разницу в профиле рекурсии и цикла. 

'''
