from math import *
numbers = []
x = 1
while x <= 10:
    numbers = numbers + [input("Input integer:\n")]
    x = x+1
smallest_difference = abs(int(numbers[9]) - int(numbers[8]))
                                                                
for i in range(0,9):
    for j in range(0,9):
        if i != j:
            y = abs(int(numbers[i]) - int(numbers[j]))
            if y <= smallest_difference:
                smallest_difference = y
                a = int(numbers[i])
                b = int(numbers[j])
print(a, " and %d are the nearest"  % b)
        
