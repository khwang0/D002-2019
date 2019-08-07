print(8*3.57)
print(5+30*20)
print((5+30)*20)
print(1+(2+20*3)/(4*2))
print(1+2**10)
a = int(input('number of passenger'))
if int(a)%4 > 0 :
    print('the number of car needed : ' + str(a//4 +1))
else :
    print('the number of car needed : ' + str(a//4))
