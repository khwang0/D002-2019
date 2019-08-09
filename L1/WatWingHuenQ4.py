from math import *
a=int(input("what is the year"))
b=(a % 4)
c=(a % 400)
if b==0 or c==0:
    print("leap year")
else:
    print("not a leap year")
