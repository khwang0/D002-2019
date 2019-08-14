def factor(x):
    result=[]
    x = int(x)
    for i in range(1,x+1):
        if x%i == 0 :
            print('%d is a foctor of %d' % (i,x))
            result.append(i)
    return result
print(factor(40))
