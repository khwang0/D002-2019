import random
count = 0
print("Welcome to the banana guessing game! Dave hid some bananas, can you guess how many?")
n = int(random.randint(1,100))
print("Dave hid %d bananas"% n)
while count < 3:
    count += 1
    guess = int(input("What is your guess"))
    if guess == n:
      print("Congrats! You got the guess correct after %d trial(s)" % count)
      print("Dave's bananas are all yours")
      break
    else:
        print("Wrong! Try again")
    print("The correct answer is %d. You failed" % n)
              
