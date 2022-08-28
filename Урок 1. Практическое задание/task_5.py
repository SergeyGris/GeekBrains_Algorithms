"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class Buffet:

    def __init__(self, max_len=4):
        self.elems = [[]]
        self.max_len = max_len

    def __str__(self):
        rez = ''
        if self.shelfs()==0:
            rez='[ ]'
        for i in self.elems:
            rez += f'{i}\n'

        return rez

    def empty(self):
        self.elems = []
        return

    def push_in(self, el=1):

        if self.shelfs() == 0:
            self.new_shelf()

        for i in range(el):
            if len(self.last_shelf()) == 4:
                self.new_shelf()
            self.last_shelf().append('(')

    def new_shelf(self):
        self.elems.append([])

    def pop_out(self):
        if self.last_shelf_len() == 0:
            self.shelf_del()
        self.last_shelf().pop()
        if self.last_shelf_len() == 0:
            self.shelf_del()
        return self.elems

    def shelf_del(self):
        self.elems.pop()
        return self.elems

    def last_shelf_len(self):
        return len(self.elems[self.shelfs() - 1])

    def last_shelf(self):
        if self.shelfs() != 0:
            return self.elems[self.shelfs() - 1]
        else:
            return self.elems[0]

    def shelfs(self):
        return len(self.elems)


if __name__ == '__main__':
    buffet = Buffet()
    print(buffet)
    buffet.push_in(15)
    print(buffet)
    buffet.pop_out()
    print(buffet)
    buffet.pop_out()
    print(buffet)
    buffet.pop_out()
    print(buffet)
    buffet.pop_out()
    print(buffet)
    buffet.push_in(5)
    print(buffet)
    buffet.empty()
    print(buffet)
