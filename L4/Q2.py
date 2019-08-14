def factor(x) :
    x = int(x)
    for i in range(1,x+1):
        if x%i == 0 :
            print('%d divides %d' % (x,i))
factor(40)
factor(5)
