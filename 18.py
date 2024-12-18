from __future__ import annotations
import lib, re

def p1():
    data = lib.read()
    data = [lib.Point(*[int(j) for j in i.split(',')]) for i in data.split('\n')]

    # grid_size = 7
    grid_size = 71

    grid = lib.Grid.from_size(grid_size, grid_size, lambda: '.')
    for point in data[:1024]:
        grid[point] = '#'

    start = lib.Point(0, 0)
    end = lib.Point(grid_size - 1, grid_size - 1)

    print(grid.invert_y())

    def get_neighbours(p: lib.Point):
        neighbours = []
        for d in lib.CARDINAL_DIRECTIONS:
            next = p + d
            if grid.has_cell(next) and grid[next] != '#':
                neighbours.append((next, 1))
        return neighbours
    dijksrta = lib.Dijkstra(start, end, get_neighbours)
    result = dijksrta.search()

    print(result[end])

def p2():
    data = lib.read()
    data = [lib.Point(*[int(j) for j in i.split(',')]) for i in data.split('\n')]

    # grid_size = 7
    grid_size = 71

    start = lib.Point(0, 0)
    end = lib.Point(grid_size - 1, grid_size - 1)

    grid = lib.Grid.from_size(grid_size, grid_size, lambda: '.')
    def get_neighbours(p: lib.Point):
        neighbours = []
        for d in lib.CARDINAL_DIRECTIONS:
            next = p + d
            if grid.has_cell(next) and grid[next] != '#':
                neighbours.append((next, 1))
        return neighbours

    for point in data:
        grid[point] = '#'

        dijkstra = lib.Dijkstra(start, end, get_neighbours)
        result = dijkstra.search(True)

        if end not in result:
            print(point)
            break

p2()
