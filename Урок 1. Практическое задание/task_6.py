"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskList:
    def __init__(self):
        self.tasks_list = []
        self.revision_list = []
        self.tasks_done_list = []

    def __str__(self):
        rez = ''
        if self.tasks_list != []:
            tasks_rez = 'Задачи: '
            for i in range(len(self.tasks_list) - 1, -1, -1):
                task = self.tasks_list[i]
                tasks_rez += '\n' + task
            rez += '\n' + tasks_rez

        if self.revision_list != []:
            revision_rez = 'Задачи на доработке: '
            for i in range(len(self.revision_list) - 1, -1, -1):
                task = self.revision_list[i]
                revision_rez += '\n' + task
            rez += '\n' + revision_rez
        if self.tasks_done_list != []:
            tasks_done_rez = 'Выполненные задачи: '
            for i in range(len(self.tasks_done_list) - 1, -1, -1):
                task = self.tasks_done_list[i]
                tasks_done_rez += '\n' + task
            rez += '\n' + tasks_done_rez
        return rez

    def is_empty(self):
        return self.tasks_list == []

    def input(self, task):
        self.tasks_list.insert(0, task)

    def task_done(self):
        task = self.tasks_list.pop()
        self.tasks_done_list.insert(0, task)

    def revise(self):
        task = self.tasks_list.pop()
        return self.revision_list.insert(0, task)

    def size(self):
        return len(self.tasks_list)


if __name__ == '__main__':
    tasklist = TaskList()
    tasklist.input('1 Помыть посуду')
    tasklist.input('2 Подмести пол')
    tasklist.input('3 Приготовить обед')

    print(tasklist)
    tasklist.task_done()
    tasklist.revise()
    print(tasklist)
