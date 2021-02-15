from random import*
x = 0
c = 0
while x <= 100:
    x = x + 1
    n = 0
    while n!= 6:
        n = randint(1,6)
        c = c + 1
print("It takes an average of %f times to get from rolling a dice a 100 times" % (c/100))
    
    
