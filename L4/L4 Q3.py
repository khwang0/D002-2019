def Factor(n):
    result = []
    for x in range(1, n + 1):
        if n % x == 0:
            result.append(x)
    print("All the factors of the number are shown below") 
    print(result)
           
    
