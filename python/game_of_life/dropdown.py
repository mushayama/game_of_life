import pygame
from .constants import ConfigManager
from .own_types import BoardPresets

class DropdownMenu:
    def __init__(self, initialState : BoardPresets, options: list[BoardPresets], x_begin: int, y_begin: int):
        self._config: ConfigManager = ConfigManager()
        self._rect = pygame.Rect(
            x_begin,
            y_begin,
            self._config.button_constants.BUTTON_WIDTH,
            self._config.button_constants.BUTTON_HEIGHT
            )
        self._options: list[BoardPresets] = options
        self._open: bool = False
        self._selected: BoardPresets = initialState
        self._option_rects: list[pygame.Rect] = []
        self._font = pygame.font.SysFont(None, 24)

    def draw(self, screen: pygame.Surface) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, self._config.button_constants.BUTTON_HOVER_COLOR, self._rect)
        else:
            pygame.draw.rect(screen, self._config.button_constants.BUTTON_COLOR, self._rect)
        text_surface = self._font.render(self._selected.value, True, self._config.button_constants.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self._rect.center)
        screen.blit(text_surface, text_rect)

        # # Draw the dropdown options if open
        if self._open:
            i = 0
            for option in self._options:
                if option == self._selected:
                    continue
                option_rect = pygame.Rect(self._rect.x, self._rect.y - (i + 1) * 30, self._rect.width, self._rect.height)
                self._option_rects.append(option_rect)
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if option_rect.collidepoint(mouse_x, mouse_y):
                    pygame.draw.rect(screen, self._config.button_constants.BUTTON_HOVER_COLOR, option_rect)
                else:
                    pygame.draw.rect(screen, self._config.button_constants.BUTTON_COLOR, option_rect)
                text_surface = self._font.render(option.value, True, self._config.button_constants.TEXT_COLOR)
                text_rect = text_surface.get_rect(center=option_rect.center)
                screen.blit(text_surface, text_rect)
                i += 1

    def is_clicked(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if self._rect.collidepoint(mouse_x, mouse_y):
                self._open = not self._open  # Toggle dropdown
                return False
            if self._open:
                for i, option_rect in enumerate(self._option_rects):
                    if option_rect.collidepoint(mouse_x, mouse_y):
                        if self._options.index(self._selected)<=i:
                            i+=1
                        self._selected = self._options[i]
                        self._open = not self._open
                        return True
        return False

    def get_action(self) -> BoardPresets:
        return self._selected
