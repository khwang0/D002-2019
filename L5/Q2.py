# Tic-Tac-Toe

def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)


def check_col(cells):
    for i in range(0, 2):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False


    

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

printcell(cells)
while True:
    col = int(input("Please enter column"))
    row = int(input("Please enter row"))
    if cells[row][col] == ' ':
        break
    print("It is taken already")


