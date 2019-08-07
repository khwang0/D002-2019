from math import *
year = input ("Enter year:\n")
if year%400 == 0:
    check400 = True
else:
    check400 = False
if year%100 == 0:
    check100 = True
else:
    check100 = False
if year%4 == 0:
    check4 = True
else:
    check4 = False
leap = False
if check4 == True and check100 == False:
    leap = True
if check400 == True:
    leap = True
if leap == True:
    print ("Yes, it is a leap year")
else:
    print ("No, it is not a leap year")
