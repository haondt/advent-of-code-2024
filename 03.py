import lib, re

def p1():
    data = lib.read()
    matches = re.findall(r'mul\(([0-9]+),([0-9]+)\)', data)
    print(sum([int(i) * int(j) for i, j in matches]))

def p2():
    data = lib.read()
    matches = re.findall(r'(do\(\))|(don\'t\(\))|(mul\([0-9]+,[0-9]+\))', data)
    is_enabled = True
    s = 0
    for do, dont, mul in matches:
        if do:
            is_enabled = True
        elif dont:
            is_enabled = False
        elif is_enabled and mul:
            l, r = mul[4:-1].split(',')
            s += int(l)*int(r)
    print(s)

p2()
