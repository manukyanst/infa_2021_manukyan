import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

points = 0
try_numb = 0

def new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(100, 200)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            try_numb+=1
            a = event.pos[0]
            b = event.pos[1]
            if  ((x - a)**2 + (y - b)**2) < r**2 :
                points+=1
                print('Счет: ',points, ' Количество попыток: ', try_numb)
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
