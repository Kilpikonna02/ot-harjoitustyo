import pygame
from gameloop import GameLoop


def main():

    pygame.init()

    display_height = 600
    display_width = 600
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Snake")


    game_loop = GameLoop(display)
    game_loop.startgame()


if __name__ == "__main__":
    main()
