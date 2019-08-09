year = input('Year')
year = int(year)
if year%4 > 0:
    ans = 0
if year%4 == 0:
    if year%100 > 0 :
        ans = 1
    if year%100 == 0 :
        if year%400 >0 :
            ans = 0
        if year%400 == 0:
            ans = 1
if ans == 1 :
    print('Yes, it is a leap year')
if ans == 0 :
    print("No, it is not a leap year")
    
