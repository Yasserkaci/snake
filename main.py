import pygame
import sys
pygame.init()

class Fruit:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.v = pygame.Vector2(self.x, self.y)

    def draw_fruit(self):
        pygame.draw.rect(win, RED, (self.v.x * CELL_NUMBER, self.v.y * CELL_NUMBER, CELL_SIZE, CELL_SIZE ))

RED = (255, 0, 0)
GREEN = (175, 215, 70)


CELL_SIZE = 40
CELL_NUMBER = 15


win = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE,CELL_NUMBER*CELL_SIZE))
pygame.display.set_caption("snake !")
clock = pygame.time.Clock()

while True :
    win.fill(GREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

        
    fruit = Fruit()
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)