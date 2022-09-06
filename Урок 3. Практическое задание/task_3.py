"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib

def substring(st):
    rez = set()
    for i in st:

        hash_obj = hashlib.sha256(st.encode('utf-8'))
        hash_hexdig_obj = hash_obj.hexdigest()
        rez.add(hash_hexdig_obj)
        a = st.split(i, 1)
        for j in a:
            if j!='':
                hash_obj = hashlib.sha256(j.encode('utf-8'))
                hash_hexdig_obj = hash_obj.hexdigest()
                rez.add(hash_hexdig_obj)
                rez.add(hash_hexdig_obj)

    return len(rez)


st='abcd'
print(f'{st} - {substring(st)} уникальных подстрок')
