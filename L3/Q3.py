vowels = []
for i in range (0,10):
    w = input("Please input word%d:\n"%(i+1))
    if w[0] == "A" or w[0] == "E" or w[0] == "I" or w[0] == "A" or w[0] == "O" or w[0] == "U":
        vowels.append(w)

print (vowels)
