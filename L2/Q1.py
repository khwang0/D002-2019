from math import*
y = int(input("Please input a positive integer larger than 2\n."))
n = 2
check = 0
while n <= y/2:
    if y % n == 0:
        print("It isn't a prime number")
        check = check + 1
        break
    else:
        n= n + 1
        continue
if (check == 0):
    print("It is a prime number.")
