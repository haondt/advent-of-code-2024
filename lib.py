from __future__ import annotations
from collections.abc import Callable
from typing import TypeVar, Generic, Generator
import math


T = TypeVar('T')
U = TypeVar('U')

def read():
    lines = []
    with open('input.txt') as f:
        for line in f:
            if len(line) > 0:
                lines.append(line.strip())
    return '\n'.join(lines)

def flatten(l):
    return [i for j in l for i in j]

class Gridv1(Generic[T]):
    def __init__(self, cells: list[list[T]]):
        self._width = len(cells[0])
        self._height = len(cells)
        self._cells: list[list[T]] = cells

    @classmethod
    def from_size(cls, width: int, height: int, default_value: Callable[[], T]):
        return cls([[default_value() for x in range(width)] for y in range(height)])

    def clone(self):
        return Gridv1([[cell for cell in row] for row in self._cells])

    def cell(self, x: int, y: int) -> None | T:
        if self.has_cell(x, y):
            return self._cells[self._height - 1 - y][x]
        return None

    def __getitem__(self, xy: tuple[int, int]):
        return self.cell(xy[0], xy[1])

    def __setitem__(self, xy: tuple[int, int], value: T):
        self._cells[self._height - 1 - xy[1]][xy[0]] = value 


    def enumerate(self) -> Generator[tuple[tuple[int, int], T], None, None]:
        for y in range(self._height):
            for x in range(self._width):
                yield ((x, y), self._cells[self._height - 1 - y][x])

    def __str__(self):
        rows = [''.join([str(cell) for cell in row]) for row in self._cells]
        return '\n'.join(rows)

    def has_cell(self, x: int, y: int) -> bool:
        return y >= 0 and y < self._height and x >= 0 and x < self._width

    def find(self, value: T) -> None | tuple[int, int]:
        for y in range(self._height):
            for x in range(self._width):
                if self.cell(x, y) == value:
                    return (x, y)
        return None

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self._hash = hash((self.x, self.y))

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return str(self)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __neg__(self) -> Point:
        return Point(-self.x, -self.y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return other.x == self.x and other.y == self.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def integer_direction(self):
        gcd = math.gcd(self.x, self.y)
        if gcd == 1:
            return self
        return Point(self.x // gcd, self.y // gcd)

    def __hash__(self):
        return self._hash

    def __mul__(self, scalar: int) -> Point:
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: int) -> Point:
        return self.__mul__(scalar)



class Grid(Generic[T]):
    def __init__(self, cells: list[list[T]]):
        self._width = len(cells[0])
        self._height = len(cells)
        self._cells: list[list[T]] = cells

    @classmethod
    def from_size(cls, width: int, height: int, default_value: Callable[[], T]):
        return cls([[default_value() for _x in range(width)] for _y in range(height)])

    @classmethod
    def from_string(cls, input: str, caster: Callable[[str], T]):
        return cls([[caster(j) for j in i] for i in input.split('\n')])

    def clone(self):
        return Grid([[cell for cell in row] for row in self._cells])

    def convert(self, converter: Callable[[T], U]) -> Grid[U]:
        return Grid([[converter(cell) for cell in row] for row in self._cells])

    def invert_y(self):
        return Grid([[cell for cell in row] for row in self._cells][::-1])

    def cell(self, point: Point) -> None | T:
        if self.has_cell(point):
            return self._cells[self._height - 1 - point.y][point.x]
        return None

    def __getitem__(self, point: Point) -> T:
        cell = self.cell(point)
        if cell is None:
            raise KeyError(f"Point {point} not inside grid")
        return cell

    def __setitem__(self, point: Point, value: T):
        self._cells[self._height - 1 - point.y][point.x] = value 

    def try_set(self, point: Point, value: T) -> bool:
        if self.has_cell(point):
            self[point] = value
            return True
        return False

    def enumerate(self) -> Generator[tuple[Point, T], None, None]:
        for y in range(self._height):
            for x in range(self._width):
                yield (Point(x, y), self._cells[self._height - 1 - y][x])

    def __str__(self):
        rows = [''.join([str(cell) for cell in row]) for row in self._cells]
        return '\n'.join(rows)

    def __repr__(self):
        return str(self)

    def has_cell(self, point: Point) -> bool:
        return point.y >= 0 and point.y < self._height and point.x >= 0 and point.x < self._width

    def find(self, value: T) -> None | Point:
        for y in range(self._height):
            for x in range(self._width):
                point = Point(x, y)
                if self.cell(point) == value:
                    return point
        return None


CARDINAL_DIRECTIONS = [
    Point(1, 0),
    Point(-1, 0),
    Point(0, 1),
    Point(0, -1)
]

ALL_DIRECTIONS = [
    Point(1, 0),
    Point(-1, 0),
    Point(0, 1),
    Point(0, -1),
    Point(1, 1),
    Point(-1, -1),
    Point(-1, 1),
    Point(1, -1)
]
