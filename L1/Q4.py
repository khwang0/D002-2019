y = input("Please eneter a year:\n")
y = int(y)
if ((y%4 == 0 and y%100 != 0) or y%400 == 0 ):
          print("Yes, it is a leap year\n")
else:
              print("No, it is not a leap year\n")
          
