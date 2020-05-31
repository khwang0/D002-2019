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

def full_board(x):
    a = 0
    b = 0
    for a in range(0, 3):
        for b in range(0, 3):
            if cells[a][b] != ' ':
                b = b + 1
            else:
                return False
        a = a + 1
    return True

print("Welcome to tictactoe.\nPlayer 1 plays as 'X'.\nPlayer 2 plays as 'O'")

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
printcell(cells)
while True:
    if player == 1:
        print("Player 1's turn")
    else:
        print("Player 2's turn")
    col = int(input("Please enter column\n"))
    row = int(input("Please enter row\n"))
    if cells[row][col] != ' ':
         print("It is taken already\n")
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
            print("Congratulations, Player 2 wins!")
            break
        else:
            print("Congratulations, Player 1 wins!")
            break
    if full_board(cells) == True and win_status == False:
        print("Draw")
        break

        
