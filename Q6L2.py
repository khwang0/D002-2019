#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
import random
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
#Step 3: Choose a random number between 1-100
n = random.randint(1,100)
print ("shhh, Dave hides %s bananas" % n)
# define a flag for found/not found and counter on how many trials
found = False
count = 1
m=0
#Step 4: Give three chances to the players 
while count<4 and m!=n:
    m=int(input("what is your guess"))
    if m>n:
        print("too high")
        count=count+1
        continue
    elif m<n:
          print("too low")
          count = count + 1
          continue
    else:
        found=True
    
if found == True:
        print('You got the correct guess in %d trials' % count)
        print('Dave\'s banana are now all yours!')
else:
        print("You failed to find the number of bananas Dave hid! Try again next")
