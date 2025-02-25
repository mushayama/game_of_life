from dataclasses import dataclass
from .own_types import Color

@dataclass(frozen=True)
class Settings:
    FPS: int = 10

    CELL_SIZE: int = 5
    WIDTH: int = 250
    HEIGHT: int = 150
    GRID_SIZE: tuple[int, int] = (WIDTH, HEIGHT)
    SCREEN_SIZE: tuple[int, int] = (WIDTH*CELL_SIZE, HEIGHT*CELL_SIZE)

    LIFE_COLOR: Color = (30, 200, 50)
    BACKGROUND_COLOR: Color = (0, 0, 0)
    TOOLBAR_COLOR: Color = (200, 200, 200)
    BUTTON_COLOR: Color = (150, 150, 150)
    BUTTON_HOVER_COLOR: Color = (100, 100, 100)
    TEXT_COLOR: Color = (0, 0, 0)