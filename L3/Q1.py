# D002 Lesson 3
# Q1:  Warm up exercise

# a) Go Dutch
from math import *

people = int(input("How many people are sharing the bill?\n"))
bill = float(input("How much is the bill?\n"))
print("Kevin paid the bill first. But Kevin only has 100 dollar notes")
print("So Kevin is going to pay", ceil(bill/100)*100)
print("The cafe is giving $", (ceil(bill/100)*100-bill), "to Kevin.")
print("Each one should give $", (round(ceil(bill/100)*100/people, 2)), "to Kevin.") 

number = 1
while number <= 100:
    if number % 10 == 7 or number % 7 == 0:   # replace with your code
        print('X', end=' ')
    else:
        print(number, end=' ')    
    number = number + 1
print("\nGame Over.")

from random import randint

#code for rolling a dice
count = 0
while number!=6 :
    number = randint(1,6)
    print("I got a %d" % number)
    count = count + 1
print("Oh, it takes me %d times to get a 6!!!" % count)
