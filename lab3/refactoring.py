import pygame
import random 
from pygame.draw import *

pygame.init()

FPS = 30
h=600
w=600
r=150


GRAY = (130, 130, 130)
DARK_GRAY = (50, 50, 50)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
ASHEN = (195, 195, 195)
LIGHT_GRAY = (225, 225, 225)

screen = pygame.display.set_mode((h, w))
A=[]
K=[]

#draws background and moon
rect(screen,(0,0,50),(0,0,h,w))
rect(screen,(0,50,0),(0,w//2,h,w))
r=min(h,w)/8
circle(screen, WHITE,(w/2+r,h/4),r)

#random two-color clouds, with an adjustable amount
n=4
for i in range(n):
    ellipse(screen, GRAY,(h*random.random(),w*random.random()/2-w/5,   h//2,w//10))
    ellipse(screen,DARK_GRAY,(h*random.random(),w*random.random()/2-w/5,   h//2,w//10))

#auxiliary function
def sign1(x):
    if x!=0: return x/abs(x)
    else:    return 1


def UFO(x,y,k):
    """draws light from a flying saucer, x,y coordinates"""
    if (k*y > w/12) or (y>w/2) :
        z=random.uniform(1.75,3)
        polygon(surf  , WHITE,[(x,y),(x-h//8,(1-sign1(y-w/2))/2*(w/z-y)+y-w/8*3+w//8*5),(x+h//8,(1-sign1(y-w/2))/2*(w/z-y)+y-w/8*3+w//8*5),(x,y)])
    A.append((x,y))
    K.append(k)

def UFOBody(z):
    """draws a flying saucer"""
    global h,w
    for i in range(z): 
        x,y=A[i]
        k=K[i]
        h=h*k
        w=w*k
    for i, j, q, l, m in [[ASHEN, 0, 0, 2.4, 10], [LIGHT_GRAY, (h//2.4-h//3)/2, -w//100, 3, 12], [WHITE, (h//2.4-h//3)/2, w//16, 20, 60 ],[WHITE, (h//2.4+h//3)/2-h//20, w//16, 20, 60], [WHITE, (h//2.4-h//3)/2+h/15, w//13, 20, 60],[WHITE, (h//2.4+h//3)/2-h/15-h//20, w//13, 20, 60], [WHITE, h//6+h//60, w//12.5, 20, 60]]:
        ellipse(screen, i,(x-h//4.8 + j,y +q, h//l, w//m))
    h, w=h/k, w/k
    print(h,w)



def Inoplanet(x,y,r,k):
    s=(k/abs(k))
    k=abs(k)+0.5

    circle(screen,'red'                 ,(x+s*k*(3/4*h-h*2/3)                 ,y+k*(3/4*w-w/30-2/3*w)) ,k*r/8)
    ellipse(screen,(0,200,0)            ,(x+s*k*(3/4*h-2/3*h)                 ,y+k*(3/4*w-r/8-r/10-w/30-2/3*w),k*r/12,k*r/7))


    ellipse(screen,(195,195,195)        ,(x-k*h/40                          ,y+k*w/20                ,k*h/20,k*w//10))
    ellipse(screen,(195,195,195)        ,(x-k*h/40                          ,y                       ,k*h/20,k*w//20))
    ellipse(screen,(195,195,195)        ,(x-k*h/20                          ,y-k*w/40                ,k*h/10,k*w//20))
    ellipse(screen,(195,195,195)        ,(x+k*h/40                          ,y-k*w/20                ,k*h/40,k*w//20))
    ellipse(screen,(195,195,195)        ,(x-k*h/20                          ,y-k*w/20                ,k*h/40,k*w//20))
    ellipse(screen,(195,195,195)        ,(x+k*(h/40+h/80)                   ,y-k*w/15                ,k*h/40,k*w//20))
    ellipse(screen,(195,195,195)        ,(x-k*(h/20+h/80)                   ,y-k*w/15                ,k*h/40,k*w//20))
    circle(screen, BLACK               ,(x-k*h/40                          ,y)                      ,k*r/8)
    circle(screen, BLACK              ,(x+k*h/40                          ,y)                      ,k*r/8)
    circle(screen, WHITE              ,(x+k*h/35*s                        ,y+k*w/125)              ,k*r/18)
    circle(screen, WHITE               ,(x-k*h/45*s                        ,y+k*w/125)              ,k*r/18)
    ellipse(screen,(195,195,195)        ,(x-k*h/35                          ,y+k*w/7.5               ,k*h/40,k*w//15))
    ellipse(screen,(195,195,195)        ,(x-k*(h/40-h/35)                   ,y+k*w/7.5               ,k*h/40,k*w//15))
    ellipse(screen,(195,195,195)        ,(x-k*h/35                          ,y+k*(w/7.5+w/20)        ,k*h/40,k*w//20))
    ellipse(screen,(195,195,195)        ,(x-h/40+h/35                       ,y+k*(w/7.5+w/20)        ,k*h/40,k*w//20))
    ellipse(screen,(195,195,195)        ,(x-(h/40-h/35)*k                   ,y+k*(w/7.5+w/20)        ,k*h/40,k*w//20))
    ellipse(screen,(195,195,195)        ,(x+k*(-h/35-h/40)                  ,y+k*(w/7.5+w/12)        ,k*h/20,k*w//30))
    ellipse(screen,(195,195,195)        ,(x+k*(-h/40+h/35)                  ,y+k*(w/7.5+w/12)        ,k*h/20,k*w//30))
    ellipse(screen,(195,195,195)        ,(x+k*(-h/40+h/35)                  ,y+k*w/20                ,k*h/20,k*w//40))
    ellipse(screen,(195,195,195)        ,(x-k*(h/40-h/35-h/25)              ,y+k*w/17                ,k*h/20,k*w//40))
    ellipse(screen,(195,195,195)        ,(x+k*(h/40-h/35-h/20)              ,y+k*w/20                ,k*h/20,k*w//40))
    ellipse(screen, ASHEN        ,(x+k*(h/40-h/35-h/25-h/20)         ,y+k*w/17                ,k*h/20,k*w//40))

surf = pygame.Surface((h, w))
surf.set_alpha(50)
surf1=pygame.Surface((h, w)) 

for i in range(n):
    Inoplanet(h*random.random(),w/2*(random.random()+1),min(h,w)/8,(1-2*random.random())/2/2)
for i in range(n):
    UFO(h*random.random(),w*(random.random()),(random.random()))
screen.blit(surf, (0, 0))
UFOBody(n)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
screen.blit(surf, (0, 0))

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
