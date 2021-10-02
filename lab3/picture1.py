import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((450, 600))
surface1 = screen.convert_alpha()
surface1.fill([0,0,0,0])
surface2 = screen.convert_alpha()
surface2.fill([0,0,0,0])

ICYSUN_COLOR = (249, 249, 210, 175)
ICE_COLOR = (230, 230, 230)
DARK_BLUE = (0, 68, 102)
GRAY = (77, 77, 77)
BLUE = (0, 255, 255)
BLACK = (0, 0, 0)

rect(screen, BLUE, (0, 0, 450, 330)) 
rect(screen, ICE_COLOR, (0, 330, 450, 270 ))
line(screen, BLACK, (0,330), (450, 330), 1)

def sun(b:int):
    """b - the brightness of the sun as a percentage of max"""
    circle(surface1, ICYSUN_COLOR, (300, 130), 140, 23)
    line(surface2, ICYSUN_COLOR, (292, 265), (308, -10), 15)
    line(surface2, ICYSUN_COLOR, (160, 122), (435, 138), 15)
    for i, j, k in [[305, 130, b], [292, 260, int(b/2)], [308, 0, int(b/2)], [165, 122, int(b/2)], [430, 138, int(b/2)]]:
        sun_brightness(i, j, k)

def sun_brightness(x, y, r):
    """auxiliary function for sun"""
    for z in range(r,0,-1):
        circle(screen, (0+255/r*(r-z), 255, 255 - 55/r * (r-z)), (x, y), z)

def bear_fisherman(x, y, s):
    """ x,y - bear's position, s - its size """
    if 0.25 < s < 0.5: i = 2
    elif s < 0.25: i = 1
    else: i = 4
    lines(surface2, (0, 0, 0), False, [[x + 151*s, y + 125*s], [x + 181*s, y + 60*s], [x + 220*s, y + 20*s], [x + 280*s, y - 25*s], [x + 340*s, y - 45*s]], i)
    for c, i, j, k, l in [[ICE_COLOR, 0, 0, 150, 260], [ICE_COLOR, 77, -35, 98, 55], [ICE_COLOR, 117, 60, 70, 30], [ICE_COLOR, 72, 185, 110, 80], [ICE_COLOR, 122, 235, 95, 35], [GRAY, 252, 160, 160, 60], [DARK_BLUE, 264, 172, 136, 48]]:
        ellipse(surface2, c, (x + i*s, y + j*s, k*s, l*s))
        ellipse(surface2, (0, 0, 0), (x + i*s, y + j*s, k*s, l*s), 1)
    line(surface2, (0, 0, 0), [x + 340*s, y - 45*s], [x + 340*s, y + 205*s], 1)
    for i, j in [[117, -15], [174, -14]]:
        circle(surface2, BLACK, (x+ i*s, y+ j*s), 4*s)
    for i, j in [[ICE_COLOR, 40*s], [BLACK, 1]]:
        arc(surface2, i, (x + 88*s, y - 34*s, 20*s, 18*s), 0.5, 4.9, int(j))
    line(surface2, BLACK, (x + 98*s, y - 18*s), (x + 106*s, y - 29*s))
    arc(surface2, BLACK, (x + 67*s, y, 100*s, 10*s), 5, 6.4, 1)
    for i,j in [[150, -20], [60, 20], [-20, -8], [-70, -130]]:
        fish(x + i*s, y + j*s, s)

def fish(x, y, s):
    ellipse(surface2, (148, 184, 184), (x + 277*s, y + 250*s, 100*s, 20*s))
    for i, j, k, l in [[x + 252*s, y + 250*s, 35*s, 25*s], [x + 312*s, y + 240*s, 35*s, 15*s], [x + 342*s, y + 260*s, 20*s, 25*s], [x + 297*s, y + 260*s, 15*s, 15*s]]:
        rect(screen, (255, 153, 153), (i, j, k, l))
    for i in [y + 283*s, y + 237*s]:
        circle(surface2, ICE_COLOR, (x + 273*s, i), 22*s)
    for i, j, k, l in [[282*s + x, 240*s + y, 35*s, 15*s], [377*s + x, 230*s + y, -35*s, 30*s], [355*s + x, 260*s + y, 20*s, 25*s], [287*s + x, 260*s + y, 15*s, 15*s]]:
        ellipse(surface1, ICE_COLOR, (i, j, k, l))
    circle(surface2, GRAY, (357*s + x, 260*s + y), 4*s)

sun(100)
for i, j, k in [[3, 450, 0.4], [150, 350, 0.3], [30, 320, 0.2], [330, 450, 0.7], [340, 320, 0.15]]:
    bear_fisherman(i, j, k)


screen.blit(surface1, (0,0))
screen.blit(surface2, (0,0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
