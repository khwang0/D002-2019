def  factors(n):
    for x in range(1,n+1):
        if n%x == 0:
            print("%d divides %d" % (x,n))


factors(40)
factors(5)
