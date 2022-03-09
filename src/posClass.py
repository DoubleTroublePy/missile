from math import sqrt, atan2, degrees
import  math


class Missile:
    def __init__(self, x=100, y=600, velocity=800, time=1/1000):
        self._x, self._y = x, y
        # The initial launch position of the missile
        self._velocity = velocity  # Missile speed
        self._time = time

        self._RTM_old = 0
        self._old_angle = 0
        self._positions = []

    def direct_navigation(self, x, y):
        distance = sqrt(pow(self._x-x, 2)+pow(self._y-y, 2))  # Two point distance formula
        section = self._velocity * self._time  # The distance each time slice needs to move
        sina = (self._y-y)/distance
        cosa = (x-self._x)/distance
        angle = atan2(y-self._y, x-self._x)  # Radian value of two-point line segment
        self._x, self._y = (self._x+section*cosa, self._y-section*sina)
        d_angle = degrees(angle)  # The angle of arc

        dis_angle = d_angle-self._old_angle  #dis_angle Is the angle that needs to be changed to the next position
        self._old_angle = d_angle  # Update initial angle
        self._positions.append((self._x, self._y))

        return self._x, self._y, self._positions

    def prediction_navigation(self, target_pos):
        # 1- calculate time to target if going straight line
        distance = (sqrt(((self._x - target_pos[0])**2) + ((self._y - target_pos[1])**2)))
        time = distance / self._velocity

        # 2- calculate where the target will be with it is current heading

        # 3- set heading to be that spot
        pass

    def proportional_navigation(self, target_pos):
        pass
