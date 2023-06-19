import math


class Calculator:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, radius):
        self._radius = radius

    # 周长
    def get_circumference(self):
        return 2 * math.pi * self._radius

    # 面积
    def get_area(self):
        return math.pi * self._radius ** 2

    # 球的表面积
    def get_surface_area(self):
        return 4 * math.pi * self._radius ** 2

    # 球的体积
    def get_volume(self):
        return 4 / 3 * math.pi * self._radius ** 3
