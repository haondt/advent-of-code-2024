from typing import TypeVar, Generic, Generator
T = TypeVar('T')

def read():
    lines = []
    with open('input.txt') as f:
        for line in f:
            if len(line) > 0:
                lines.append(line.strip())
    return '\n'.join(lines)

def flatten(l):
    return [i for j in l for i in j]

class Grid(Generic[T]):
    def __init__(self, cells: list[list[T]]):
        self._width = len(cells[0])
        self._height = len(cells)
        self._cells: list[list[T]] = cells

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

    def has_cell(self, x: int, y: int) -> bool:
        return y >= 0 and y < self._height and x >= 0 and x < self._width

    def find(self, value: T) -> None | tuple[int, int]:
        for y in range(self._height):
            for x in range(self._width):
                if self.cell(x, y) == value:
                    return (x, y)
        return None


