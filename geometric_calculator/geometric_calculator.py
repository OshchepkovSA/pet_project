from tkinter import *
import tkinter as tk  # python 3
import numpy as np
import math
from scipy.linalg import norm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import Rectangle
plt.rcParams["backend"] = "TkAgg"


class GFigure3D:

    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.view_init(15, 15)

    def view_scale(self, x, y, z): # TODO Axis labels are displayed incorrectly, you need to divide the axis by your value and not by the maximum
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

    def sphere(self, radius):
        """
        Draw sphere
        :param radius: float
        :return: None
        """
        u, v = np.mgrid[0:np.pi:50j, 0:2 * np.pi:50j]
        x = radius * np.sin(u) * np.cos(v) + radius
        y = radius * np.sin(u) * np.sin(v) + radius
        z = radius * np.cos(u) + radius
        self.ax.plot_surface(x, y, z, color='red')
        self.view_scale(radius/2, radius/2, radius/2)
        self.limit_axes(radius*2, radius*2, radius*2)
        plt.show()

    def cube(self, side_a):
        """
        Draw cube
        :param side_a: float
        :return: None
        """
        x, y = np.meshgrid([0, side_a], [0, side_a])
        one = np.ones(4).reshape(2, 2)
        self.ax.plot_surface(x, y, one * side_a, color='red')
        self.ax.plot_surface(x, y, one * 0, color='red')
        self.ax.plot_surface(x, one * 0, y, color='red')
        self.ax.plot_surface(x, one * side_a, y, color='red')
        self.ax.plot_surface(one * side_a, x, y, color='red')
        self.ax.plot_surface(one * 0, x, y, color='red')
        self.view_scale(side_a/2, side_a/2, side_a/2)
        plt.show()

    def parallelepiped(self, side_a, side_b, side_c):
        """
        Draw parallelepiped
        :param side_a: float
        :param side_b: float
        :param side_c: float
        :return: None
        """
        a = side_a
        b = side_b
        c = side_c
        r_x = [0, a]
        r_y = [0, b]
        r_z = [0, c]
        one = np.ones(4).reshape(2, 2)
        x, y = np.meshgrid(r_x, r_y)
        self.ax.plot_surface(x, y, one * c, color='r')
        x, y = np.meshgrid(r_x, r_y)
        self.ax.plot_surface(x, y, one * 0, color='r')
        x, z = np.meshgrid(r_x, r_z)
        self.ax.plot_surface(x, one * 0, z, color='r')
        x, z = np.meshgrid(r_x, r_z)
        self.ax.plot_surface(x, one * b, z, color='r')
        y, z = np.meshgrid(r_y, r_z)
        self.ax.plot_surface(one * a, y, z, color='r')
        y, z = np.meshgrid(r_y, r_z)
        self.ax.plot_surface(one * 0, y, z, color='r')
        self.view_scale(a/2, b/2, c/2)
        self.limit_axes(a, b, c)
        plt.show()

    def pyramid(self, base_a, height):
        """
        Draw pyramid
        :param base_a: float
        :param height: float
        :return: None
        """
        x = base_a
        h = height
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
        self.ax.add_collection3d(Poly3DCollection(points_for_trace, facecolors='r', edgecolors='black'))
        self.view_scale(x/2, x/2, h/2)
        self.limit_axes(x, x, h)
        plt.show()

    def cylinder(self, radius, height):
        """
        Draw cylinder
        :param radius: float
        :param height: float
        :return: None
        """
        A0 = np.array([radius, radius, height])
        A1 = np.array([radius, radius, 0])
        X, Y, Z = self.truncated_cone(A0, A1, radius, radius)
        self.ax.plot_surface(X, Y, Z, color='r', linewidth=0, antialiased=False)

        u, v = np.mgrid[0:np.pi:100j, 0:2 * np.pi:100j]
        x = radius * np.sin(u) * np.cos(v) + radius
        y = radius * np.sin(u) * np.sin(v) + radius
        z = radius * np.cos(u) * 0 + height * 0
        self.ax.plot_surface(x, y, z, color='r')

        z = radius * np.cos(u) * 0 + height
        self.ax.plot_surface(x, y, z, color='r')

        self.view_scale(radius, radius, height / 2)
        plt.show()

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

    def cone(self, radius, height):
        """
        Draw cone
        :param radius: float
        :param height: float
        :return: None
        """
        A0 = np.array([radius, radius, height])
        A1 = np.array([radius, radius, 0])
        X, Y, Z = self.truncated_cone(A0, A1, 0, radius)
        self.ax.plot_surface(X, Y, Z, color='r', linewidth=0, antialiased=False)

        u, v = np.mgrid[0:np.pi:100j, 0:2 * np.pi:100j]
        x = radius * np.sin(u) * np.cos(v) + radius
        y = radius * np.sin(u) * np.sin(v) + radius
        z = radius * np.cos(u) * 0 + height*0
        self.ax.plot_surface(x, y, z, color='r')

        self.view_scale(radius, radius, height/2)
        plt.show()


class GFigure2D:

    def __init__(self):
        self.ax = None
        self.round = None
        self.fig = None

    def circle(self, radius):
        """
        Draw circle
        :param radius: float
        :return: None
        """
        self.ax = plt.gca()
        self.round = plt.Circle((radius, radius), radius, color='r', fill=True)
        self.ax.add_patch(self.round)
        plt.axis('scaled')
        plt.show()

    def square(self, side_a):
        """
        Draw square
        :param side_a: float
        :return: None
        """
        self.ax = plt.gca()
        self.ax.add_patch(Rectangle(xy=(0, 0), width=side_a, height=side_a, angle=0.0, color='r'))
        plt.axis('scaled')
        plt.show()

    def rectangle(self, side_a, side_b):
        """
        Draw rectangle
        :param side_a: float
        :param side_b: float
        :return: None
        """
        self.ax = plt.gca()
        self.ax.add_patch(Rectangle(xy=(0, 0), width=side_a, height=side_b, angle=0.0, color='r'))
        plt.axis('scaled')
        plt.show()

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

    def triangle(self, side_a, side_b, side_c):
        """
        Draw triangle
        :param side_a: float
        :param side_b: float
        :param side_c: float
        :return: None
        """
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal")
        _triangle = plt.Polygon(self.get_triangle(side_a, side_b, side_c))
        self.ax.add_patch(_triangle)
        self.ax.autoscale_view()
        plt.show()

    def trapezium(self, base_a, base_b, height):
        """
        Draw trapezium
        :param base_a: float
        :param base_b: float
        :param height: float
        :return: None
        """
        x_1 = abs(base_a - base_b) / 2
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal")
        trapez = plt.Polygon(
            [(0, 0), (x_1, height), (x_1 + np.min([base_a, base_b]), height), (np.max([base_a, base_b]), 0)], color='r')
        self.ax.add_patch(trapez)
        self.ax.autoscale_view()
        plt.show()

    def rhombus(self, side_a, angle):
        """
        Draw rhombus
        :param side_a: float
        :param angle: float
        :return: None
        """
        x = side_a * np.sin(math.radians(angle))
        y = side_a * np.cos(math.radians(angle))
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal")
        rhomb = plt.Polygon([(x, 0), (0, y), (x, y * 2), (x * 2, y)], color='r')
        self.ax.add_patch(rhomb)
        self.ax.autoscale_view()
        plt.show()


class Window(tk.Tk, GFigure3D, GFigure2D, Axes3D):

    @staticmethod
    def question_to_start():
        """
        This is humor ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
        :return: boolean
        """
        if answer in ['Да', 'да', 'yes', 'y', 'Y', 'Д', 'д', 'Yes']:
            return True
        return False

    def __init__(self, title, geometry):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.id_figure = IntVar()
        self.side_a = StringVar()
        self.side_b = StringVar()
        self.side_c = StringVar()
        self.height = StringVar()
        self.base_a = StringVar()
        self.base_b = StringVar()
        self.radius = StringVar()
        self.angle = StringVar()
        self.rdb = None
        self.text = ''
        self.value = 0
        self.row = 0
        self.column = 0
        self.command = None
        self.show_btn = None
        self.text_name = dict()
        self.object_destroy = []
        self.entry_radius = None
        self.entry_side_a = None
        self.entry_side_b = None
        self.entry_side_c = None
        self.entry_base_a = None
        self.entry_base_b = None
        self.entry_height = None
        self.entry_angle = None
        self.fig2d = None
        self.fig3d = None
        self.median_a = 0
        self.median_b = 0
        self.median_c = 0

    def rdb_draw(self, text, value, row, column):
        """
        Draw radiobutton in tkinter
        :param text: str
        :param value: int
        :param row: int
        :param column: int
        :return: object
        """
        self.rdb = tk.Radiobutton(self, text=text, value=value, variable=self.id_figure,
                                  padx=15, pady=10, command=self.parameter_field)
        self.rdb.grid(row=row, column=column, sticky=W)
        self.text_name[value] = text
        return self.rdb

    def btn_draw(self, text, row, column, command):
        """
        Draw button in tkinter
        :param text: str
        :param row: int
        :param column: int
        :param command: function
        :return: object
        """
        self.show_btn = tk.Button(self, text=text, background="#555", foreground="#ccc",
                                  padx="15", pady="10", font="16", command=command)
        self.show_btn.grid(row=row, column=column, sticky=W)
        return self.show_btn

    def parameter_field(self):
        """
        Draw field entry
        :return: None
        """
        if self.id_figure.get() != 0:
            for object_name in self.object_destroy:
                object_name.destroy()
            label = tk.Label(text=self.text_name[self.id_figure.get()])
            label.grid(row=0, column=2, sticky=NW)
            self.object_destroy.append(label)
            if self.id_figure.get() == 1:  # Circle
                label_radius = tk.Label(text='Radius')
                label_radius.grid(row=1, column=2, sticky=NW)
                self.entry_radius = tk.Entry(textvariable=self.radius)
                self.entry_radius.grid(row=2, column=2, sticky=NW)
                self.object_destroy.append(label_radius)
                self.object_destroy.append(self.entry_radius)
            elif self.id_figure.get() == 2:  # Square
                label_side_a = tk.Label(text='Side A')
                label_side_a.grid(row=1, column=2, sticky=NW)
                self.entry_side_a = tk.Entry(textvariable=self.side_a)
                self.entry_side_a.grid(row=2, column=2, sticky=NW)
                self.object_destroy.append(label_side_a)
                self.object_destroy.append(self.entry_side_a)
            elif self.id_figure.get() == 3:  # Rectangle
                label_side_a = tk.Label(text='Side A')
                label_side_a.grid(row=1, column=2, sticky=NW)
                self.entry_side_a = tk.Entry(textvariable=self.side_a)
                self.entry_side_a.grid(row=2, column=2, sticky=NW)
                label_side_b = tk.Label(text='Side B')
                label_side_b.grid(row=3, column=2, sticky=NW)
                self.entry_side_b = tk.Entry(textvariable=self.side_b)
                self.entry_side_b.grid(row=4, column=2, sticky=NW)
                self.object_destroy.append(label_side_a)
                self.object_destroy.append(self.entry_side_a)
                self.object_destroy.append(label_side_b)
                self.object_destroy.append(self.entry_side_b)
            elif self.id_figure.get() == 4:  # Triangle
                label_side_a = tk.Label(text='Side A')
                label_side_a.grid(row=1, column=2, sticky=NW)
                self.entry_side_a = tk.Entry(textvariable=self.side_a)
                self.entry_side_a.grid(row=2, column=2, sticky=NW)
                label_side_b = tk.Label(text='Side B')
                label_side_b.grid(row=3, column=2, sticky=NW)
                self.entry_side_b = tk.Entry(textvariable=self.side_b)
                self.entry_side_b.grid(row=4, column=2, sticky=NW)
                label_side_c = tk.Label(text='Side C')
                label_side_c.grid(row=5, column=2, sticky=NW)
                self.entry_side_c = tk.Entry(textvariable=self.side_c)
                self.entry_side_c.grid(row=6, column=2, sticky=NW)
                self.object_destroy.append(label_side_a)
                self.object_destroy.append(self.entry_side_a)
                self.object_destroy.append(label_side_b)
                self.object_destroy.append(self.entry_side_b)
                self.object_destroy.append(label_side_c)
                self.object_destroy.append(self.entry_side_c)
            elif self.id_figure.get() == 5:  # Trapezium isosceles
                label_base_a = tk.Label(text='Base A')
                label_base_a.grid(row=1, column=2, sticky=NW)
                self.entry_base_a = tk.Entry(textvariable=self.base_a)
                self.entry_base_a.grid(row=2, column=2, sticky=NW)
                label_base_b = tk.Label(text='Base B')
                label_base_b.grid(row=3, column=2, sticky=NW)
                self.entry_base_b = tk.Entry(textvariable=self.base_b)
                self.entry_base_b.grid(row=4, column=2, sticky=NW)
                label_height = tk.Label(text='Height')
                label_height.grid(row=5, column=2, sticky=NW)
                self.entry_height = tk.Entry(textvariable=self.height)
                self.entry_height.grid(row=6, column=2, sticky=NW)
                self.object_destroy.append(label_base_a)
                self.object_destroy.append(self.entry_base_a)
                self.object_destroy.append(label_base_b)
                self.object_destroy.append(self.entry_base_b)
                self.object_destroy.append(label_height)
                self.object_destroy.append(self.entry_height)
            elif self.id_figure.get() == 6:  # Rhombus
                label_side_a = tk.Label(text='Side A')
                label_side_a.grid(row=1, column=2, sticky=NW)
                self.entry_side_a = tk.Entry(textvariable=self.side_a)
                self.entry_side_a.grid(row=2, column=2, sticky=NW)
                label_angle = tk.Label(text='Angle')
                label_angle.grid(row=3, column=2, sticky=NW)
                self.entry_angle = tk.Entry(textvariable=self.angle)
                self.entry_angle.grid(row=4, column=2, sticky=NW)
                self.object_destroy.append(label_side_a)
                self.object_destroy.append(self.entry_side_a)
                self.object_destroy.append(label_angle)
                self.object_destroy.append(self.entry_angle)
            elif self.id_figure.get() == 7:  # Sphere
                label_radius = tk.Label(text='Radius')
                label_radius.grid(row=1, column=2, sticky=NW)
                self.entry_radius = tk.Entry(textvariable=self.radius)
                self.entry_radius.grid(row=2, column=2, sticky=NW)
                self.object_destroy.append(label_radius)
                self.object_destroy.append(self.entry_radius)
            elif self.id_figure.get() == 8:  # Cube
                label_side_a = tk.Label(text='Side A')
                label_side_a.grid(row=1, column=2, sticky=NW)
                self.entry_side_a = tk.Entry(textvariable=self.side_a)
                self.entry_side_a.grid(row=2, column=2, sticky=NW)
                self.object_destroy.append(label_side_a)
                self.object_destroy.append(self.entry_side_a)
            elif self.id_figure.get() == 9:  # Parallelepiped
                label_side_a = tk.Label(text='Side A')
                label_side_a.grid(row=1, column=2, sticky=NW)
                self.entry_side_a = tk.Entry(textvariable=self.side_a)
                self.entry_side_a.grid(row=2, column=2, sticky=NW)
                label_side_b = tk.Label(text='Side B')
                label_side_b.grid(row=3, column=2, sticky=NW)
                self.entry_side_b = tk.Entry(textvariable=self.side_b)
                self.entry_side_b.grid(row=4, column=2, sticky=NW)
                label_side_c = tk.Label(text='Side C')
                label_side_c.grid(row=5, column=2, sticky=NW)
                self.entry_side_c = tk.Entry(textvariable=self.side_c)
                self.entry_side_c.grid(row=6, column=2, sticky=NW)
                self.object_destroy.append(label_side_a)
                self.object_destroy.append(self.entry_side_a)
                self.object_destroy.append(label_side_b)
                self.object_destroy.append(self.entry_side_b)
                self.object_destroy.append(label_side_c)
                self.object_destroy.append(self.entry_side_c)
            elif self.id_figure.get() == 10:  # Pyramid isosceles
                label_base_a = tk.Label(text='Base A')
                label_base_a.grid(row=1, column=2, sticky=NW)
                self.entry_base_a = tk.Entry(textvariable=self.base_a)
                self.entry_base_a.grid(row=2, column=2, sticky=NW)
                label_height = tk.Label(text='Height')
                label_height.grid(row=3, column=2, sticky=NW)
                self.entry_height = tk.Entry(textvariable=self.height)
                self.entry_height.grid(row=4, column=2, sticky=NW)
                self.object_destroy.append(label_base_a)
                self.object_destroy.append(self.entry_base_a)
                self.object_destroy.append(label_height)
                self.object_destroy.append(self.entry_height)
            elif self.id_figure.get() == 11:  # Cylinder
                label_radius = tk.Label(text='Radius')
                label_radius.grid(row=1, column=2, sticky=NW)
                self.entry_radius = tk.Entry(textvariable=self.radius)
                self.entry_radius.grid(row=2, column=2, sticky=NW)
                label_height = tk.Label(text='Height')
                label_height.grid(row=3, column=2, sticky=NW)
                self.entry_height = tk.Entry(textvariable=self.height)
                self.entry_height.grid(row=4, column=2, sticky=NW)
                self.object_destroy.append(label_radius)
                self.object_destroy.append(self.entry_radius)
                self.object_destroy.append(label_height)
                self.object_destroy.append(self.entry_height)
            elif self.id_figure.get() == 12:  # Cone
                label_radius = tk.Label(text='Radius')
                label_radius.grid(row=1, column=2, sticky=NW)
                self.entry_radius = tk.Entry(textvariable=self.radius)
                self.entry_radius.grid(row=2, column=2, sticky=NW)
                label_height = tk.Label(text='Height')
                label_height.grid(row=3, column=2, sticky=NW)
                self.entry_height = tk.Entry(textvariable=self.height)
                self.entry_height.grid(row=4, column=2, sticky=NW)
                self.object_destroy.append(label_radius)
                self.object_destroy.append(self.entry_radius)
                self.object_destroy.append(label_height)
                self.object_destroy.append(self.entry_height)

    def click_show_btn(self):  # TODO Input Validation
        """
        Event click button "ShowMe"
        :return: None
        """
        if self.id_figure.get() != 0:
            if self.id_figure.get() == 1:  # Circle
                self.fig2d = GFigure2D()
                self.fig2d.circle(float(self.radius.get()))
            if self.id_figure.get() == 2:  # Square
                fig2d = GFigure2D()
                fig2d.square(float(self.side_a.get()))
            if self.id_figure.get() == 3:  # Rectangle
                fig2d = GFigure2D()
                fig2d.rectangle(float(self.side_a.get()), float(self.side_b.get()))
            if self.id_figure.get() == 4:  # Triangle
                fig2d = GFigure2D()
                fig2d.triangle(float(self.side_a.get()), float(self.side_b.get()), float(self.side_c.get()))
            if self.id_figure.get() == 5:  # Trapezium
                fig2d = GFigure2D()
                fig2d.trapezium(float(self.base_a.get()), float(self.base_b.get()), float(self.height.get()))
            if self.id_figure.get() == 6:  # Rhombus
                fig2d = GFigure2D()
                fig2d.rhombus(float(self.side_a.get()), float(self.angle.get()))
            if self.id_figure.get() == 7:  # Sphere
                fig3d = GFigure3D()
                fig3d.sphere(float(self.radius.get()))
            if self.id_figure.get() == 8:  # Cube
                fig3d = GFigure3D()
                fig3d.cube(float(self.side_a.get()))
            if self.id_figure.get() == 9:  # Parallelepiped
                fig3d = GFigure3D()
                fig3d.parallelepiped(float(self.side_a.get()), float(self.side_b.get()), float(self.side_c.get()))
            if self.id_figure.get() == 10:  # Pyramid
                fig3d = GFigure3D()
                fig3d.pyramid(float(self.base_a.get()), float(self.height.get()))
            if self.id_figure.get() == 11:  # Cylinder
                fig3d = GFigure3D()
                fig3d.cylinder(float(self.radius.get()), float(self.height.get()))
            if self.id_figure.get() == 12:  # Cone
                fig3d = GFigure3D()
                fig3d.cone(float(self.radius.get()), float(self.height.get()))

    def click_calc_btn(self):  # TODO Input Validation
        """
        Event click button "CalcMe"
        :return: None
        """
        root_calc_btn = Window("Calculation figure", "300x150")
        Label(root_calc_btn, text="Area: " + str(round(self.area(), 2))).pack()
        if self.id_figure.get() == 4:
            med_a, med_b, med_c = self.median()
            text = "Median A: " + str(round(med_a, 2)) + \
                   "\n"+"Median B: " + str(round(med_b, 2)) + \
                   "\n"+"Median C: "+str(round(med_c, 2))
            Label(root_calc_btn, text=text).pack()
        root_calc_btn.mainloop()

    def area(self):
        """
        Calculate area
        :return: float area
        """
        if self.id_figure.get() != 0:
            if self.id_figure.get() == 1:  # Circle
                return np.pi * float(self.radius.get())**2
            if self.id_figure.get() == 2:  # Square
                return float(self.side_a.get()) ** 2
            if self.id_figure.get() == 3:  # Rectangle
                return float(self.side_a.get()) * float(self.side_b.get())
            if self.id_figure.get() == 4:  # Triangle
                p = (float(self.side_a.get())+float(self.side_b.get())+float(self.side_c.get()))/2
                return (p*(p-float(self.side_a.get()))*(p-float(self.side_b.get()))*(p-float(self.side_c.get())))**0.5
            if self.id_figure.get() == 5:  # Trapezium
                return float(self.height.get())*((float(self.base_a.get())+float(self.base_b.get()))/2)
            if self.id_figure.get() == 6:  # Rhombus
                return float(self.side_a.get())**2 * math.sin(np.radians(float(self.angle.get())))
            if self.id_figure.get() == 7:  # Sphere
                return np.pi * float(self.radius.get())**2 * 4
            if self.id_figure.get() == 8:  # Cube
                return float(self.side_a.get()) ** 2 * 6
            if self.id_figure.get() == 9:  # Parallelepiped
                return 2 * (float(self.side_a.get())*float(self.side_b.get()) +
                            float(self.side_a.get())*float(self.side_c.get()) +
                            float(self.side_b.get())*float(self.side_c.get()))
            if self.id_figure.get() == 10:  # Pyramid
                return float(self.base_a.get()) * (float(self.base_a.get()) + 2*float(self.height.get()))
            if self.id_figure.get() == 11:  # Cylinder
                return 2*np.pi*float(self.radius.get()) * (float(self.radius.get()) + float(self.height.get()))
            if self.id_figure.get() == 12:  # Cone
                lateral_line = (float(self.radius.get())**2 + float(self.height.get())**2)**0.5
                return np.pi*float(self.radius.get()) * (float(self.radius.get()) + lateral_line)

    def median(self):
        """
        Calculate median triangle
        :return: float median
        """
        self.median_a = (2*float(self.side_b.get())**2 + 2*float(self.side_c.get())**2 + float(self.side_a.get())**2)**2/2
        self.median_b = (2*float(self.side_a.get())**2 + 2*float(self.side_c.get())**2 + float(self.side_b.get())**2)**2/2
        self.median_c = (2*float(self.side_a.get())**2 + 2*float(self.side_b.get())**2 + float(self.side_c.get())**2)**2/2
        return self.median_a, self.median_b, self.median_c


print('Вы уверены что хотите запустить программу? Да/Нет...')
answer = input()
if Window.question_to_start():
    root = Window("Geometric calculator", "500x350")
    header = Label(root, text="Choose figure:", padx=15, pady=10)
    header.grid(row=0, column=0, sticky=W)
    circle = root.rdb_draw(text="Circle", value=1, row=1, column=0)
    square = root.rdb_draw(text="Square", value=2, row=2, column=0)
    rectangle = root.rdb_draw(text="Rectangle", value=3, row=3, column=0)
    triangle = root.rdb_draw(text="Triangle", value=4, row=4, column=0)
    trapezium = root.rdb_draw(text="Trapezium", value=5, row=5, column=0)
    rhombus = root.rdb_draw(text="Rhombus", value=6, row=6, column=0)
    sphere = root.rdb_draw(text="Sphere", value=7, row=1, column=1)
    cube = root.rdb_draw(text="Cube", value=8, row=2, column=1)
    parallelepiped = root.rdb_draw(text="Parallelepiped", value=9, row=3, column=1)
    pyramid = root.rdb_draw(text="Pyramid", value=10, row=4, column=1)
    cylinder = root.rdb_draw(text="Cylinder", value=11, row=5, column=1)
    cone = root.rdb_draw(text="Cone", value=12, row=6, column=1)
    show_btn = root.btn_draw(text="ShowMe", row=7, column=0, command=root.click_show_btn)
    calc_btn = root.btn_draw(text="CalcMe", row=7, column=1, command=root.click_calc_btn)

    if __name__ == "__main__":
        root.mainloop()

