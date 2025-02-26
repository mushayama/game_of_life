from typing import Tuple
from enum import Enum

Color = Tuple[int, int, int]
Grid = list[list[bool]]

class ButtonAction(Enum):
    PAUSE = "pause"
    STEP = "step"

class BoardPresets(Enum):
    RANDOM = "Random"
    BLANK = "Blank"
    GLIDER = "Glider"
    GLIDER_GUN = "Glider Gun"
    BLINKER = "Blinker"
    BEACON = "Beacon"
    FUNNY_FACE = "Funny Face"