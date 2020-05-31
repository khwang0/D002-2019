def ins(a, c, t):
    if ((a[0] < t[0] < c[0] or a[0] > t[0] > c[0]) and (a[1] < t[1] < c[1] or a[1] > t[1] > c[1])):
        return True
    else:
        return False
def overlap(a, c):
    b = [[], [], []]
    d = [[], [], []]
    b[1] = [c[1][0], a[1][1]]
    d[1] = [a[1][0], c[1][1]]
    b[2] = [c[2][0], a[2][1]]
    d[2] = [a[2][0], c[2][1]]
    for i in range (1, 3):
        if ins(a[3-i], c[3-i], a[i]):
            return True
        elif ins(a[3-i], c[3-i], b[i]):
            return True
        elif ins(a[3-i], c[3-i], c[i]):
            return True
        elif ins(a[3-i], c[3-i], d[i]):
            return True
    return False
p = input('Enter the coordinates of the top left corner of rectangle 1 : ')
q = input('Enter the coordinates of the bottom right corner of rectangle 1 : ')
r = input('Enter the coordinates of the top left corner of rectangle 2 : ')
s = input('Enter the coordinates of the bottom right corner of rectangle 2 : ')
a = [[], p, r]
c = [[], q, s]
if overlap(a, c):
    print('They overlap')
else:
    print('They don\'t overlap')
