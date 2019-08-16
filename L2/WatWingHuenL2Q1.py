n=int(input("input a positive no larger then 2"))
prime = True
if n%2 ==0:
    prime= False

x=3
while x <= n/2:
    if n%x ==0:
        prime = False
    x=x+2
        
    
if prime == True:
    print("prime")
else:
    print("No prime")
