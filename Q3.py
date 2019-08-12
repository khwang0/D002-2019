vocab=[]
n=0
while True :
    n+=1
    temp=input('letter no. ' + str(n))
    if temp[0]=='a' or temp[0]=='i' or temp[0]=='e' or temp[0]=='u' or temp[0]=='o' :
        vocab.append(temp)
    if n==10:
        break
print(vocab)
