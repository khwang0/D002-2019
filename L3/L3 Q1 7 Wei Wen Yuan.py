n = 1
print("In this game, all multiples of 7 or numbers that end with 7 will be marked with a x")
while n <= 100:
    if ((n % 7 == 0) or ((n-7) % 10 == 0)):
        print('X')
        n = n + 1
    else:
        print(n)
        n = n + 1

print("\nGame Over.")
