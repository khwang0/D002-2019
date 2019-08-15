def factors(n):
    result=[]
    for x in range(1,n+1):
        if n%x == 0:
            result.append(x)
    return result
print (factors(30))
a = factors(30)
if 5 in a :
    print ("5 is a factor of 30")
