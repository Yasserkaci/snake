import pygame
import time
import random
# 
pygame.init()
#
RED = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
#
WIDTH = 500
HEIGHT = 600
x = WIDTH / 2
y = HEIGHT / 2
snake_pixels = [[x, y]]
#
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('my snake !')
Clock = pygame.time.Clock()
#
class Snake:
    SNAKE_SIZE = 15
    SNAKE_SPEED = 15
    def __init__(self, length:int, pixels):
        self.length = length
        self.pixels = [[x ,y]]
        self.x_speed = 0
        self.y_speed = 0
#
    def move(self, x_speed, y_speed):
        if self.length < len(self.pixels):
            self.pixels.append([x + x_speed, y + y_speed])
            del self.pixels[0]
#

    def draw_snake(self):
        for pixles in self.pixels :
           pygame.draw.rect(WIN, WHITE, [pixles[0], pixles[1], self.SNAKE_SIZE, self.SNAKE_SIZE])
#
def runing():
    game_over = False 
    snake_length = 1
    snale = Snake( snake_length, snake_pixels)
#
    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP:
                    snale.x_speed =  0
                    snale.y_speed = - snale.SNAKE_SPEED
                if event.key == pygame.K_DOWN:
                    snale.x_speed =  0
                    snale.y_speed = snale.SNAKE_SPEED
                if event.key == pygame.K_LEFT:
                    snale.x_speed =  snale.SNAKE_SPEED
                    snale.y_speed =  0
                if event.key == pygame.K_RIGHT:
                    snale.x_speed =  snale.SNAKE_SPEED
                    snale.y_speed = 0     
#
        x += snale.x_speed
        y += snale.y_speed
#
        WIN.fill(BLACK)
        snale.draw_snake()
        snale.move(x, y)
        pygame.display.update()  
        Clock.tick(snale.SNAKE_SPEED)
#
    pygame.quit
    quit          
#
runing()                     