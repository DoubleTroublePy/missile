import time
from math import atan2, pi, sqrt
import pygame, sys
from posClass import Missile, Coordinate


if __name__ == '__main__':
    ms = Missile()
    ms2 = Missile()

    pygame.init()

    screen = pygame.display.set_mode((800, 700), 0, 32)

    target_pos = Coordinate(0, 0)
    old_target_pos = Coordinate(0, 0)

    # The length of each time slice
    clock = pygame.time.Clock()
    timer = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(300)

        x, y = pygame.mouse.get_pos()  # Get mouse position , The mouse is the target that needs to be hit

        # screen.blit(missile, (x1-missile.get_width(), y1-missile.get_height()/2))
        screen.fill((0, 0, 0))

        targe_angle = atan2(y - old_target_pos.y, x - old_target_pos.x) * 180 / pi

        angle = atan2(old_target_pos.y - target_pos.y, old_target_pos.x - target_pos.x) * 100 / pi
        distance = sqrt(pow(old_target_pos.x - x, 2) + pow(old_target_pos.y - y, 2))  # Two point distance formula
        speed = distance/(time.time()-timer)
        target_pos.vector((x, y), angle, speed)

        x1, y1, positions = ms.direct_navigation(target_pos.x, target_pos.y)
        x2, y2, positions2 = ms2.prediction_navigation(target_pos)

        pygame.draw.circle(screen, (255, 0, 0), (x1, y1), 2)
        pygame.draw.circle(screen, (0, 0, 255), (x2, y2), 2)

        for x10, y10 in positions:
            pygame.draw.circle(screen, (0, 255, 0), (x10, y10), 1)

        for x10, y10 in positions2:
            pygame.draw.circle(screen, (255, 0, 255), (x10, y10), 1)

        old_target_pos.coordinates((x, y))

        pygame.display.update()
