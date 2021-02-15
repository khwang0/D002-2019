def checker(sentence, letter):
    result = []
    # Your code here
    for i in range(0,len(sentence)):
        if sentence[i] == letter:
            result.append(i)
    return result
    
    
a = checker("Apple", "p") # a = [1, 2] 
b = checker("Banana", "p") # b = []
c = checker("Cat", "a") # c = [1]

print(a,b,c)
