list = []
start = []
z=1
for x in range(1, 11):
    word = str(input("please enter a word:\n"))
    list.append(word)
for z in range(0, 10):
    if (list[z][0]) == "a" or (list[z][0]) == "e" or (list[z][0]) == "i" or (list[z][0]) == "o" or (list[z][0]) == "u":
        start.append(list[z])
        
if len(start) == 0:
    print("None start with vowels.")
else:
    print(start, "starts with a vowel")
