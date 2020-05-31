a = 1
MaxSum = 1
while a <= 57:
    b = 0
    while b <= 57:
        c = 1
        b = b + 1
        while c <= 57:
            c = c+1
            d = 60-a-b-c
            if d>0:
                XSum = a*b + b*c + c*d
                if XSum > MaxSum:
                    MaxSum = XSum
    a=a+1
print(MaxSum)

