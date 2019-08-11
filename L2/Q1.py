num = int(input("Please input a positive integer number:\n"))

if num<1:
    print("Please input a positive number.\n")
elif num == 1:
    print(num, "is not a prime number.")
elif num == 2:
    print(num, "is a prime number.")
else:
    for x in range (2, num):
        if num%x == 0:
            print (num, "is not a prime number")
            break
    if num%x != 0:
            print (num, "is a prime number")
        

        
        


        
