def factors (n): # your code here
 for x in range(1, n + 1):
    if n % x == 0:
        print("%d divides %d" % (x, n))

factors(40) # print 1 divids 40
            #       2 divids 40
            #       4 divids 40
            #       5 divids 40
            #       8 divids 40
            #      10 divids 40
            #      20 divids 40
            #      40 divids 40
factors(5)  # print 1 divids 5   
            #       5 divids 5
