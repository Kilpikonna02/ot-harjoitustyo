import pygame
import time

class GameLoop:
    def __init__(self, level, renderer, event_queue, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self.snake_speed_x = 0
        self.snake_speed_y = 0
        self.speed = 5
        
    def start(self):
        while True:
            if self._handle_events() == False:
                break

            self._render()

            self._clock.tick(60)


    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake_speed_x = -self.speed
                    self.snake_speed_y = 0
                if event.key == pygame.K_RIGHT:
                    self.snake_speed_x = self.speed
                    self.snake_speed_y = 0
                if event.key == pygame.K_UP:
                    self.snake_speed_x = 0
                    self.snake_speed_y = -self.speed
                if event.key == pygame.K_DOWN:
                    self.snake_speed_x = 0
                    self.snake_speed_y = self.speed
            elif event.type == pygame.QUIT:
                return False
        self._level.move_snake(dx=self.snake_speed_x)
        self._level.move_snake(dy=self.snake_speed_y)
        
    def _render(self):
        self._renderer.render()
