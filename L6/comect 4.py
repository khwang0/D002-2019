# Connect 4
cells = [[' ',' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ']]
win_status = False
player = 1
def printcell(cells):
    print("-" * 33)
    for i in range(0, 8):
        for j in range(0, 8):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 33)

def check_col(cells):
    for i in range(0, 8):
        if cells[0][i] == cells[1][i] == cells[2][i] == cells[3][i] != ' ':
            return True
    return False


def check_row(cells):
    for i in range(0, 8):
        if cells[i][0] == cells[i][1] == cells[i][2] == cells[i][3]!= ' ':
            return True
        return False
    

def check_diagonal(cells):
    for i in range(0, 8):
        if cells[i][i] == cells[i+1][i+1] == cells[i+2][i+2] == cells[i+3][i+3] != ' ':
            return True
        return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False

print("*incomplete*\n---------------Welcome to Connect 4---------------\n\t       Player 1 plays as 'X'\n\t       Player 2 plays as 'O'")

printcell(cells)
lowest_row = [7,7,7,7,7,7,7,7]
while True:
    if player == 1:
        print("Player 1's turn")
    else:
        print("Player 2's turn")
    col = int(input("Please enter column:\n"))    
    if player == 1:
        if lowest_row[col] < 0:
            print("This row is full, try another.")
            continue
        cells[lowest_row[col]][col] = "X"
        lowest_row[col] = lowest_row[col] - 1
        player = 2
    else:
        
        if lowest_row[col] < 0:
            print("This row is full, try another.")
            continue
        cells[lowest_row[col]][col] = "O"
        lowest_row[col] = lowest_row[col] - 1
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
