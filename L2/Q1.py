from math import *
x = int(input("Enter a positive integer larger than 2 : "))
y = 2
prime = True
if(x <= 1):
    prime = False
else:
    while y <= sqrt(x):
        if(x % y == 0):
            prime = False
            break
        y += 1
if prime:
    print("%d is a prime number" % x)
else:
    print("%d is not a prime number" % x)
