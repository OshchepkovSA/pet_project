from tkinter import *
from geometric_calculator.GFigure2D import *
from geometric_calculator.GFigure3D import *
from geometric_calculator.Window import Window

plt.rcParams["backend"] = "TkAgg"


def check_input_positiv_float(*parameter_field):
    """
    Checking for a positive number input
    :param parameter_field: tuple((),)
    :return: boolean
    """
    try:
        for el in parameter_field[0]:
            if not (float(el) > 0):
                return False
        return True
    except:
        return False


def check_triangle_correct(*parameter_field):
    """
    Triangle Input Validation
    :param parameter_field:  tuple((),)
    :return: boolean
    """
    id_figure, side_a, side_b, side_c = parameter_field[0]
    id_figure, side_a, side_b, side_c = int(id_figure), float(side_a), float(side_b), float(side_c)
    if ((side_a + side_b) > side_c) & ((side_b + side_c) > side_a) & ((side_a + side_c) > side_b):
        return True
    return False


def check_romb_angle_correct(*parameter_field):
    """
    Rhombus Input Validation
    :param parameter_field:  tuple((),)
    :return: boolean
    """
    id_figure, side_a, angle = parameter_field[0]
    id_figure, side_a, angle = int(id_figure), float(side_a), float(angle)
    if angle < 90:
        return True
    return False


def click_calc_btn(*parameter_field):
    """
    Event click button "CalcMe"
    :return: None
    """
    text = ''
    if check_input_positiv_float(parameter_field[0]):
        id_figure = int(parameter_field[0][0])
        if id_figure == 1:  # Circle
            fig1 = Circle(parameter_field[0])
        elif id_figure == 2:  # Square
            fig1 = Square(parameter_field[0])
        elif id_figure == 3:  # Rectangle
            fig1 = Rectangles(parameter_field[0])
        elif id_figure == 4:  # Triangle
            if check_triangle_correct(parameter_field[0]):
                fig1 = Triangle(parameter_field[0])
                med_a, med_b, med_c = fig1.median()
                text = "Median A: " + str(round(med_a, 2)) + \
                       "\n" + "Median B: " + str(round(med_b, 2)) + \
                       "\n" + "Median C: " + str(round(med_c, 2))
            else:
                return None
        elif id_figure == 5:  # Trapezium
            fig1 = Trapezium(parameter_field[0])
        elif id_figure == 6:  # Rhombus
            if check_romb_angle_correct(parameter_field[0]):
                fig1 = Rhombus(parameter_field[0])
            else:
                return None
        elif id_figure == 7:  # Sphere
            fig1 = Sphere(parameter_field[0])
        elif id_figure == 8:  # Cube
            fig1 = Cube(parameter_field[0])
        elif id_figure == 9:  # Parallelepiped
            fig1 = Parallelepiped(parameter_field[0])
        elif id_figure == 10:  # Pyramid
            fig1 = Pyramid(parameter_field[0])
        elif id_figure == 11:  # Cylinder
            fig1 = Cylinder(parameter_field[0])
        elif id_figure == 12:  # Cone
            fig1 = Cone(parameter_field[0])
        root_calc_btn = Window("Calculation figure", "300x150")
        Label(root_calc_btn, text="Area: " + str(round(fig1.area(), 2))).pack()
        Label(root_calc_btn, text=text).pack()


def click_show_btn(*parameter_field):
    """
    Event click button "ShowMe"
    :return: None
    """
    if check_input_positiv_float(parameter_field[0]):
        id_figure = int(parameter_field[0][0])
        if id_figure == 1:  # Circle
            fig1 = Circle(parameter_field[0])
        elif id_figure == 2:  # Square
            fig1 = Square(parameter_field[0])
        elif id_figure == 3:  # Rectangle
            fig1 = Rectangles(parameter_field[0])
        elif id_figure == 4:  # Triangle
            if check_triangle_correct(parameter_field[0]):
                fig1 = Triangle(parameter_field[0])
            else:
                return None
        elif id_figure == 5:  # Trapezium
            fig1 = Trapezium(parameter_field[0])
        elif id_figure == 6:  # Rhombus
            if check_romb_angle_correct(parameter_field[0]):
                fig1 = Rhombus(parameter_field[0])
            else:
                return None
        elif id_figure == 7:  # Sphere
            fig1 = Sphere(parameter_field[0])
            fig1.init()
        elif id_figure == 8:  # Cube
            fig1 = Cube(parameter_field[0])
            fig1.init()
        elif id_figure == 9:  # Parallelepiped
            fig1 = Parallelepiped(parameter_field[0])
            fig1.init()
        elif id_figure == 10:  # Pyramid
            fig1 = Pyramid(parameter_field[0])
            fig1.init()
        elif id_figure == 11:  # Cylinder
            fig1 = Cylinder(parameter_field[0])
            fig1.init()
        elif id_figure == 12:  # Cone
            fig1 = Cone(parameter_field[0])
            fig1.init()
        fig1.draw()


def main():
    plt.rcParams["backend"] = "TkAgg"
    print('Вы уверены что хотите запустить программу? Да/Нет...')
    answer = input()
    if Window.question_to_start(answer):
        root = Window("Geometric calculator", "500x350")
        header = Label(root, text="Choose figure:", padx=15, pady=10)
        header.grid(row=0, column=0, sticky=W)
        root.rdb_draw(text="Circle", value=1, row=1, column=0)
        root.rdb_draw(text="Square", value=2, row=2, column=0)
        root.rdb_draw(text="Rectangle", value=3, row=3, column=0)
        root.rdb_draw(text="Triangle", value=4, row=4, column=0)
        root.rdb_draw(text="Trapezium", value=5, row=5, column=0)
        root.rdb_draw(text="Rhombus", value=6, row=6, column=0)
        root.rdb_draw(text="Sphere", value=7, row=1, column=1)
        root.rdb_draw(text="Cube", value=8, row=2, column=1)
        root.rdb_draw(text="Parallelepiped", value=9, row=3, column=1)
        root.rdb_draw(text="Pyramid", value=10, row=4, column=1)
        root.rdb_draw(text="Cylinder", value=11, row=5, column=1)
        root.rdb_draw(text="Cone", value=12, row=6, column=1)
        root.btn_draw(text="ShowMe", row=7, column=0,
                      command=lambda: click_show_btn(root.parameter_field()))
        root.btn_draw(text="CalcMe", row=7, column=1,
                      command=lambda: click_calc_btn(root.parameter_field()))
        root.mainloop()


if __name__ == "__main__":
    main()
