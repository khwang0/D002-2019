def asd() :
    emp = input('please input a positive integer ')
    emp = int(emp)
    n=2
    status = 0
    while True :
        if emp == 3 or emp == 2 :
            print(str(emp) + ' is a prime number')
            break
        if emp%n == 0 :
            print(str(emp) + ' has factor ' + str(n))
            status = 1
        n += 1
        if n == emp :
            if status==1 :
                break
            if status == 0 :
                print(str(emp) + ' is a prime number')
                break
asd()
