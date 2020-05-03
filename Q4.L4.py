def checker(sentence,letter):
    result=[]
    x=0
    while x < len(sentence):
        if letter == sentence[x]:
            result.append(x)
        x=x+1
    print (result)
    return result

a=checker("apple","p")
b=checker("banana","p")
c=checker("cat","a")         
