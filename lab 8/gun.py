import math
from random import choice
import random as rnd

import pygame
import sys

FPS = 60



WIDTH = 1024 
HEIGHT = 576
Dr_length = 200
Dr_high = 120
ball_size = 45

ball_pikch = pygame.image.load('шарик.png')
ball_pikch = pygame.transform.flip(ball_pikch, True, False)
ball_pikch = pygame.transform.scale(ball_pikch, (ball_size, ball_size))


background = pygame.image.load('фон.jpg')

dragon_pikch = pygame.image.load('дракон.png')
dragon_pikch = pygame.transform.scale(dragon_pikch, (Dr_length, Dr_high ))
dragon_pikch = pygame.transform.flip(dragon_pikch, True, False)

g = 0.1


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        vx - горизонтальная скорость
        vy - вертикальная скорость
        color - цвет мяча
        live - время жизни
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = ball_size
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        angle = - math.atan(self.vy/self.vx)*180/3.14
        #ball_pikch = pygame.transform.rotate(ball_pikch, angle)

        if (self.x < (WIDTH - self.size )) and (self.x > self.size ):
            self.x += self.vx
            self.vx *= 0.97
        else:
            self.live = 0
        if (self.y < (HEIGHT - self.size)) and (self.y > self.size):
            self.y += self.vy
            self.vy += g
            self.vy *= 0.99
        else:
            self.live = 0

    def new_position(self, x, y):
        """ Функция задает начальные координаты шарика
            x - координата по горизонтали
            y - координата по вертикали """
        self.x = x + Dr_length*0.5
        self.y = y + 0.5*Dr_high

    def draw(self):
        """ Функция прорисовывает шар"""    
        self.screen.blit(ball_pikch, (self.x, self.y))



    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (((self.x - obj.x)**2 + (self.y - obj.y)**2) < (self.r + obj.r)**2)

class Dragon:
    def __init__(self, screen):
        """Конструктор класса Dragon

        Args:
        f2_power - скорость вылета мяча
        f2_on - значение, обозначающее, в каком режиме дракон
        an - угол прицеливания
        """
        self.x = 40
        self.y = 250
        self.screen = screen
        self.f2_power = 5
        self.f2_on = 0
        self.an = 1
        self.speed = 5

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.new_position(self.x, self.y)
        new_ball.size = ball_size
        self.an = - math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        

    def move(self, key):
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed
            

    def draw(self):
        self.screen.blit(dragon_pikch,(self.x, self.y))


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 40:
                self.f2_power += 0.001


'''class Target:
    
    def __init__(self, screen):
        """Конструктор класса Target

        Args:
        x - положение цели по горизонтали
        y - положение цели по вертикали
        r - радиус цели
        color - цвет цели
        """
        self.x = rnd.randint(600, 780)
        self.y = rnd.randint(300, 550)
        self.r = 10
        self.color = RED
        self.screen = screen
        self.live = 1
        self.points = 0

    def new_target(self):
        """ Инициализация новой цели. """
        x  = self.x = rnd.randint(600, 780)
        y  = self.y = rnd.randint(300, 550)
        r  = rnd.randint(2, 50)
        color = self.color = RED
        self.live = 1
        self.points = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)'''


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.blit(background, (0,0))
bullet = 0
balls = []

clock = pygame.time.Clock()
dragon = Dragon(screen)
#target = Target(screen)
finished = False

while not finished:
    screen.blit(background, (0,0))
    #target.draw()
    dragon.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        
        pressed_keys = pygame.key.get_pressed()
        
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dragon.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            dragon.fire2_end(event)
        if pressed_keys:
                dragon.move(pressed_keys)
                

    for b in balls:
        b.move()
        if b.live == 0:
            b.size = 0
        #if b.hittest(target) and target.live:
        #    target.live = 0
         #   target.hit()
         #   target.new_target()
    dragon.power_up()

pygame.quit()
