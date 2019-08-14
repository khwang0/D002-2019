def  prime(x):
    x = int(x)
    n = 2
    if x>1 :
        while n<x :
            if x%n ==0 :
                print(str(x) + ' has factor ' + str(n))
                break
            else :
                n = n+1
            if  n+1 == x :
                print( str(x) + ' is a prime number')
            if x == 3 :
                print( str(x) + ' is a prime number')
        if x == 2 :
            print( str(x) + ' is a prime number')
                
prime(input('Please input a positive integer number: '))
