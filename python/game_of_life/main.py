import pygame
import sys
import time
from typing import Optional
from .constants import ConfigManager
from .board import Board
from .toolbar import Toolbar
from .own_types import ButtonAction, BoardPresets

class Game:
    def __init__(self) -> None:
        pygame.init()
        self._config: ConfigManager = ConfigManager()
        self._screen: pygame.Surface = pygame.display.set_mode(self._config.screen_size)
        print(self._config.board_constants.GRID_SIZE)
        pygame.display.set_caption("Game Of Life")

        self._board: Board = Board(randomize = True)
        self._toolbar: Toolbar = Toolbar()

    def run(self) -> None:
        prev_update_t: float = time.time()
        paused: bool = True
        mouse_dragging: bool = False
        advance_one_step: bool = False
        while 1:
            '''
            Mouse, keyboard and toolbar events
            '''
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused = not paused
                    if paused and event.key == pygame.K_RIGHT:
                        advance_one_step = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    col, row = x//self._config.board_constants.CELL_SIZE, y//self._config.board_constants.CELL_SIZE
                    if col<self._config.board_constants.GRID_WIDTH and row<self._config.board_constants.GRID_HEIGHT:
                        self._board.set_cell((col, row), True)

                    mouse_dragging = True

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_dragging = False

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                toolbar_clicked: tuple[bool, Optional[ButtonAction | BoardPresets]] = self._toolbar.is_clicked(event)
                if toolbar_clicked[0] and toolbar_clicked[1]:
                    if toolbar_clicked[1] == ButtonAction.PAUSE:
                        paused = not paused
                    elif toolbar_clicked[1] == ButtonAction.STEP:
                        advance_one_step = True
                    elif isinstance(toolbar_clicked[1], BoardPresets):
                        self._board.load_preset(toolbar_clicked[1])

            if mouse_dragging:
                x, y = pygame.mouse.get_pos()
                col, row = x//self._config.board_constants.CELL_SIZE, y//self._config.board_constants.CELL_SIZE
                if col<self._config.board_constants.GRID_WIDTH and row<self._config.board_constants.GRID_HEIGHT:
                    self._board.set_cell((col, row), True)

            '''
            FPS check
            '''
            if time.time() - prev_update_t<1/self._config.game_constants.FPS:
                continue
            prev_update_t = time.time()

            '''
            lay base color
            '''
            self._screen.fill(self._config.game_constants.BACKGROUND_COLOR)

            '''
            update board
            '''
            if not paused:
                self._board.advance()
            elif advance_one_step:
                self._board.advance()
            advance_one_step = False

            '''
            draw board
            '''
            self._board.draw(self._screen)

            self._toolbar.draw(self._screen)

            pygame.display.flip()

def main() -> None:
    game = Game()
    game.run()