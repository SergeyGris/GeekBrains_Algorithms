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
from os.path import join, dirname
from sqlite3 import connect, OperationalError, IntegrityError


class UrlCache():
    def __init__(self):
        self.db_obj = join(dirname(__file__), 'UrlCache.sqlite')
        self.conn = connect(self.db_obj)
        self.crs = self.conn.cursor()

    def create_table(self):
        create_stmt = 'CREATE TABLE url_cache (url VARCHAR(255) ' \
                      'UNIQUE, url_hash VARCHAR(255));'
        try:
            self.crs.execute(create_stmt)
        except OperationalError:
            print('таблица уже есть')
        else:
            self.conn.commit()
            print('Таблица добавлена в БД')

    @staticmethod
    def get_hash():
        url = input('Введите url:')
        salt = 'my_salt'
        hash_obj = hashlib.sha512((url + salt).encode()).hexdigest()
        return url, hash_obj

    def return_cache(self, url=''):
        select_stmt = 'SELECT url_hash FROM url_cache WHERE url= ?'
        self.crs.execute(select_stmt, (url,))
        out_hash = self.crs.fetchone()
        print(out_hash)

    def cache_url(self):
        url, url_hash = self.get_hash()
        insert_stmt = 'INSERT INTO url_cache(url,' \
                      ' url_hash)VALUES(?,?)'
        url_info = url, url_hash
        try:
            self.crs.execute(insert_stmt, (url, url_hash))
        except IntegrityError:
            print('Данный url уже есть в базе')
            self.return_cache(url)
        else:
            self.conn.commit()
            print('url успешно добавлен в БД')



U1 = UrlCache()
U1.create_table()
U1.cache_url()


