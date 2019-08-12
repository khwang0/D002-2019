numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'nineth', 'tenth']
ten_words = []

for x in numbers:
    word = input("Input %s word: " %x)
    if word[0]== "a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
        ten_words = ten_words + [word]
print (ten_words)
