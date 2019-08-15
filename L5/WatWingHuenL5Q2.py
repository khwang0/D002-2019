import random
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
        cells [row][col]='X'
        printcell(cells)
        check_col(cells)
    
    else:
        print("It is taken already")
    col = random.randrange(0,3)
    row = random.randrange(0,3)
    if cells[row][col] == ' ':
        cells [row][col]='o'
        printcell(cells)
        check_col(cells)
    
    else:
        col = random.randrange(0,3)
        row = random.randrange(0,3)
        cells [row][col]='o'
        printcell(cells)
        check_col(cells)

print("game over")
     
