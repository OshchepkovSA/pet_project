#  ## Алгоритм Литтла "Метод ветвей и границ" для решения задачи коммивояжера
# ### Использованная литература:
# 1. https://uchimatchast.ru/teoriya/algoritm-littla-primer-1/
# 2. http://galyautdinov.ru/post/zadacha-kommivoyazhera
# 3. http://www.math.nsc.ru/LBRT/k4/or/or_part4.pdf
# 4. https://math.semestr.ru/kom/index.php
# 
import numpy as np
from typing import Tuple


def distance_matrix(dict_coord: dict, inf: float = float('inf')) -> np.array:
    """
    Функция делает из координатной сетки dict_coord матрицу расстояний matrix,
    добавляя числовые индексы слева и сверху по строкам и столбцам соответственно.
    
    dict_coord: словарь с координатами узлов
    inf: обозначает поля движения города в самого себя, а также поле пересечения индексов matrix[0][0]
    return: matrix - матрица расстояний
    """
    matrix = []
    for i in dict_coord.values():
        for j in dict_coord.values():
            if i != j:
                matrix.append(((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5)
            else:
                matrix.append(inf)
    matrix = np.array(matrix).reshape(len(dict_coord), len(dict_coord))
    index_from_city = np.array(list((dict_coord.keys()))).reshape(len(dict_coord), 1)
    matrix = np.append(index_from_city, matrix, axis=1)
    index_to_city = np.concatenate((np.array([inf]), np.array(list((dict_coord.keys())))), axis=0)
    matrix = np.append([index_to_city], matrix, axis=0)
    return matrix


def reduce_matrix(reduce_mtx: np.array, lower_bound: int) -> Tuple[np.array, int]:
    """
    Функция делает редукцию матрицы reduce_m и вычисляет нижнюю границу H
    
    reduce_m: матрица которую редуцируем
    H: нижняя граница до редуцирования
    return: reduce_m - рецуцированная матрица
            H - нижняя граница после редуцирования
    """
    min_for_rows = reduce_mtx[1:, 1:].min(axis=1)  # Rows
    for col in reduce_mtx.T[1:]:
        col[1:] -= min_for_rows

    min_for_columns = reduce_mtx[1:, 1:].min(axis=0)  # Columns
    for row in reduce_mtx[1:]:
        row[1:] -= min_for_columns
    lower_bound += sum(min_for_rows) + sum(min_for_columns)
    return reduce_mtx, lower_bound


def zero_coordinates(reduce_m: np.array) -> np.array:
    """
    Функция поиска нолей и их индексов в reduce_m
    
    reduce_m: редуцированная матрица
    return: coord_zeros - список кортежей с координатами нолей
    """
    coord_zeros = []
    for cnt_i, row in enumerate(reduce_m):
        for cnt_j, col in enumerate(row):
            if col == 0:
                coord_zeros.append((reduce_m[cnt_i][0], reduce_m[0][cnt_j]))
    return coord_zeros


def convert_index(reduce_m: np.array, coord: tuple) -> Tuple[int, int]:
    """
    Вспомогательная функция конвертирует "мнимый" индекс матрицы в "настоящий"
    
    reduce_m: матрица для конвертации индексов
    coord: координаты с первоначальной матрицы
    return: row, col - координаты матрицы в номерации Python
    """
    col = list(reduce_m[0]).index(coord[1])
    row = list(reduce_m[:, 0]).index(coord[0])
    return row, col


def search_branch(zero_coordinates: np.array, reduce_mtx: np.array) -> np.array:
    """
    Функция поиска веток для отслеживания

    zero_coordinates:список кортежей с координатами нолей в редуцированной матрице
    reduce_m: редуцированная матрица
    list_branch: пустой список, переменная на вырост если добавлять функционал ходить сразу по разным веткам
    return: list_branch - список координат (согласно первоначальной матрице) нулевых клеток с максимальной оценкой
    """
    sum_zero_cells = dict()
    list_branch = []
    for cnt, el in enumerate(zero_coordinates):  # Вычисление оценок нулевых клеток
        row, col = convert_index(reduce_mtx, el)
        reduce_mtx[row][col] = float('inf')
        sum_zero_cells[el] = reduce_mtx[row][1:].min() + reduce_mtx[:, col][1:].min()
        reduce_mtx[row][col] = 0
    for k, v in sum_zero_cells.items():
        if v == max(sum_zero_cells.values()):
            list_branch.append(k)
    return list_branch


def matrix_truncation(matrix: np.array, branch: np.array) -> np.array:
    """
    Функция отрезания строк и столбцов матрицы
    
    matrix: матрица которая усекается
    branch: координаты по которым усекается
    return: matrix - усеченная матрица
    """
    matrix = np.delete(matrix, list(matrix[0]).index(branch[1]), axis=1)  # Delete row
    matrix = np.delete(matrix, list(matrix[:, 0]).index(branch[0]), axis=0)  # Delete col
    return matrix


def remove_looping(matrix: np.array) -> np.array:
    """
    Функция ищет строку и столбец не содержащие inf и ставит на их пересечение inf
    
    matrix: матрица в которой убираются возможные циклы
    return: matrix - обновленная матрица
    """
    row = list(matrix.max(axis=1))  # Максимумы по строкам
    row = row.index(min(row))
    col = list(matrix.max(axis=0))  # Максимумы по столбцам
    col = col.index(min(col))
    matrix[row][col] = float('inf')
    return matrix


def sorted_ready_path(ready_path: np.array, start: int) -> np.array:
    """
    Функция сортировки маршрута
    
    ready_path: список кортежей всех переходов коммивояжера
    start: пункт из которого стартуем
    return sorted_ready_p - отсортированный (правильный) список переходов коммивояжера
    """
    sorted_path = []
    for begin, end in ready_path:
        if begin == start:  # Start point
            sorted_path.append((begin, end))
            ready_path.remove((begin, end))
            break
    while True:
        if len(ready_path) == 0:
            break
        for begin, end in ready_path:
            if sorted_path[-1][1] == begin:
                sorted_path.append((begin, end))
                ready_path.remove((begin, end))
                break
    return sorted_path


def drow_path(sorted_ready_path: np.array, data: dict) -> str:
    """
    Функция отрисовки вывода
    
    sorted_ready_path: отсортированный (правильный) список переходов коммивояжера
    data: словарь с координатами
    return: s - строка вывода
    """
    matrix_len = distance_matrix(dict_coord=data)
    s = str(data[sorted_ready_path[0][0]]) + ' -> '
    lenght = 0
    for begin, end in sorted_ready_path:
        lenght += matrix_len[int(begin), int(end)]
        s += str(data[end]) + str([lenght]) + ' -> '
    s = s[:-4] + ' = ' + str([lenght])
    return s


def main(data: dict, start: int):
    lower_bound = 0  # Lower bound start
    matrix = distance_matrix(dict_coord=data, inf=float('inf'))
    ready_path = []
    while True:
        reduce_mtx, lower_bound = reduce_matrix(reduce_mtx=matrix, lower_bound=lower_bound)
        zero_coord = zero_coordinates(reduce_mtx)
        list_branch = search_branch(zero_coordinates=zero_coord,
                                    reduce_mtx=reduce_mtx,
                                    )  # Список с координатами "максимальных нулей"
        ready_path.append(list_branch[0])
        if len(list_branch) > 1:
            pass  # TODO Добавить обход по по другим веткам
        matrix = matrix_truncation(matrix=matrix, branch=list_branch[0])  # Срезание матрицы по индексам
        matrix = remove_looping(matrix=matrix)  # Убирание возможного зацикливания
        if matrix.shape[0] == 3:
            break
    ready_path.append((matrix[1][0], matrix[0][2]))
    ready_path.append((matrix[2][0], matrix[0][1]))
    sorted_ready_p = sorted_ready_path(ready_path, start=start)
    return print(drow_path(sorted_ready_path=sorted_ready_p, data=data))


if __name__ == "__main__":
    data = {'Почтовое отделение': (0, 2),
            'Ул. Грибоедова, 104/25': (2, 5),
            'Ул. Бейкер стрит, 221б': (5, 2),
            'Ул. Большая Садовая, 302-бис': (6, 6),
            'Вечнозелёная Аллея, 742': (8, 3),
            }
    # TODO сделать связь текстового и численного ключа
    data = {1: (0, 2),
            2: (2, 5),
            3: (5, 2),
            4: (6, 6),
            5: (8, 3),
            }
    start = 1  # Point start data[start]
    main(data, start)
