def printboard(a):
    print(' 1 2 3 4 5 6 7')
    print()
    print('+-+-+-+-+-+-+-+')
    for i in range(7):
        for j in range(7):
            print('|' + a[j][6-i], end='')
        print('|')
        print('+-+-+-+-+-+-+-+')

def checkcol(a):
    for i in range(7):
        for j in range(4):
            if (a[i][j] == a[i][j+1] == a[i][j+2] == a[i][j+3] != ' '):
                return True
    return False

def checkrow(a):
    for i in range(7):
        for j in range(4):
            if (a[j][i] == a[j+1][i] == a[j+2][i] == a[j+3][i] != ' '):
                return True
    return False

def checkdiag(a):
    for i in range(4):
        for j in range(4):
            if (a[i][j] == a[i+1][j+1] == a[i+2][j+2] == a[i+3][j+3] != ' '):
                return True
    for i in range(4):
        for j in range(3, 7):
            if (a[i][j] == a[i+1][j-1] == a[i+2][j-2] == a[i+3][j-3] != ' '):
                return True
    return False

def check(a):
    return checkcol(a) or checkrow(a) or checkdiag(a)

a = []
for i in range(7):
    a += [[]]
    for j in range(7):
        a[i] += [' ']
sign = ['', 'X', 'O']
player = 2
while not check(a):
    printboard(a)
    player = 3 - player
    print()
    print('Player %d\'s turn.' % player)
    x = 0
    while (x < 1 or x > 7):
        x = int(input('Enter the column you want to put your piece in : '))
        if (x < 1 or x > 7):
            print('Input out of range.')
        if (a[x-1][6] != ' '):
            print('That column is full.')
            continue
    x -= 1
    b = 0
    p = True
    while p:
        if a[x][b] == ' ':
            a[x][b] = sign[player]
            p = False
        b += 1
print('Player %d wins!' % player)
        
