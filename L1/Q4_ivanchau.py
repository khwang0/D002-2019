y = int(input(' Enter a year\n'))
if ((y%400!=0) and (y%100!=0) and (y%4==0)):
    print('Yes, it is a leap year')
else:
    print('No, it is not a leap year')
    
