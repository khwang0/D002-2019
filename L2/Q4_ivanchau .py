a=0

while a < 11:
     b = 10 - a
     print( a, b , a* b)
     a = a + 1

a=0
b=0

while a < 11 and b < 11:
    c = 20 - b - a
    print ( a, b, c,(a*b) + (b* c))
    a = a + 1
    b = b + 1



a=0
b=0
c=0

while a< 21 and b< 21 and c < 21:
     d = 60 - a - b - c
     print ( a, b, c, d, (a*b) + (b*c) + (c*d))
     a = a + 1
     b = b + 1
     c = c + 1
