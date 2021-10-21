import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 80
A = 1200
B = 900
screen = pygame.display.set_mode((1200, 900))

" Цвета шариков "

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

BALL = []

n = 60


def new_ball():
    ''' создает новый шарик '''
    global x, y, r, color
    x = randint(100, 1100)
    y = randint(200, 800)
    r = randint(20, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def move_ball(x, y, r, color):
    """
    рисует шарик в новом местоположении
    x, y - координаты шарика
    r - радиус шарика
    color - цвет шарика

    """
    circle(screen, color, (x, y), r)




pygame.display.update()
clock = pygame.time.Clock()
finished = False


""" Создание массива шариков с их данными:\
    [<абцисса>, <ордината>, <радиус>, <цвет>, <горизонтальная скорость>, <вертикальная скорость>]
"""
for i in range(n):
    new_ball()
    BALL.append([x, y, r, color, randint(-5,5), randint(-5, 5)])
    

" Подсчет очков "

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Число очков: ', True,
                  (180, 180, 0))

end = pygame.font.Font(None, 100)
text_end = end.render(' Ура, победа!!! ', True,
                      (200, 200, 0))


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            try_numb+= 1
            a = event.pos[0]
            b = event.pos[1]
            
# Проверяет, было ли попадание по какому-то шарику 
            for i in range(n):
                if  ((BALL[i - 1][0] - a)**2 + (BALL[i - 1][1] - b)**2) < (BALL[i - 1][2])**2 :
                    BALL[i - 1][2] = 0
                    points+=1
                    print('Счет: ',points, ' Количество попыток: ', try_numb)

# Отскакивание шарика от стенок              
    for i in range(n):
        if (BALL[i - 1][0] < (A - BALL[i - 1][2]) and  BALL[i - 1][0] > BALL[i - 1][2]):
            BALL[i - 1][0] = BALL[i - 1][0] + BALL[i - 1][4]
        else:
            BALL[i - 1][4] = - BALL[i - 1][4]
            BALL[i - 1][0] = BALL[i - 1][0] + 2 * BALL[i - 1][4]
            
        if (BALL[i - 1][1] < (B  - BALL[i - 1][2]) and BALL[i - 1][1] > BALL[i - 1][2] + 100):
            BALL[i - 1][1] = BALL[i -1][1] + BALL[i - 1][5]
        else:
            BALL[i - 1][5] = - BALL[i - 1][5]
            BALL[i - 1][1] = BALL[i - 1][1] + 2 * BALL[i - 1][5] 
        

# Обновление числа попаданий на экране 
    screen.blit(text1, (10, 50))
    p=str(points)
    text2 = f1.render(p, True,
                      (180, 180, 0))
    screen.blit(text2, (300, 50))

# Изменение местоположения каждого шарика

    for i in range (n):
        move_ball( BALL[i - 1][0], BALL[i - 1][1], BALL[i - 1][2], BALL[i - 1][3])


    pygame.display.update()
    screen.fill(BLACK)


    if (points==n):
        screen.fill(BLACK)
        screen.blit(text_end, (300, 400))
    

pygame.quit()
