def checker(sentence, letter):
    result = []
    # Your code here
    x = 0
    for i in sentence:
        if i == letter:
            result = result + [x]
        x = x + 1
    return result
    
    
a = checker("Apple", "p") # a = [1, 2]
b = checker("Banana", "p") # b = []
c = checker("Cat", "a") # c = [1]

print (a)
print (b)
print (c)
