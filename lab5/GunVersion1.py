import math
from random import randint
from random import choice

import pygame
from pygame.draw import *
import pygame.transform as transf

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



class Ball:
    def __init__(self):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.weight = 0
        self.color = choice(GAME_COLORS)
        self.id = circle(screen, self.color, (self.x, self.y), self.r)

    

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна.
        """
        if self.x > WIDTH:
            self.vx = -self.vx
        if self.y > HEIGHT:
            self.vy = -0.4*self.vy
        if self.weight == 5:
            self.vy += 1
        else: self.vy += 2
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
        if (obj.x + 80 - self.x) ** 2 + (obj.y - self.y) ** 2 <= (self.r + 40) ** 2:
            return True
        else:
            return False

class Gun:
    def __init__(self):
        """ Конструктор класса Gun
        Args:
        x - начальное положение танка по горизонтали
        y - начальное положение танка по вертикали
        l - длина пушки
        live - количество жизней, задается в начальных настройках игры
        type_of_shells - начальное состояние зарядов: 0 - стандартные, 1 - тяжёлые
        """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 150
        self.y = 500
        self.l = 3
        self.live = your_lives
        self.type_of_shells = 0

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event, x, y):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Ball()
        if self.type_of_shells == 0:
            new_ball.r += 5
            new_ball.weight += 5
        else: new_ball.r += 20
        new_ball.x = x 
        new_ball.y = y
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event = 0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            q = event.pos[0]-20
            if q == 0:
                q = 1
            self.an = math.atan((event.pos[1]-450) / q)
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY
        self.draw()

    def draw(self):
        polygon(screen, self.color, [(self.x - math.sin(self.an) * self.l, self.y + math.cos(self.an) * self.l),
             (self.x + math.sin(self.an) * self.l, self.y - math.cos(self.an) * self.l),
             (self.x + math.sin(self.an) * self.l + math.cos(self.an) * self.f2_power,
              self.y - math.cos(self.an) * self.l + math.sin(self.an) * self.f2_power),
             (self.x - math.sin(self.an) * self.l + math.cos(self.an) * self.f2_power,
              self.y + math.cos(self.an) * self.l + math.sin(self.an) * self.f2_power)])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

def move(direction, spritex, spritey):
    """Перемещение танка. При нажатии клавиш танк перемещается в соответствующем направлении."""
    if direction:
        if direction == pygame.K_UP:
            spritey-=5
        elif direction == pygame.K_DOWN:
            spritey+=5
        if direction == pygame.K_LEFT:
            spritex-=5
        elif direction == pygame.K_RIGHT:
            spritex+=5
    return spritex, spritey
    

class Plane:
    def __init__(self):
        """ Конструктор класса Plane
        Args:
        x, y - начальное положение самолета
        vx - скорость самолета
        live - количество жизней
        """
        self.x = WIDTH
        self.y = 200
        self.vx = -20
        self.live = 1
        planes.append(self)

    def move(self):
        self.x += self.vx

    def draw(self):
        if self.live == 1:
            screen.blit(plane_img,(self.x, self.y))
            
    def shoot(self):
        """Сбрасывание бомбы."""
        new_shoot = Shoot()
        new_shoot.x = self.x + 50
        new_shoot.y = self.y
        shootes.append(new_shoot)

plane_img = pygame.image.load('plane.png')
plane_img = transf.scale(plane_img, (int(plane_img.get_width()*0.15), int(plane_img.get_height()*0.15)))
shoot_img = pygame.image.load('bomb.png')
shoot_img = transf.scale(shoot_img, (int(shoot_img.get_width()*0.15), int(shoot_img.get_height()*0.15)))

class Shoot:
    def __init__(self):
        """ Конструктор класса Shoot
        vy - скорость бомбы
        live - количество жизней"""
        self.live = 1
        shootes.append(self)
        self.vy = 10
    def move(self):
        self.y += self.vy
    def draw(self):
        if self.live == 1 and self.y < HEIGHT:
            screen.blit(shoot_img,(self.x, self.y))

def hittest(obj1, obj2):
    """Функция проверяет сталкивалкивается ли данные обьекты с целью.
    Создана с учетом ошибок габаритов, которые возникают из-за того, что координаты объектов - координаты их задающих изображений.
    Args:
        obj1, obj2: объекты, столкновение которых проверяется.
    Returns:
        Возвращает True в случае столкновения. В противном случае возвращает False.
    """
    if (obj1.x - (obj2.x + 80)) ** 2 + (obj1.y - obj2.y) ** 2 <= 5000:
        return True
    else:
         return False

#начальные настройки игры
WIDTH = 1200
HEIGHT = 1000
Score = 0
your_lives = 5


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#обслуживающий блок
balls = []
planes = []
shootes = []
gun = Gun()
global sprite, spritex, spritey
sprite = pygame.image.load('tank.png')
sprite = transf.scale(sprite, (int(sprite.get_width()*0.15), int(sprite.get_height()*0.15)))
spritex = gun.x - 100
spritey = gun.y - 20
direction=False
p1 = Plane()


finished = False
clock = pygame.time.Clock()
while not finished:
    screen.fill(WHITE)
    gun.draw()
    screen.blit(sprite,(spritex, spritey))
    All = balls + planes + shootes
    for a in All:
        a.draw()

    #вывод информации на экран
    fontObj = pygame.font.Font('freesansbold.ttf', 10)
    textSurfaceObj = fontObj.render('points = ' + str(Score) + '\n your lives = ' + str(gun.live), True, BLACK) #ОШИБКА: не срабатывает перенос строки
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (40, 25)    
    screen.blit(textSurfaceObj, textRectObj)

    pygame.display.update()
    clock.tick(FPS)
    
    #механизм появления самолетов и сбрасывания бомб, основывается на случайных числах
    f = randint(0, 80)
    if f == 3 and p1.x < -100:
        p1.x = WIDTH
    if p1.x < -120:
        p1.live = 1
    r = randint(0,10)
    if r == 5 and p1.live == 1:
        p1.shoot()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gun.type_of_shells == 0:
                    gun.type_of_shells = 1
                else: gun.type_of_shells = 0
            elif event.type == pygame.KEYDOWN: direction = event.key
        elif event.type == pygame.KEYUP:  direction = False
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event, gun.x, gun.y)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        
    spritex, spritey = move(direction, spritex, spritey) #получаем новые координаты танка
    gun.x, gun.y = [spritex + 100, spritey + 20]
    
    for a in All:
        a.move()

    #внутреннее взаимодействие объектов, подсчет очков
    for b in balls:
        if b.x < 0 or b.x > WIDTH or b.y > HEIGHT:
            balls.remove(b)
        if b.hittest(p1) == True and p1.live == 1:
            p1.live = 0
            Score += 5
        for s in shootes:
            if b.hittest(s) and s.live == 1:
                Score += 3
                s.live = 0
    for s in shootes:
        if s.y > HEIGHT:
            shootes.remove(s)
        if hittest(gun, s) and s.live == 1:
            gun.live -= 1
            s.live = 0
    gun.power_up()
    
pygame.quit()
