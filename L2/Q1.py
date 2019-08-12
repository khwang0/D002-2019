from math import *
n = int(input("Please input a positive integer larger than 2:\n"))

x=2
while x < sqrt(n):
    if x > sqrt(n):
        print("prime")

        break
        
    if n%x == 0:
        print("not prime")
        break
    else:
        x=x+1
    if x > sqrt(n):
        print("prime")

        break
if n==2 or n==3:
    print("prime")
if n==4:
    print("not prime")
    
