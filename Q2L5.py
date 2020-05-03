# Tic-Tac-Toe

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
    for j in range(0, 3):
        if cells[j][0] == cells[j][1] == cells[j][2] != ' ':
            return True
        
    return False
def check_diagonal(cells):
    if cells[0][0] == cells[1][1] == cells[2][2] != ' ':
        return True
    elif cells[2][0] == cells[1][1] == cells[0][2] != ' ':
        return True
    else:
        return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    else:
        return False
    


    

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

printcell(cells)
while not check(cells):
    player=int(input("enter player num"))
    col = int(input("Please enter column"))
    row = int(input("Please enter row"))
    if player > 3 or col > 3 or row > 3:
        print ("invalid input")
        continue
    while player == 1:
        if cells[row][col] == ' ':
            cells[row][col]="x"
            
        else:
            print("It is taken already")
        break
    while player == 2:
        if cells[row][col] == ' ':
            cells[row][col]="o"
            
        else:
            print("It is taken already")
        break
    
    printcell(cells)
    
if check(cells) and player ==  1:
    print ("Player 1 won")
else:
    print ("Player 2 won")



