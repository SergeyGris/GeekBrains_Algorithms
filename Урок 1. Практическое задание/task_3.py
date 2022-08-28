"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
# Алгоритм 1. Когда словарь "прибыль:компания"
companies = {1500: 'Apple', 3000: 'Honor', 2500: 'ICl', 2300: 'Oppo',
             2000: 'Samsung', 1000: 'Sony'}
companies_lst = list(companies.items())  # O(n)
companies_lst.sort()  # O(n log n)
i = 1  # O(1)
for x, y in companies_lst:  # O(n)
    i += 1  # O(1)
    print(f'{y} {x}')  # O(1)
    if i > 3:  # O(1)
        break
#  Сложность: O(n log n), более эффективное, т.к. затрачивает меньше времени


# Алгоритм 2. Когда словарь "компания:прибыль"
companies = {'Sony': 1000, 'Samsung': 2000, 'ICl': 2500, 'Apple': 1500,
             'Honor': 3000, 'Oppo': 2300}


def sort_func1(lst):  # Сложность: O(n^2)
    for i in range(len(lst)):  # O(n)
        num_idx = i
        for j in range(i + 1, len(lst)):  # O(n)
            if lst[j] < lst[num_idx]:  # O(1)
                num_idx = j  # O(1)
        lst[i], lst[num_idx] = lst[num_idx], lst[i]  # O(1)
    return lst[0:3]  # O(1)


def max_income(dic): #O(n)
    new_dict = {y: x for x, y in dic.items()} #O(n)
    max_income_list = sort_func1(list(new_dict.keys())) #O(n)
    for i in max_income_list: #O(n)
        print(f'{new_dict[i]} {i}') #O(1)

#Сложность: O(n^2)
max_income(companies)

