import random
from itertools import product
from .own_types import Grid

class Board:
    def __init__(self, grid_size: tuple[int, int], randomize: bool = False) -> None:
        self._width: int = grid_size[0];
        self._height: int = grid_size[1];
        self._board: Grid = self._make_board(randomize)


    def _make_board(self, randomize: bool = False) -> Grid:
        new_board: Grid = [[]]
        if randomize:
            new_board = [
                [random.choice([False, True]) for _ in range(self._height)]
                for _ in range(self._width)
            ]
        else:
            new_board = [
                [False for _ in range(self._height)]
                for _ in range(self._width)
            ]
        return new_board

    def get_cell(self, coords: tuple[int, int]) -> bool:
        return self._board[coords[0]][coords[1]]

    def set_cell(self, coords: tuple[int, int], alive: bool) -> None:
        self._board[coords[0]][coords[1]] = alive

    def _get_neighbour_count(self, x: int, y: int) -> int:
        neighbour_count: int = 0
        for delta_x in [-1,0,1]:
            for delta_y in [-1,0,1]:
                nx: int = (x+delta_x)%self._width
                ny: int = (y+delta_y)%self._height
                neighbour_count += self._board[nx][ny]
        return neighbour_count-self._board[x][y]

    def advance(self) -> None:
        new_board: Grid = self._make_board()
        coords: product[tuple[int,int]] = product(range(self._width), range(self._height))
        for x, y in coords:
            neighbour_count: int = self._get_neighbour_count(x,y)
            if self._board[x][y] and neighbour_count in [2, 3]:
                new_board[x][y] = True
            if not self._board[x][y] and neighbour_count in [3]:
                new_board[x][y] = True
        self._board = new_board
        return