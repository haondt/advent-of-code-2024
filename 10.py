from __future__ import annotations
import lib

def p1():
    data = lib.read()
    grid = lib.Grid.from_string(data, lambda x: 100 if x == '.' else int(x))
    peaks: dict[lib.Point, list[lib.Point]] = {}

    # return the peaks reachable from a given position
    def search_peaks(pos: lib.Point):
        if pos in peaks:
            return peaks[pos]

        height = grid[pos]
        if height == 9:
            return [pos]

        found_peaks = []
        for direction in [lib.Point(0,1), lib.Point(1,0), lib.Point(0,-1), lib.Point(-1,0)]:
            next = pos + direction
            if not grid.has_cell(next):
                continue

            next_height = grid[next]
            if next_height != height + 1:
                continue

            next_peaks = search_peaks(next)
            found_peaks += next_peaks

        peaks[pos] = list(set(found_peaks))
        return peaks[pos]

    s = 0
    for (cell, value) in grid.enumerate():
        if value != 0:
            continue
        s += len(search_peaks(cell))
    print(s)

def p2():
    data = lib.read()
    grid = lib.Grid.from_string(data, lambda x: 100 if x == '.' else int(x))
    trails: dict[lib.Point, int] = {}

    # return the distinct trails reachable from a given position
    def search_trails(pos: lib.Point) -> int:
        if pos in trails:
            return trails[pos]

        height = grid[pos]
        if height == 9:
            return 1

        found_trails = 0
        for direction in [lib.Point(0,1), lib.Point(1,0), lib.Point(0,-1), lib.Point(-1,0)]:
            next = pos + direction
            if not grid.has_cell(next):
                continue

            next_height = grid[next]
            if next_height != height + 1:
                continue

            next_trails = search_trails(next)
            found_trails += next_trails

        trails[pos] = found_trails
        return trails[pos]

    s = 0
    for (cell, value) in grid.enumerate():
        if value != 0:
            continue
        s += search_trails(cell)
    print(s)
    

p2()



    
