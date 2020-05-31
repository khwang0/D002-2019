a = []
for i in range(10):
    a += [0]
for i in range(10):
    a[i] = int(input('Enter a number : '))
a.sort()
b = []
for i in range(9):
    b += [0]
m = 9999999909999999997784578689
for i in range(9):
    b[i] = a[i+1] - a[i]
    if b[i] < m:
        c = i
        m = b[i]
print('%d and %d are the nearest' % (a[c], a[c+1]))
