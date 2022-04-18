from tkinter import *
import tkinter as tk  # python 3


class Window(tk.Tk):

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
        # self.fig2d = None
        # self.fig3d = None
        # self.median_a = 0
        # self.median_b = 0
        # self.median_c = 0

    @staticmethod
    def question_to_start(answer):
        """
        This is humor ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
        :return: boolean
        """
        return answer in ['Да', 'да', 'yes', 'y', 'Y', 'Д', 'д', 'Yes']

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
        Draw field entry, return data fields
        :return: tuple((),)
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
                return self.id_figure.get(), self.radius.get()
            elif self.id_figure.get() == 2:  # Square
                label_side_a = tk.Label(text='Side A')
                label_side_a.grid(row=1, column=2, sticky=NW)
                self.entry_side_a = tk.Entry(textvariable=self.side_a)
                self.entry_side_a.grid(row=2, column=2, sticky=NW)
                self.object_destroy.append(label_side_a)
                self.object_destroy.append(self.entry_side_a)
                return self.id_figure.get(), self.side_a.get()
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
                return self.id_figure.get(), self.side_a.get(), self.side_b.get()
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
                return self.id_figure.get(), self.side_a.get(), self.side_b.get(), self.side_c.get()
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
                return self.id_figure.get(), self.base_a.get(), self.base_b.get(), self.height.get()
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
                return self.id_figure.get(), self.side_a.get(), self.angle.get()
            elif self.id_figure.get() == 7:  # Sphere
                label_radius = tk.Label(text='Radius')
                label_radius.grid(row=1, column=2, sticky=NW)
                self.entry_radius = tk.Entry(textvariable=self.radius)
                self.entry_radius.grid(row=2, column=2, sticky=NW)
                self.object_destroy.append(label_radius)
                self.object_destroy.append(self.entry_radius)
                return self.id_figure.get(), self.radius.get()
            elif self.id_figure.get() == 8:  # Cube
                label_side_a = tk.Label(text='Side A')
                label_side_a.grid(row=1, column=2, sticky=NW)
                self.entry_side_a = tk.Entry(textvariable=self.side_a)
                self.entry_side_a.grid(row=2, column=2, sticky=NW)
                self.object_destroy.append(label_side_a)
                self.object_destroy.append(self.entry_side_a)
                return self.id_figure.get(), self.side_a.get()
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
                return self.id_figure.get(), self.side_a.get(), self.side_b.get(), self.side_c.get()
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
                return self.id_figure.get(), self.base_a.get(), self.height.get()
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
                return self.id_figure.get(), self.radius.get(), self.height.get()
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
                return self.id_figure.get(), self.radius.get(), self.height.get()
