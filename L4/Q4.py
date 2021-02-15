def checker(sentence, letter):
    result = []
    index = 0
    while index < len(sentence):
        if letter == sentence[index]:
            result.append(index)
        index = index + 1
        
    return result



a = checker("Apple","p")
b = checker("Banana","p")
c = checker("Cat", "a")
print(a)
