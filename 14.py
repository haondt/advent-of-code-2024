from __future__ import annotations
import lib, re
import time

def p1():
    robots: list[tuple[lib.Point, lib.Point]] = [] # (location, direction)

    for line in lib.read().split('\n'):
        m = re.match(r'p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)', line)
        assert bool(m)
        location = lib.Point(int(m.group(1)), int(m.group(2)))
        direction = lib.Point(int(m.group(3)), int(m.group(4)))
        robots.append((location, direction))

    space_height = 103
    space_width = 101
    duration_seconds = 100

    final_positions = []
    for robot in robots:
        future_pos = robot[0] + robot[1] * duration_seconds
        wrapped_x = future_pos.x % space_width
        wrapped_y = future_pos.y % space_height

        final_positions.append(lib.Point(wrapped_x, wrapped_y))

    def print_robots(b: list[lib.Point]):
        grid = lib.Grid.from_size(space_width, space_height, lambda: 0)
        for r in b:
            grid[r] += 1

        str_grid = grid.convert(lambda i: str(i) if i != 0 else '.').invert_y()
        print(str_grid)

    def calculate_safety_factor(b: list[lib.Point]):
        center_x = space_width // 2
        center_y = space_height // 2
        factors = [0, 0, 0, 0]
        def get_quadrant(p: lib.Point):
            if p.x < center_x:
                if p.y < center_y:
                    return 0
                if p.y > center_y:
                    return 1
            if p.x > center_x:
                if p.y < center_y:
                    return 2
                if p.y > center_y:
                    return 3
            return -1
        for point in b:
            q = get_quadrant(point)
            if q == -1:
                continue
            factors[q] += 1
        print(factors)
        s = 1
        for f in factors:
            s *= f
        return s

    print_robots(final_positions)
    print(calculate_safety_factor(final_positions))

    # print(final_positions)



def p2():
    robots: list[tuple[lib.Point, lib.Point]] = [] # (location, direction)

    for line in lib.read().split('\n'):
        m = re.match(r'p=(-?[0-9]+),(-?[0-9]+) v=(-?[0-9]+),(-?[0-9]+)', line)
        assert bool(m)
        location = lib.Point(int(m.group(1)), int(m.group(2)))
        direction = lib.Point(int(m.group(3)), int(m.group(4)))
        robots.append((location, direction))

    space_height = 103
    space_width = 101

    # space_height = 7
    # space_width = 11
    def print_robots():
        grid = lib.Grid.from_size(space_width, space_height, lambda: 0)
        for r in robots:
            grid[r[0]] += 1

        str_grid = grid.convert(lambda i: str(i) if i != 0 else '.').invert_y()
        print(str_grid)


    current = 7
    for i, robot in enumerate(robots):
        future_pos = robot[0] + robot[1] * current
        wrapped_x = future_pos.x % space_width
        wrapped_y = future_pos.y % space_height

        robots[i] = (lib.Point(wrapped_x, wrapped_y), robot[1])

    
    while True:
        # print('----------------------------------------')
        # print_robots()
        current += 101
        duration_seconds = 101
        for i, robot in enumerate(robots):
            future_pos = robot[0] + robot[1] * duration_seconds
            wrapped_x = future_pos.x % space_width
            wrapped_y = future_pos.y % space_height

            robots[i] = (lib.Point(wrapped_x, wrapped_y), robot[1])
        # counts = {}
        # for i, robot in robots:
        #     if i not in counts:
        #         counts[i] = 0
        #     counts[i] += 1
        # if max(counts.values()) > 3:
        print_robots()
        print(current)
        input()

p2()
