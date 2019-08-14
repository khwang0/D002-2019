def checker(sen,letter) :
    result=[]
    sen = sen.lower()
    letter = letter.lower()
    n=1
    while True :
        if sen[n-1] == letter :
            result.append(n-1)
        n+=1
        if n>len(sen):
            break
    return result
a=checker('Apple','p')
b=checker('Banana','p')
c=checker('Cat','a')
