from math import *
maxvalue = 0
a = 0
b = 0
c = 0
d = 60
while a < 60:
    a = a + 1
    while b <= 60 - a - c:
        b = b + 1
        while c <= 60 - a - b:
            c = c + 1
            d = 60 - a - b - c
            if d <= 0:
                c=0
                d=0
                break
            if maxvalue < a*b + b*c + c*d:
                maxvalue = a*b + b*c + c*d
                print(a,b,c,d)
        if d <=0:
            b=0
            c=0
            d=0
            break
        d = 60 - a - b - c
        if maxvalue < a*b + b*c + c*d:
            maxvalue = a*b + b*c + c*d
            print(a,b,c,d)
    if d <=0:
        b=0
        c=0
        d=0
        break
    d = 60 - a - b - c
    if maxvalue < a*b + b*c + c*d:
        maxvalue = a*b + b*c + c*d
        print(a,b,c,d)
print(maxvalue)
