x=int(input('enter a year'))
if x%4 == 0 or x%400 == 0 or x%100:
print ("Yes, it is a leap year")
else:
    print ("No, it is not a leap year")
