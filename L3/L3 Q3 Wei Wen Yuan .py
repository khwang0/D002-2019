l = []
check = 0
while check < 10:
    check += 1
    w = input("Enter a word")
    if (w[0].lower() == "a" or w[0].lower() == "e" or w[0].lower() == "u" or w[0].lower() == "i" or w[0].lower() == "o"):
        l.append(w)
    else:
        print("no")
print(l)
    
