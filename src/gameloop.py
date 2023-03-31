import pygame
from gameover import Gameover
from start import Start
from wall import Wall
from score import Score
from random import randint


class GameLoop:
    def __init__(self, display):
        self._display = display
        self.snake_body_size = 20
        self.tickspeed = 20
        self.clock = pygame.time.Clock()
        x,y = self._display.get_size()
        self._display_width = x
        self._display_height = y
        self.game_start = True

    
    def snakes(self, snakebody, list):
        for i in list:
            pygame.draw.rect(self._display,(0,0,0),[i[0],i[1],snakebody,snakebody])
    
    def startgame(self):
        while self.game_start == True:
            start = Start(self._display)
            start.start_screen()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.game()
                        self.game_start = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()


    def game(self):

        game_over = False
        game_close = False

        self.snake_posx = (self._display_width/2)
        self.snake_posy = (self._display_height/2)

        self.snake_speed_x = 0
        self.snake_speed_y = 0

        size = self._display_width/15

        self.pointx = round(randint(size,self._display_width-size-self.snake_body_size)/20)*20
        self.pointy = round(randint(size,self._display_height-size-self.snake_body_size)/20)*20

        self.snakesbody = []
        self.snakelenght = 1

        game_end = Gameover(self._display)
        wall = Wall(self._display,size)
        score = Score(self._display)

        while not game_close:

            while game_over == True:
                game_end.game_over_screen(self.snakelenght-1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_q:
                            game_close = True
                            game_over = False
                        if event.key == pygame.K_r:
                            self.game_start = True
                            self.startgame()

            for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.snake_speed_x = -self.snake_body_size
                            self.snake_speed_y = 0
                        if event.key == pygame.K_RIGHT:
                            self.snake_speed_x = self.snake_body_size
                            self.snake_speed_y = 0
                        if event.key == pygame.K_UP:
                            self.snake_speed_x = 0
                            self.snake_speed_y = -self.snake_body_size
                        if event.key == pygame.K_DOWN:
                            self.snake_speed_x = 0
                            self.snake_speed_y = self.snake_body_size
                    elif event.type == pygame.QUIT:
                        game_close = True
            
            if self.snake_posx >= self._display_width-size or self.snake_posy >= self._display_height-size or self.snake_posx < size or self.snake_posy < size:
                game_over = True
            
            self.snake_posx += self.snake_speed_x
            self.snake_posy += self.snake_speed_y
            self._display.fill((150,255,110))
            pygame.draw.rect(self._display,(255,0,0), [self.pointx,self.pointy,self.snake_body_size,self.snake_body_size])
            snake_head = []
            snake_head.append(self.snake_posx)
            snake_head.append(self.snake_posy)
            self.snakesbody.append(snake_head)
            if len(self.snakesbody) > self.snakelenght:
                del self.snakesbody[0]
            for i in self.snakesbody[:-1]:
                if i == snake_head:
                    game_over = True
            self.snakes(self.snake_body_size,self.snakesbody)
            wall.draw()
            score.draw_scrore(self.snakelenght-1)

            pygame.display.update()

            if self.snake_posx == self.pointx and self.snake_posy == self.pointy:
                self.pointx = round(randint(size,self._display_width-size-self.snake_body_size)/20)*20
                self.pointy = round(randint(size,self._display_height-size-self.snake_body_size)/20)*20
                self.snakelenght += 1
            
            self.clock.tick(self.tickspeed)
        pygame.quit()
        quit()


   
