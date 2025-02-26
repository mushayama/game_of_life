import pygame
from typing import Optional
from .constants import ConfigManager
from .own_types import Color, ButtonAction, BoardPresets
from .button import Button
from .dropdown import DropdownMenu

class Toolbar:
    def __init__(self) -> None:
        self._config: ConfigManager = ConfigManager()
        self._x_begin: int = self._config.toolbar_constants.TOOLBAR_X_BEGIN
        self._y_begin: int = self._config.board_constants.BOARD_HEIGHT
        self._width: int = self._config.board_constants.BOARD_WIDTH
        self._height: int = self._config.toolbar_constants.TOOLBAR_HEIGHT
        self._toolbar_color: Color = self._config.toolbar_constants.TOOLBAR_COLOR
        self._top_margin: int = self._config.toolbar_constants.TOP_MARGIN

        self._buttons: list[DropdownMenu | Button] = [
            DropdownMenu(
                BoardPresets.RANDOM,
                list(BoardPresets),
                self._config.preset_dropdown_x_begin,
                self._y_begin + self._top_margin
                ),
            Button("Pause", ButtonAction.PAUSE, self._config.pause_button_x_begin, self._y_begin + self._top_margin),
            Button("Step", ButtonAction.STEP, self._config.step_button_x_begin, self._y_begin + self._top_margin),
        ]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen,
                         self._toolbar_color,
                         pygame.Rect(self._x_begin, self._y_begin, self._width, self._height)
                         )  # Toolbar background

        for button in self._buttons:
            button.draw(screen)

    def is_clicked(self, event: pygame.event.Event) -> tuple[bool, Optional[ButtonAction | BoardPresets]]:
        button_clicked: bool = False
        action: Optional[ButtonAction | BoardPresets] = None
        for button in self._buttons:
            if button.is_clicked(event):
                button_clicked = True
                action = button.get_action()

        return (button_clicked, action)