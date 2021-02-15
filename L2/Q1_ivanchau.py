n = int(input(' Enter an integer\n'))
prime = True
x = 3
if (n/2) % 2 == 0:
     prime = False
elif n % 5 == 0:
     prime = False
elif n % x == 0:
     prime = False
elif n % 10 == 0:
     prime = False
elif n < 0:
     prime = False
else:
     prime = True

if prime == False:
      print (" Not a prime")
if prime == True:
      print (" Prime")
    
