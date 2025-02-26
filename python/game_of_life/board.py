import random
import pygame
from itertools import product
from .own_types import Grid, Color, BoardPresets
from .constants import ConfigManager
from . import presets

class Board:
    def __init__(self, randomize: bool = False) -> None:
        self._config: ConfigManager = ConfigManager()
        self._width: int = self._config.board_constants.GRID_WIDTH
        self._height: int = self._config.board_constants.GRID_HEIGHT
        self._cell_size: int = self._config.board_constants.CELL_SIZE
        self._life_color: Color = self._config.board_constants.LIFE_COLOR
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

    def draw(self, screen: pygame.Surface) -> None:
        for x, y in product(range(self._width), range(self._height)):
            coords = ((x+0.5)*self._cell_size, (y+0.5)*self._cell_size)
            if self._board[x][y]:
                pygame.draw.circle(screen, self._life_color, coords, self._cell_size/2)

    def load_preset(self, preset: BoardPresets) -> None:
        if preset == BoardPresets.BLANK:
            self._board = self._make_board()
        elif preset == BoardPresets.RANDOM:
            self._board = self._make_board(randomize=True)
        elif preset == BoardPresets.GLIDER_GUN:
            self._board = self._make_board()
            glider_gun: list[list[int]] = presets.get_glider_gun()
            for x, y in product(range(len(glider_gun)), range(len(glider_gun[0]))):
                if glider_gun[x][y] == 1:
                    self._board[x+10][y+10] = True
        elif preset == BoardPresets.GLIDER:
            self._board = self._make_board()
            glider: list[list[bool]] = presets.get_glider()
            for x, y in product(range(len(glider)), range(len(glider[0]))):
                self._board[x+10][y+10] = glider[x][y]
        elif preset == BoardPresets.BLINKER:
            self._board = self._make_board()
            blinker: list[list[bool]] = presets.get_blinker()
            for x, y in product(range(len(blinker)), range(len(blinker[0]))):
                self._board[x+10][y+10] = blinker[x][y]
        elif preset == BoardPresets.BEACON:
            self._board = self._make_board()
            beacon: list[list[bool]] = presets.get_beacon()
            for x, y in product(range(len(beacon)), range(len(beacon[0]))):
                self._board[x+10][y+10] = beacon[x][y]
        elif preset == BoardPresets.FUNNY_FACE:
            self._board = self._make_board()
            funny_face: str = presets.get_funny_face()
            for coords in funny_face.split(';'):
                split_coords = [int(x) for x in coords.split(',')]
                self._board[split_coords[0]+20][split_coords[1]+20] = True