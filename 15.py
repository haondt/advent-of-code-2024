from __future__ import annotations
import lib, re
import time

def p1():
    data = lib.read()
    grid_data, move_data = data.split('\n\n')
    grid = lib.Grid.from_string(grid_data, lambda x: x)
    moves = ''.join(move_data.split('\n'))
    pos = grid.find('@')
    assert pos is not None

    step = False
    for move in moves:
        if step:
            input(grid)
        direction = {
            '<': lib.Point(-1, 0),
            '>': lib.Point(1, 0),
            '^': lib.Point(0, 1),
            'v': lib.Point(0, -1),
        }[move]

        next = pos + direction
        while grid[next] != '#' and grid[next] != '.':
            next += direction

        if grid[next] == '#':
            continue

        previous = next - direction
        while grid[previous] != '@':
            grid[next] = grid[previous]
            previous -= direction
            next -= direction

        grid[next] = grid[previous]
        grid[previous] = '.'
        pos = next

    print(grid)
    s = 0
    for i, cell in grid.invert_y().enumerate():
        if cell != 'O':
            continue
        s += 100 * i.y + i.x
    print(s)


def p2():
    data = lib.read()
    grid_data, move_data = data.split('\n\n')
    def widen_cell(v: str) -> str:
        match v:
            case '#':
                return '##'
            case 'O':
                return '[]'
            case '.':
                return '..'
            case '@':
                return '@.'
        raise Exception()
    tmp_grid = lib.Grid.from_string(grid_data, widen_cell)
    grid = lib.Grid.from_string(str(tmp_grid), lambda x: x)

    moves = ''.join(move_data.split('\n'))
    pos = grid.find('@')
    assert pos is not None

    step = True
    for move in moves:
        if step:
            print(grid)
            input(move)
        direction = {
            '<': lib.Point(-1, 0),
            '>': lib.Point(1, 0),
            '^': lib.Point(0, 1),
            'v': lib.Point(0, -1),
        }[move]

        def perform_move(to_move: list[lib.Point], grid: lib.Grid) -> tuple[bool, lib.Grid]:
            if to_move == []:
                return True, grid

            # expand for wide boxes
            new_to_move = set()
            for p in to_move:
                new_to_move.add(p)
                if grid[p] == '[' and direction.x == 0:
                    new_to_move.add(p + lib.Point(1,0))
                if grid[p] == ']' and direction.x == 0:
                    new_to_move.add(p + lib.Point(-1,0))

            needs_moving = []
            for p in new_to_move:
                np = p + direction
                if grid[np] == '.':
                    continue
                if grid[np] == '#':
                    return False, grid
                needs_moving.append(np)

            result, grid = perform_move(needs_moving, grid)
            if not result:
                return False, grid

            for p in new_to_move:
                np = p + direction
                grid[np] = grid[p]
                grid[p] = '.'

            return True, grid

        result, out_grid = perform_move([pos], grid.clone())
        if result:
            grid = out_grid
            pos = pos + direction

    print(grid)
    s = 0
    for i, cell in grid.invert_y().enumerate():
        if cell != '[':
            continue
        s += 100 * i.y + i.x
    print(s)




p2()
