    
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

def check_row(cells):
    for i in range(0, 2):
        if cells[i][0] == cells[i][1] == cells[i][2] != ' ':
            return True
    return False

def check_diagonal(cells):
    if ((cells[0][0] == cells[1][1] == cells[2][2] != ' ') or (cells[0][2] == cells[1][1] == cells[2][0] != ' ')):
        return True
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
sign = [' ', 'X', 'O']
win = False
player = 1
count = 0
while (not win and count < 9):
    b = True
    print('Player %d\'s turn' % player)
    printcell(cells)
    while b:
        c = True
        while c:
            col = int(input("Please enter column : "))
            row = int(input("Please enter row : "))
            if not (col > 2 or row > 2 or col < 0 or row < 0):
                c = False
            if c:
                print('Input out of range')
        if cells[row][col] == ' ':
            b = False
        if b:
            print("It is taken already")
    cells[row][col] = sign[player]
    win = check(cells)
    player = 3 - player
    count += 1
if win:
    print('Player %d wins.' % player)
else:
    print('Draw.')

