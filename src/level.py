import pygame
import time
from sprites.snake import Snake
from sprites.wall import Wall
from sprites.floor1 import Floor1
from sprites.floor2 import Floor2

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.snake = None
        self.wall = pygame.sprite.Group()
        self.floor1 = pygame.sprite.Group()
        self.floor2 = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites(level_map)

    def _initialize_sprites(self, level_map):
        self.height = len(level_map)
        self.width = len(level_map[0])

        for y in range(self.height):
            for x in range(self.width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.wall.add(Wall(normalized_x, normalized_y))
                elif cell == 1:
                    self.floor1.add(Floor1(normalized_x, normalized_y))
                elif cell == 2:
                    self.floor2.add(Floor2(normalized_x, normalized_y))
                elif cell == 3:
                    self.snake = Snake(normalized_x, normalized_y)
                    self.floor1.add(Floor1(normalized_x, normalized_y))

        self.all_sprites.add(
            self.floor1,
            self.wall,
            self.floor2,
            self.snake
        )    

    def move_snake(self,dx=0,dy=0):
        if not self._snake_can_move(dx,dy):
            print("GAME OVER")
            time.sleep(2)
            return pygame.quit()
        self.snake.rect.move_ip(dx,dy)


    
    
    def _snake_can_move(self, dx=0, dy=0):
        self.snake.rect.move_ip(dx, dy)

        colliding_walls = pygame.sprite.spritecollide(self.snake, self.wall, False)

        can_move = not colliding_walls

        self.snake.rect.move_ip(-dx, -dy)

        return can_move
