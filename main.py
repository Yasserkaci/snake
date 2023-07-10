import pygame
from pygame import Vector2
import sys
import random

pygame.init()

class Snake:
    def __init__(self):
        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
        
        self.body = [Vector2(10, 10),Vector2(10, 11),Vector2(10, 12)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
            self.update_head_graphics()
            self.update_tail_graphics()

            for index,block in enumerate(self.body):
                x_pos = int(block.x * CELL_SIZE)
                y_pos = int(block.y * CELL_SIZE)
                block_rect = pygame.Rect(x_pos,y_pos,CELL_SIZE,CELL_SIZE)

                if index == 0:
                    win.blit(self.head,block_rect)
                elif index == len(self.body) - 1:
                    win.blit(self.tail,block_rect)
                else:
                    previous_block = self.body[index + 1] - block
                    next_block = self.body[index - 1] - block
                    if previous_block.x == next_block.x:
                        win.blit(self.body_vertical,block_rect)
                    elif previous_block.y == next_block.y:
                        win.blit(self.body_horizontal,block_rect)
                    else:
                        if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                            win.blit(self.body_tl,block_rect)
                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            win.blit(self.body_bl,block_rect)
                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            win.blit(self.body_tr,block_rect)
                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            win.blit(self.body_br,block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        if self.add_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)



class Fruit:
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.v = Vector2(self.x, self.y)

    def draw_fruit(self):
        self.pos = Vector2(self.v.x * CELL_SIZE, self.v.y * CELL_SIZE )
        #pygame.draw.rect(win, FRUIT_COLOR, (self.pos.x, self.pos.y, CELL_SIZE, CELL_SIZE ))
        rect = pygame.Rect(self.pos.x, self.pos.y, CELL_SIZE, CELL_SIZE )
        win.blit(appl, rect)


class main:
    def __init__(self):



        self.snake = Snake()
        self.fruit = Fruit()
        self.run   = True
    def update(self):
        main.snake.move_snake()
        self.check_colegion()
        
    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
    
    def game_over(self):
        self.run = False

    def check_colegion(self):
        if (self.fruit.x, self.fruit.y) == self.snake.body[0]:
            self.fruit.x = random.randint(0, CELL_NUMBER - 1)
            self.fruit.y = random.randint(0, CELL_NUMBER-1)
            self.fruit.v = Vector2(self.fruit.x, self.fruit.y)
            self.snake.body.insert(-1, self.snake.body[-1] )

        if self.snake.body[0] in self.snake.body[1:]:
            self.run = False
        if  not(0 <= self.snake.body[0].x <= CELL_NUMBER -1 ):
            self.game_over()
            
        if not (0 <= self.snake.body[0].y <= CELL_NUMBER - 1):
            self.game_over()

RED = (255, 0, 0)
GREEN = (175, 215, 70)
BLUE = (183,191, 255)
FRUIT_COLOR =   (129,166,114)
appl = pygame.image.load('Graphics/apple.png')


CELL_SIZE = 40
CELL_NUMBER = 15


win = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE,CELL_NUMBER*CELL_SIZE))
pygame.display.set_caption("snake !")
clock = pygame.time.Clock()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 100)
main = main()


while main.run :
    win.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            main.run = False
        if event.type == screen_update:
            main.update()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN :
                if main.snake.direction.y != -1: 
                    main.snake.direction = Vector2(0,1)
            if event.key == pygame.K_UP : 
                if main.snake.direction.y != 1 :
                    main.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_LEFT : 
                if main.snake.direction.x != 1 :
                    main.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT : 
                if main.snake.direction.x != -1 :
                    main.snake.direction = Vector2(1,0)
               


    main.draw_elements()
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
sys.exit()
        