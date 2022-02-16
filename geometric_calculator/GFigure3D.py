import numpy as np
from scipy.linalg import norm
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class GFigure3D:

    def __init__(self):
        self.fig = None
        self.ax = None

    def init(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.view_init(15, 15)

    def view_scale(self, x, y, z):  # TODO Axis labels are displayed incorrectly, you need to divide the axis by your value and not by the maximum
        """
        Formats labels on x, y, z axes
        :param x: float limit value x
        :param y: float limit value y
        :param z: float limit value z
        :return:None
        """
        self.ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        self.ax.xaxis.set_major_locator(MultipleLocator(x))
        self.ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        self.ax.yaxis.set_major_locator(MultipleLocator(y))
        self.ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        self.ax.zaxis.set_major_locator(MultipleLocator(z))

    def limit_axes(self, x, y, z):
        """
        Looking for the maximum value from x, y, z and sets the dimensions of the axes by the maximum value
        :param x: float limit value x
        :param y: float limit value y
        :param z: float limit value z
        :return:None
        """
        self.ax.set_xlim(0, np.max([x, y, z]))
        self.ax.set_ylim(0, np.max([x, y, z]))
        self.ax.set_zlim(0, np.max([x, y, z]))

    @classmethod
    def truncated_cone(cls, p0, p1, R0, R1):
        """
        Based on https://stackoverflow.com/a/39823124/190597 (astrokeat)
        https://stackoverflow.com/questions/48703275/3d-truncated-cone-in-python
        :param p0: np.array([x, y, z]) cone vertex coordinates
        :param p1: np.array([x, y, z]) cone base coordinates
        :param R0: float radius vertex
        :param R1: float radius base
        :return: X, Y, Z generated coordinates for surface
        """
        # vector in direction of axis
        v = p1 - p0
        # find magnitude of vector
        mag = norm(v)
        # unit vector in direction of axis
        v = v / mag
        # make some vector not in the same direction as v
        not_v = np.array([1, 1, 0])
        if (v == not_v).all():
            not_v = np.array([0, 1, 0])
        # make vector perpendicular to v
        n1 = np.cross(v, not_v)
        n1 /= norm(n1)
        # make unit vector perpendicular to v and n1
        n2 = np.cross(v, n1)
        # surface ranges over t from 0 to length of axis and 0 to 2*pi
        n = 80
        t = np.linspace(0, mag, n)
        theta = np.linspace(0, 2 * np.pi, n)
        # use meshgrid to make 2d arrays
        t, theta = np.meshgrid(t, theta)
        R = np.linspace(R0, R1, n)
        # generate coordinates for surface
        X, Y, Z = [p0[i] + v[i] * t + R *
                   np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in [0, 1, 2]]
        return X, Y, Z


class Sphere(GFigure3D):

    def __init__(self, *args):
        super().__init__()
        self.id_figure, self.radius = args[0]
        self.id_figure, self.radius = int(self.id_figure), float(self.radius)

    def draw(self, color='r'):
        """
        Draw sphere
        :param color: color
        :return: None
        """
        u, v = np.mgrid[0:np.pi:50j, 0:2 * np.pi:50j]
        x = self.radius * np.sin(u) * np.cos(v) + self.radius
        y = self.radius * np.sin(u) * np.sin(v) + self.radius
        z = self.radius * np.cos(u) + self.radius
        self.ax.plot_surface(x, y, z, color=color)
        self.view_scale(self.radius / 2, self.radius / 2, self.radius / 2)
        self.limit_axes(self.radius * 2, self.radius * 2, self.radius * 2)
        plt.show()

    def area(self):
        return np.pi * self.radius ** 2 * 4


class Cube(GFigure3D):

    def __init__(self, *args):
        super().__init__()
        self.id_figure, self.side_a = args[0]
        self.id_figure, self.side_a = int(self.id_figure), float(self.side_a)

    def draw(self, color='r'):
        """
        Draw cube
        :param color: color
        :return: None
        """
        x, y = np.meshgrid([0, self.side_a], [0, self.side_a])
        one = np.ones(4).reshape(2, 2)
        self.ax.plot_surface(x, y, one * self.side_a, color=color)
        self.ax.plot_surface(x, y, one * 0, color=color)
        self.ax.plot_surface(x, one * 0, y, color=color)
        self.ax.plot_surface(x, one * self.side_a, y, color=color)
        self.ax.plot_surface(one * self.side_a, x, y, color=color)
        self.ax.plot_surface(one * 0, x, y, color=color)
        self.view_scale(self.side_a / 2, self.side_a / 2, self.side_a / 2)
        plt.show()

    def area(self):
        return self.side_a ** 2 * 6


class Parallelepiped(GFigure3D):

    def __init__(self, *args):
        super().__init__()
        self.id_figure, self.side_a, self.side_b, self.side_c = args[0]
        self.id_figure, self.side_a, self.side_b, self.side_c = int(self.id_figure), float(self.side_a), float(
            self.side_b), float(self.side_c)

    def draw(self, color='r'):
        """
        Draw parallelepiped
        :param color: color
        :return: None
        """
        a, b, c = self.side_a, self.side_b, self.side_c
        r_x, r_y, r_z, = [0, a], [0, b], [0, c]
        one = np.ones(4).reshape(2, 2)
        x, y = np.meshgrid(r_x, r_y)
        self.ax.plot_surface(x, y, one * c, color=color)
        x, y = np.meshgrid(r_x, r_y)
        self.ax.plot_surface(x, y, one * 0, color=color)
        x, z = np.meshgrid(r_x, r_z)
        self.ax.plot_surface(x, one * 0, z, color=color)
        x, z = np.meshgrid(r_x, r_z)
        self.ax.plot_surface(x, one * b, z, color=color)
        y, z = np.meshgrid(r_y, r_z)
        self.ax.plot_surface(one * a, y, z, color=color)
        y, z = np.meshgrid(r_y, r_z)
        self.ax.plot_surface(one * 0, y, z, color=color)
        self.view_scale(a / 2, b / 2, c / 2)
        self.limit_axes(a, b, c)
        plt.show()

    def area(self):
        return 2 * (self.side_a * self.side_b + self.side_a * self.side_c + self.side_b * self.side_c)


class Pyramid(GFigure3D):

    def __init__(self, *args):
        super().__init__()
        self.id_figure, self.base_a, self.height = args[0]
        self.id_figure, self.base_a, self.height = int(self.id_figure), float(self.base_a), float(self.height)

    def draw(self, color='r'):
        """
        Draw pyramid
        :param color: color
        :return: None
        """
        x = self.base_a
        h = self.height
        coord_prmd = np.array([
            [0, 0, 0],
            [x, 0, 0],
            [x, x, 0],
            [0, x, 0],
            [x / 2, x / 2, h]
        ])
        # generate list of sides' polygons of our pyramid
        points_for_trace = [[coord_prmd[0], coord_prmd[1], coord_prmd[4]],
                            [coord_prmd[0], coord_prmd[3], coord_prmd[4]],
                            [coord_prmd[2], coord_prmd[1], coord_prmd[4]],
                            [coord_prmd[2], coord_prmd[3], coord_prmd[4]],
                            [coord_prmd[0], coord_prmd[1], coord_prmd[2], coord_prmd[3]]]
        self.ax.add_collection3d(Poly3DCollection(points_for_trace, facecolors=color, edgecolors='black'))
        self.view_scale(x / 2, x / 2, h / 2)
        self.limit_axes(x, x, h)
        plt.show()

    def area(self):
        return self.base_a * (self.base_a + 2 * self.height)


class Cylinder(GFigure3D):

    def __init__(self, *args):
        super().__init__()
        self.id_figure, self.radius, self.height = args[0]
        self.id_figure, self.radius, self.height = int(self.id_figure), float(self.radius), float(self.height)

    def draw(self, color='r'):
        """
        Draw cylinder
        :param color: color
        :return: None
        """
        A0 = np.array([self.radius, self.radius, self.height])
        A1 = np.array([self.radius, self.radius, 0])
        X, Y, Z = self.truncated_cone(A0, A1, self.radius, self.radius)
        self.ax.plot_surface(X, Y, Z, color=color, linewidth=0, antialiased=False)

        u, v = np.mgrid[0:np.pi:100j, 0:2 * np.pi:100j]
        x = self.radius * np.sin(u) * np.cos(v) + self.radius
        y = self.radius * np.sin(u) * np.sin(v) + self.radius
        z = self.radius * np.cos(u) * 0 + self.height * 0
        self.ax.plot_surface(x, y, z, color=color)

        z = self.radius * np.cos(u) * 0 + self.height
        self.ax.plot_surface(x, y, z, color=color)

        self.view_scale(self.radius, self.radius, self.height / 2)
        plt.show()

    def area(self):
        return 2 * np.pi * self.radius * (self.radius + self.height)


class Cone(GFigure3D):

    def __init__(self, *args):
        super().__init__()
        self.id_figure, self.radius, self.height = args[0]
        self.id_figure, self.radius, self.height = int(self.id_figure), float(self.radius), float(self.height)

    def draw(self, color='r'):
        """
        Draw cone
        :param color: color
        :return: None
        """
        A0 = np.array([self.radius, self.radius, self.height])
        A1 = np.array([self.radius, self.radius, 0])
        X, Y, Z = self.truncated_cone(A0, A1, 0, self.radius)
        self.ax.plot_surface(X, Y, Z, color=color, linewidth=0, antialiased=False)

        u, v = np.mgrid[0:np.pi:100j, 0:2 * np.pi:100j]
        x = self.radius * np.sin(u) * np.cos(v) + self.radius
        y = self.radius * np.sin(u) * np.sin(v) + self.radius
        z = self.radius * np.cos(u) * 0 + self.height * 0
        self.ax.plot_surface(x, y, z, color=color)

        self.view_scale(self.radius, self.radius, self.height / 2)
        plt.show()

    def area(self):
        lateral_line = (self.radius ** 2 + self.height ** 2) ** 0.5
        return np.pi * self.radius * (self.radius + lateral_line)
