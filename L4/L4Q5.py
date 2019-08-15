def printer(secret, opened):
    i = 0
    while i < len(secret):
         if i in opened:
             a = secret[i]
         else:
             a = '_'
         i = i + 1
         print(a, end = ' ')
    print()
# Note: you might use print(x, end="") to print x without changing line

printer("apple", [1, 2]) # _pp__
printer("orange", [0, 5]) # o____e
printer("cat", []) # ___
