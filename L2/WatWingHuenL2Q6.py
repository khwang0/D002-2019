import random
n = random.randint(1,100)

print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')

n = random.randint(1,100)
print ("shhh, Dave hides %s bananas" % n)

found = False
count = 0

while count<3:
    count=count+1
    guess=input("please enter your guess")
    if guess==n:
        break
    if guess<n:
        print("Too small")
    if guess>n:
        print("too big")
if found == True:
        print('You got the correct guess in %d trials' % count)
        print('Dave\'s banana are now all yours!')
else:
        print("You failed to find the number of bananas Dave hid! Try again next")
