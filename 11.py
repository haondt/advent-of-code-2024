from __future__ import annotations
import lib

class Stone:
    def __init__(self, value: int):
        self.value = value
        self.str_value = str(value)
        self.next: Stone | None = None

    def set_value(self, value: int):
        self.value = value
        self.str_value = str(value)


def p1():
    data = lib.read()

    head: Stone | None = None
    prev: Stone | None = None

    for value in data.split(' '):
        stone = Stone(int(value))
        if head is None:
            head = stone

        if prev is not None:
            prev.next = stone

        prev = stone

    def print_stones():
        current = head
        while current is not None:
            print(current.value, end=' ')
            current = current.next
        print()

    def blink():
        current = head
        while current is not None:
            if current.value == 0:
                current.set_value(1)

                current = current.next
                continue

            if len(current.str_value) % 2 == 0:
                length = len(current.str_value)
                l, r = current.str_value[:length // 2], current.str_value[length // 2:]
                current.set_value(int(l))
                next = current.next
                current.next = Stone(int(r))
                current.next.next = next

                current = next
                continue

            current.set_value(current.value * 2024)
            current = current.next

    def count_stones():
        s = 0
        current = head
        while current is not None:
            s += 1
            current = current.next
        return s

    for i in range(25):
        blink()
    print(count_stones())

def p2():
    data = lib.read()
    stones = [int(i) for i in data.split(' ')]
    cache = {}

    # returns the number of stones after x blinks 
    def evaluate_stone(stone: int, blinks: int):
        if blinks == 0:
            return 1

        if (stone, blinks) in cache:
            return cache[(stone, blinks)]

        if stone == 0:
            result = evaluate_stone(1, blinks - 1)
            cache[(stone, blinks)] = result
            return result

        stone_str = str(stone)
        stone_str_len = len(stone_str)
        if stone_str_len % 2 == 0:
            l_result = evaluate_stone(int(stone_str[:stone_str_len//2]), blinks - 1)
            r_result = evaluate_stone(int(stone_str[stone_str_len//2:]), blinks - 1)
            cache[(stone, blinks)] = l_result + r_result
            return l_result + r_result

        mult_result = evaluate_stone(stone*2024, blinks - 1)
        cache[(stone, blinks)] = mult_result
        return mult_result

    print(sum(evaluate_stone(s, 75) for s in stones))

p2()


