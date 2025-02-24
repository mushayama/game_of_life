# import sys
# import time
# import random
# import pygame
# from itertools import product
# from .game.button import Button

# FPS = 10
# CELL_SIZE = 5
# GRID_SIZE = (WIDTH, HEIGHT) = (250,150)
# TOOLBAR_HEIGHT = 50
# SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (WIDTH*CELL_SIZE, HEIGHT*CELL_SIZE + TOOLBAR_HEIGHT)

# GREEN = 30, 200, 50
# BLACK = 0, 0, 0
# GRAY = (200, 200, 200)

# pygame.init()
# screen = pygame.display.set_mode(SCREEN_SIZE)
# pygame.display.set_caption("Game Of Life")

# def make_board(width: int, height: int, randomize: bool = False) -> list[list[int]]:
#     if randomize:
#         new_board = [
#             [random.choice([0,1]) for _ in range(height)]
#             for _ in range(width)
#         ]
#     else:
#         new_board = [
#             [0 for _ in range(height)]
#             for _ in range(width)
#         ]
#     return new_board

# def get_neighbour_count(board: list[list[int]], x: int, y: int) -> int:
#     neighbour_count = 0
#     width = len(board)
#     height = len(board[0])
#     for delta_x in [-1,0,1]:
#         for delta_y in [-1,0,1]:
#             nx = (x+delta_x)%width
#             ny = (y+delta_y)%height
#             neighbour_count += board[nx][ny]
#     return neighbour_count-board[x][y]

# def advance(board: list[list[int]]) -> list[list[int]]:
#     width = len(board)
#     height = len(board[0])
#     new_board = make_board(width, height)
#     coords = product(range(width), range(height))
#     for x, y in coords:
#         neighbour_count = get_neighbour_count(board,x,y)
#         if board[x][y] == 1 and neighbour_count in [2,3]:
#             new_board[x][y] = 1
#         if board[x][y] == 0 and neighbour_count in [3]:
#             new_board[x][y] = 1
#     return new_board

# def draw_toolbar():
#     pygame.draw.rect(screen, GRAY, pygame.Rect(0, 0, SCREEN_WIDTH, 50))  # Toolbar background
#     for button in buttons:
#         button.draw(screen)

# board = make_board(WIDTH, HEIGHT, randomize=True)

# buttons = [
#     Button(10, 10, 100, 30, "Pause", action="pause"),
#     Button(120, 10, 100, 30, "Step", action="step"),
#     Button(230, 10, 100, 30, "Random", action="random"),
#     Button(340, 10, 100, 30, "Blank", action="blank"),
# ]

# prev_update_t = time.time()
# paused = True
# mouse_dragging = False
# running = True
# while running:
#     '''
#     Mouse and keyboard events
#     '''
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 paused = not paused

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = pygame.mouse.get_pos()
#             col, row = x//CELL_SIZE, y//CELL_SIZE

#             state = board[col][row]
#             board[col][row] = 1
#             mouse_dragging = True

#         if event.type == pygame.MOUSEBUTTONUP:
#             mouse_dragging = False

#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     if mouse_dragging:
#         x, y = pygame.mouse.get_pos()
#         col, row = x//CELL_SIZE, y//CELL_SIZE
#         board[col][row] = 1

#     '''
#     FPS check
#     '''
#     if time.time() - prev_update_t<1/FPS:
#         continue
#     prev_update_t = time.time()

#     screen.fill(BLACK)

#     if not paused:
#         board = advance(board)

#     '''
#     canvas update
#     '''
#     for x, y in product(range(WIDTH), range(HEIGHT)):
#         coords = ((x+0.5)*CELL_SIZE, (y+0.5)*CELL_SIZE)
#         if board[x][y]:
#             pygame.draw.circle(screen, GREEN, coords, CELL_SIZE/2)

#     draw_toolbar()

#     pygame.display.flip()