list = []
for i in range(10):
    word = input("Enter 10 words\n")
    print(word[0])
    if word[0]in "a, e, i, o, u, A, E, I, O, U" :
        list.append(word)
        print(list)
    
