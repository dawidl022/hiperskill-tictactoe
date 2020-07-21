game_over = False
moves = 0
def check_result(move=moves):
    global game_over
    o_wins = False
    x_wins = False
    for row in grid:
        if row[0] == "X" and row[1] == "X" and row[2] == "X":
            x_wins = True
        if row[0] == "O" and row[1] == "O" and row[2] == "O":
            o_wins = True
    for column in columns:
        if column[0] == "X" and column[1] == "X" and column[2] == "X":
            x_wins = True
        if column[0] == "O" and column[1] == "O" and column[2] == "O":
            o_wins = True
    for diagonal in diagonals:
        if diagonal[0] == "X" and diagonal[1] == "X" and diagonal[2] == "X":
            x_wins = True
        if diagonal[0] == "O" and diagonal[1] == "O" and diagonal[2] == "O":
            o_wins = True
    if x_wins is True:
        print("X wins")
        game_over = True
    elif o_wins is True:
        print("O wins")
        game_over = True
    elif move > 8:
        print("Draw")
        game_over = True

cell_info = "         "

grid = [[cell_info[0], cell_info[1], cell_info[2]],
        [cell_info[3], cell_info[4], cell_info[5]],
        [cell_info[6], cell_info[7], cell_info[8]]]

def update_grid():
    global columns, diagonals
    columns = [[row[0] for row in grid],
               [row[1] for row in grid],
               [row[2] for row in grid]]
    diagonals = [[grid[0][0], grid[1][1], grid[2][2]],
                 [grid[0][2], grid[1][1], grid[2][0]]]
    print_grid = []
    for row in grid:
        for element in row:
            print_grid.append(element)

    grid_print(print_grid)

def grid_print(cell=cell_info):
    print("---------")
    print("| {0} {1} {2} |".format(cell[6], cell[7], cell[8]))
    print("| {0} {1} {2} |".format(cell[3], cell[4], cell[5]))
    print("| {0} {1} {2} |".format(cell[0], cell[1], cell[2]))
    print("---------")

def x_move():
    global grid
    x, y = input("Enter the coordinates: > ").split()
    try:
        x = int(x)
        y = int(y)
    except:
        print("You should enter numbers!")
        x_move()
    if 0 < x < 4 and 0 < y < 4:
        if grid[y-1][x-1] == "X" or grid[y-1][x-1] == "O":
            print("This cell is occupied! Choose another one!")
            x_move()
        else:
            grid[y-1][x-1] = "X"
    else:
        print("Coordinates should be from 1 to 3!")
        x_move()

def o_move():
    global grid
    x, y = input("Enter the coordinates: > ").split()
    try:
        x = int(x)
        y = int(y)
    except:
        print("You should enter numbers!")
        o_move()
    if 0 < x < 4 and 0 < y < 4:
        if grid[y-1][x-1] == "X" or grid[y-1][x-1] == "X":
            print("This cell is occupied! Choose another one!")
            o_move()
        else:
            grid[y-1][x-1] = "O"
    else:
        print("Coordinates should be from 1 to 3!")
        o_move()

grid_print()

while not game_over:
    x_move()
    update_grid()
    check_result(moves)
    moves += 1
    if game_over:
        break
    o_move()
    update_grid()
    check_result(moves)
    moves += 1