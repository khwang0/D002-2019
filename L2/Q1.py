n=int(input('Enter a positive number'))
p=2
prime = True
while n > 2 and p < n:
    if n % p == 0:
        prime = False
        p = p+1
    else:
        p = p+1
        continue

if prime == True:
    print(n,'is a prime number.')
else:
    print(n,'is not a prime number.')
