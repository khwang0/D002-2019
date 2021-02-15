from random import randint

print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')

n =randint(1,100)

print ("shhh, Dave hides %s bananas" % n)

found = False
count = 0

print("You will have three chances.")
while count < 3:
    count = count + 1
    guess = int(input("Guess a number between 1 and 100.\n"))
    if guess < n:
        print("Your guess is too low, guess again")
       
        found = False
    elif guess > n:
        print("Your guess is too high, guess again")
       
        found = False
    else:
        found = True

   
if found == True and count < 4:
    print("You guess the correct numberin %d counts"% count)
    print("Now all the bananas are yours!")
else:
    print("You failed!Try again next time")
