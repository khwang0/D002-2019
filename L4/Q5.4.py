def printer(secret, opened):
    i = 0
    while i < len(secret):
        if i in opened:
            print(secret[i])
            i = i + 1
        else:
            print("_")
            i = i + 1
printer("banana", [1, 4])

