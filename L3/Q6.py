import random
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.\nWhat is your guess\n''')
n = random.randint(1,100)
found = False
count = 1

while found == True or count < 4:
    if n == int(input()):
        found == True
        print('You got the correct guess in %d trials' % count)
        print('Dave\'s banana are now all yours!')
        break    
    else:
        count = count + 1
        print("Try again!")
    
if n != int(input()) and count >= 3:
    print("You failed to find the number of bananas Dave hid!")
    print("He had", n, "bananas.")
