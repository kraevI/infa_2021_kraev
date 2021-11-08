"""
Game: Catch the ball
"""
import pygame
from pygame.draw import *
from random import randint
import random
import math

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

FPS = 120
WINDOW_x = 800
WINDOW_y = 600
screen = pygame.display.set_mode((WINDOW_x, WINDOW_y))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def cross_check(dot1, dot2, rad):
    """
    Checks dot1 in circle with center dot2 and radius rad.
    """
    dist = ((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2) ** (1 / 2)
    return dist < rad


def draw_score(score):
    """
    Draws score.
    """
    textsurface = myfont.render('Your Score: ' + str(score), False, BLACK)
    screen.blit(textsurface, (20, 20))
    textsurface = myfont.render('Your Score: ' + str(score), False, WHITE)
    screen.blit(textsurface, (20, 20))


def draw_time(time_):
    """
    Draws time.
    """
    textsurface = myfont.render('Time left: ' + str(time_), False, BLACK)
    screen.blit(textsurface, (WINDOW_x - 220, 20))
    textsurface = myfont.render('Time left: ' + str(time_), False, WHITE)
    screen.blit(textsurface, (WINDOW_x - 220, 20))


class Ball:

    def __init__(self, coords):
        """
        Sets:
            Ball coordinates (x, y);
            Ball speed;
            Ball color corresponding speed;
            Ball radius r;
            Ball score corresponding speed and r;
            Ball starting angle.
        """
        self.speed = randint(1, 6)
        self.color = COLORS[self.speed - 1]

        self.r = randint(5, 10)
        self.score = self.speed * (11 - self.r)

        self.speed = self.speed * 150 / FPS
        self.r = self.r * 5

        self.x = coords[0]
        self.y = coords[1]
        self.angle = random.uniform(0, 2 * math.pi)

    def update(self):
        """
        Updates parameters
        """
        if self.x - self.r + self.speed * math.cos(self.angle) < 0:
            self.angle = math.pi - self.angle
        elif self.x + self.r + self.speed * math.cos(self.angle) > WINDOW_x:
            self.angle = math.pi - self.angle
        elif self.y - self.r + self.speed * math.sin(self.angle) < 0:
            self.angle = 2 * math.pi - self.angle
        elif self.y + self.r + self.speed * math.sin(self.angle) > WINDOW_y:
            self.angle = 2 * math.pi - self.angle

        self.x = self.x + self.speed * math.cos(self.angle)
        self.y = self.y + self.speed * math.sin(self.angle)

        self.draw()

    def draw(self):
            circle(screen, self.color, (self.x, self.y), self.r * (10 - 2 * 1) / 10)


def smash(ball_1, ball_2):
    """
    Gets two balls and makes smashing and updates angels.
    """
    if cross_check(
            (ball_1.x + ball_1.speed * math.cos(ball_1.angle), ball_1.y + ball_1.speed * math.sin(ball_1.angle)),
            (ball_2.x + ball_2.speed * math.cos(ball_2.angle), ball_2.y + ball_2.speed * math.sin(ball_2.angle)),
            ball_1.r + ball_2.r):
        beta = math.atan((ball_1.y - ball_2.y) / (ball_1.x - ball_2.x))
        ball_1.angle = 2 * beta + math.pi - ball_1.angle
        ball_2.angle = 2 * beta + math.pi - ball_2.angle


def crossing_check(coords_, balls_):
    """
    Checks balls coordinates crossing.
    """
    for ball_ in balls_:
        if cross_check(coords_, (ball_.x, ball_.y), ball_.r + 50):
            return True
    return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False

Score = 0
n_balls = 10

balls = []
for k in range(n_balls):
    coords = (randint(100, WINDOW_x - 100), randint(100, WINDOW_y - 100))
    while crossing_check(coords, balls):
        coords = (randint(100, WINDOW_x - 100), randint(100, WINDOW_y - 100))
    balls.append(Ball(coords))

start_ticks = pygame.time.get_ticks()
seconds = 0
while not finished:
    if seconds < 10:
        clock.tick(FPS)
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for ball in balls:
                    if cross_check(event.pos, (ball.x, ball.y), ball.r):
                        if seconds < 10:
                            Score += ball.score
                        draw_score(Score)

                        coords = (randint(100, WINDOW_x - 100), randint(100, WINDOW_y - 100))
                        while crossing_check(coords, balls):
                            coords = (randint(100, WINDOW_x - 100), randint(100, WINDOW_y - 100))
                        ball.__init__(coords)

        for i in range(n_balls):
            for j in range(i + 1, n_balls):
                smash(balls[i], balls[j])
        for ball in balls:
            ball.update()
        draw_score(Score)
        draw_time(max(round(10 - seconds, 1), 0))
        pygame.display.update()
        screen.fill(BLACK)
    else:
        #Output of the result to the table
        from random import randint

        print('Введите Ваше имя:')
        name = input()

        output = open('scores', 'r+')
        s = output.readlines()
        c = []
        for k in range(0, len(s)):
            a = s[k]
            b = a.split()
            for i in b:
                if(i.isdigit()):
                    c.append(int(i))
        p = len(s)
        for i in range(len(c)-1, -1, -1):
            if Score >= c[i]:
                p = i
        c.insert(p, Score)
        s.insert(p, 'Имя: '+str(name)+'    Результат: '+str(Score)+'\n')

        output.seek(0)
        for i in range(0, len(s)):
            output.write(str(s[i]))

        output.close()
        print('Вы заняли', p+1, 'место с результатом', Score,'очков.\nНовая игра начнется через 10 секунд\n')
        Score = 0
        pygame.time.wait(10000)
        start_ticks = pygame.time.get_ticks()
        seconds = 0

pygame.quit()


