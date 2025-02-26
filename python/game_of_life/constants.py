from dataclasses import dataclass
from typing import Optional
from .own_types import Color

@dataclass(frozen=True)
class GameConstants:
    FPS: int = 10
    BACKGROUND_COLOR: Color = (0, 0, 0)

@dataclass(frozen=True)
class BoardConstants:
    GRID_WIDTH: int = 250
    GRID_HEIGHT: int = 150
    CELL_SIZE: int = 5
    LIFE_COLOR: Color = (30, 200, 50)

    @property
    def GRID_SIZE(self) -> tuple[int, int]:
        return (self.GRID_WIDTH, self.GRID_HEIGHT)

    @property
    def BOARD_HEIGHT(self) -> int:
        return self.GRID_HEIGHT * self.CELL_SIZE

    @property
    def BOARD_WIDTH(self) -> int:
        return self.GRID_WIDTH * self.CELL_SIZE

@dataclass(frozen=True)
class ToolbarConstants:
    TOP_MARGIN: int = 10
    TOOLBAR_X_BEGIN: int = 0
    TOOLBAR_HEIGHT: int = 50
    TOOLBAR_COLOR: Color = (200, 200, 200)

@dataclass(frozen=True)
class ButtonConstants:
    BUTTON_WIDTH: int = 100
    BUTTON_HEIGHT: int = 30
    BUTTON_COLOR: Color = (150, 150, 150)
    BUTTON_HOVER_COLOR: Color = (100, 100, 100)
    TEXT_COLOR: Color = (0, 0, 0)

class ConfigManager:
    _instance: Optional["ConfigManager"] = None
    game_constants: GameConstants
    board_constants: BoardConstants
    toolbar_constants: ToolbarConstants
    button_constants: ButtonConstants

    def __new__(cls) -> "ConfigManager":
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.game_constants = GameConstants()
            cls._instance.board_constants = BoardConstants()
            cls._instance.toolbar_constants = ToolbarConstants()
            cls._instance.button_constants = ButtonConstants()
        return cls._instance

    @property
    def screen_height(self) -> int:
        return self.board_constants.BOARD_HEIGHT + self.toolbar_constants.TOOLBAR_HEIGHT

    @property
    def screen_size(self) -> tuple[int, int]:
        return (self.board_constants.BOARD_WIDTH, self.screen_height)

    @property
    def pause_button_x_begin(self) -> int:
        return self.board_constants.BOARD_WIDTH//2 - self.button_constants.BUTTON_WIDTH//2

    @property
    def step_button_x_begin(self) -> int:
        return self.board_constants.BOARD_WIDTH*3//4 - self.button_constants.BUTTON_WIDTH//2

    @property
    def preset_dropdown_x_begin(self) -> int:
        return self.board_constants.BOARD_WIDTH//4 - self.button_constants.BUTTON_WIDTH//2