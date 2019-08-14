def checker(sentence, letter):
    result = []
    for i in range(len(sentence)):
      if letter == sentence [i]:
          result.append(i)
    
    
    
    return result
    
    
a = checker("Apple", "p") # a = [1, 2]
b = checker("Banana", "p") # b = []
c = checker("Cat", "a") # c = [1]

print(a,b,c)
