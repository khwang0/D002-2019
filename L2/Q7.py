# -*- coding: UTF-8 -*-
import random
p1g=0
p2g=0
found1 = 0
found2 = 0
##########################################################################################
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
ans = random.randint(1,100)
print (ans)
########################################################################################
while True:
    p1g=int(input('''P1
your guess? '''))      
    if p1g == ans:
        found1=1
    if found1 == True:
        print('You got the correct guess!')
        print('Dave\'s banana are now all yours!')
        break
    else:
        print("You failed to find the number of bananas Dave hid! Try again next")
##########################################################################################
    p2g=int(input('''P2
your guess? '''))
    if p2g==ans :
            found2=1
    if found2 == True:
        print('You got the correct guess!')
        print('Dave\'s banana are now all yours!')
        break
    else:
        print("You failed to find the number of bananas Dave hid! Try again next")
