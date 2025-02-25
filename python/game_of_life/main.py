import pygame
import sys
import time
from itertools import product
from .settings import Settings
from .board import Board

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.settings: Settings = Settings()
        self.screen: pygame.Surface = pygame.display.set_mode(self.settings.SCREEN_SIZE)
        pygame.display.set_caption("Game Of Life")

        self.board = Board(self.settings.GRID_SIZE, randomize = True)


    def run(self) -> None:
        prev_update_t: float = time.time()
        paused: bool = True
        mouse_dragging: bool = False
        advance_one_step: bool = False
        while 1:
            '''
            Mouse and keyboard events
            '''
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused = not paused
                    if paused and event.key == pygame.K_RIGHT:
                        advance_one_step = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    col, row = x//self.settings.CELL_SIZE, y//self.settings.CELL_SIZE
                    self.board.set_cell((col, row), True)

                    mouse_dragging = True

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_dragging = False

                if event.type == pygame.QUIT:
                    sys.exit()

            if mouse_dragging:
                x, y = pygame.mouse.get_pos()
                col, row = x//self.settings.CELL_SIZE, y//self.settings.CELL_SIZE
                self.board.set_cell((col, row), True)

            '''
            FPS check
            '''
            if time.time() - prev_update_t<1/self.settings.FPS:
                continue
            prev_update_t = time.time()

            self.screen.fill(self.settings.BACKGROUND_COLOR)

            if not paused:
                self.board.advance()
            elif advance_one_step:
                self.board.advance()
                advance_one_step = False

            '''
            canvas update
            '''
            for x, y in product(range(self.settings.WIDTH), range(self.settings.HEIGHT)):
                coords = ((x+0.5)*self.settings.CELL_SIZE, (y+0.5)*self.settings.CELL_SIZE)
                if self.board.get_cell((x, y)):
                    pygame.draw.circle(self.screen, self.settings.LIFE_COLOR, coords, self.settings.CELL_SIZE/2)

            pygame.display.flip()

def main() -> None:
    game = Game()
    game.run()