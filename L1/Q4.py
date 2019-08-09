Y=int(input('The year:'))
if (Y%4 > 0):
    a=0
elif (Y%4 == 0):
    if (Y%100 == 0):
        if(Y%400 == 0):
            a=1
        else:
            a=0
    elif (Y%100 > 0):
        a=1
if (a == 0):
    print(Y,'is not a leap year.')
if (a == 1):
    print(Y,'is a leap year.')
