# import pygame

# BUTTON_COLOR = (150, 150, 150)
# BUTTON_HOVER_COLOR = (100, 100, 100)
# TEXT_COLOR = (0, 0, 0)

# class Button:
#     def __init__(self, x: int, y: int, width: int, height: int, text: str, action: str = None) -> None:
#         self.rect = pygame.Rect(x, y, width, height)
#         self.text = text
#         self.action = action
#         self.font = pygame.font.SysFont(None, 24)

#     def draw(self, screen: pygame.Surface) -> None:
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#         if self.rect.collidepoint(mouse_x, mouse_y):
#             pygame.draw.rect(screen, BUTTON_HOVER_COLOR, self.rect)
#         else:
#             pygame.draw.rect(screen, BUTTON_COLOR, self.rect)

#         text_surface = self.font.render(self.text, True, TEXT_COLOR)
#         text_rect = text_surface.get_rect(center=self.rect.center)
#         screen.blit(text_surface, text_rect)

#     def is_clicked(self) -> bool:
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#         if self.rect.collidepoint(mouse_x, mouse_y):
#             if pygame.mouse.get_pressed()[0]:
#                 return True
#         return False
