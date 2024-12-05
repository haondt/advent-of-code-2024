import lib
from functools import cmp_to_key

def p1():
    data = lib.read()

    rules = {}
    updates = []
    for line in data.split('\n'):
        if '|' in line:
            before, after = line.split('|')
            rules.setdefault(after, set()).add(before)
        elif ',' in line:
            updates.append(line.split(','))


    s = 0
    for update in updates:
        disallowed_pages = set()
        is_in_correct_order = True
        for page in update:
            if page in disallowed_pages:
                is_in_correct_order = False
                break
            if page in rules:
                disallowed_pages = disallowed_pages.union(rules[page])

        if is_in_correct_order:
            s += int(update[len(update)//2])
    print(s)

def p2():
    data = lib.read()

    rules = {}
    updates = []
    for line in data.split('\n'):
        if '|' in line:
            before, after = line.split('|')
            rules.setdefault(before, set()).add(after)
        elif ',' in line:
            updates.append(line.split(','))

    def cmp(a, b):
        if a in rules:
            if b in rules[a]:
                return -1
        if b in rules:
            if a in rules[b]:
                return 1
        return 0
    key = cmp_to_key(cmp)

    s = 0
    for update in updates:
        sorted_update = sorted(update, key=key)
        if (sorted_update != update):
            s += int(sorted_update[len(sorted_update)//2])
    print(s)

    
p2()





