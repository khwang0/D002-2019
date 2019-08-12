#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
import random
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
#Step 3: Choose a random number between 1-100
n = random.randint(1,100)

# define a flag for found/not found and counter on how many trials
found = False
count = 0
player = 2
#Step 4: Give three chances to the players 
while not found:
    player = 3 - player
    print('Player %d\'s turn.' % player)
    g = int(input('Guess the number : '))
    if g < n:
        print('Your guess is too small')
    elif g > n:
        print('Your guess is too big')
    else:
        found = True

#Step 5: Display a message
if found:
        print('Player %d got the correct guess.' % player)
        print('Dave\'s banana are now all yours!')
else:
        print("You failed to find the number of bananas Dave hid! Try again next")
