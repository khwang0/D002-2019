from random import randint
door=["a","b","c"]
win=0
count=0
#car=['a','b','c']
while (count<=999):
    car=door[randint(0,2)]
    count=count+1
    choice=door[randint(0,2)]
    fake=door[randint(0,2)]
    fake2=door[randint(0,2)]
    choice2=door[randint(0,2)]
   # print(car,fake,fake2)

    while car==fake or car ==fake2 or fake==fake2:
        #print("loop1_1")
        fake=door[randint(0,2)]
        fake2=door[randint(0,2)]
        car=door[randint(0,2)]
      
    while choice2 == choice or choice2 == fake2:
        choice2=door[randint(0,2)]
            
        
    #print(choice)
    #print("The host choose door with goat%s"%fake2)
    #print(car)
    #print("do you want to choose again ")
    #print(choice2)

    if choice2 == car:
        #print("you get the car")
        win=win+1
    #else:
        #print("Try next time")
print("experiment time:%d"%count)
print(win)

print("if dont use this method,the winning percentage is:%f"%(count/3))


