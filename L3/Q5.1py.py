def checker(sentence, letter):
    result = []
    i = 0
    for i in range(0, len(sentence)):
        if letter == sentence[i]:
            result.append(i)
        i = i+1
    return result
print(checker("apple", "p"))
print(checker("banana", "p"))
print(checker("cat", "a"))
