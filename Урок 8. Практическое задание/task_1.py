"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from collections import defaultdict


def frequency(str):
    def_dict = defaultdict(int)
    for i in str:
        def_dict[i] += 1
    return def_dict


class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None


class HuffmanTree(object):
    def __init__(self, char_Weights):
        self.Leaf = [Node(k, v) for k, v in char_Weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node: node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    def hu_generate(self, tree, length):
        node = tree
        if not node:
            return
        elif node.name:
            print(node.name + ' - ', end='')
            for i in range(length):
                print(self.Buffer[i], end='')
            print('\n')
            return
        self.Buffer[length] = 0
        self.hu_generate(node.lchild, length + 1)
        self.Buffer[length] = 1
        self.hu_generate(node.rchild, length + 1)

    def get_code(self):
        self.hu_generate(self.root, 0)


if __name__ == '__main__':
    text = r'boop beep beer'
    result = frequency(text)
    print(result)
    tree = HuffmanTree(result)
    tree.get_code()
