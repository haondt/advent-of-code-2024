import lib

def turn_right(direction):
    return {
        (0, 1): (1, 0),
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
    }[direction]


def p1():
    data = lib.read()

    grid = lib.Gridv1([list(i) for i in data.split('\n')])
    pos = grid.find('^')
    assert pos is not None
    direction = (0, 1)
    visited = set()
    visited_vectors = set()
    visited_vectors.add(pos + direction)
    visited.add(pos)

    while True:
        next = (pos[0] + direction[0], pos[1] + direction[1])
        next_value = grid.cell(next[0], next[1])
        if next_value is None:
            break
        if next_value == '#':
            direction = turn_right(direction)
            next = (pos[0] + direction[0], pos[1] + direction[1])
            next_value = grid.cell(next[0], next[1])
            if next_value is None:
                break
            if next_value == '#':
                direction = turn_right(direction)
                next = (pos[0] + direction[0], pos[1] + direction[1])

        pos = next

        current = pos + direction
        if current in visited_vectors:
            break
        visited_vectors.add(current)
        visited.add(pos)


    print(len(visited))
    

def p2():
    data = lib.read()
    grid = lib.Gridv1([list(i) for i in data.split('\n')])
    start = grid.find('^')
    assert start is not None
    start_dir = (0, 1)

    def has_loop():
        pos = start
        direction = start_dir
        visited_vectors = set()
        visited_vectors.add(pos + direction)

        while True:
            next = (pos[0] + direction[0], pos[1] + direction[1])
            next_value = grid.cell(next[0], next[1])
            if next_value is None:
                return False
            if next_value == '#':
                direction = turn_right(direction)
                next = (pos[0] + direction[0], pos[1] + direction[1])
                next_value = grid.cell(next[0], next[1])
                if next_value is None:
                    return False
                if next_value == '#':
                    direction = turn_right(direction)
                    next = (pos[0] + direction[0], pos[1] + direction[1])

            pos = next

            current = pos + direction
            if current in visited_vectors:
                return True
            visited_vectors.add(current)

    s = 0
    for pos, value in grid.enumerate():
        if value != '.':
            continue
        grid[pos] = '#'
        if has_loop():
            s += 1
        grid[pos] = '.'

    print(s)

p2()
