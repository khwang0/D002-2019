year = int(input("What year do you want to have checked?\n"))
if(year%4 == 0 and year%100 != 0):
    print("%d is a leap year" % year)
elif(year%400 == 0):
    print("%d is a leap year" % year)
else:
    print ("%d is not a leap year" % year)
