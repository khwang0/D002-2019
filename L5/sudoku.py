import random
def board(a):
    for x in range(6):
        a += [[]]
        for y in range(1, 7):
            a[x] += [0]
    for x in range(6):
        a[0][x] = x
    for x in range(10):
        p = random.randint(0, 5)
        q = random.randint(0, 5)
        swap(a[0][p], a[0][q])
    

def swap(a, b):
    t = a
    a = b
    b = t

def sort(arr):
    for x in range(len(arr)-1):
        for y in range(x + 1, len(arr)):
            if arr[x] > arr[y]:
                swap(arr[x], arr[y])
                
def checkrow(a):
    for x in range(6):
        b = a[x]
        sort(b)
        for y in range(5):
            if b[y] == b[y+1]:
                return False
    return True

def checkcol(a):
    b = []
    for x in range(6):
        for y in range(6):
            b += [a[y][x]]
        sort(b)
        for y in range(5):
            if b[y] == b[y+1]:
                return False
    return True

def check2x3(a):
    for x in range(2):
        for y in range(3):
            b = []
            for p in range(3):
                for q in range(2):
                    b += a[2*y+q][3*x+p]
            sort(b)
            for r in range(5):
                if b[r] == b[r+1]:
                    return False
    return True

def check(a):
    return checkrow(a) and checkcol(a) and check2x3(a)

def printboard(a):
    print('#' + '=' * 5 + '#' + '=' * 5 + '#')
    for x in range(3):
        print('#'+a[3*x+1][0]+'|'+a[3*x+1][1]+'|'+a[3*x+1][2]+'#'+a[3*x+1][3]+'|'+a[3*x+1][4]+'|'+a[3*x+1][5]+'#')
        print('#'+'-'*5+'#'+'-'*5+'#')
        print('#'+a[3*x+2][0]+'|'+a[3*x+2][1]+'|'+a[3*x+2][2]+'#'+a[3*x+2][3]+'|'+a[3*x+2][4]+'|'+a[3*x+2][5]+'#')
        print('#'+'='*5+'#'+'='*5+'#')

a = []
board(a)
while not check(a):
    p = random.randint(0, 5)
    q = random.randint(0, 5)
    r = random.randint(0, 5)
    s = random.randint(0, 5)
    swap(a[p][r], a[q][s])
printboard(a)
