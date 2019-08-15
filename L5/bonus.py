# Tic-Tac-Toe

def printcell(cells):
    print("-" * 26)
    for i in range(0, 6):
        for j in range(0, 6):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 26)


def check_col(cells):
    for i in range(0, 5):
        if int(cells[0][i]) + int(cells[1][i]) + int(cells[2][i]) + int(cells[3][i]) + int(cells[4][i]) + int(cells[5][i]) == 21:
            if int(cells[0][i]) * int(cells[1][i]) * int(cells[2][i]) * int(cells[3][i]) * int(cells[4][i]) * int(cells[5][i]) == 720:
                return True
    return False

def check_row(cells):
    for i in range(0, 5):
        if int(cells[i][0]) + int(cells[i][1]) + int(cells[i][2]) + int(cells[i][3]) + int(cells[i][4]) + int(cells[i][5]) == 21:
            if int(cells[i][0]) * int(cells[i][1]) * int(cells[i][2]) * int(cells[i][3]) * int(cells[i][4]) * int(cells[i][5]) == 720:
                return True
    return False
def check_box(cells):
    for i in range(1,3):
        for j in range(1,2):
            x = i*2 - 2
            y = i*3 - 3
            if int(cells[x][y]) + int(cells[x+1][y]) + int(cells[x][y+1]) + int(cells[x][y+2]) + int(cells[x+1][y+1]) + int(cells[x][y+2]) == 21:
                if int(cells[x][y]) * int(cells[x+1][y]) * int(cells[x][y+1]) * int(cells[x][y+2]) * int(cells[x+1][y+1]) * int(cells[x][y+2]) == 720:
                    return True
    return False
def check(cells):
    if check_col(cells) == check_row(cells) == check_box(cells) == True:
        return True
    return False

cells = [[' ',' ','3',' ','1',' '],['5','6',' ','3','2',' '],[' ','5','4','2',' ','3'],['2',' ','6','4','5',' '],[' ','1','2',' ','4','5'],[' ','4',' ','1',' ',' ']]
answer = [[4,2,3,5,1,6],[5,6,1,3,2,4],[1,5,4,2,6,3],[2,3,6,4,5,1],[3,1,2,6,4,5],[6,4,5,1,3,2]]


printcell(cells)


while True:
    col = int(input("Please enter column\n")) -1
    row = int(input("Please enter row\n")) -1
    cells[row][col] = 'X'
    printcell(cells)
    num = int(input("Please enter number\n"))
    cells[row][col] = num
    printcell(cells)
    if cells == answer:
        print("You win!")
        break
    

    
        
