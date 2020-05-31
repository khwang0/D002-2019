from math import*
y = int(input("Enter year:"))
if y % 4 == 0:
   if y % 100 == 0:
       if y % 400 == 0:
           print("Yes", y, "is a leap year")
       else:
           print("No,", y, "is not a leap year")
   else:
       print("Yes", y, "is a leap year")
else:
   print("No,", y, "is not a leap year")
