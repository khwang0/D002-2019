n = int (input('please enter an positive integer'))
x=2
prime = True
while n >= x :
    if  n % x == 0:
        prime = False
        break
    else:
        x=x+1
        continue
if n == x:
    prime = True
if n == 1:
    prime = False
if prime == True:
    print("it is a prime number")
else:
    print ("it is not a prime number")
