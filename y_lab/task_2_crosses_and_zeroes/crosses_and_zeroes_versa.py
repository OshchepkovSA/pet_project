# ### Крестики нолики наоборот

# 1. Игрок человек начинает ходить первым
# 1. У игрока человека всегда крестики
# 1. Игровое поле можно задавать любого разумного размера

# TODO:
# 1. Выход через q
# 2. Очистку экрана консоли
#
import numpy as np
import random

ROWS, COLS = 10, 10  # Size can be changed
LENGTH_LOSE = 5  # Length for lose


def create_game_field(rows=ROWS, cols=COLS):
    """Create new game field"""
    field = np.zeros([rows, cols])
    return field


def drow_game_field(field, rows=ROWS, cols=COLS):
    """Drow and print game field"""
    print('New round!')
    drow = [[None] * cols] * rows
    print(f"  |", end='')  # Offset 2 characters
    for cnt_y, y in enumerate(field[0]):
        print(f"{cnt_y + 1:2.0f}|", end='')
    print('')
    for cnt_x, x in enumerate(field):
        print(f"{cnt_x + 1:2.0f}|", end='')  # Offset 2 characters
        for cnt_y, y in enumerate(x):
            if y == 0:
                drow[cnt_x][cnt_y] = '  |'
                print(drow[cnt_x][cnt_y], end='')
            elif y == 1:
                drow[cnt_x][cnt_y] = ' X|'
                print(drow[cnt_x][cnt_y], end='')
            elif y == 2:
                drow[cnt_x][cnt_y] = ' O|'
                print(drow[cnt_x][cnt_y], end='')
        print('')


def is_cells_void(field, move):
    """Checking the correctness of the input by the player of the coordinates of the field"""
    if field[move[0] - 1][move[1] - 1] == 0:
        return True
    return False


def change_game_field(field, move, player):
    """Making changes to the playing field after a move has been made"""
    if player:
        field[move[0] - 1][move[1] - 1] = 1  # 1 - move human, drow cross
    else:
        field[move[0] - 1][move[1] - 1] = 2  # 2 - move AI, drow zero
    return field


def search_void_cells(field):
    """Returns the indices of null values"""
    void_cells = []
    for cnt_x, x in enumerate(field):
        for cnt_y, y in enumerate(x):
            if field[cnt_x][cnt_y] == 0:
                void_cells.append((cnt_x + 1, cnt_y + 1))
    return void_cells


def ai_player(field, player):
    """AI player move"""
    void_cells = search_void_cells(field)
    move = random.choice(void_cells)
    field = change_game_field(field, move, player)
    return field, move


def full_length(field, move, rows=ROWS, cols=COLS, length_lose=LENGTH_LOSE):
    """Function search line, which will complete the game"""
    cnt_y_min = 0 if (move[0] - 1) - (length_lose - 1) <= 0 else (move[0] - 1) - (length_lose - 1)
    cnt_y_max = rows if (move[0] - 1) + length_lose > rows else (move[0] - 1) + length_lose
    if game_end_columns(field, move, cnt_y_min, cnt_y_max, length_lose=length_lose):
        return True
    cnt_x_min = 0 if (move[1] - 1) - (length_lose - 1) <= 0 else (move[1] - 1) - (length_lose - 1)
    cnt_x_max = cols if (move[1] - 1) + length_lose > cols else (move[1] - 1) + length_lose
    if game_end_rows(field, move, cnt_x_min, cnt_x_max, length_lose=length_lose):
        return True
    diag_x_min = (move[1])
    diag_y_min = (move[0])
    for el in range(length_lose):
        diag_x_min -= 1
        diag_y_min -= 1
        if diag_y_min == 0 or diag_x_min == 0:
            break
    diag_x_max = cnt_x_max
    diag_y_max = cnt_y_max
    if game_end_diagonals(field, diag_x_min, diag_y_min, diag_x_max, diag_y_max, length_lose=length_lose):
        return True
    if game_end_anti_diagonals(field, move, length_lose=length_lose):
        return True
    return False


def is_finish_game(field, move, player, rows=ROWS, cols=COLS, length_lose=LENGTH_LOSE):
    """Determines whether the end of the game has come"""
    if field.min() != 0:  # Not free cells, draw in game
        player = 2  # 2 it`s index - no free cells
        return True, player
    if full_length(field, move, rows=rows, cols=cols, length_lose=length_lose):  # Find line, game over
        return True, player
    return False, player


def game_end_columns(field, move, cnt_y_min, cnt_y_max, length_lose=LENGTH_LOSE):
    """The function looks for length_lose crosses or zeros in a row in a column"""
    cnt_lose_hum = 0
    cnt_lose_ai = 0
    for y in range(cnt_y_min, cnt_y_max):
        if field[y][move[1] - 1] == 1:  # Search lose player
            cnt_lose_hum += 1
            if cnt_lose_hum == length_lose:
                return True
        elif (field[y][move[1] - 1] == 0) or (field[y][move[1] - 1] == 2):
            cnt_lose_hum = 0
        if field[y][move[1] - 1] == 2:  # Search lose AI
            cnt_lose_ai += 1
            if cnt_lose_ai == length_lose:
                return True
        elif (field[y][move[1] - 1] == 0) or (field[y][move[1] - 1] == 1):
            cnt_lose_ai = 0
    return False


def game_end_rows(field, move, cnt_x_min, cnt_x_max, length_lose=LENGTH_LOSE):
    """ The function looks for length_lose crosses or zeros in a row in a string"""
    cnt_lose_hum = 0
    cnt_lose_ai = 0
    for x in range(cnt_x_min, cnt_x_max):
        if field[move[0] - 1][x] == 1:  # Lose player
            cnt_lose_hum += 1
            if cnt_lose_hum == length_lose:
                return True
        elif (field[move[0] - 1][x] == 0) or (field[move[0] - 1][x] == 2):
            cnt_lose_hum = 0

        if field[move[0] - 1][x] == 2:  # Lose AI
            cnt_lose_ai += 1
            if cnt_lose_ai == length_lose:
                return True
        elif (field[move[0] - 1][x] == 0) or (field[move[0] - 1][x] == 1):
            cnt_lose_ai = 0
    return False


def game_end_diagonals(field, diag_x_min, diag_y_min, diag_x_max, diag_y_max, length_lose=LENGTH_LOSE):
    """The function looks for length_lose crosses or zeros in a row on the main diagonal"""
    matrix = field[diag_y_min:diag_y_max, diag_x_min:diag_x_max]
    diag_elements = np.diagonal(np.array(matrix))
    cnt_lose_hum = 0
    cnt_lose_ai = 0
    for el in diag_elements:
        if el == 1:  # Lose player
            cnt_lose_hum += 1
            if cnt_lose_hum == length_lose:
                return True
        elif (el == 0) or (el == 2):
            cnt_lose_hum = 0

        if el == 2:  # Lose AI
            cnt_lose_ai += 1
            if cnt_lose_ai == length_lose:
                return True
        elif (el == 0) or (el == 1):
            cnt_lose_ai = 0
    return False


def game_end_anti_diagonals(field, move, length_lose=LENGTH_LOSE, rows=ROWS):
    """The function looks for length_lose crosses or zeros in a row on the secondary diagonal"""
    rotation_matrix = tuple(zip(*list(field)[::-1]))
    move = (move[1], move[0])
    diag_x_min = rows - move[1] + 1
    diag_y_min = move[0]
    for el in range(length_lose):
        diag_x_min -= 1
        diag_y_min -= 1
        if diag_y_min == 0 or diag_x_min == 0:
            break
    diag_x_max = rows - move[1] + 1 + length_lose
    diag_y_max = move[0] + length_lose
    if game_end_diagonals(np.array(rotation_matrix), diag_x_min, diag_y_min, diag_x_max, diag_y_max,
                          length_lose=length_lose):
        return True
    return False


def result_game(player):
    """The fuction print result game"""
    print('Game over')
    if player == 1:
        print("You win, try again!")
    elif player == 0:
        print("You lose, try again!")
    elif player == 2:
        print("Draw, try again!")
    else:
        print('╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ')


def is_int(string):
    """Checks if the input string is an integer or not"""
    try:
        int(string)
        return True
    except ValueError:
        return False


def input_coord(size_field, message):
    """Accepts the entered player data and checks their correctness"""
    coord = input(f"{message} {size_field}: ")
    if is_int(coord):
        if 0 < int(coord) & int(coord) <= size_field:
            return int(coord)
    print("Enter correct coordinates")
    return False


def main():
    field = create_game_field(rows=ROWS, cols=COLS)
    drow_game_field(field)
    player = 1  # 1 - human, 0 - AI
    while True:
        message = 'Enter the line number of the playing field from 1 to'
        x = input_coord(ROWS, message)
        if x == 0:
            continue
        message = 'Enter the number of the playing field column from 1 to'
        y = input_coord(COLS, message)
        if y == 0:
            continue
        move = (x, y)
        if is_cells_void(field, move):
            field = change_game_field(field, move, player=player)
            player = 0
        else:
            print("The cell is busy. Enter correct coordinates")
            continue
        drow_game_field(field)
        is_finish, player = is_finish_game(field, move, rows=ROWS, cols=COLS, length_lose=LENGTH_LOSE, player=player)
        if is_finish:
            break
        field, move = ai_player(field=field, player=player)
        player = 1
        drow_game_field(field)
        is_finish, player = is_finish_game(field, move, rows=ROWS, cols=COLS, length_lose=LENGTH_LOSE, player=player)
        if is_finish:
            break
    return result_game(player=player)


if __name__ == '__main__':
    main()
