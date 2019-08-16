from math import *

total_combinations = factorial(20)/factorial(5)/factorial(20-5)

invalid_combinations = 0
a=1
b=2
c=3
d=4
e=5
while a <= 16:
    while b <=17:
        while c <=18:
            while d <=19:
                while e <= 20:
                    if b - a == 1 or c - b == 1 or d - c == 1 or e - d == 1:
                        invalid_combinations = invalid_combinations + 1
                    e = e + 1
                d = d + 1
                e = d + 1
            c = c + 1
            d = c + 1
        b = b + 1
        c = b + 1
    a = a + 1
    b = a + 1

valid_combinations = total_combinations - invalid_combinations
print(valid_combinations)
