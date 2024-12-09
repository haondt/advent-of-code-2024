from __future__ import annotations
import lib

def p1():
    data = lib.read()
    expanded = []
    is_block = True
    file_id = 0
    for digit in data:
        digit = int(digit)
        if is_block:
            expanded += [file_id]*digit
            file_id += 1
        else:
            expanded += [-1]*digit

        is_block = not is_block

    empty_ptr = 0
    while expanded[empty_ptr] != -1:
        empty_ptr += 1

    current_ptr = len(expanded)-1
    while current_ptr >= 0:
        if expanded[current_ptr] == -1:
            current_ptr -= 1
            continue

        if(current_ptr <= empty_ptr):
            break


        expanded[empty_ptr] = expanded[current_ptr]
        expanded[current_ptr] = -1
        while expanded[empty_ptr] != -1:
            empty_ptr += 1

    s = 0
    for i, d in enumerate(expanded):
        if (d == -1):
            break
        s += i*d
    print(s)


class File:
    def __init__(self, id: int, size: int, previous: Gap | None = None, next: Gap | None = None):
        self.id = id
        self.size = size
        self.previous = previous
        self.next = next

    def __repr__(self):
        return f"File<{self.id}>[{self.size}]"

class Gap:
    def __init__(self, size: int, previous: File, next: File | None = None):
        self.size = size
        self.previous = previous
        self.next = next

    def __repr__(self):
        return f"Gap[{self.size}]"

def p2():
    data = lib.read()

    files: list[File] = []
    head: None | File = None
    file_id = 0
    current_position = 0
    current_item: None | File | Gap = head
    for digit in data:
        digit = int(digit)
        if current_item == None:
            file = File(file_id, digit)
            files.append(file)
            head = file
            current_item = file
            current_position += digit
            file_id += 1
        elif isinstance(current_item, Gap):
            file = File(file_id, digit, current_item)
            files.append(file)
            current_item.next = file

            current_item = file
            current_position += digit
            file_id += 1
        else:
            gap = Gap(digit, current_item)
            current_item.next = gap

            current_item = gap
            current_position += digit

    def print_file_system():
        current = head
        while current is not None:
            if isinstance(current, File):
                print(str(current.id)*current.size, end='')
            elif isinstance(current, Gap):
                print('.'*current.size, end='')
            current = current.next
        print('')


    print_file_system()
    files = files[::-1]
    for file in files:
        # skip the head file
        if file.previous is None:
            continue
        current = head
        while True:
            if current == None:
                break
            if current == file:
                break
            if not isinstance(current, Gap):
                current = current.next
                continue
            if file.size > current.size:
                current = current.next
                continue

            gap = current

            # pull the file out of its current spot
            # expanding the previous gap to fill it
            # and merging the next gap with the previous gap
            prev = file.previous
            next = file.next
            if next is not None:
                prev.next = next.next
                if next.next is not None:
                    next.next.previous = prev
                prev.size += next.size
            else:
                prev.next = None
            prev.size += file.size

            # insert an empty gap before the gap
            prev = gap.previous
            next = gap.next
            empty_gap = Gap(0, prev)
            prev.next = empty_gap

            # insert the file after the empty gap
            empty_gap.next = file
            file.previous = empty_gap
            gap.previous = file
            file.next = gap

            # shrink the gap to fit the file
            gap.size -= file.size
            break


    print_file_system()
    checksum_values = []
    current = head
    while current is not None:
        if isinstance(current, File):
            for i in range(current.size):
                checksum_values.append(current.id)
            pass
        elif isinstance(current, Gap):
            for i in range(current.size):
                checksum_values.append(-1)
        current = current.next

    s = 0
    for i, d in enumerate(checksum_values):
        if (d == -1):
            continue
        s += i*d
    print(s)


p2()
