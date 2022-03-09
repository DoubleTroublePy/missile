from math import atan2, pi
import pygame, sys
from posClass import Missile


class Cordinate:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y


ms = Missile()

ms2 = Missile()
pygame.init()

screen = pygame.display.set_mode((800, 700), 0, 32)


old_target_pos = {'y': 0, 'x': 0}

# The length of each time slice
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    clock.tick(300)

    x, y = pygame.mouse.get_pos()  # Get mouse position , The mouse is the target that needs to be hit

    # screen.blit(missile, (x1-missile.get_width(), y1-missile.get_height()/2))
    screen.fill((0, 0, 0))

    targe_angle = atan2(y - old_target_pos.y , x - old_target_pos[1]) * 180 / pi

    x1, y1, positions = ms.direct_navigation(x, y)
    x2, y2, positions2 = ms.proportional_navigation((x, y))

    pygame.draw.circle(screen, (255, 0, 0), (x1, y1), 2)
    pygame.draw.circle(screen, (0, 255, 0), (x2, y2), 2)

    for x10, y10 in positions:
        pygame.draw.circle(screen, (0, 0, 255), (x10, y10), 1)


    old_target_pos = [x1, y1]

    pygame.display.update()
