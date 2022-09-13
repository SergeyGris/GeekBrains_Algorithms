"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return int("".join(reversed(str(enter_num))))


num = 984654321898754621

print(
    timeit.timeit(
        f'revers_1({num})',
        globals=globals(),
        number=10000))

print(
    timeit.timeit(
        f'revers_2({num})',
        globals=globals(),
        number=10000))

print(
    timeit.timeit(
        f'revers_3({num})',
        globals=globals(),
        number=10000))

print(
    timeit.timeit(
        f'revers_4({num})',
        globals=globals(),
        number=10000))

'''
Значения замеров времени:
1. Рекурсия
0.038807699999999994
2.Цикл
0.024506
3. Срез
0.0028006999999999893
4. reversed +join
0.0079544

Самая быстрая функция оказалась с использованием срезов, т.к. она проходит 
число с конца, не вызывая дополнительных функций. Сложность в данном случае будет 
O(n).
'''
