year = int(input("Year : "))
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Yes, it is a leap year")
        else:
            print("No, it is not a leap year")
    else:
        print("Yes, it is a leap year")
else:
    print("No, it is not a leap year")
