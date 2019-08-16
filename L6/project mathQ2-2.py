import random
car=['a','b','c']
car=random.choice(['a','b','c'])
choice=input("please input your choice \n" )
fake=random.choice(['a','b','c'])

while choice==fake:
    fake=random.choice(['a','b','c'])

print("The host choose door %s"%fake)
print(car)
real=input("Do you want to pick door %s ?\n"%choice)
if real==car:
    print("you get the car")
else:
    print("Try next time")




