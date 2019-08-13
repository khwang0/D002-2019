# L4 Worksheet

1. Finish Q1.py.

2. Write a void function called `factors` that prints all factors of an integer `n`.
```py
________________ # your code here
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
```

3. Write a function called factors that finds all factors of an integer `n`. It returns all factors as a list.
```py
____________ # your code here
    result = []
    for x in range(1, n + 1):
        if n % x == 0:
            _________
    __________
    
print(facotrs(40))  # prints [1, 2, 4, 5, 8, 10, 20, 40]
a = factors(30)
if 5 in a:
     print("5 is a factor of 30") # it prints!
```

4. Write a function called checker that reveals the index(s) of the sentence of which a letter is located.
It returns an empty list if the letter is not inside the sentence.

```py
def checker(sentence, letter):
    result = []
    # Your code here
    
    
    
    return result
    
    
 a = checker("Apple", "p") # a = [1, 2]
 b = checker("Banana", "p") # b = []
 c = checker("Cat", "a") # c = [1]
```

5. Write a void function called printer that takes two parameters: `secret` and `opened`.
`secret` is a string and `opened` is a list of indexes. The function prints all letter of the string `secret` by masking
all indexes that is not in `opened` as `_`.

```py
def printer(secret, opened):
    i = 0
    while i < len(secret):
         # Your code here
         
         
         i = i + 1
         print()
# Note: you might use print(x, end="") to print x without changing line

printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___
```
