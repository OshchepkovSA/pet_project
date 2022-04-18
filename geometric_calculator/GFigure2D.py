import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class Circle:

    def __init__(self, *args):
        self.id_figure, self.radius = args[0]
        self.id_figure, self.radius = int(self.id_figure), float(self.radius)

    def draw(self, color='r'):
        """
        Draw circle
        :return: None
        """
        ax = plt.gca()
        ax.add_patch(plt.Circle((self.radius, self.radius), self.radius, color=color, fill=True))
        plt.axis('scaled')
        plt.show()

    def area(self):
        return np.pi * self.radius ** 2


class Triangle:

    def __init__(self, *args):
        self.id_figure, self.side_a, self.side_b, self.side_c = args[0]
        self.id_figure, self.side_a, self.side_b, self.side_c = int(self.id_figure), float(self.side_a), float(
            self.side_b), float(self.side_c)

    @classmethod
    def calc_angles(cls, a, b, c):
        """
        Calculate angle
        :param a: float
        :param b: float
        :param c: float
        :return: alpha, beta, gamma
        """
        alpha = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2. * b * c))
        beta = np.arccos((-b ** 2 + c ** 2 + a ** 2) / (2. * a * c))
        gamma = np.pi - alpha - beta
        return alpha, beta, gamma

    @classmethod
    def calc_point(cls, alpha, beta, c):
        """
        Calculate coordinate free point
        :param alpha: float
        :param beta: float
        :param c: float
        :return: (x, y)
        """
        x = (c * np.tan(beta)) / (np.tan(alpha) + np.tan(beta))
        y = x * np.tan(alpha)
        return tuple([x, y])

    @classmethod
    def get_triangle(cls, a, b, c):
        """
        Calculate coordinates 3 points
        :param a: float
        :param b: float
        :param c: float
        :return: list of tuples coordinates
        """
        z = np.array([a, b, c])
        while z[-1] != np.max(z):
            z = z[[2, 0, 1]]  # make sure last entry is largest
        alpha, beta, _ = cls.calc_angles(*z)
        x, y = cls.calc_point(alpha, beta, z[-1])
        return [(0, 0), (z[-1], 0), (x, y)]

    def draw(self, color='r'):
        """
        Draw triangle
        :return: None
        """
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        _triangle = plt.Polygon(self.get_triangle(self.side_a, self.side_b, self.side_c), color=color)
        ax.add_patch(_triangle)
        ax.autoscale_view()
        plt.show()

    def area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5

    def median(self):
        median_a = (2 * self.side_b ** 2 + 2 * self.side_c ** 2 + self.side_a ** 2) ** 2 / 2
        median_b = (2 * self.side_a ** 2 + 2 * self.side_c ** 2 + self.side_b ** 2) ** 2 / 2
        median_c = (2 * self.side_a ** 2 + 2 * self.side_b ** 2 + self.side_c ** 2) ** 2 / 2
        return median_a, median_b, median_c


class Square:

    def __init__(self, *args):
        self.id_figure, self.side_a = args[0]
        self.id_figure, self.side_a = int(self.id_figure), float(self.side_a)

    def draw(self, color='r'):
        """
        Draw square
        :return: None
        """
        ax = plt.gca()
        ax.add_patch(Rectangle(xy=(0, 0), width=self.side_a, height=self.side_a, angle=0.0, color=color))
        plt.axis('scaled')
        plt.show()

    def area(self):
        return self.side_a ** 2


class Rectangles:

    def __init__(self, *args):
        self.id_figure, self.side_a, self.side_b = args[0]
        self.id_figure, self.side_a, self.side_b = int(self.id_figure), float(self.side_a), float(self.side_b)

    def draw(self, color='r'):
        """
        Draw rectangle
        :return: None
        """
        ax = plt.gca()
        ax.add_patch(Rectangle(xy=(0, 0), width=self.side_a, height=self.side_b, angle=0.0, color=color))
        plt.axis('scaled')
        plt.show()

    def area(self):
        return self.side_a * self.side_b


class Trapezium:

    def __init__(self, *args):
        self.id_figure, self.base_a, self.base_b, self.height = args[0]
        self.id_figure, self.base_a, self.base_b, self.height = int(self.id_figure), float(self.base_a), float(
            self.base_b), float(self.height)

    def draw(self, color='r'):
        """
        Draw trapezium
        :return: None
        """
        x_1 = abs(self.base_a - self.base_b) / 2
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        trapezium = plt.Polygon([(0, 0), (x_1, self.height),
                                 (x_1 + np.min([self.base_a, self.base_b]),
                                  self.height),
                                 (np.max([self.base_a, self.base_b]), 0)], color=color)
        ax.add_patch(trapezium)
        ax.autoscale_view()
        plt.show()

    def area(self):
        return self.height * (self.base_a + self.base_b) / 2


class Rhombus:

    def __init__(self, *args):
        self.id_figure, self.side_a, self.angle = args[0]
        self.id_figure, self.side_a, self.angle = int(self.id_figure), float(self.side_a), float(self.angle)

    def draw(self, color='r'):
        """
        Draw rhombus
        :return: None
        """
        x = self.side_a * np.sin(math.radians(self.angle))
        y = self.side_a * np.cos(math.radians(self.angle))
        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        rhombus = plt.Polygon([(x, 0), (0, y), (x, y * 2), (x * 2, y)], color=color)
        ax.add_patch(rhombus)
        ax.autoscale_view()
        plt.show()

    def area(self):
        return self.side_a ** 2 * math.sin(np.radians(self.angle))
