# D002 Lesson 3
# Q1:  Warm up exercise

# a) Go Dutch
from math import *

people = int(input("How many people are sharing the bill?\n"))
bill = float(input("How much is the bill?\n"))
print("Kevin paid the bill first. But Kevin only has 100 dollar notes")
print("So Kevin is going to paid $%d." % (ceil(bill/100)*100))  # replace with your code
print("The cafe is giving %f to Kevin." % ((ceil(bill/100)*100)-bill))  # replace with your code
print("Each one should give %f to Kevin." % (bill/people)) # replace with your code

# b) Clap at Seven 
# The purpose of the following program is to print the number from 1 to 100,
# in order. However, when the number is a multiple of 7 (e.g. 7/14/21) or when
# the last digit of the number is 7 (e.g. 17/27/37), it print a X instead

number = 1
while number <= 100:
    if number%7==0 or number%10==7:   # replace with your code
        print('X', end=' ')
    else:
        print(number, end=' ')    
    number = number + 1
print("\nGame Over.")

# c) How long it takes?
# In a Chinese board game the player can start its game only when he can
# get a 6 in rolling a dice. Please do an experiment to test your luck today
# and see how long it takes to get a dice

from random import randint
number = randint(1,6)
print("I got a %d" % number)
count = 1
while True : 
    print("I got a %d" % number)
    if number==6:
        break
    count = count + 1
    number = randint(1,6)
    
print("Oh, it takes me %d times to get a 6!!!" % count)


# d) How long it takes, in general?
# Repeat the experiment in part c for 100 times and see what is the average 
# value of the count would be. This is challenging, isn't it?
qwer=[]
asdfghjkl=0
while asdfghjkl<100 :
    number = randint(1,6)
    print("I got a %d" % number)
    count = 1
    while True : 
        print("I got a %d" % number)
        if number==6:
            break
        count = count + 1
        number = randint(1,6)
    
    print("Oh, it takes me %d times to get a 6!!!" % count)
    qwer.append(count)
    asdfghjkl+=1
qwe=0
for zxcv in qwer :
    qwe=qwe+zxcv
print(qwe/100)

