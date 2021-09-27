import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (210, 210, 210), (0, 0, 400, 400)) #фон

circle(screen, (255, 255, 0), (200, 200), 100) 
circle(screen, (0, 0, 0), (200, 200), 100, 1) #голова
circle(screen, (255, 0, 0), (150, 180), 20)
circle(screen, (0, 0, 0), (150, 180), 20, 1)
circle(screen, (0, 0, 0), (150, 180), 8) #левый глаз
circle(screen, (255, 0, 0), (245, 180), 15)
circle(screen, (0, 0, 0), (245, 180), 15, 1)
circle(screen, (0, 0, 0), (245, 180), 8) #правый глаз
rect(screen, (0, 0, 0), (148, 250, 104, 20)) #рот
polygon(screen, (0, 0, 0), [(180, 174), (185, 165), (98, 120), (93, 129)]) 
polygon(screen, (0,0,0), [(215, 174), (212,165), (302,135), (305,144)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
