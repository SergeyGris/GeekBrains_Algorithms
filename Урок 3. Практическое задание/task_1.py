"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def time_diff(function):
    def time_stamp(*args):
        start = time.perf_counter_ns()
        markup = function(*args)
        stop = time.perf_counter_ns()
        print(f'Затрачено времени: {stop - start}\n')
        return markup

    return time_stamp


# заполнение списка O(n)
@time_diff
def list_input(from_list):
    print('# заполнение списка')
    return [x for x in from_list]


list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
          14, 15, 16, 17, 18, 19, 20]
list_2 = list_input(list_1)


#  Заполнение словаря O(n)
@time_diff
def dict_input(keys, values):
    print('# Заполнение словаря O(n)')
    return {key: value for key, value in zip(keys, values)}


dict1 = dict_input(list_1, list_2)

"""
# заполнение списка методом insert
Затрачено времени: 46500

# Заполнение словаря 
Затрачено времени: 24200

при заполнении списка затрачено больше времени, не смотря на одинаковую 
сложность и хэширование ключей словаря

"""


# Получение элемента списка O(1)
@time_diff
def list_get(from_list, n):
    print('# Получение элемента списка O(1)')
    return from_list[n]


list_get(list_1, int(len(list_1) / 2))


#  Получение элемента словаря O(1)
@time_diff
def dict_get(from_dict, key):
    print('# Получение элемента словаря O(1)')
    return from_dict.get(key)


dict_get(dict1, 10)

"""
# Получение элемента списка O(1)
Затрачено времени: 14000

# Получение элемента словаря O(1)
Затрачено времени: 13700


Получение элемента по ключу словаря происходит быстрее, хотя сравнительно
небольшое различие во времени, скорее всего связанное с 
малым количеством элементов - 20

"""


# Удаление элемента списка методом pop O(n)
@time_diff
def list_pop(from_list):
    print('# Удаление элемента списка методом pop O(n)')
    while len(from_list) > 0:
        from_list.pop()


list_3 = list_1.copy()
list_pop(list_3)


# Удаление элемента списка по номеру O(n)
@time_diff
def list_del(from_list, n):
    print('# Удаление элемента списка по номеру O(n)')
    return from_list.remove(from_list[n])


list_3 = list_1.copy()
list_del(list_3, int(len(list_3) / 2))


# Удаление элемента словаря pop O(1)
@time_diff
def dict_pop(from_dict):
    print('# Удаление элемента словаря pop O(1)')
    while len(from_dict) > 0:
        from_dict.popitem()


dict2 = dict_input(list_1, list_2)

dict_pop(dict2)


# Удаление элемента словаря по ключу O(1)
@time_diff
def dict_del(from_dict, key):
    print('# Удаление элемента словаря по ключу O(1)')
    from_dict.pop(key)
    return from_dict


dict_del(dict1, 10)
"""
# Удаление элемента списка методом pop O(n)
Затрачено времени: 25200

# Удаление элемента списка по номеру O(n)
Затрачено времени: 16800

# Удаление элемента словаря pop O(1)
Затрачено времени: 18800

# Удаление элемента словаря по ключу O(1)
Затрачено времени: 11000


Удаление элементов словаря обоими способами происходит быстрее, 
т.к. не алгоритм не проходит полный список элементов при каждой итерации

"""