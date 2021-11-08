import math
from random import randint
from random import choice

import pygame
from pygame.draw import *


FPS = 30


RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.id = circle(screen, self.color, (self.x, self.y), self.r)

    

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x < 0:
            self.die()
        if self.x > WIDTH:
            self.vx = -self.vx
        if self.y > 550:
            self.vy = -0.8*self.vy
        self.vy += 1
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pygame.draw.circle(self.screen, self.color,(self.x, self.y),self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False
        
    def die(self):
        self.x = -20
        self.y = -5
        self.vx = 0
        self.vy = 0

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

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
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
        self.draw()

    def draw(self):
        polygon(screen, self.color, [[20, 450], [20, 445], [20 + max(self.f2_power, 20) * math.cos(self.an), 445 + max(self.f2_power, 20) * math.sin(self.an)],
                                     [20 + max(self.f2_power, 20) * math.cos(self.an), 450 + max(self.f2_power, 20) * math.sin(self.an)]])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(2, 50)
        color = self.color = RED
        fontObj = pygame.font.Font('freesansbold.ttf', 25)
        textSurfaceObj = fontObj.render('Вы уничтожили цель за ' + str(s) + ' выстрелов(-а)', True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (400, 250)    
        screen.blit(textSurfaceObj, textRectObj)
        pygame.display.update()
        pygame.time.wait(1000)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        circle(screen, RED, (self.x, self.y), self.r)
        fontObj = pygame.font.Font('freesansbold.ttf', 10)
        textSurfaceObj = fontObj.render('points = ' + str(self.points), True, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (40, 25)    
        screen.blit(textSurfaceObj, textRectObj)
        pygame.display.update()

s = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
t1 = Target()
#t2 = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    t1.draw()
    #t2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
                gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(t1):
            t1.live = 0
            t1.hit()
            for b in balls:
                b.die()
                s+= 1
            t1.new_target()
            s = 0
            
    gun.power_up()

pygame.quit()
