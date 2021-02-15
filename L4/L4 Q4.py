def checker(sentence, letter):
    result = []
    for i in range(0,int(len(sentence)-1)):
        if letter in sentence[i]:
            result.append(i)
    return result
    
    
