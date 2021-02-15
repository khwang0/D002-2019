max = -1000
for a in range(1 ,11):
    b = 10-a
    y = a * b
    if y > max:
        max = y
print("a*b =",max)
c = 20-(a+b)
d = 60-(a+b+c)
print("a+b+c+d =",a+b+c+d)
