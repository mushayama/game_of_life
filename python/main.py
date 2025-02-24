import sys
import time
import random
import pygame
from itertools import product

FPS = 10
CELL_WIDTH = 5
GRID_SIZE = (WIDTH, HEIGHT) = (250,150)
SCREEN_SIZE = WIDTH*CELL_WIDTH, HEIGHT*CELL_WIDTH

GREEN = 30, 200, 50
BLACK = 0, 0, 0

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Game Of Life")

def make_board(width, height, randomize=False):
    if randomize:
        new_board = [
            [random.choice([0,1]) for y in range(height)]
            for x in range(width)
        ]
    else:
        new_board = [
            [0 for y in range(height)]
            for x in range(width)
        ]
    return new_board

def get_neighbour_count(board, x, y):
    neighbour_count = 0
    width = len(board)
    height = len(board[0])
    for delta_x in [-1,0,1]:
        for delta_y in [-1,0,1]:
            nx = (x+delta_x)%width
            ny = (y+delta_y)%height
            neighbour_count += board[nx][ny]
    return neighbour_count-board[x][y]

def advance(board):
    width = len(board)
    height = len(board[0])
    new_board = make_board(width, height)
    coords = product(range(width), range(height))
    for x, y in coords:
        neighbour_count = get_neighbour_count(board,x,y)
        if board[x][y] == 1 and neighbour_count in [2,3]:
            new_board[x][y] = 1
        if board[x][y] == 0 and neighbour_count in [3]:
            new_board[x][y] = 1
    return new_board

prev_update_t = time.time()
board = make_board(WIDTH, HEIGHT, randomize=True)
paused = True
mouse_dragging = False
while 1:
    '''
    Mouse and keyboard events
    '''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                paused = not paused

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col, row = x//CELL_WIDTH, y//CELL_WIDTH

            state = board[col][row]
            board[col][row] = 1
            mouse_dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_dragging = False

        if event.type == pygame.QUIT:
            sys.exit()

    if mouse_dragging:
        x, y = pygame.mouse.get_pos()
        col, row = x//CELL_WIDTH, y//CELL_WIDTH
        board[col][row] = 1

    '''
    FPS check
    '''
    if time.time() - prev_update_t<1/FPS:
        continue
    prev_update_t = time.time()

    screen.fill(BLACK)

    if not paused:
        board = advance(board)

    '''
    canvas update
    '''
    for x, y in product(range(WIDTH), range(HEIGHT)):
        coords = ((x+0.5)*CELL_WIDTH, (y+0.5)*CELL_WIDTH)
        if board[x][y]:
            pygame.draw.circle(screen, GREEN, coords, CELL_WIDTH/2)

    pygame.display.flip()