"""Object-Oriented Homework."""
import math


class Line:
    """Line."""

    def __init__(self, coor1, coor2):
        """Constructor."""
        self.p1 = coor1
        self.p2 = coor2

    def distance(self):
        """Distance."""
        dx = self.p2[0] - self.p1[0]
        dy = self.p2[1] - self.p1[1]
        return math.sqrt(dx * dx + dy * dy)

    def slope(self):
        """Slope."""
        dx = self.p2[0] - self.p1[0]
        dy = self.p2[1] - self.p1[1]
        if dx == 0:
            raise ZeroDivisionError("Can't handle vertical lines.")
        return dy/dx


# Test Line
coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(f'distance = {li.distance()}')
print(f'slope = {li.slope()}')


class Cylinder:
    """Cylinder."""

    def __init__(self, height=1, radius=1):
        """Constructor."""
        self.height = height
        self.radius = radius

    def end_area(self):
        """Area of end of cylinder."""
        return math.pi * self.radius * self.radius

    def end_circumference(self):
        """Circumference of end of cylinder."""
        return 2 * math.pi * self.radius

    def volume(self):
        """Volume."""
        return self.end_area() * self.height

    def surface_area(self):
        """Surface Area."""
        return 2 * self.end_area() + self.height * self.end_circumference()


# Test Cylinder
c = Cylinder(2, 3)
print(f'volume = {c.volume()}')
print(f'area  = {c.surface_area()}')
