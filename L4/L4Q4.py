def checker(sentence, letter):
    result = []
    for i in range(len(sentence)):
        if sentence[i] = letter:
            result += [i]        
    return result
    
    
 a = checker("Apple", "p") # a = [1, 2]
 b = checker("Banana", "p") # b = []
 c = checker("Cat", "a") # c = [1]
