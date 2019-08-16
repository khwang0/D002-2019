def printcell(cells):
    print("-" * 30)
    for i in range(0, 6):
        for j in range(0, 7):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 30)

def check_col(cells):
    for i in range(0, 6):
     #  for j in range(0, 5):
            if cells[0][i] == cells[1][i] == cells[2][i] == cells[3][i]!= ' ' or cells[1][i] == cells[2][i] == cells[3][i] == cells[4][i]!= ' ' or cells[2][i] == cells[3][i] == cells[4][i] == cells[5][i] != ' ':
                return True
    return False

def check_row(cells):
    for i in range(0, 6):
        #for j in range(0, 5):
            if cells[i][0] == cells[i][1] == cells[i][2] == cells[i][3] != ' 'or cells[i][1] == cells[i][2] == cells[i][3] == cells[i][4] != ' 'or cells[i][2] == cells[i][3] == cells[i][4] == cells[i][5] != ' '\
               or cells[i][3] == cells[i][4] == cells[i][5] == cells[i][6] != ' ':
                return True
    return False
def check_diagonal(cells):
    for i in range(0, 3):
        for j in range(0, 2):
            if cells[i][j] == cells[i+1][j+1] == cells[i+2][j+2] == cells[i+3][j+3] != ' 'or cells[i+3][j] == cells[i+2][j+1] == cells[i+1][j+2] == cells[i][j+3] != ' ':
                return True
    return False
def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False


cells = [[' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ']]
row = 5
row_0 = 5
row_1 = 5
row_2 = 5
row_3 = 5
row_4 = 5
row_5 = 5

while True:
    col = int(input("Please enter column"))
    if col == 1:
        row = row_1 
    elif col == 2:
        row = row_2
    elif col == 3:
        row = row_3
    elif col == 4:
        row = row_4 
    elif col == 5:
        row = row_5 
    if cells[row][col] == ' ':
        cells[row][col]= 'X'
        printcell(cells)
        check(cells)
        row = row - 1
        if check(cells) == True:
            print("Game over.Player X wins.")
            break
    else:
        if col == 1:
            row_1 = row_1 - 1
        elif col == 2:
            row_2 = row_2 -1
        elif col == 3:
            row_3 = row_3 - 1
        elif col == 4:
            row_4 = row_4 - 1
        elif col == 5:
            row_5 = row_5 - 1
            if cells[row][col] == ' ':
                cells[row][col] = 'X'
                printcell(cells)
                check(cells)
                if check(cells) == True:
                    print("Game over.Player X wins.")
                    break
    
    col = int(input("Please enter column"))
    if col == 1:
        row = row_1 
    elif col == 2:
        row = row_2
    elif col == 3:
        row = row_3
    elif col == 4:
        row = row_4 
    elif col == 5:
        row = row_5 
    if cells[row][col] == ' ':
        cells[row][col]= 'O'
        printcell(cells)
        check(cells)
        row = row - 1
        if check(cells) == True:
            print("Game over.Player O wins.")
            break
    else:
        if col == 1:
            row_1 = row_1 - 1
        elif col == 2:
            row_2 = row_2 - 1
        elif col == 3:
            row_3 = row_3 - 1
        elif col == 4:
            row_4 = row_4 - 1
        elif col == 5:
            row_5 = row_5 - 1
            if cells[row][col] == ' ':
                cells[row][col] = 'O'
                printcell(cells)
                check(cells)
                if check(cells) == True:
                    print("Game over.Player O wins.")
                    break

                     
