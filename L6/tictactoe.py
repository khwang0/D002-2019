# Tic-Tac-Toe
win_status = False
player = 1
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
        if cells[i][0] == cells[i][1] == cells[i][2] != ' ':
            return True
    return False

def check_diagonal(cells):
    for i in range(0, 3):
        if cells[0][0] == cells[1][1] == cells[2][2] != ' ':
            return True
        return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False

print("Welcome to tictactoe.\nPlayer 1 plays as 'X'.\nPlayer 2 plays as 'O'")

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
printcell(cells)
while True:
    if player == 1:
        print("Player 1's turn")
    else:
        print("Player 2's turn")
    col = int(input("Please enter column"))
    row = int(input("Please enter row"))
    if cells[row][col] != ' ':
         print("It is taken already")
         continue
    if player == 1:
        cells[row][col] = "X"
        player = 2
    else:
        cells[row][col] = "O"
        player = 1 
    printcell(cells)
    if check(cells) == True:
        win_status = True
        if player == 1:
            print("Player 2 wins")
            break
        else:
            print("Player 1 wins")
            break

