x=int(input('enter a year'))
if x%4 == 0 and x%400 == 0:
    print ("Yes, it is a leap year")
elif x%100==0:
    print ("No, it is not a leap year")
else:
    print ("No, it is not a leap year")
