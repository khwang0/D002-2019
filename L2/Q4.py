'''a = 0
max = 0
while a <= 10:
    b = 10 - a
    if a*b > max:
        max = a*b
    a = a+ 1

print("The max value is %d" % max
'''
sum = int(input("a+b+c+d + ?"))
a = 0
max = 0
for a in range (0,(sum+1)):
    for b in range (0, (sum+1)-a):
        c = sum-a-b
        value = a*b + b*c
        if value > max:
            max=value
            print(a, b, c, d, max)

print (max)
