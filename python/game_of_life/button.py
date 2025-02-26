import pygame
from .constants import ConfigManager
from .own_types import ButtonAction, Color

class Button:
    def __init__(self, text: str, action: ButtonAction, x_begin: int, y_begin: int) -> None:
        self._config: ConfigManager = ConfigManager()
        self._rect = pygame.Rect(
            x_begin,
            y_begin,
            self._config.button_constants.BUTTON_WIDTH,
            self._config.button_constants.BUTTON_HEIGHT
            )
        self._text: str = text
        self._action: ButtonAction = action
        self._font = pygame.font.SysFont(None, 24)
        self._clicked: bool = False

    def draw(self, screen: pygame.Surface) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, self._config.button_constants.BUTTON_HOVER_COLOR, self._rect)
        else:
            pygame.draw.rect(screen, self._config.button_constants.BUTTON_COLOR, self._rect)

        text_surface = self._font.render(self._text, True, self._config.button_constants.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self._rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self._rect.collidepoint(mouse_x, mouse_y):
                if not self._clicked:
                    self._clicked = True
                    return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Release left click
            self._clicked = False
        return False

    def get_action(self) -> ButtonAction:
        return self._action
