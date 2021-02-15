from random import*
n = randint(1,6)
c = 1
print("The player casts his dice")
print("I got a %d" % n)
while n < 6:
    n = randint(1,6)
    c = c + 1
    print("I got a %d" % n)
    continue 
print("Oh, it takes me %d times to get a 6!!!" % c)
