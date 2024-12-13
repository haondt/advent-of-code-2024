from __future__ import annotations
import lib, re

def p1():
    data = lib.read()

    ax = 0
    ay = 0
    bx = 0
    by = 0
    px = 0
    py = 0

    def solve():
        b = ((px/ax)-(py/ay))/((bx/ax)-(by/ay))
        a = ((px/ax)-(bx/ax)*b)
        tol = 0.000000000001
        if abs(b - round(b)) < tol:
            b = round(b)
        if abs(a - round(a)) < tol:
            a = round(a)

        if a == round(a) and b == round(b):
            return a*3 + b
        return 0

    s = 0
    for line in data.split('\n'):
        if len(line) == 0:
            s += solve()
        else:
            m = re.match(r'Button A: X\+([0-9]+), Y\+([0-9]+)', line)
            if (m):
                ax, ay = float(m.group(1)), float(m.group(2))
            m = re.match(r'Button B: X\+([0-9]+), Y\+([0-9]+)', line)
            if (m):
                bx, by = float(m.group(1)), float(m.group(2))
            m = re.match(r'Prize: X=([0-9]+), Y=([0-9]+)', line)
            if (m):
                px, py = float(m.group(1)), float(m.group(2))
    s += solve()
    print(s)

def p2():
    data = lib.read()

    ax = 0
    ay = 0
    bx = 0
    by = 0
    px = 0
    py = 0

    def solve():
        b = ((px/ax)-(py/ay))/((bx/ax)-(by/ay))
        a = ((px/ax)-(bx/ax)*b)
        tol = 0.001
        if abs(b - round(b)) < tol:
            b = round(b)
        if abs(a - round(a)) < tol:
            a = round(a)

        if a == round(a) and b == round(b):
            return a*3 + b
        return 0

    s = 0
    for line in data.split('\n'):
        if len(line) == 0:
            s += solve()
        else:
            m = re.match(r'Button A: X\+([0-9]+), Y\+([0-9]+)', line)
            if (m):
                ax, ay = float(m.group(1)), float(m.group(2))
            m = re.match(r'Button B: X\+([0-9]+), Y\+([0-9]+)', line)
            if (m):
                bx, by = float(m.group(1)), float(m.group(2))
            m = re.match(r'Prize: X=([0-9]+), Y=([0-9]+)', line)
            if (m):
                px, py = float(m.group(1)) + 10000000000000, float(m.group(2)) + 10000000000000
    s += solve()
    print(s)

        
        

p2()
