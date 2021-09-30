import pygame
from pygame.draw import *

pygame.init()

green=(23,114,69)
peach=(255, 204, 153)
black=(0,0,0)
white=(255,255,255)


def tree(x,y, a, b): #a - "ширина" дерева, b - "длина" дерева

#ствол   
    rect(screen, green, (x,y-b,a,b),0)
    rect(screen, green, (x,y-17*b/8,a,b),0)
    polygon(screen, green,[[x+a/2,y-18*b/8],[x-a/8,y-9*b/4-a/5],[x+a/2,y-3*b],[x+9*a/8,y-3*b+a/5]])
    aalines(screen, green, True, [[x+a/2,y-18*b/8],[x-a/8,y-9*b/4-a/5],[x+a/2,y-3*b],[x+9*a/8,y-3*b+a/5]])
    polygon(screen, green, [[x+3*a/4,y-25*b/8],[x+7*a/16,y-25*b/8-a/10],[x+27*a/16,y-4*b],[x+2*a,y-4*b+a/10]])
    aalines(screen, green, True, [[x+3*a/4,y-25*b/8],[x+7*a/16,y-25*b/8-a/10],[x+27*a/16,y-4*b],[x+2*a,y-4*b+a/10]])

#листочки 5 штук
    sur=pygame.Surface([6*a,0.8*b], pygame.SRCALPHA,32)
    sur=sur.convert_alpha()
    ellipse(sur, green, (0, 0, 0.6*a, 0.7*b),0)
    ellipse(sur, green, (a, 0.1*b, 0.6*a, 0.7*b),0)
    ellipse(sur, green, (2*a, 0, 0.6*a, 0.7*b),0)
    ellipse(sur, green, (3*a, 0, 0.6*a, 0.7*b),0)
    ellipse(sur, green, (4*a, 0.1*b, 0.6*a, 0.7*b),0)
    sur2=pygame.transform.rotate(sur,-15)
    sur3=pygame.transform.rotate(sur,15)
    screen.blit(sur2,(x-8*a,y-3.5*b))
    screen.blit(sur3,(x+4*a,y-3.9*b))
    
#листочки 3 штуки
    mur=pygame.Surface([3*a,0.8*b],pygame.SRCALPHA, 32)
    mur=mur.convert_alpha()
    ellipse(mur, green, (0, 0, 0.6*a, 0.7*b),0)
    ellipse(mur, green, (1.2*a, 0.1*b, 0.6*a, 0.7*b),0)
    ellipse(mur, green, (2.4*a, 0, 0.6*a, 0.7*b),0)
    mur2=pygame.transform.rotate(mur,-15)
    mur3=pygame.transform.rotate(mur,10)
    screen.blit(mur2,(x-5*a,y-2*b))
    screen.blit(mur3,(x+3*a,y-2.2*b))
    
    
#ветви
    arc(screen, green, (x-17*a,y-3.5*b,17*a,2.3*b),0.2,3.14/2,2)
    arc(screen, green, (x-7*a,y-2*b,7*a,2*b),0.3,2.5*3.14/4,2)
    arc(screen, green, (x, y-3.8*b,18*a,3*b),3.14/2,3.14-0.6,2)
    arc(screen, green, (x+a, y-2.3*b,7*a,2*b),3.14/3,3.14-0.4,2)


def panda(x,y,size,scr): #x,y -координаты, size - размер, scr -пространство
    ellipse(scr, white,(x-1.8*size,y,1.8*size,size),0)

#лапы
    def b_ell(x,y,a,b,angle,color):
        lapa=pygame.Surface([a,b],pygame.SRCALPHA, 32)
        lapa=lapa.convert_alpha()
        ellipse(lapa,color,(0,0,a,b),0)
        lapa1=pygame.transform.rotate(lapa,angle)
        scr.blit(lapa1, (x,y))
    polygon(scr, black,[[x-size/10,y+size/2], [x-size/5,y+1.3*size], [x-size/2,y+1.58*size], [x-0.8*size,y+1.28*size]])
    b_ell(x-size*0.57,y+size*0.45,size*0.37,size,-18,black)
    b_ell(x-0.95*size,y+0.95*size,0.45*size,0.7*size,-52,black)
    polygon(scr,black,[[x-0.8*size,y],[x-0.8*size,y+size],[x-size,y+1.3*size],[x-1.3*size,y+1.5*size],[x-1.4*size,y+1.1*size]])
    b_ell(x-1.7*size,y+0.95*size,size*0.4,size*0.6,-55,black)
    b_ell(x-2.2*size,y+0.3*size,size*0.4,size*1.1,-30,black)


#голова
    polygon(scr, white, [[x-1.2*size,y-0.3*size],[x-0.9*size,y],[x-0.9*size,y+0.8*size],[x-1.65*size,y+size],[x-1.9*size,y]])
    b_ell(x-1.9*size,y-0.38*size,0.74*size,0.2*size,25,white)
    b_ell(x-2*size,y,0.2*size,1*size,14,white)
    b_ell(x-1.7*size,y+0.7*size,0.8*size,0.2*size,15,white)
    b_ell(x-1.2*size,y-0.25*size,size*0.3,0.55*size,28,black)
    b_ell(x-2.1*size,y-0.25*size,size*0.3,0.55*size,-20,black)
    circle(scr,black,(x-1.3*size,y+0.55*size),0.17*size)
    ellipse(scr,black,(x-1.72*size,y+0.9*size,0.3*size,0.17*size))
    ellipse(scr,black,(x-1.87*size,y+0.45*size,0.28*size,0.34*size))

    

    
FPS = 30
screen = pygame.display.set_mode((900, 600))
rect(screen,peach, (0,0,900,600),0)

tree(480,400,23,90)
tree(90,420,12,55)
tree(260,440,10,68)
tree(800,380,10,75)

panda(770,360,120, screen)
panda(500,450,60, screen)

turn=pygame.Surface([240,220],pygame.SRCALPHA, 32)
turn=turn.convert_alpha()
panda(220,60,90,turn)
turnp=pygame.transform.flip(turn,True, False)
screen.blit(turnp,(50,380))





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

