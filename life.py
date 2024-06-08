import pygame
import toroidal_rules
from sys import exit
# import seeds


def init_state(width: int, height: int):
    """
    Create and return a blank 2D state (filled with zeros)
    of the specified width and height.
    :param width:
    :param height:
    :return: A blank 2D state list.
    """
    return [[0 for _ in range(width)] for _ in range(height)]


def blit_state(screen_p, state_p: list[list[int]]):
    for i in range(len(state_p)):
        for j in range(len(state_p[i])):
            # edge cells (border)
            # if i == 0 or j == 0 or i == len(state_p)-1 or j == len(state_p[0])-1:
            #     cell_surf.fill("Black")
            #     screen_p.blit(cell_surf, (j*CELL_SIZE, i*CELL_SIZE))

            # live cells
            if state_p[i][j] == 1:
                cell_surf.fill("White")
                screen_p.blit(cell_surf, (j*CELL_SIZE, i*CELL_SIZE))
            elif state_p[i][j] == 0:
                cell_surf.fill("Black")
                screen_p.blit(cell_surf, (j*CELL_SIZE, i*CELL_SIZE))


# state = seeds.glider_state
state = init_state(70, 40)


# constants
GRID_WIDTH, GRID_HEIGHT = len(state[0]), len(state)
GRID_SIZE = (GRID_WIDTH, GRID_HEIGHT)

CELL_SIZE = 20

SCREEN_WIDTH, SCREEN_HEIGHT = GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

UPDATE_TIME = 0.1
FRAME_INTERVAL = int(UPDATE_TIME * 60)  # number of frames between updates


# setup
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Game of Life")
icon_surf = pygame.image.load("graphics/icon.png").convert()
pygame.display.set_icon(icon_surf)

clock = pygame.time.Clock()
frame = 1
tick = 1


# surfs
# bg_surf = pygame.Surface(SCREEN_SIZE)
# bg_surf.fill("#222222")  # dark grey
# bg_surf.fill("Black")

cell_surf = pygame.Surface((CELL_SIZE, CELL_SIZE))
cell_surf.fill("White")

# cell_surf = pygame.image.load("graphics/cell.png").convert()  # 20 x 20


# game states
selection_mode = True
generation_mode = False

original_state = state


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if selection_mode:
        mouse_buttons: tuple = pygame.mouse.get_pressed()

        # left click to select
        if mouse_buttons[0]:
            pos = pygame.mouse.get_pos()
            # allow "toroidal" drawing outside window
            cell_x = (pos[0] // CELL_SIZE) % GRID_WIDTH
            cell_y = (pos[1] // CELL_SIZE) % GRID_HEIGHT

            # toggle state on click
            if state[cell_y][cell_x] == 0:
                state[cell_y][cell_x] = 1

        # right click to deselect
        if mouse_buttons[2]:
            pos = pygame.mouse.get_pos()
            cell_x = pos[0] // CELL_SIZE
            cell_y = pos[1] // CELL_SIZE

            # toggle state on click
            if state[cell_y][cell_x] == 1:
                state[cell_y][cell_x] = 0

        # escape to clear all selections
        if keys[pygame.K_ESCAPE]:
            for row in state:
                for i in range(len(row)):
                    row[i] = 0

        # return (enter) to enter generation mode
        if keys[pygame.K_RETURN]:
            original_state = state
            selection_mode = False
            generation_mode = True

        blit_state(screen, state)

    if generation_mode:
        if FRAME_INTERVAL == 0:  # maximum speed
            on_update_tick = True
        else:
            on_update_tick = frame % FRAME_INTERVAL == 0

        if frame == 1:
            # screen.blit(bg_surf, (0, 0))
            blit_state(screen, state)

        if on_update_tick:
            # screen.blit(bg_surf, (0, 0))
            blit_state(screen, state)
            state = toroidal_rules.update_state(state)  # toroidal grid
            tick += 1

        # space to pause generation,
        # enter selection mode
        if keys[pygame.K_SPACE]:
            generation_mode = False
            selection_mode = True

        # R to restart from original state,
        # enter selection mode
        if keys[pygame.K_r]:
            state = original_state
            generation_mode = False
            selection_mode = True

        frame += 1

    pygame.display.update()  # update screen
    clock.tick(60)  # limit fps to 60
