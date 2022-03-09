from math import sqrt, atan2, degrees
import math


class Coordinate:
    def __init__(self, x: float, y: float, angle=0, velocity=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = velocity

    def coordinates(self, coord: tuple):
        self.x, self.y = coord

    def vector(self, coord: tuple, angle: float, velocity: float):
        self.x, self.y = coord
        self.angle = angle


class Missile:
    def __init__(self, x=100, y=600, velocity=800, time=1/1000):
        self._position = Coordinate(x, y)
        # The initial launch position of the missile
        self._velocity = velocity  # Missile speed
        self._time = time

        self._RTM_old = 0
        self._old_angle = 0
        self._positions = []

    def direct_navigation(self, x: float, y: float) -> tuple:
        distance = sqrt(pow(self._position.x - x, 2) + pow(self._position.y - y, 2))  # Two point distance formula
        section = self._velocity * self._time  # The distance each time slice needs to move
        sina = (self._position.y-y)/distance
        cosa = (x-self._position.x)/distance
        self._position.coordinates((self._position.x+section*cosa, self._position.y-section*sina))

        if len(self._positions) > 1000:
            self._positions.pop(0)
        self._positions.append((self._position.x, self._position.y))

        return self._position.x, self._position.y, self._positions

    def prediction_navigation(self, target_pos: Coordinate):
        # 1- calculate time to target if going straight line
        distance = (sqrt(((self._position.x - target_pos.x)**2) + ((self._position.y - target_pos.y)**2)))
        distance1 = sqrt(pow(self._position.x - target_pos.x, 2) + pow(self._position.y - target_pos.y, 2))  # Two point distance formula
        time = distance / self._velocity

        # 2- calculate where the target will be with it is current heading
        distance = target_pos.velocity * time
        new_target_pos = Coordinate(distance*math.cos(target_pos.angle), distance*math.sin(target_pos.angle))
        heading_angle = atan2(self._position.y - target_pos.y, self._position.x - target_pos.x) * 100 / math.pi

        # 3- set heading to be that spot
        section = self._velocity * self._time  # The distance each time slice needs to move

        self._position.coordinates((self._position.x + section * math.sin(heading_angle),
                                    self._position.y - section * math.cos(heading_angle)))

        if len(self._positions) > 1000:
            self._positions.pop(0)
        self._positions.append((self._position.x, self._position.y))

        return 0, 0, self._positions

    def proportional_navigation(self, target_pos: tuple):
        pass
