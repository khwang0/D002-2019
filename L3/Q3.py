vowels = []
for i in range (0,10):
    w = input("Please input word%d:\n"%(i+1))
    if w[0] in "AEIOUaeiou":
        vowels.append(w)

print (vowels)
