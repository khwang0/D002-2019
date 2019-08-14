def factors(n):
    result = []
    for x in range(1, n + 1):
        if n % x == 0:
            result += [x]
    return result
print(factors(40))  # prints [1, 2, 4, 5, 8, 10, 20, 40]
a = factors(30)
if 5 in a:
     print("5 is a factor of 30") # it prints!
