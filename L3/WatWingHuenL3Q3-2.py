words=[]
letter=["a","e","i","o","u"]
y=0
for i in range(0,11):
    
    
    word=input("input 10 words" )
    if i !=10:
        print("next", end=",")
        print(word[0])
        y=y+1
    if word[0] in letter:
        words.append(word)
  
    if y==11:
        break

print(words)
    
    

    
