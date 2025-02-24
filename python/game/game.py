import pygame
import random
import sys
import time
from itertools import product
from game import Settings
from game.types import Color, Grid

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.settings: Settings = Settings()
        self.screen: pygame.Surface = pygame.display.set_mode(self.settings.SCREEN_SIZE)
        pygame.display.set_caption("Game Of Life")

    def _make_board(self, width: int, height: int, randomize: bool = False) -> Grid:
        new_board: Grid = [[]]
        if randomize:
            new_board = [
                [random.choice([0,1]) for _ in range(height)]
                for _ in range(width)
            ]
        else:
            new_board = [
                [0 for _ in range(height)]
                for _ in range(width)
            ]
        return new_board

    def _get_neighbour_count(self, board: Grid, x: int, y: int) -> int:
        neighbour_count: int = 0
        width: int = len(board)
        height: int = len(board[0])
        for delta_x in [-1,0,1]:
            for delta_y in [-1,0,1]:
                nx: int = (x+delta_x)%width
                ny: int = (y+delta_y)%height
                neighbour_count += board[nx][ny]
        return neighbour_count-board[x][y]

    def _advance(self, board: Grid) -> Grid:
        width: int = len(board)
        height: int = len(board[0])
        new_board: Grid = self._make_board(width, height)
        coords: product[tuple[int,int]] = product(range(width), range(height))
        for x, y in coords:
            neighbour_count: int = self._get_neighbour_count(board,x,y)
            if board[x][y] == 1 and neighbour_count in [2,3]:
                new_board[x][y] = 1
            if board[x][y] == 0 and neighbour_count in [3]:
                new_board[x][y] = 1
        return new_board

    def run(self) -> None:
        prev_update_t: float = time.time()
        board: Grid = self._make_board(self.settings.WIDTH, self.settings.HEIGHT, randomize=True)
        paused: bool = True
        mouse_dragging: bool = False
        while 1:
            '''
            Mouse and keyboard events
            '''
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused = not paused

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    col, row = x//self.settings.CELL_SIZE, y//self.settings.CELL_SIZE

                    board[col][row] = 1
                    mouse_dragging = True

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_dragging = False

                if event.type == pygame.QUIT:
                    sys.exit()

            if mouse_dragging:
                x, y = pygame.mouse.get_pos()
                col, row = x//self.settings.CELL_SIZE, y//self.settings.CELL_SIZE
                board[col][row] = 1

            '''
            FPS check
            '''
            if time.time() - prev_update_t<1/self.settings.FPS:
                continue
            prev_update_t = time.time()

            self.screen.fill(self.settings.BACKGROUND_COLOR)

            if not paused:
                board = self._advance(board)

            '''
            canvas update
            '''
            for x, y in product(range(self.settings.WIDTH), range(self.settings.HEIGHT)):
                coords = ((x+0.5)*self.settings.CELL_SIZE, (y+0.5)*self.settings.CELL_SIZE)
                if board[x][y]:
                    pygame.draw.circle(self.screen, self.settings.LIFE_COLOR, coords, self.settings.CELL_SIZE/2)

            pygame.display.flip()