from __future__ import annotations
import lib, re
import time
import heapq


class NodeIdentity:
    def __init__(self, position: lib.Point, direction: lib.Point):
        self.position = position
        self.direction = direction

    def __hash__(self) -> int:
        return hash((self.position, self.direction))

    def __eq__(self, other):
        if not isinstance(other, NodeIdentity):
            return False
        return self.position == other.position and self.direction == other.direction

    def __ne__(self, other):
        return not self.__eq__(other)



    def __repr__(self):
        return f'NodeIdentity(Position={self.position},Direction={self.direction})'

    def rotate_clockwise(self):
        return NodeIdentity(self.position, self._rotate_direction_clockwise())

    def _rotate_direction_clockwise(self):
        if self.direction.x == 0:
            if self.direction.y == 1:
                return lib.Point(1, 0)
            return lib.Point(-1, 0)
        if self.direction.x == 1:
            return  lib.Point(0, -1)
        return lib.Point(0, 1)

    def rotate_counter_clockwise(self):
        return NodeIdentity(self.position, self._rotate_direction_counter_clockwise())

    def _rotate_direction_counter_clockwise(self):
        if self.direction.x == 0:
            if self.direction.y == 1:
                return lib.Point(-1, 0)
            return lib.Point(1, 0)
        if self.direction.x == 1:
            return  lib.Point(0, 1)
        return lib.Point(0, -1)

class Node:
    def __init__(self, id: NodeIdentity):
        self.id = id
        self.distance: int | None = None
        self.closest_neighbours: dict[NodeIdentity, Node] = {}
        self.is_visited = False

    def __repr__(self):
        return f'Node(Id={self.id},Distance={self.distance},Visited={self.is_visited})'

    def __lt__(self, other: Node):
        assert self.distance != None
        assert other.distance != None
        return self.distance < other.distance

class NodeMap:
    def __init__(self, grid: lib.Grid):
        self._grid = grid
        self._nodes: dict[NodeIdentity, Node] = {}

    def get_node(self, id: NodeIdentity):
        if id not in self._nodes:
            self._nodes[id] = Node(id)
        return self._nodes[id]

    def get_neighbours(self, node: Node):
        neighbours: list[tuple[Node, int]] = []

        step_position = node.id.position + node.id.direction
        if self._grid.has_cell(step_position) and self._grid[step_position] != '#':
            id = NodeIdentity(step_position, node.id.direction)
            if id not in self._nodes:
                self._nodes[id] = Node(id)
            neighbours.append((self._nodes[id], 1))

        id = node.id.rotate_clockwise()
        if id not in self._nodes:
            self._nodes[id] = Node(id)
        neighbours.append((self._nodes[id], 1000))

        id = node.id.rotate_counter_clockwise()
        if id not in self._nodes:
            self._nodes[id] = Node(id)
        neighbours.append((self._nodes[id], 1000))

        return neighbours

def p1():
    data = lib.read()
    grid = lib.Grid.from_string(data, lambda x: x)
    start_pos = grid.find('S')
    end_pos = grid.find('E')

    map = NodeMap(grid)
    start = map.get_node(NodeIdentity(start_pos, lib.Point(1, 0)))
    start.distance = 0

    todo_heap = lib.Heap([start])
    todo_set = set([start])

    display_grid = grid.clone()
    while len(todo_heap) != 0:

        current = todo_heap.pop()
        todo_set.remove(current)
        display_grid[current.id.position] = '@'

        if current.id.position == end_pos:
            continue

        for neighbour, distance in map.get_neighbours(current):
            if neighbour.is_visited:
                continue
            display_grid[neighbour.id.position] = '+'
            new_distance = distance + current.distance
            if neighbour.distance is None or new_distance < neighbour.distance:
                neighbour.distance = new_distance
                neighbour.closest_neighbours = { current.id: current }
                if neighbour not in todo_set:
                    todo_set.add(neighbour)
                    todo_heap.push(neighbour)
            elif neighbour.distance == new_distance:
                neighbour.closest_neighbours[current.id] = current

        current.is_visited = True
        print(display_grid)
        time.sleep(0.001)

    print(min([v.distance for n,v in map._nodes.items() if n.position == end_pos and v.distance is not None]))
    return display_grid, map, start_pos, end_pos

def p2():
    display_grid, map, start_pos, end_pos = p1()
    end_nodes = [node for id, node in map._nodes.items() if id.position == end_pos]
    min_dist = min([node.distance for node in end_nodes if node.distance is not None])
    end_nodes: list[Node] = [node for node in end_nodes if node.distance == min_dist]

    path_positions: set[lib.Point] = set()
    def walk(node: Node):
        if display_grid[node.id.position] != 'O':
            display_grid[node.id.position] = 'O'
            print(display_grid)
            time.sleep(0.01)
        path_positions.add(node.id.position)
        if node.id.position is not start_pos:
            for next in node.closest_neighbours.values():
                walk(next)
    for end_node in end_nodes:
        walk(end_node)
    print(display_grid)
    print(len(path_positions))


p2()

