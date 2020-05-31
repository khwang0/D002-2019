x = 0
for a in range(1,61):
    for b in range(1,61-a):
        for c in range(1,61-a-b):
            for d in range(1,61-a-b-c):
                e = a*b + b*c + c*d
                if e > x:
                    x = e
print("max : %d" % x)
    
