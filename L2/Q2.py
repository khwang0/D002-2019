num = int(input("Please input an positive integer number:\n"))
y = 2
while y < num:
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

'''Please input an positive integer number:'''
'''10'''
'''3 is a prime'''
'''4 is even continue'''
'''5 is a prime'''
'''6 is even continue'''
'''7 is a prime'''
'''8 is even continue'''
'''9 has factor 3; break'''
'''10 is even continue'''
