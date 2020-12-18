def print_cells(cells_):
    print(f'---------')
    print(f'| {cells_[0]} {cells_[1]} {cells_[2]} |')
    print(f'| {cells_[3]} {cells_[4]} {cells_[5]} |')
    print(f'| {cells_[6]} {cells_[7]} {cells_[8]} |')
    print(f'---------')


def play_game(cell_string):
    cell_string = cell_string.lower()
    x_count = cell_string.count('x')
    o_count = cell_string.count('o')
    xo_dif = x_count - o_count if x_count > o_count else o_count - x_count
    cell_row_metrics = [[x for count, x in enumerate(cell_string) if count < 3],
                        [x for count, x in enumerate(cell_string) if 6 > count > 2],
                        [x for count, x in enumerate(cell_string) if 9 > count > 5]]

    xo_col_metrics = [[x for count, x in enumerate(cell_string) if count in [0, 3, 6]],
                      [x for count, x in enumerate(cell_string) if count in [1, 4, 7]],
                      [x for count, x in enumerate(cell_string) if count in [2, 5, 8]]]

    xo_d_metrics = [[x for count, x in enumerate(cell_string) if count in [0, 4, 8]],
                    [x for count, x in enumerate(cell_string) if count in [6, 4, 2]]]
    x_win = False
    o_win = False

    for row in cell_row_metrics:
        if row.count('x') == 3:
            x_win = True
        if row.count('o') == 3:
            o_win = True

    for col in xo_col_metrics:
        if col.count('x') == 3:
            x_win = True
        if col.count('o') == 3:
            o_win = True

    for d in xo_d_metrics:
        if d.count('x') == 3:
            x_win = True
        if d.count('o') == 3:
            o_win = True

    if xo_dif > 1 or (x_win and o_win):
        print("Impossible")
        return False
    elif x_win:
        print("X wins")
        return False
    elif o_win:
        print("O wins")
        return False
    elif x_count + o_count == 9 and not x_win and not o_win:
        print("Draw")
        return False
    elif x_count + o_count != 9:
        return True


xo_string = ''.join([' ' for x in range(1, 10)])
xo_string_list = list(xo_string)
c_status = False
xo_row_metrics = [[x for count, x in enumerate(xo_string) if count < 3],
                  [x for count, x in enumerate(xo_string) if 6 > count > 2],
                  [x for count, x in enumerate(xo_string) if 9 > count > 5]]
print_cells(xo_string)

game_running = True
x_turn = True
while game_running:
    coordinates = input('Enter the coordinates:').split()
    row_c = ''
    col_c = ''

    if len(coordinates) == 2:
        row_c = coordinates[0]
        col_c = coordinates[1]

    if row_c.isnumeric() and col_c.isnumeric():

        row_c = int(row_c) - 1
        col_c = int(col_c) - 1

        if row_c not in range(0, 3) or col_c not in range(0, 3):
            print("Coordinates should be from 1 to 3!")
        elif xo_row_metrics[row_c][col_c] != ' ':
            print("This cell is occupied! Choose another one!")
        else:
            if x_turn:
                xo_row_metrics[row_c][col_c] = 'X'
                x_turn = False
            else:
                xo_row_metrics[row_c][col_c] = 'O'
                x_turn = True
    else:
        print("You should enter numbers!")

    xo_string = [x for single in xo_row_metrics for x in single]
    xo_string = ''.join(xo_string).replace('_', ' ')
    print_cells(xo_string)
    game_running = play_game(xo_string)
