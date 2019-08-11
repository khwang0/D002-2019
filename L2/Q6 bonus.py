#L2 Q6: Banana Guessing game


#Step 1: Import necessary modules
import random
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
round = 1
while True:
 
 if round%2 ==0:
     x = 1
     y = 2
 else:
     x = 2
     y = 1

#Step 3: Choose a random number between 1-100
 n = int(input("Player %d, pleaese enter your number\n"%x))
 print ("shhh, Player %d hides %s bananas" % (x,n))

# define a flag for found/not found and counter on how many trials
 found = False
 count = 0
#Step 4: Give three chances to the players 

 while (count < 3 and found == False):
    p = int(input("Player %d input your guess:\n"%y))
    count = count +1
    if p == n:
        found = True
    else:
        found = False
        print("Try again")
        
#Step 5: Display a message
 if found == True:
        print('You got the correct guess in %d trials' % count)
        print('Player %d\'s banana are now all yours!'%x)
        
 else:
        print("You failed to find the number of bananas Player %d hid! Try again next"%x)

 round = round +1
 
