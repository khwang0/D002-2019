n = int(input("Please input an positive integer number:\n"))
y = 2
while y < n:
    y = y + 1
    if y % 2 == 0:
        print("%d is even continue" % y)
        continue
    x = int(y/2)
    while x > 1:
        if y % x == 0:
            print("%d has factor %d; break" % (y, x))
            break
        x = x - 1
    if x == 1:
        print("%d is a prime" % y)
