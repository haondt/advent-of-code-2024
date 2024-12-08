import lib
import itertools

def get_grids():
    data = lib.read()

    # generate seperate grids per type
    grid = lib.Grid([list(x) for x in data.split('\n')])
    grids: dict[str,tuple[lib.Grid,list[lib.Point]]] = {}
    for pos, value in grid.enumerate():
        if value == '.':
            continue
        if value not in grids:
            grids[value] = (lib.Grid.from_size(grid._width, grid._height, lambda: '.'), [])
        grids[value][0][pos] = value
        grids[value][1].append(pos)
    return grids


def p1():
    grids = get_grids()

    antinodes: set[lib.Point] = set()
    for (grid, antennas) in grids.values():
        for left, right in itertools.combinations(antennas, 2):
            direction = left - right
            antinode = left + direction
            if grid.try_set(antinode, '#'):
                antinodes.add(antinode)

            antinode = right - direction
            if grid.try_set(antinode, '#'):
                antinodes.add(antinode)
        # print()
        # print(grid)

    print(len(antinodes))

def p2():
    grids = get_grids()

    antinodes: set[lib.Point] = set()
    for (grid, antennas) in grids.values():
        for left, right in itertools.combinations(antennas, 2):
            direction = (left - right).integer_direction()
            antinode = left
            while grid.has_cell(antinode):
                antinodes.add(antinode)
                if grid[antinode] == '.':
                    grid[antinode] = '#'
                antinode += direction

            antinode = left - direction
            while grid.has_cell(antinode):
                antinodes.add(antinode)
                if grid[antinode] == '.':
                    grid[antinode] = '#'
                antinode -= direction
        # print()
        # print(grid)

    print(len(antinodes))
    
p2()
