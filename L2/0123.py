from random import randint

print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')

n =randint(1,100)

# print ("shhh, Dave hides %s bananas" % n)

found = False
count = 0

print("You will have three chances.")

guess = int(input("Guess a number between 1 and 100.\n"))

if guess < n:
    print("Your guess is too low, guess again")
    count = count + 1
    found = False
    if guess < n:
        print("Your guess is too low, guess again")
        count = count + 1
        found = False
    elif guess > n:
        print("Your guess is too high, guess again")
        count = count + 1
        found = False
    elif guess == n:
        found = True

elif guess > n:
    print("Your guess is too high, guess again")
    count = count + 1
    found = False
    if guess < n:
        print("Your guess is too low, guess again")
        count = count + 1
        found = False
    elif guess > n:
        print("Your guess is too high, guess again")
        count = count + 1
        found = False
    elif guess == n:
        found = True

elif guess == n:
    found = True

   



if found == True and count < 4:
    print("You guess the correct number! Congradulations!")
if count > 3:
          print("Out of chances! Try again") 
    
    
        
