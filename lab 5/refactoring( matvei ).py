import pygame
from pygame.draw import *

pygame.init()

#цвета rgb
purple = (255, 20, 147)
beige = (255, 228, 196)
black = (0, 0, 0)
grey = (119, 136, 153)
white = (255, 245, 238)
red = (255, 0, 0)
brown = (173, 135, 98)
pesoch = (255, 165, 0)


FPS = 30

screen = pygame.display.set_mode((1000, 500))

"прорисовка фона картины"

rect (screen, (135, 206, 235), (0, 0, 1000, 250))
rect (screen, (60, 179, 113), (0, 250, 1000, 250))


def boy (surface, x, y, a):
    
    """ Функция рисует мальчика
        x, y - координаты головы
        a - размеры мальчика
        color - цвет одежды """
    lines (surface, black, False, [(x - 2.5 * a, y + 4 * a), (x, y + a), (x + 2.5 *a, y + 4 * a)])
    lines (surface, black, False, [(x, y + 5 * a), (x - a, y + 8 * a),(x - 2 * a, y + 8 * a)])
    lines (surface, black, False, [(x, y + 5 * a), (x + a, y + 8 * a),(x + 2 * a, y + 8 * a)])
    ellipse(surface, grey, (x - a, y, 2 * a, 6 * a))
    circle (surface, beige, (x, y), a)

       
def girl (surface, x, y, a):
    
    """ Функция рисует девочку
        x, y - координаты головы
        a - размеры девочки
        color - цвет одежды """
    lines (surface, black, False, [(x - 2.5 * a, y + 4 * a), (x, y + a), (x + 2.5 *a, y + 4 * a)])
    polygon (surface, purple, [(x, y), (x - 1.5 * a, y + 6 * a), (x + 1.5 * a, y + 6 * a)])
    circle (surface, beige, (x, y), a)
    lines (surface, black, False, [(x - 0.5 * a, y + 6 * a), (x - 0.5 * a, y + 8 * a), (x - a, y + 8 * a)])
    lines (surface, black, False, [(x + 0.5 * a, y + 6 * a), (x + 0.5 * a, y + 8 * a), (x + a, y + 8 * a)])


def ice_cream (surface, x, y, a):
    """ Функция рисует девочку
        x, y - координаты конца рожка
        a - размеры мороженного """

    polygon (surface,  pesoch, [(x , y), (x + a, y - 3*a), (x - a, y - 3*a)])
    circle (surface, brown, (x - 0.5 * a, y - 3.45 * a), 0.75 * a)
    circle (surface, white, (x + 0.5 * a, y - 3.45 * a), 0.75 * a)
    circle (surface, red, (x, y - 4 * a), 0.75 * a)
   

def rotation (function, x, y, a, angle):
    """ Функция, поворачивающая изображение на определенный угол
        function - функция изображения
        x, y , a - параметры функции
        angle - угол поворота """
    sur1 = pygame.Surface([1000, 500], pygame.SRCALPHA, 32)
    sur1 = sur1.convert_alpha()
    function(sur1, x, y+200, a)
    sur2 = pygame.transform.rotate( sur1, angle)
    screen.blit(sur2 ,(0, 0))

" изображение шарика "

line(screen, (0, 0, 0), (100, 300), (100, 175))
polygon(screen, (255, 0, 0), [(100, 175), (90, 105), (45, 140)])
circle(screen, (255, 0, 0), (70, 100), 20)
circle(screen, (255, 0, 0), (50, 120), 20)


" вызов всех функций, чтобы нарисовать картинку"   

girl(screen, 400, 140, 40)
girl(screen, 600, 140, 40)
boy(screen, 800, 140, 40)
boy(screen, 200, 140, 40)
ice_cream(screen, 500, 130, 27)


line( screen, black, (500, 300), (500, 130))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
