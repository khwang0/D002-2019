def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)


def check_col(cells):
    for i in range(0, 3):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
    return False

def check_row(cells):
    for i in range(0, 3):
        if cells[i][0] == cells[i][1] == cells[i][2] != ' ' :
            return True
    return False

def check_diagonal(cells):
    if cells[0][0] == cells[1][1] == cells[2][2] != ' ' or cells[0][2] == cells[1][1] == cells[2][0] != ' ':
        return True
    return False


def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
turn = 0
printcell(cells)
while check(cells) == False:
    col = int(input("Please enter column"))
    row = int(input("Please enter row"))
    if cells[row][col] == ' ' and turn == 0:
        cells[row][col] = "X"
        printcell(cells)
        turn= turn+1
    elif cells[row][col] == ' ' and turn == 1:
        cells[row][col] = "O"
        printcell(cells)
        turn= turn-1
    else:
        print("It is taken already")
if turn == 1:
    print("Player 1 wins")
else:
    print("Player 2 wins")

# For the check turn == 1 as python goes back to while loop before deducting 1
