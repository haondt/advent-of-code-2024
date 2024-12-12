from __future__ import annotations
import lib

def p1():
    data = lib.read()

    grid = lib.Grid.from_string(data, str)
    visited: set[lib.Point] = set()

    def expand_region(pos: lib.Point) -> list[lib.Point]:
        if pos in visited:
            return []
        visited.add(pos)

        cells = [pos]
        for direction in lib.CARDINAL_DIRECTIONS:
            next = pos + direction
            if not grid.has_cell(next):
                continue

            if grid[next] != grid[pos]:
                continue

            expansion = expand_region(next)
            cells += expansion
        return cells

    def get_perimeter(region: list[lib.Point]):
        s = 0
        for pos in region:
            s += 4
            for direction in lib.CARDINAL_DIRECTIONS:
                next = pos + direction
                if grid.cell(next) == grid[pos]:
                    s -= 1
        return s



    cost = 0
    for pos, cell in grid.enumerate():
        if pos in visited:
            continue

        region = expand_region(pos)
        area = len(region)
        perimeter = get_perimeter(region)
        price = area * perimeter
        cost += price

    print(cost)

def p2():
    data = lib.read()

    grid = lib.Grid.from_string(data, str)
    visited: set[lib.Point] = set()

    def expand_region(pos: lib.Point) -> list[lib.Point]:
        if pos in visited:
            return []
        visited.add(pos)

        cells = [pos]
        for direction in lib.CARDINAL_DIRECTIONS:
            next = pos + direction
            if not grid.has_cell(next):
                continue

            if grid[next] != grid[pos]:
                continue

            expansion = expand_region(next)
            cells += expansion
        return cells

    def get_sides(region: list[lib.Point]):
        sides: dict[lib.Point, list[lib.Point]] = {}
        for pos in region:
            sides[pos] = [i for i in lib.CARDINAL_DIRECTIONS]
            for direction in lib.CARDINAL_DIRECTIONS:
                next = pos + direction
                if grid.cell(next) == grid[pos]:
                    sides[pos].remove(direction)



        visited = set()
        s = 0
        for pos, directions in sides.items():
            for direction in directions:
                if (pos, direction) in visited:
                    continue

                s += 1
                visited.add((pos, direction))

                if direction.x == 0:
                    next = pos + lib.Point(-1, 0)
                    while next in sides and direction in sides[next]:
                        visited.add((next, direction))
                        next = next + lib.Point(-1, 0)

                    next = pos + lib.Point(1, 0)
                    while next in sides and direction in sides[next]:
                        visited.add((next, direction))
                        next = next + lib.Point(1, 0)

                elif direction.y == 0:
                    next = pos + lib.Point(0, 1)
                    while next in sides and direction in sides[next]:
                        visited.add((next, direction))
                        next = next + lib.Point(0, 1)

                    next = pos + lib.Point(0, -1)
                    while next in sides and direction in sides[next]:
                        visited.add((next, direction))
                        next = next + lib.Point(0, -1)
        return s



    cost = 0
    for pos, cell in grid.enumerate():
        if pos in visited:
            continue

        region = expand_region(pos)
        area = len(region)
        sides = get_sides(region)
        price = area * sides
        cost += price

    print(cost)




p2()
