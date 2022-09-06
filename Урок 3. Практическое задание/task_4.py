"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib


class UrlCache():
    def __init__(self):
        self.cache = {}

    def cache_url(self, url):
        if self.cache.get(url, False):
            return print(self.cache.get(url))

        else:
            url_hash = hashlib.sha512(url.encode('utf-8'))
            url_hash_hex = url_hash.hexdigest()
            self.cache[url] = url_hash_hex
            return print(f'{url} добавлен')


U1 = UrlCache()

print(U1.cache)
U1.cache_url('https://gb.ru/education')
U1.cache_url('https://gb.ru/education')
print(U1.cache)
