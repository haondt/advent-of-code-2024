from __future__ import annotations
import functools
import lib, re

class Node:
    def __init__(self, value):
        self.value = value
        self.nexts: dict[str, Node] = {}

    def __repr__(self) -> str:
        return f'({self.value})'

def p1():
    data = lib.read()
    towels, designs = data.split('\n\n')
    towels = towels.split(', ')
    designs = designs.split('\n')

    root = Node('.')

    for towel in towels:
        current: Node = root
        for stripe in towel:
            if stripe in current.nexts:
                current = current.nexts[stripe]
            else:
                new = Node(stripe)
                current.nexts[stripe] = new
                current = new
        current.nexts['.'] = root

    def print_nodes(node: Node, indentation: int = 0):
        if indentation > 1:
            print('  '*(indentation-1), end='')
        if indentation > 0:
            print('|-', end='')
        print(node.value)
        if indentation > 0 and node.value == '.':
            return
        for node in node.nexts.values():
            print_nodes(node, indentation + 1)

    # for node in root.nexts:
    #     path = []
    #     while node is not root:
    #         path.append(node)
    #         node = node.nexts[0]
    #     print(path)

    @functools.cache
    def is_possible(design: str, current: Node):
        # if len(design) > 0:
        #     print('searching', design[0], 'in node', current.value)
        # else:
        #     print('searching', '.', 'in node', current.value)
        if design == '':
            if '.' in current.nexts:
                # print('success!')
                return True
            return False

        if design[0] in current.nexts:
            if is_possible(design[1:], current.nexts[design[0]]):
                return True

        if '.' not in current.nexts:
            return False

        return is_possible(design, current.nexts['.'])

    s = 0
    for design in designs:
        # print('checking', design)
        if is_possible(design, root):
            s += 1
    print(s)

def p2():
    data = lib.read()
    towels, designs = data.split('\n\n')
    towels = towels.split(', ')
    designs = designs.split('\n')

    root = Node('.')

    for towel in towels:
        current: Node = root
        for stripe in towel:
            if stripe in current.nexts:
                current = current.nexts[stripe]
            else:
                new = Node(stripe)
                current.nexts[stripe] = new
                current = new
        current.nexts['.'] = root

    def print_nodes(node: Node, indentation: int = 0):
        if indentation > 1:
            print('  '*(indentation-1), end='')
        if indentation > 0:
            print('|-', end='')
        print(node.value)
        if indentation > 0 and node.value == '.':
            return
        for node in node.nexts.values():
            print_nodes(node, indentation + 1)

    # for node in root.nexts:
    #     path = []
    #     while node is not root:
    #         path.append(node)
    #         node = node.nexts[0]
    #     print(path)

    @functools.cache
    def arrangements(design: str, current: Node):
        # if len(design) > 0:
        #     print('searching', design[0], 'in node', current.value)
        # else:
        #     print('searching', '.', 'in node', current.value)
        if design == '':
            if '.' in current.nexts:
                # print('success!')
                return 1
            return 0

        s = 0
        if design[0] in current.nexts:
            s += arrangements(design[1:], current.nexts[design[0]])

        if '.' not in current.nexts:
            return s

        s += arrangements(design, current.nexts['.'])
        return s

    fs = 0
    for design in designs:
        # print('checking', design)
        fs += arrangements(design, root)
    print(fs)


p2()
