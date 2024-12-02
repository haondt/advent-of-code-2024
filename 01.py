import lib
data = lib.read()

def load():
    left = []
    right = []
    for i in data.split('\n'):
        i = i.split(' ')
        l, r = int(i[0]), int(i[-1])
        left.append(l)
        right.append(r)
    return left, right


def p1():
    left, right = load()

    left.sort()
    right.sort()

    tdist = 0
    for i in range(len(left)):
        l, r = left[i], right[i]
        dist = abs(l - r)
        tdist += dist

    print(tdist)


def p2():
    left, right = load()

    rl_counts = {}
    for n in right:
        if n in rl_counts:
            rl_counts[n] += 1
        else:
            rl_counts[n] = 1

    sim = 0
    for n in left:
        if n in rl_counts:
            sim += n * rl_counts[n]
    print(sim)

p2()
