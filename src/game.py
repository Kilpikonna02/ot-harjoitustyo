import pygame
import time
from level import Level
from gameloop import GameLoop
from eventque import EventQueue
from renderer import Renderer
from clock import Clock


LEVEL_MAP = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,3,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,0],
             [0,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

CELL_SIZE = 50

pygame.init()

height = len(LEVEL_MAP)
width = len(LEVEL_MAP[0])
display_height = height * CELL_SIZE
display_width = width * CELL_SIZE
display = pygame.display.set_mode((display_width, display_height))

font = pygame.font.SysFont("arial",50)

def message(message):
    msg = font.render(message, True, (255,0,0))
    display.blit(msg, [display_height/2+50,display_width/2])

def main():

    pygame.display.set_caption("Snake")

    level = Level(LEVEL_MAP, CELL_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock, CELL_SIZE)

    game_loop.start()

    if level.snakemoving() == False:
        pygame.quit()


if __name__ == "__main__":
    main()
