"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""

import collections
import functools


class HexOperation():
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16)
                        + int(''.join(other.second_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16) * int(
            ''.join(other.second_num), 16)))[2:]


hex_num_first = list(input("Первое число:"))
hex_num_second = list(input("Второе число:"))

res_sum = HexOperation(hex_num_first, hex_num_second) + HexOperation(
    hex_num_first, hex_num_second)

res_mul = HexOperation(hex_num_first, hex_num_second) * HexOperation(
    hex_num_first, hex_num_second)
print(f'Сумма: {res_sum}, Произведение: {res_mul}')
