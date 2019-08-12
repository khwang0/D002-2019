from math import *
maxvalue = 0
a = 0
b = 0
c = 0
d = 60
while a < 60:
    while b <= 60 - a - c:
        while c <= 60 - a - b -d:
            c = c + 1
            d = 60 - a - b - c
            if d <= 0:
                break
            if maxvalue < a*b + b*c + c*d:
                maxvalue = a*b + b*c + c*d
            print(a,b,c,d)
            d = 0
        b = b + 1
        c=0
        d=0
    a = a + 1
    b=0
    c=0
    d=0
        #d = 60 - a - b - c
        #if d<= 0:
            #break
        #if maxvalue < a*b + b*c + c*d:
            #maxvalue = a*b + b*c + c*d
        #print(a,b,c,d)
        #d=0

    #d = 60 - a - b - c
    #if d <= 0:
        #break
    #if maxvalue < a*b + b*c + c*d:
        #maxvalue = a*b + b*c + c*d
    #print(a,b,c,d)
    #d=0
print(maxvalue)




