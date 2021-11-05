import math
from random import choice
import random as rnd
from pygame.draw import *

import pygame
import sys

FPS = 60

WIDTH = 1300 
HEIGHT = 650
dragon_length = 200
dragon_high = 120
ball_size = 45
heart_size = 30
target_size = 60
stone_size = 45
g = 0.1


game_over = pygame.image.load('images\игра окончена.jpg')
game_over = pygame.transform.scale(game_over, (WIDTH, HEIGHT))
                                   
stone_pikch = pygame.image.load('images\камень.png')
stone_pikch = pygame.transform.scale(stone_pikch, (stone_size, stone_size))

goodtarget_pikch = pygame.image.load('images\мишень 1.png')
goodtarget_pikch = pygame.transform.scale(goodtarget_pikch, (target_size, target_size))


heart_pikch = pygame.image.load('images\сердце.png')
heart_pikch = pygame.transform.scale(heart_pikch, (heart_size, heart_size))



ball_pikch = pygame.image.load('images\шарик.png')
ball_pikch = pygame.transform.flip(ball_pikch, True, False)
ball_pikch = pygame.transform.scale(ball_pikch, (ball_size, ball_size))


background = pygame.image.load('images\фон.jpg')
background = pygame.transform.scale(background,(WIDTH, HEIGHT))

dragon_pikch = pygame.image.load('images\дракон.png')
dragon_pikch = pygame.transform.scale(dragon_pikch, (dragon_length, dragon_high ))
dragon_pikch = pygame.transform.flip(dragon_pikch, True, False)




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
        self.live = 1

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 1600х900).
        """

        if (self.x < (WIDTH - self.size )) and (self.x > -self.size ):
            self.x += self.vx
        else:
            self.live = 0
        if (self.y < (HEIGHT - self.size)) and (self.y > -self.size):
            self.y += self.vy
            self.vy += g
            self.vy *= 0.99
        else:
            self.live = 0


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
        return (((self.x + self.size*0.5  - obj.x - obj.size*0.5)**2 +(self.y + self.size*0.5 - obj.y - obj.size*0.5)**2) < 0.2*(self.size + obj.size)**2)

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
        self.speed = 5
        self.length = dragon_length
        self.high = dragon_length
        self.health = 5
        self.f2_power = 5
        self.f2_on = 0
        self.an = 1


    def fire2_start(self, event):
        """Активирует режим прицеливания дракона"""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.x = self.x + 0.5*dragon_length
        new_ball.y = self.y + 0.5*dragon_high
        new_ball.size = ball_size
        self.an = - math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        

    def move(self, key):
        """Движение дракона в заданном направлении в зависимости от кнопки
            w - вверх
            s - вниз
            a - влево
            d - вправо"""
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed
            

    def draw(self):
        """Прорисовывает дракона"""
        self.screen.blit(dragon_pikch,(self.x, self.y))


    def power_up(self):
        """Определение мощности вылета мяча"""
        if self.f2_on:
            if self.f2_power < 40:
                self.f2_power += 0.01

    def get_health(self):
        for number in range (0, self.health, 1):
            self.screen.blit(heart_pikch, (heart_size*number, HEIGHT - heart_size))
        
                


class Target:
    
    def __init__(self, screen):
        """Конструктор класса Target

        Args:
        x - положение цели по горизонтали
        y - положение цели по вертикали
        size - размер цели
        """
        self.x = rnd.randint(600, 780)
        self.y = rnd.randint(300, 550)
        self.size = target_size
        self.screen = screen
        self.live = 1
        self.points = 0

    def new_target(self):
        """ Инициализация новой цели. """
        x  = self.x = rnd.randint(self.size, WIDTH - self.size)
        y  = self.y = rnd.randint(self.size, HEIGHT - self.size)
        self.live = 1
        self.points = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        self.screen.blit(goodtarget_pikch, (self.x, self.y))
        
    def move(self):
        self.x += rnd.randint(-5, 5)
        self.y += rnd.randint(-5, 5)


class Hindrance:
    
    def __init__(self, screen):
        """ Конструктор класса Hindrance
            """
        self.screen = screen
        self.size = stone_size
        self.x = rnd.randint(self.size, WIDTH - self.size)
        self.y = 0
        self.life = 1
        self.vy = 5

    def new_hindrance(self):
        """Инициализация нового камня"""
        x = self.x = rnd.randint(self.size, WIDTH  - self.size)
        self.y = 0
        self.life = 1
        self.vy = 5
        
    def move(self):
        """Движение камня"""
        self.y += self.vy
        self.vy += g

    def end_life(self):
        return (HEIGHT < self.y)


    def draw(self):
        """Проорисовка камня"""
        self.screen.blit(stone_pikch, (self.x, self.y))



    def hittest(self, obj):
        """Проверка стоклновения камня с драконом: минус жизнь"""
        return (((self.y + self.size) > obj.y) and (self.y < (obj.y + obj.high)) and ((self.x + self.size) > obj.x) and (self.x < (obj.x + obj.length)))
                                                                                                                    
        


'''def __init__ (self, screen):
    super().__init__(screen)'''


'''f1 = pygame.font.Font(None, 36)
text = f1.render('Score: ', True,
                  (250, 0, 0))'''



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.blit(game_over, (0,0))
bullet = 0
balls = []

clock = pygame.time.Clock()
dragon = Dragon(screen)
target = Target(screen)
hindrance = Hindrance(screen)
finished = False

while not finished:
    screen.blit(background, (0,0))
    target.draw()
    target.move()
    hindrance.draw()
    hindrance.move()
    dragon.draw()
    dragon.get_health()
    for b in balls:
        b.draw()

    if dragon.health < 1:
        screen.blit(game_over, (0,0))
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

    if hindrance.hittest(dragon) and hindrance.life:
        hindrance.live = 0
        hindrance.new_hindrance()
        dragon.health -= 1
        
    if hindrance.end_life():
        hindrance.live = 0
        hindrance.new_hindrance()



    for b in balls:
        b.move()
        if b.live == 0:
            b.size = 0
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
    dragon.power_up()


pygame.quit()
