max = -999
for a in range (1,61):
    for b in range (1,60-a+1):
        for c in range(1,60-a-b+1):
            d=60-a-b-c
            m=a*b+b*c+c*d
    if m>max:
        max=m
        print (a,b,c,d,max)
print (max)


